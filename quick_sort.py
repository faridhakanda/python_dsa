def partition(A, low, high):
    pivot = A[high]
    i = low-1
    for j in range(low, high):
        if A[j] < pivot:
            i += 1
            t = A[i]
            A[i] = A[j]
            A[j] = t

    t = A[high]
    A[high] = A[i+1]
    A[i+1] = t
    return i+1

def quick_sort(A, low, high):
    if low >= high:
        return
    p = partition(A, low, high)
    quick_sort(A, low, p-1)
    quick_sort(A, p+1, high)

if __name__=='__main__':
    A = [3, 10, 100, 283, 15, 6, 8, 9, 1, 2, 4, 5, 7]
    n = len(A)
    quick_sort(A, 0, n-1)
    print(A)