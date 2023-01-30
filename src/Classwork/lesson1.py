def count(a,b,c):
    answer1 = (-b + ((b**2 + 4*a*c)**0.5))/(2*a)
    answer2 = (-b - ((b**2 + 4*a*c)**0.5))/(2*a)
    return answer1,answer2
    

# print(count(2,5,6))

def triangle(a,b):
    c = (a**2 + b**2)**0.5
    return c
# print(triangle(3,4))

def simple(n):
    answer = str(n)
    return answer[-1]
# print(simple(1558))

def sum_number(d):
    sum_digit = 0
    stringify = str(d)
    
    for i in stringify:
        make_int = int(i)
        sum_digit = sum_digit + make_int
    return sum_digit
#print(sum_number(1234))

def distance(x1,x2,y1,y2):
    dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return dis
# print(distance(2,3,4,5))

def toxayin(s,n):
    return s[:n] + s[n+1:]

# print(toxayin("12345", 1))

def reverse_fl(s):
    a = s[-1] + s[1:-1] + s[0]
    return a
# print(reverse_fl("abcd"))

def round(num):
    number = num * 100//1/100
    # num_str = str(number)
    return number

# 

def maximize(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c
def minimum(a,b,c):
    if(a<b and a<c):
        return a
    elif(b<c and b<a):
        return b
    else:
        return c
# print(maximize(5,3,4))
# print(minimum(5,3,4))

def odd_or_even(num):
    if num % 2==0:
        return 'even'
    else: 
       return "number is odd"
        
        
# print(odd_or_even(13))

def divides(num):
    if(num %5 ==0 and num % 7 ==0):
        return "number is divisible on 5 and 7"
    else:
         return "number isn't divisible on 5 and 7"

# print(divides(37))


def three(word):
    thr = ""
    for i in range(len(word)):
        if(i % 3 == 0):
            thr += word[i]
    return thr

    # s = word[::3]
    # return s
        
# print(three("123456"))

def divs(n):
    for i in range(1,n+1):
        if(n % i == 0):
            print(i)
    return " "
# 
def rectangle(n,m):
    for i in range(n):
        print("*"*m)
        
    return " "

# print(rectangle(4,9))

def factorial(num):
    if(num == 1):
        return num
    return num * factorial(num-1)
# print(factorial(5))

def gcd(n1,n2):
    if n1<n2:
        small = n1
    else:
        small = n2
    for i in range(1, small+1):
            if(n1 % i == 0 and n2 %i == 0):
                gcd =i
    return gcd
# print(gcd(12,18))

def degree(n):
    count = 0
    return degree_helper(n, count)

def degree_helper(n, count):
    if(n<10):return count
    array = [int(i) for i in str(n)]
    n = sum(array)
    return degree_helper(n, count+1)
    
              
print(degree(625))

    