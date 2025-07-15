def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Not found


# Main function
def main():
    print("=== Binary Search (Divide and Conquer) ===")
    arr = list(map(int, input("Enter sorted elements (space-separated): ").split()))
    target = int(input("Enter the value to search for: "))

    result = binary_search(arr, target)

    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the list.")


if __name__ == "__main__":
    main()