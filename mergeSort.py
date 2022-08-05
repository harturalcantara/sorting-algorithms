def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
if __name__ == '__main__':
    arr = [42, 27, 5, 14, 73, 12]
    print("Given array:", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array: ", end="\n")
    printList(arr)

# Python program for implementation of MergeSort
# Time Complexity: O(n log(n)),  Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. T(n) = 2T(n/2) + θ(n)
# Auxiliary Space: O(n)
# Space Complexity: In merge sort all elements are copied into an auxiliary array, so N auxiliary space is required for merge sort.