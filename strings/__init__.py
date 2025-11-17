"""
1. 2sum:
    a. create a hashmap
    b. iterate through the array
    c. compliment = target - arr[i]
    d. saves the arr[i] to the hashmap
    e. check if complement is in the hashmap
        if yes then return the complement index and the current index

"""


def tow_sum(arr, target):
    hashmap = {}
    for num, i in enumerate(arr):
        compliment = target - num
        if compliment in hashmap:
            return [hashmap[compliment], i]
        hashmap[num] = i

"""
2. 3sum:
    a. sort the array
    b. iterate through the array
    c. if i > 0 and arr[i] == arr[i-1] then continue
    d. left = i + 1
    e. right = len(arr) - 1
    f. while left < right
        if arr[i] + arr[left] + arr[right] == 0 then append to the result
        if arr[i] + arr[left] + arr[right] < 0 then left += 1
        if arr[i] + arr[left] + arr[right] > 0 then right -= 1
    g. while i < len(arr) - 1 and arr[i] == arr[i+1] then i += 1
    h. return result
"""

def three_sum(arr):
    sorted_arr = arr.sort()
    for num,i in enumerate(sorted_arr):
        if i>0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = len(arr)-1
        while left < 
