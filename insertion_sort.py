def insertion_sort(A):
    for i in range(len(A)):
        t = A[i]
        j = i - 1
        while j >= 0 and A[j] > t:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = t

if __name__=='__main__':
    A = [3, 1, 2, 4, 5, 9, 10, 7, 6, 8]
    insertion_sort(A)
    print(A)