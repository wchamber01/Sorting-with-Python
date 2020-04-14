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
    changed=False
    while not changed:
        changed=True
        for iteration in range(0, len(arr)-1):
            for item in range(1, len(arr)):
                if arr[iteration] > arr[item]:
                    arr[iteration], arr[item] = arr[item], arr[iteration]
                    changed=False
                
    return arr
# def bubble_sort( arr ):
#     changed=False
#     while not changed:
#         changed=True
#         for iteration in range(0, len(arr)-1):
#             #print(arr[iteration])
#             if arr[iteration] > arr[iteration+1]:
#                 arr[iteration], arr[iteration+1] = arr[iteration+1], arr[iteration]
#                 changed=False
                
#     return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # for i in range(0, len(arr) -1):

    return arr