import math

def linear_search(arr, target):
	for i, val in enumerate(arr):
		if val == target:
			return i
	return -1
	
def binary_search_iterative(arr, target):
	low, high = 0, len(arr)-1
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	return -1
	
def binary_search_recursive(arr, target, low, high):
	if low > high:
		return -1
	mid = (low + high) // 2
	if arr[mid] == target:
		return mid
	elif arr[mid] > target:
		return binary_search_recursive(arr, target, low, mid-1)
	else:
		return binary_search_recursive(arr, target, mid+1, high)
		
def ternary_search(arr, target, low, high)
def exponential_search(arr, target)
def jump_search(arr, target)
def interpolation_search(arr, target)
def fibonacci_search(arr, target)

if __name__ == "__main__":
    arr = sorted([3, 10, 17, 23, 45, 55, 67, 78, 89, 101, 120])
    target = 67
    print("Array:", arr)
    print("Target:", target)
    
    search_algos = [
        ("Linear Search", linear_search),
        ("Binary Search (Iterative)", binary_search_iterative),
        ("Binary Search (Recursive)", lambda a, t: binary_search_recursive(a, t, 0, len(a)-1)),
        ("Ternary Search", lambda a, t: ternary_search(a, t, 0, len(a)-1)),
        ("Exponential Search", exponential_search),
        ("Jump Search", jump_search),
        ("Interpolation Search", interpolation_search),
        ("Fibonacci Search", fibonacci_search),
    ]

    for name, func in search_algos:
        result = func(arr, target)
        print(f"{name}: Index {result}")
