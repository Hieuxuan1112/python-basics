# Practice with list, dict, set, and tuple data structures
# Covers basic operations and manipulations for Day 3

# Practice with List
my_list = [1, 2, 3, 4, 5]
print(f"Initial list: {my_list}")
my_list.append(6)
print(f"List after appending 6: {my_list}")
my_list.pop(1)
print(f"List after popping index 1: {my_list}")
my_list.insert(2, 8)
print(f"List after inserting 8 at index 2: {my_list}")
my_list.remove(3)
print(f"List after removing 3: {my_list}")
print(f"Length of list: {len(my_list)}")
my_list.extend([9, 10, 11])
print(f"List after extending with [9, 10, 11]: {my_list}")
sub_list1 = my_list[0:4]
sub_list2 = my_list[:]
print(f"Sublist from index 0 to 3: {sub_list1}")
print(f"Copied list: {sub_list2}")
my_list.sort()
print(f"List after sorting: {my_list}")
my_list.reverse()
print(f"List after reversing: {my_list}")

# Practice with Dict
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
print(f"Dictionary after adding 'c': {my_dict}")
dict_keys = my_dict.keys()
print(f"Dictionary keys: {dict_keys}")
dict_values = my_dict.values()
print(f"Dictionary values: {dict_values}")
sub_dict = {'d': 4, 'e': 5, 'f': 6}
my_dict.update(sub_dict)
print(f"Dictionary after updating with sub_dict: {my_dict}")
my_dict.pop('b', 0)
print(f"Dictionary after popping 'b': {my_dict}")
del my_dict['a']
print(f"Dictionary after deleting 'a': {my_dict}")

# Practice with Set
my_set = {1, 2, 3, 5, 6}
print(f"Initial set: {my_set}")
my_set.add(4)
print(f"Set after adding 4: {my_set}")
my_set.discard(1)
print(f"Set after discarding 1: {my_set}")
my_set.remove(2)
print(f"Set after removing 2: {my_set}")
check_2 = 2 in my_set
print(f"Is 2 in the set? {check_2}")
popped_element = my_set.pop()
print(f"Set after popping {popped_element}: {my_set}")

set_a = {1, 2, 3, 6}
set_b = {3, 4, 5, 6}
union_set = set_a | set_b
union_result = set_a.union(set_b)
print(f"Union of set A and set B: {union_set}")
print(f"Union result of set A and set B: {union_result}")
intersection_set = set_a & set_b
intersection_result = set_a.intersection(set_b)
print(f"Intersection of set A and set B: {intersection_set}")
print(f"Intersection result of set A and set B: {intersection_result}")
difference_set = set_a - set_b
difference_result = set_b.difference(set_a)
print(f"Difference of set A - set B: {difference_set}")
print(f"Difference of set B - set A: {difference_result}")

# Practice with Tuple
my_tuple = (1, 2, 3, 2, 4, 1)
print(f"Initial tuple: {my_tuple}")
print(f"Count of 2 in tuple: {my_tuple.count(2)}")
print(f"Index of first 1 in tuple: {my_tuple.index(1)}")
student_info = ("Hieu", 22, "Vietnam")
name, age, country = student_info
print(f"Student info: Name: {name}, Age: {age}, Country: {country}")

# Exercise 1: Count character frequency in a string
def count_characters(input_string):
    if not input_string:
        print("No string provided")
        return
    char_freq = {}
    for char in input_string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    print(f"Character frequency: {char_freq}")
count_characters("Hello")
count_characters("")

# Exercise 2: Remove duplicates from a list using set
def remove_duplicates(input_list):
    if not input_list:
        return set()
    unique_set = set()
    for item in input_list:
        unique_set.add(item)
    return unique_set
print(f"Unique elements: {remove_duplicates([1, 2, 3, 4, 2, 5, 3, 1, 6])}")

# Exercise 3: Find max and min in a list
def find_max_min_method1(input_list):
    if not input_list:
        print("No values provided")
        return
    temp_list = input_list.copy()
    temp_list.sort()
    length = len(temp_list)
    print(f"Max (method 1): {temp_list[length - 1]}")
    temp_list.reverse()
    print(f"Min (method 1): {temp_list[length - 1]}")

def find_max_min_method2(input_list):
    if not input_list:
        print("No values provided")
        return
    temp_list = input_list.copy()
    max_value = temp_list[0]
    min_value = temp_list[0]
    for num in temp_list:
        if max_value < num:
            max_value = num
        if min_value > num:
            min_value = num
    print(f"Max (method 2): {max_value}")
    print(f"Min (method 2): {min_value}")
find_max_min_method1([1, 5, 7, 2, 4, 6, 9, 8])
find_max_min_method2([1, 5, 7, 2, 4, 6, 9, 8])
find_max_min_method2([])

# Exercise 4: Create and sort a list
def sort_list(lst):
    if not lst:
        return []
    new_lst = lst.copy()
    new_lst.sort()
    return new_lst
original = [5, 2, 8, 1, 9]
sorted_result = sort_list(original)
print(f"Original: {original}")
print(f"Sorted: {sorted_result}")

# Exercise 5: Check and add elements to a dictionary
def update_dict(d, key, value):
    if not d:
        d = {}
    d[key] = d.get(key, 0) + value
    print(f"Updated dict: {d}")
my_dict = {"a": 1, "b": 2}
update_dict(my_dict, "a", 1)
update_dict(my_dict, "c", 3)

# Exercise 6: Find the intersection of two sets
def find_intersection(set1, set2):
    if not set1 or not set2:
        return set()
    return set1.intersection(set2)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
result = find_intersection(s1, s2)
print(f"Intersection: {result}")

# Exercise 7: Create a tuple from user input
def create_tuple_from_string(s):
    if not s:
        return ()
    nums = s.split(",")
    tuple_nums = tuple(int(num) for num in nums) 
    print(f"Tuple: {tuple_nums}")
create_tuple_from_string("1,2,3")

# Exercise 8: Reverse a list without using reverse()
def reverse_list(lst):
    if not lst:
        return []
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
original = [1, 2, 3, 4]
reversed_result = reverse_list(original)
print(f"Original: {original}")
print(f"Reversed: {reversed_result}")

# Exercise 9: Check if one set is a subset of another
def is_subset(set1, set2):
    if not set1 or not set2:
        return False
    return set1.issubset(set2)
s1 = {1, 2}
s2 = {1, 2, 3, 4}
print(f"Is {s1} subset of {s2}? {is_subset(s1, s2)}")

# Exercise 10: Combine dictionary and tuple data
def print_student_info(students):
    if not students:
        print("No students provided")
        return
    for name, (age, score) in students.items():
        print(f"{name}: age {age}, Score: {score}")
student_dict = {"Alice": (25, 85), "Bob": (30, 90)}
print_student_info(student_dict)