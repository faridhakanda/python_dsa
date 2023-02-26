def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                t = A[j]
                A[j] = A[j+1]
                A[j+1] = t
            
if __name__=='__main__':
    A = [3, 1, 100, 83, 12, 4, 5, 8, 7, 9, 10]
    bubble_sort(A)
    print(A)