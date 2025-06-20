def selection_sort(array):
    array_length = len(array)

    for i in range(array_length):
        #i contains the smallest index
        min_index = i

        for j in range(i + 1, array_length):
            #find an element smaller than the current minimum
            if array[j] < array[min_index]:
                #update the index of the minimum element
                min_index = j

        if min_index != i:
            #swap  the minimum element with the element in position i
            array[i], array[min_index] = array[min_index], array[i]

    return array

my_list = [1,34,6,78,2,99]
print(f"Original list: {my_list}")
selection_sort(my_list)
print(f"Sorted list: {my_list}")
    # TODO: Implement selection sort
    # pass
