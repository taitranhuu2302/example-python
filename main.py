# This is a sample Python script.
import math

eps = 0.00001 #Sai số

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

# 4
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
    second = 1 - (x**(i))/math.factorial(i)
    y = 0

    while(abs(first - second) > eps):
        i += 2
        y += 1
        
        first = second
        
        if (i % 2 == 0):
            second -= x**i/math.factorial(i)
        else:
            second += x**i/math.factorial(i)  
        
    return first

print(f"Example Six: {exampleSix(1)}")


# 7
def exampleSeven(x):
    i = 2
    
    first = 1
    second = 1 - (x**(i))/math.factorial(i)
    y = 0

    while(abs(first - second) > eps):
        y += 1
        i += 2
        
        first = second
        
        if (i % 2 != 0):
            second -= x**i/math.factorial(i)
        else:
            second += x**i/math.factorial(i)  
        
    return first


print(f"Example Seven: {exampleSeven(1)}")


# # 8
def exampleEight(x):
    i = 3
    first = x
    tuSo = 1
    mauSo = 2
    second = first + ( (tuSo/mauSo) * (x**i)/i )  
    while(abs(first - second) > eps):
        i += 2
        tuSo = tuSo * (i - 2)
        mauSo = mauSo * ( i - 1)

        first = second
        second = first + ( (tuSo/mauSo) * (x**i)/i )
    return first

# Kiểm tra kết quả với x = 0.5
print(f"Example Eight: {exampleEight(0.5)}")


# 9
def exampleNine(x):
    step = 2
    i = 0
    first = 1
    second = (first - x**step / math.factorial(step+1))

    while abs(first - second) > eps:
        step += 2
        i += 1
        first = second
        if (i % 2 != 0):
            second = first + x**step / math.factorial(step+1)
        else:
            second = first - x**step / math.factorial(step+1)
    return first

# Kiểm tra kết quả với x = 1 và n = 5
print(f"Example Nine: {exampleNine(1)}")


# 10
def exampleTen(x):
    step = 3
    i = 0
    first = x
    second = (first - x**step / step)

    while abs(first - second) > eps:
        step += 2
        i += 1
        first = second
        if (i % 2 != 0):
            second = first + x**step / step
        else:
            second = first - x**step / step

    return first

# Kiểm tra kết quả với x = 0.5 
print(f"Example Ten: {exampleTen(0.5)}")


# 11
def exampleEleven(x):
    step = 3
    first = x
    second = first + x**step / step

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x**step / step
    return first

# Kiểm tra kết quả với x = 0.5
print(f"Example Eleven: {exampleEleven(0.5)}")


# 12
def exampleTwelve(x):
    step = 3
    first = x
    second = first + x**step / step

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x**step / step
    return first

# Kiểm tra kết quả với x = 0.5 
print(f"Example Twelve: {exampleTwelve(0.5)}")


# 13
def exampleThirteen(x):
    step = 3
    first = x
    second = first + x**step / math.factorial(step)

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x**step / math.factorial(step)
    return first


# Kiểm tra kết quả với x = 0.5
print(f"Example Thirteen {exampleThirteen(0.5)}")


# 14
def exampleFourteen(x):
    step = 2
    first = x
    second = first + x**step / math.factorial(step)

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x**step / math.factorial(step)
    return first

# Kiểm tra kết quả với x = 0.5
print(f"Example Fourteen: {exampleFourteen(0.5)}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('----------------')
    print('Hi, Tran Huu Tai')
    print('----------------')

