                                                #  [0,  1,  2,  3,  4   5,  6]
def selection_sort(arr):                        #1 [64, 34, 25, 12, 22, 11, 90]
                                                #2 [11, 34, 25, 12, 22, 64, 90]
    for i in range(len(arr)):                   #i [0,1,2,3,4,5,6]
        min_index = i                           #  [0]
        for j in range(i + 1, len(arr)):        #j [1,2,3,4,5,6,7] This 1st loop run until 11 < 90 
            print(arr[j],"<", arr[min_index])
            if arr[j] < arr[min_index]:         # 34 < 64: because j idx: 34 and min_index: 64
                min_index = j                   # Why it is important this piece of code  when is smaller than
                                                # Then assign to j the value min_index and why?
                                                # Because increase the point to move towards the another value
                                                # When arr[j] is greather than arr[min_index] then min_index
                                                # Stay in the position until the comparision be true.
                                                # For example in the step 22 < 12 the code pass and arr[j] continue
                                                # iterate but the min_index is the same position in the array
                                                # 11 < 22 True.. and then continue.
        print(arr[i], arr[min_index], "=", arr[min_index], arr[i])
        print(arr)
        arr[i], arr[min_index] = arr[min_index], arr[i] # Explanation
                                                        # When the loop finished in j = 6 then
                                                        # arr[min_index] = 5 == 11 and arr[i] = 0 == 64
                                                        # So we swap them so that it becomes like this.
                                                        # Swap: [11, 34, 25, 12, 22, 64, 90]
    return arr

# Example usage
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = selection_sort(array)
# print(f"Original array: {array}")
print(f"Sorted array: {sorted_array}")
