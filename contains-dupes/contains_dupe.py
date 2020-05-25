def containsDuplicate(num):
    original_length = len(num)
    new_length = len(set(num))

    if original_length == new_length:
        return False
    return True


# tests
test1 = containsDuplicate([1, 2, 3, 1])
test2 = containsDuplicate([1, 2, 3, 4])
test3 = containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

print(test1, test2, test3)
