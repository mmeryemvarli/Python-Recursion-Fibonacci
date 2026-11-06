import time 

def fibonacci_recursive(n): # takes longer, repeatedly calculates same subproblems.
    if n <= 1: 
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)  #call itself 

def fibonacci_iterative(n): # much faster, calculates by storing only the last two values in memory.
    if n <= 1: 
        return n
    a=0     
    b=1 
    for i in range(2,n+1):
        a, b = b, a + b 
    return b    

#2
def iterative_sum(n): # O(n) time complexity , uses O(1) auxiliary space because it only updates a single variable in memory .
    total = 0
    for day in range (1,n+1):
        total +=day
    return total

def recursive_sum(n): # O(n) time complexity, uses O(n) space due to the function call stack.
    if n <= 0:  # best case, necessary to stop the fuction and prevent stack overflow.
        return 0
    return n + recursive_sum(n-1) # call itself 
#3
def linear_search(n,target): 
    steps = 0
    for number in range (1, n+1):
        steps+=1
        if number == target:
            return steps
    return steps 
#4
def factorial_while(n):
    result=1
    i = n
    while i > 1:
        result *= i
        i -= 1
    return result    

def factorial_recursive(n):
    if n <= 1: #base-case
        return 1
    return n * factorial_recursive(n-1) 

#testing funcitons
def exercise_1():

    for n in (10, 35):
        start = time.time()
        result_rec = fibonacci_recursive(n)
        end = time.time()

        print("Recursive result:", result_rec)
        print("Recursive time:", end - start)

        start = time.time()
        result_iter = fibonacci_iterative(n)
        end = time.time()

        print("Iterative result:", result_iter)
        print("Iterative time:", end - start)
    print()


def exercise_2():
    n=5
    print("Recursive Sum:", recursive_sum(n))
    print("Iterative Sum:", iterative_sum(n))
    print()


def exercise_3():
    n=100 
    for target in (1,50,100,999): 
        steps=linear_search(n,target)
        if 1 <= target <= n:
            result="Found"
        else:
            result="Not Found"  

        print("Target:",target)     
        print("Steps:",steps)   
        print("Result:",result)
        print()
# best case O(1), target is at the beggining. 
# average case O(50).
# worst case O(100) or O(999) , target is at the end or not list.

def exercise_4():
    n=5
    print("5! Recursive:",factorial_recursive(n))
    print("5! While Loop:", factorial_while(n))
    print()

exercise_1()
exercise_2()
exercise_3()
exercise_4()


