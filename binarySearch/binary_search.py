def binary_search(list, item):
    low =int(0)
    high = int(len(list) - 1)

    while low <= high:
        mid = int((low + high)/2)
        guess = list[int(mid)]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
my_list = [1, 3, 5, 7, 9, 11, 13, 15]

print(binary_search(my_list, 3))
print(binary_search(my_list, 0))