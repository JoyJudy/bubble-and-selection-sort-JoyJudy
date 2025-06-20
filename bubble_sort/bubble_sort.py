def bubble_sort(array):
    #get length of the array
    array_length = len(array)

    #runs once for each element
    for i in range(array_length):
        swapped = False

        #compare adjacent elements
        #avoids the last i elements (already sorted)
        for j in range(array_length - i - 1):
            #if element on the left > element on the right, swap
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

            #if no swaps happened in this pass, the list is already sorted
        if not swapped:
            break
    return array

my_list = [1, 3, 5, 7, 2, 4, 6, 8]
print(f"Original list: {my_list}")
bubble_sort(my_list)
print(f"Sorted list: {my_list}")

     # TODO: Implement bubble sort
    # pass
