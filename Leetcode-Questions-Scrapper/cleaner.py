import re
arr = []

with open("lc.txt", "r") as file:
    for line in file:
        arr.append(line)

def remove_unwanted_elements(array, pattern):
    new_arr = []
    for element in array:
        if pattern not in element:
            new_arr.append(element) 
        else:
            print("Removed: "+element)
    return new_arr

arr = remove_unwanted_elements(arr, "/solution")
print(len(arr))
arr = list(set(arr))

with open("lc_cleaned.txt", "a") as file:
    for i in arr:
        file.write(i)
