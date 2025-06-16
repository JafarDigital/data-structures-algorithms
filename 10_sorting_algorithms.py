def bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				
def selection_sort(arr):
	n = len(arr)
	for i in range(n):
		min_idx = i
		for j in range(i+1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_ixd], arr[i]
		
def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key

def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		L = arr[:mid]
		R = arr[mid:]
		
		merge_sort(L)
		merge_sort(R)
		
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
			
		arr[k:] = L[i:] + R[j:]
		
def quick_sort(arr):
	def _quick_sort(items, low, high):
		if low < high:
			pi = partition(items, low, high)
			_quick_sort(items, low, pi - 1)
			_quick_sort(items, pi + 1, high)
	
	def partition(items, low, high):
		pivot = items[high]
		i = low - 1
		for j in range(low, high):
			if items[j] <= pivot:
				i += 1
				items[i], items[j] = items[j], items[i]
		items[i+1], items[high] = items[high], items[i+1]
		return i+1
		
	_quick_sort(arr, 0, len(arr) - 1)
	
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def counting_sort(arr):
    if not arr: return
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    idx = 0
    for i, c in enumerate(count):
        for _ in range(c):
            arr[idx] = i
            idx += 1

if __name__ = "__main__":
	algorithms = [
        bubble_sort, selection_sort, insertion_sort,
        merge_sort, quick_sort, heap_sort, counting_sort
	]
	
	sample = [64, 25, 12, 22, 11]
	print("Original:", sample)
	for algo in algorithms:
		arr = sample.copy()
		algo(arr)
		print(f"{algo.__name__}: {arr}")
