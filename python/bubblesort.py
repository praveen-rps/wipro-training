def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swapping happens
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred in a pass, the list is already sorted
        if not swapped:
            break
    return arr


# Main function
def main():
    print("=== Bubble Sort ===")
    arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)


if __name__ == "__main__":
    main()
