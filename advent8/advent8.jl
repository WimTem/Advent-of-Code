using Random

data = readlines("input.txt")

function sign(x)
    if occursin("+", x)
        tmp = findfirst("+", x)[1]
    else
        tmp = findfirst("-", x)[1]
    end
    return tmp
end

function cmd(x, i)
    if occursin("acc", x)
        tmp = parse(Int, x[sign(x)+1:end])
        if occursin("+", x)
            val = tmp
        else
            val = -tmp
        end
        return i+1, val
    end

    if occursin("jmp", x)
        tmp = parse(Int, x[sign(x)+1:end])
        if occursin("+", x)
            i += tmp
        else
            i -= tmp
        end
        return i, 0
    end

    if occursin("nop", x)
        return i+1, 0
    end
end

function run(x)
    i, acc, l = 1, 0, length(x)
    safe = 1
    A = zeros(l)
    while A[i] < 1
        if safe == 1e3
            return "FAIL"
        end
        A[i] += 1
        i, val = cmd(x[i], i)
        acc += val
        safe += 1
    end
    return acc
end

run(data)



#Part 2
function switch(x)
    l = length(x)
    d = Dict()
    for i = 1:l
        if occursin("jmp", x[i])
            d[i] = 1
        elseif occursin("nop", x[i])
            d[i] = 2
        else
            d[i] = 0
        end
    end

    tmp = rand(keys(d))
    if d[tmp] == 1
        return vcat(x[1:tmp-1], string("nop", x[tmp][4:end]), x[tmp+1:end])
    elseif d[tmp] == 2
        return vcat(x[1:tmp-1], string("jmp", x[tmp][4:end]), x[tmp+1:end])
    end
    return switch(x)
end

function run2(x)
    i, acc, l = 1, 0, length(x)
    tmp = switch(x)
    safe = 1
    while safe < 1e3
        safe += 1
        i, val = cmd(tmp[i], i)
        acc += val
        if i == l+1
            return true, acc
        end
    end
    return false, 0
end

function run3(x)
    safe = 1
    while safe < 1e3
        safe += 1
        sol, acc = run2(x)
        if sol
            return acc
        end
    end
    return "FAIL"
end

run3(data)