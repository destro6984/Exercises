# EXE1

input_1 = "79-900"
input_2 = "80-155"


def exercise1(input_1, input_2):
    result = []
    first_code_into_number = int(input_1[0:2] + input_1[3:])
    second_code_into_number = int(input_2[0:2] + input_2[3:])
    for code in range(first_code_into_number, second_code_into_number + 1):
        code = str(code)
        result.append(f"{code[0:2]}-{code[2:]}")
    return result


print(exercise1(input_1, input_2))


# EXE2
def exercise2(list, n):
    return [num for num in range(1, n + 1) if num not in list]


n = 10
list = [2, 3, 7, 4, 9]
print(exercise2(list, n))


# EXE3

def exercise3(start, stop, step):
    return [num / 100 for num in range(int(start * 100), int(stop * 100) + 1, int(step * 100))]


print(exercise3(2, 5.5, 0.5))
