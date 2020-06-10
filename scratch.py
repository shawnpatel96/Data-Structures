#Runtime Complexity -> O(n) -> Linear
# ARR is input
# WE ARE DOING SOMETHING FOR EACH ITEM IN THE INPUT
def cool(arr): 
    for item in arr:
        print("Hello")


#Runtime Complexity -> O(1) -> Constant
# ARR IS INPUT
# WE DON'T DO ANYTHING WITH IT
def cool2(arr):
    print("cool")


#Runtime Complexity -> O(n^2) -> Quadratic
# ARR IS INPUT
# FOR EVERY ITEM IN THE ARRAY, DO SOMETHING WITH EVERY ITEM IN THE ARRAY AGAIN
# for i: [1, 2, 3, 4, 5]
# for j: [1, 2, 3, 4, 5]
def cool3(arr):
    for i in range(len(arr)): #INPUT
        i += 1
        for j in range(len(arr)): #INPUT
            j += 1

    return True
    
#Runtime Complexity -> O(n) -> Linear
# FOR LOOP OF INPUT
# FOOR LOOP OF 3
def cool4(arr):
    nums = [1, 2, 3]
    for i in range(len(arr)):
        i += 1
        for i in nums:
            print("Hello")

#Runtime Complexity -> O(n log n) -> Linearithmic
# FOR LOOP OF INPUT
# FOOR LOOP OF INPUT THAT GROWS LOGARITHMICALLY
def cool5(arr):
    for i in range(len(arr)): #O(n)
        i += 1
        for j in range(len(arr)): #O(log n)
            j *= 2

            # j=1 --> 2 --> 4 --> 8 --> 16
            # j=1 --> 2 --> 3 --> 4 --> 5


# BINARY ARRAY SEARCH
# Runtime Complexity -> O(log n) -> Logarithmic
# WE ARE SPLITTING ARRAY IN HALF FOR EACH ITERATION
def cool6(sorted_arr, target):
    mid_idx = len(sorted_arr)//2
    mid_value = sorted_arr[mid_idx]

    if mid_value == target:
        return mid_value
    
    if target < mid_value:
        left_half = sorted_arr[0:mid_idx]
        cool6(left_half, target)
    
    if target < mid_value:
        right_half = sorted_arr[mid_idx::]
        cool6(right_half, target)