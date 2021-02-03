data = readlines("input.txt")

#Part 1
function count(x)
    c = 0
    temp = []
    for i in x
        for j in i
            if j ∉ temp
                push!(temp, j)
                c += 1
            end
        end
    end
    return c
end

function wow1(x)
    a, index = 0, 1
    for i = 1:length(x)
        if isempty(x[i])
            a += count(x[index:i-1])
            index = i+1
        end
    end
    return a
end


wow1(vcat(data, [""]))

#Part 2

function wow2(x)
    a, index = 0, 1
    for i = 1:length(x)
        if isempty(x[i])
            a += count_all(x[index:i-1])
            index = i+1
        end
    end
    return a
end

function count_all(x)
    a, result = 0, 0
    if length(x) == 1
        return length(x[1])
    end
    for i in x[1]
        for j in x[2:end]
            if i in j
                a += 1
            end
        end
        if a == length(x[2:end])
            result += 1
        end
        a = 0
    end
    return result
end

wow2(vcat(data, [""]))

wow2(B)
