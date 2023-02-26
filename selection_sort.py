def selection_sort(A):
    for i in range(len(A)):
        index = i
        for j in range(i+1, len(A)):
            if A[j] < A[index]:
                index = j
        if index != i:
            t = A[i]
            A[i] = A[index]
            A[index] = t

if __name__=='__main__':
    A = [1, 3, 100, 9, 18, 83, 32, 8, 10, 2, 4, 5, 6]
    selection_sort(A)
    print(A)