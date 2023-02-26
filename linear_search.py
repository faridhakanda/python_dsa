def linear_search(A, target:int):
    for i in range(len(A)):
        if A[i] == target:
            return i
    return -1

if __name__=='__main__':
    A = [2, 1, 5, 19, 10, 3, 15, 18]
    print(A)
    print("Enter your targeted number: ")
    target = int(input())
    print("Number index is: ", linear_search(A, target))