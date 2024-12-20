def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

arr = [42, 27, 5, 14, 73, 12]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])

# Python program for implementation of Insertion Sort
# Time Complexity: O(N^2)
# This code is contributed by harturalcantara (Software Developer)