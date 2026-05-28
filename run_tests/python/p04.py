def reverse_list(lst: list) -> list:
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

original = [1, 2, 3, 4, 5]
print("Original:", original)
print("Reversed:", reverse_list(original))
