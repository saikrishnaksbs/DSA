# def permutate(list1, list2):
#     if len(list2) == 0:
#         print(list1)
#         return 
#     else:
#         for i in range(len(list1) + 1):  # Loop over possible insert positions in list1
#             next_element = list2[0]  # Get the next element from list2 (without popping)    
#             list1.insert(i, next_element)
#             permutate(list1, list2[1:])  # Use list2[1:] to avoid modifying the original list
#             list1.pop(i)
# # Example usage:
# permutate([], [1, 2, 3])


def permutate_string(current_string, remaining_string):
    if len(remaining_string) == 0:
        print(current_string)
        return
    else:
        for i in range(len(current_string) + 1):
            next_char = remaining_string[0]
            new_string = current_string[:i] + [next_char] + current_string[i:]
            permutate_string(new_string, remaining_string[1:])

permutate_string([], [1,2,3])