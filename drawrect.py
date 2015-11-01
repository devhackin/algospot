def remove_duplicate(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
        else:
            output.remove(value)
            seen.add(value)
    return output

testCase = input()
for i in range(testCase):
    x = list()
    y = list()

    for j in range(3):
        var_x, var_y = raw_input().split()
        x.append(var_x)
        y.append(var_y)

    x_result = remove_duplicate(x)
    y_result = remove_duplicate(y)

    print x_result[0] + ' ' + y_result[0]