data = readlines("input.txt")

function f1(x, a=["shiny gold"])
    for i = 1:length(x)
        for j = 1:length(a)
            if occursin(a[j], x[i][2:end])
                temp1 = findfirst(" bag", x[i])
                push!(a, x[i][1:temp1[1]-1])
            end
        end
    end
    return unique(a)
end

function conv(x)
    a_old = f1(x)
    for i = 1:10
        if length(a_old) == length(f1(x, a_old))
            return length(f1(x,a_old)), i
        end
        a_old = f1(x, a_old)
    end
    return 4
end

conv(data)

#Part 2

function collect_colours(x)
    result = []
    for i = 1:length(x)
        temp1 = findfirst(" bag", x[i])
        temp2 = x[i][1:temp1[1]-1]
        push!(result, temp2)
    end
    return result
end

col = collect_colours(data)

d = Dict()
for i = 1:length(col)
    d[col[i]] = i
end

d["shiny gold"]
data[134]

d["drab blue"]
data[411]

function c(x, key="shiny gold", a=0)
    for j = 1:length(x)
        if x[j][1:length(key)] == key
            for k in col
                if occursin(k, x[j][2:end])
                    temp1 = findfirst(k, x[j])
                    temp2 = parse(Int, x[j][temp1[1]-2])
                    a += temp2*c(x, k, 1)
                end
            end
        end
    end
    return a
end
c(data)