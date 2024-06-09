import matplotlib.pyplot as plt

def assign(new_list, i, old_list, j):
    """
    Assigns the value from old_list[j] to new_list[i].

    Parameters:
    new_list (list): The list receiving the value.
    i (int): The index in the new_list to assign the value to.
    old_list (list): The list providing the value.
    j (int): The index in the old_list to get the value from.
    """
    new_list[i] = old_list[j]

def merge_sort(lst):
    """
    Sorts a list in ascending order using the merge sort algorithm.

    Parameters:
    lst (list): The list to be sorted.
    """
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        l, r, i = 0, 0, 0

        # Merging the left and right sublists
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                assign(lst, i, left, l)
                l += 1
            else:
                assign(lst, i, right, r)
                r += 1
            i += 1

        # Copying remaining elements of left, if any
        while l < len(left):
            lst[i] = left[l]
            l += 1
            i += 1

        # Copying remaining elements of right, if any
        while r < len(right):
            lst[i] = right[r]
            r += 1
            i += 1

if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    
    # Plotting the unsorted list using a bar plot
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(my_list)), my_list, color='skyblue')
    plt.title('Unsorted List')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()

    # Sorting the list using merge_sort
    merge_sort(my_list)
    
    # Plotting the sorted list using a bar plot
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(my_list)), my_list, color='skyblue')
    plt.title('Sorted List')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()
