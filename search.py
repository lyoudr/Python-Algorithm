# 1. SequentialSearch
def sequentialSearch(listx, item):
  for i, x in enumerate(listx):
    if x == item:
      return i
  return -1

test_list = [5, 4, 3, 2, 1]
sequentialSearch(test_list, 3) # should return 2

# 2. Binary search
def binarySearch(listx, item):
  listx.sort()
  low = 0
  high = len(listx) - 1
  
  while low <= high:
    mid = (low + high) // 2
    element = listx[mid]
    if element < item:
      low = mid + 1
    elif element > item:
      high = mid - 1
    else:
      return mid
  return False

bi_list = [2, 7, 6, 9 ,8, 1]
binarySearch(bi_list, 6)