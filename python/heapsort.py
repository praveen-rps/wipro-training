def heapify(arr, n, i):
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # left child index
    right = 2 * i + 2    # right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)                      # Heapify the affected subtree


def heap_sort(arr):
    n = len(arr)

    # Build max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify(arr, i, 0)                # Heapify reduced heap


# Main function
def main():
    print("=== Heap Sort ===")
    arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
    heap_sort(arr)
    print("Sorted array:", arr)


if __name__ == "__main__":
    main()
