# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for iteration in range(0, len(arr) - 1):
        cur_index = iteration
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for item in range(smallest_index+1, len(arr)):
            if arr[item] < arr[smallest_index]:
                smallest_index = item

        # TO-DO: swap
        if smallest_index != iteration:
            arr[iteration], arr[smallest_index] = arr[smallest_index], arr[iteration]


    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    changed=True
    while changed:
        changed=False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                changed=True
                
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # for i in range(0, len(arr) -1):

    return arr