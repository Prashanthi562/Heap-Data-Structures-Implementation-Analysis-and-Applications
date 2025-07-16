## Description:The program applies the Heapsort algorithm through a max-heap which in principle, sorts an input array in ascending order. The sorting process takes place in-place by first building the heap and then taking out the largest items.

# Performing heapsort using a max-heap
def heapify(arr, n, i):
    # Setting the largest as the current index
    largest = i
    # Finding the left child index
    left = 2 * i + 1
    # Finding the right child index
    right = 2 * i + 2

    # Comparing left child with current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Comparing right child with current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swapping and continuing heapifying if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Sorting the array using heap sort
def heapsort(arr):
    n = len(arr)

    # Building a max heap from the array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extracting elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Moving current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Calling heapify on the reduced heap
        heapify(arr, i, 0)

# Running the heapsort function on a sample list
if __name__ == "__main__":
    # Creating a sample list of numbers to sort
    sample_list = [20, 5, 15, 22, 1, 8]
    
    # Printing the original unsorted list
    print("Original List:", sample_list)
    
    # Calling the heapsort function to sort the list
    heapsort(sample_list)
    
    # Printing the sorted list after heapsort is applied
    print("Sorted List:  ", sample_list)
