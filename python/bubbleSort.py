def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [42, 27, 5, 14, 73, 12]
bubbleSort(arr)
print("Sorted array:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

# Python program for implementation of Bubble Sort
# Time Complexity: O(n^2) time even if the array is sorted.
# harturalcantara