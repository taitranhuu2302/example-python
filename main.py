# This is a sample Python script.
import math

eps = 0.00001 #Sai số

def tinhgiaithua(n):
    giai_thua = 1;
    if (n == 0 or n == 1):
        return giai_thua;
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i;
        return giai_thua;

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
def exampleTwo(x):
    i = 1 
    first = 1
    second = first - ( (((i+1) * (i+2))/2)*x**i )

    while(abs(first - second) >  eps):
        i += 1
        first = second 

        if(i % 2 == 0): 
            second = first + ( (((i+1) * (i+2))/2)*x**i )
        else:
            second = first - ( (((i+1) * (i+2))/2)*x**i )
            
    return first


# Kiểm tra với giá trị x = 0.5
print(f"Example Two: {exampleTwo(0.5)}")

#3
def exampleThree(x):
    i = 1
    first = -x
    second = first - ((x**(i+1))/(i+1))
    
    while(abs(second - first) > 0.0001):
        i += 1
        first = second
        second = first - ((x**(i+1))/(i+1))
        
    return first


print(f"Example Three: {exampleThree(float(-1))}")

# # 4
def exampleFour(x):
    i = 1
    first = 1
    tuSo = 1
    mauSo = 2
    
    second = first + (tuSo / mauSo)*x
    tuSoStep = 1
    mauSoStep = 4
        
    while(abs(first - second) > eps):
        i += 1
        first = second
        
        
        tuSo *= tuSoStep
        mauSo *= mauSoStep
        
        tuSoStep += 2
        mauSoStep += 2
        
        if (i % 2 == 0):
            second -= (tuSo / mauSo)*x**i
        else:
            second += (tuSo / mauSo)*x**i
        
    return first

print(f"Example Four: {exampleFour(float(0.5))}")

# 5
def exampleFive(x):
    i = 1
    first = 1
    tuSo = 1
    mauSo = 2
    tuSoStep = 3
    mauSoStep = 4
    
    second = first - (tuSo / mauSo)*x
    while(abs(first - second) > eps):
        i += 1
        tuSo *= tuSoStep
        mauSo *= mauSoStep
        
        tuSoStep += 2
        mauSoStep += 2
        first = second
        
        if (i % 2 == 0):
            second += (tuSo / mauSo)*x**i
        else:
            second -= (tuSo / mauSo)*x**i
    
    return first

# Kiểm tra với giá trị x = 0.5
print(f"Example Five: {exampleFive(0.5)}")


# 6
def exampleSix(x):
    i = 3
    
    first = 1
    second = 1 - (x**(i))/tinhgiaithua(i)
    y = 0

    while(abs(first - second) > eps):
        i += 2
        y += 1
        
        first = second
        
        if (i % 2 == 0):
            second -= x**i/tinhgiaithua(i)
        else:
            second += x**i/tinhgiaithua(i)  
        
    return first

print(f"Example Six: {exampleSix(1)}")


# 7
def exampleSeven(x):
    i = 2
    
    first = 1
    second = 1 - (x**(i))/tinhgiaithua(i)
    y = 0

    while(abs(first - second) > eps):
        y += 1
        i += 2
        
        first = second
        
        if (i % 2 != 0):
            second -= x**i/tinhgiaithua(i)
        else:
            second += x**i/tinhgiaithua(i)  
        
    return first


print(f"Example Seven: {exampleSeven(1)}")


# # 8
# def exampleEight(x, terms=10):
#     result = 0
#     for n in range(terms):
#         numerator = 1
#         for i in range(2 * n):
#             numerator *= i + 1
#             if i % 2 == 1:
#                 numerator *= x
#         denominator = 2 ** (2 * n) * math.factorial(n) ** 2 * (2 * n + 1)
#         term = numerator / denominator
#         result += term
#     return result


# # Kiểm tra kết quả với x = 0.5
# print(f"Example Eight: {exampleEight(0.5)}")
#
#
# # 9
# def exampleNine(x, n):
#     result = 1
#     sign = -1
#     factorial = 1
#     power = x
#
#     for i in range(1, n + 1):
#         sign *= -1
#         power *= x ** 2
#         factorial *= (2 * i - 1) * (2 * i)
#         result += sign * power / factorial
#
#     return result
#
#
# # Kiểm tra kết quả với x = 1 và n = 5
# print(f"Example Nine: {exampleNine(1, 5)}")
#
#
# # 10
# def exampleTen(x, n):
#     result = 0
#     for i in range(n):
#         sign = (-1) ** i
#         term = x ** (2 * i + 1) / (2 * i + 1)
#         result += sign * term
#     return result
#
#
# # Kiểm tra kết quả với x = 0.5 và n = 10
# print(f"Example Ten: {exampleTen(0.5, 10)}")
#
#
# # 11
# def exampleEleven(x, n):
#     result = 0
#     sign = 1
#     for i in range(1, n + 1):
#         term = (x ** i) / i
#         result += sign * term
#         sign *= -1
#     return result
#
#
# # Kiểm tra kết quả với x = 0.5 và n = 10
# print(f"Example Eleven: {exampleEleven(0.5, 10)}")
#
#
# # 12
# def exampleTwelve(x, n):
#     result = 0
#     for i in range(n):
#         term = (x ** (2 * i + 1)) / (2 * i + 1)
#         result += term
#     return 2 * result
#
#
# x = 0.5  # Giá trị của x
# n = 10  # Số lượng các số hạng cần tính
#
# # Kiểm tra kết quả với x = 0.5 và n = 10
# print(f"Example Twelve: {exampleTwelve(x, n)}")
#
#
# # 13
# def exampleThirteen(x, n):
#     result = 0
#     for i in range(n):
#         term = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
#         result += term
#     return result
#
#
# # Kiểm tra kết quả với x = 1.5 và n = 10
# print(f"Example Thirteen {exampleThirteen(1.5, 10)}")
#
#
# # 14
# def exampleFourteen(x, n):
#     result = 0
#     for i in range(n):
#         term = (x ** (2 * i)) / math.factorial(2 * i)
#         result += term
#     return result
#
#
# # Kiểm tra kết quả với x = 1.5 và n = 10
# print(f"Example Fourteen: {exampleFourteen(1.5, 10)}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('----------------')
    print('Tran Huu Tai')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
