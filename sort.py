# 1. Bubble Sort
list_a = [1, 3, 9, 2, 5, 4, 3]

def bubbleSort(array):
  length = len(array)
  for i in range(0, length):
    for j in range(0, length - 1):
      if array[j] > array[j+1]:
        swap(j, j+1, array)
  print('bubble sorted array is =>', array)
  

def modifiedBubbleSort(array):
  length = len(array)
  for i in range(0, length):
    for j in range(0, length - 1 - i):
      if array[i] > array[j+1]:
        swap(j, j+1, array)
  print('modified bubble sorted array is =>', array)

def swap(index_1, index_2, array):
  aux = array[index_1]
  array[index_1] = array[index_2]
  array[index_2] = aux
  return array

# bubbleSort(list_a)
# modifiedBubbleSort(list_a)

# 2. Selection Sort

def selectionSort(array):
  length = len(array)
  for i in range(0, length - 1):
    index_min = i
    for j in range(i, length):
      if array[index_min] > array[j]:
        index_min = j
    if i != index_min:
      swap(i, index_min, array)
  print('selection sorted array is =>', array)

# selectionSort(list_a)

# 3. Insertion Sort
def insertionSort(array):
  length = len(array)
  for i in range(1, length):
    j = i
    temp = array[i]
    while j > 0 and array[j-1] > temp:
      array[j] = array[j-1]
      j -= 1
    array[j] = temp
  print('insertionSort sorted array is =>', array)

insertionSort(list_a)

# 4. Merge Sort
def mergeSortRec(array):
  if len(array) > 1:
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    mergeSortRec(left)
    mergeSortRec(right)
    i = j = k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        array[k] = left[i]
        i = i + 1
      else :
        array[k] = right[j]
        j = j + 1
      k = k + 1

    while i < len(left):
      array[k] = left[i]
      i = i + 1
      k = k + 1
    
    while j < len(right):
      array[k] = right[j]
      j = j + 1
      k = k + 1
    
    print('Merging =>', array)

nlist = [14,46,43,27,57,41,45,21,70]
mergeSortRec(nlist)

# 5. Quick Sort
def quickSort(array, left, right):
  if len(array) > 1:
    
    index = partition(array, left, right)
    if left < index - 1:
      quickSort(array, left, index - 1)
    
    if index < right :
      quickSort(array, index, right)
  print('array is =>', array) 


def partition(array, left, right):
  pivot = array[(left + right) // 2] # the value of mid point
  i = left
  j = right

  while i <= j:
    while array[i] < pivot:
      i += 1
    while array[j] > pivot:
      j -= 1
    if i <= j:
      swapQuickSort(array, i, j)
      i += 1
      j -= 1
  return i

def swapQuickSort(array, index1, index2):
  aux = array[index1]
  array[index1] = array[index2]
  array[index2] = aux

xlist = [3, 5, 1, 6, 4, 7, 2]
quickSort(xlist, 0, len(xlist) - 1)