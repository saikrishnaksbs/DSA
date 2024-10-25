def combinations(s1: str, s2: str):
    if len(s1) == 0:
        print(s2)
        return
    else:
        s2 = s2 + s1[0]
        s1 = s1[1:]
        combinations(s1, s2)
        s2 = s2[:-1]
        combinations(s1, s2)

combinations("abcd", "")


# def combinations(list1, list2):
#     if len(list2) == 0:
#         print(list1)
#         return
    
#     else:
#         # Case 1: Include the current element from list2 in the combination
#         combinations(list1 + [list2[0]], list2[1:])
        
#         # Case 2: Exclude the current element from list2
#         combinations(list1, list2[1:])
    
# combinations([], [1, 2, 3])


# def generate_combinations(current_index, current_string, original_string, all_combinations):
#     # Base case: if we've processed all characters, add the current string to the result
#     if current_index == len(original_string):
#         all_combinations.append("".join(current_string))  # Join the current combination into a string
#         return
#     # Path 1: Include the current character in the combination
#     current_string.append(original_string[current_index])
#     generate_combinations(current_index + 1, current_string, original_string, all_combinations)
#     # Backtrack: Remove the last added character to explore the other path
#     current_string.pop()
#     # Path 2: Exclude the current character from the combination
#     generate_combinations(current_index + 1, current_string, original_string, all_combinations)

# # Wrapper function to initiate and store combinations
# def get_all_combinations(input_string):
#     all_combinations = []
#     generate_combinations(0, [], input_string, all_combinations)
#     return all_combinations

# # Example usage
# combinations = get_all_combinations("abc")
# print(combinations)