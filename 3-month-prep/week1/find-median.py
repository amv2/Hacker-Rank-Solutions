def findMedian(arr):
    # Write your code here
    
    # code logic:
    
    # sort the array
    arr.sort()
    # get the middle index
    middleIndex = int(len(arr) / 2)
    # return the value at the middle index
    return arr[middleIndex]
    
arr = [0, 1, 4, 5, 3, 2, 6]

print(findMedian(arr))
