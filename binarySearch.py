arr = [3, 7, 12, 18, 25, 31, 42, 56, 68, 79]
target = 42

def binarySearch(array,left,right):
    while(left<=right):
        mid = (left+right)//2
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            right = mid-1
        else:
            left = mid+1
	return -1
    
print(binarySearch(arr,0,len(arr)-1))