# This is a sample Python script.
import math


# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# 1
def exampleOne(x):
    k = 0
    s = 1
    term = 1

    while abs(term) > 1e-8:
        k += 1
        term *= x / k
        s += term

    return s


# Kiểm tra với giá trị x = 5
print(f"Example One: {exampleOne(float(5)):.8f}")


# 2
def exampleTwo(x, n):
    k = 1
    s = 1

    while k < n:
        a = k + 1
        b = k + 2
        c = 2

        term = (-1) ** k * a * b / c * x ** (3 * k)
        s += term
        k += 1

    return s


# Kiểm tra với giá trị x = 5 và n = 10
print(f"Example Three: {exampleTwo(5, float(10))}")


# 4
def exampleFour(x, terms=10):
    result = 0
    for n in range(terms):
        numerator = 1
        denominator = 1
        for i in range(n):
            numerator *= (2 * i + 1)
            denominator *= (2 * i + 2)
        term = ((-1) ** n * numerator * x ** (n + 1)) / (denominator * 2 ** n)
        result += term
    return result + 1


# Kiểm tra với giá trị x = 0.5
print(f"Example Four: {exampleFour(0.5)}")


# 5
def exampleFive(x, terms=10):
    result = 1
    for n in range(1, terms):
        numerator = 1
        denominator = 1
        for i in range(n):
            numerator *= (2 * i - 1) if i > 0 else (-1)
            denominator *= (2 * i) if i > 0 else 1
        term = ((-1) ** n * numerator * x ** n) / (denominator * 2 ** (n - 1))
        result += term
    return result


# Kiểm tra với giá trị x = 0.5
print(f"Example Five: {exampleFive(0.5)}")


# 6
def exampleSix(x, terms=10):
    result = 0
    sign = 1
    for n in range(terms):
        numerator = x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        term = sign * numerator / denominator
        result += term
        sign *= -1
    return result


# Kiểm tra với giá trị x = pi/4
print(f"Example Six: {exampleSix(math.pi / 4)}")


# 7
def exampleSeven(x, terms=10):
    result = 0
    sign = 1
    for n in range(terms):
        numerator = x ** (2 * n)
        denominator = math.factorial(2 * n)
        term = sign * numerator / denominator
        result += term
        sign *= -1
    return result


# Kiểm tra với giá trị x = pi/4
print(f"Example Seven: {exampleSeven(math.pi / 4)}")


# 8
def exampleEight(x, terms=10):
    result = 0
    for n in range(terms):
        numerator = 1
        for i in range(2 * n):
            numerator *= i + 1
            if i % 2 == 1:
                numerator *= x
        denominator = 2 ** (2 * n) * math.factorial(n) ** 2 * (2 * n + 1)
        term = numerator / denominator
        result += term
    return result


# Kiểm tra kết quả với x = 0.5
print(f"Example Eight: {exampleEight(0.5)}")


# 9
def exampleNine(x, n):
    result = 1
    sign = -1
    factorial = 1
    power = x

    for i in range(1, n + 1):
        sign *= -1
        power *= x ** 2
        factorial *= (2 * i - 1) * (2 * i)
        result += sign * power / factorial

    return result


# Kiểm tra kết quả với x = 1 và n = 5
print(f"Example Nine: {exampleNine(1, 5)}")


# 10
def exampleTen(x, n):
    result = 0
    for i in range(n):
        sign = (-1) ** i
        term = x ** (2 * i + 1) / (2 * i + 1)
        result += sign * term
    return result


# Kiểm tra kết quả với x = 0.5 và n = 10
print(f"Example Ten: {exampleTen(0.5, 10)}")


# 11
def exampleEleven(x, n):
    result = 0
    sign = 1
    for i in range(1, n + 1):
        term = (x ** i) / i
        result += sign * term
        sign *= -1
    return result


# Kiểm tra kết quả với x = 0.5 và n = 10
print(f"Example Eleven: {exampleEleven(0.5, 10)}")


# 12
def exampleTwelve(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / (2 * i + 1)
        result += term
    return 2 * result


x = 0.5  # Giá trị của x
n = 10  # Số lượng các số hạng cần tính

# Kiểm tra kết quả với x = 0.5 và n = 10
print(f"Example Twelve: {exampleTwelve(x, n)}")


# 13
def exampleThirteen(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term
    return result


# Kiểm tra kết quả với x = 1.5 và n = 10
print(f"Example Thirteen {exampleThirteen(1.5, 10)}")


# 14
def exampleFourteen(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i)) / math.factorial(2 * i)
        result += term
    return result


# Kiểm tra kết quả với x = 1.5 và n = 10
print(f"Example Fourteen: {exampleFourteen(1.5, 10)}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('----------------')
    print_hi('Tran Huu Tai')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
