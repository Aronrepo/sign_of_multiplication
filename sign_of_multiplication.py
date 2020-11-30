#Function that givan an array A of N integers (between -100 and 100),
#returns the sign (-1,0,1) if the product of all the numbers in
#the array multiplied together. Assume that N is between 1 and 1000



A = [1,2,3,-5]


def solution(A):
    j = 0
    if 0 in A:
        return 0
    for i in A:
        if i < 0:
            j+=1
    if j%2==0:
        return 1
    else:
        return -1

print(solution(A))


