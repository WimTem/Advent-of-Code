data = readlines("input.txt")

A = zeros(Int, length(data))
for i = 1:length(data)
    A[i] = parse(Int, data[i])
end

function run(x)
    l = length(x)
    for index = 26:l
        if valid(x[index-25:index-1], x[index]) == 0
            return x[index], index+25
        end
    end
    return "FAIL"
end

function valid(x, val)
    for i = 1:25
        for j = 1:25
            if i != j
                if (x[i] + x[j]) == val
                    return 1
                end
            end
        end
    end
    return 0
end
run(A)

#Part 2

function run2(x)
    val, index = run(x)
    for i = 1:length(x)
        for j = 1:length(x)
            if i < j
                if sum(x[i:j]) == val
                    return minimum(x[i:j]) + maximum(x[i:j])
                end
            end
        end
    end
    return "FAIL"
end

run2(A)