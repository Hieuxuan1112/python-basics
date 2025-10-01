# Day 4: Hashing exercises with LeetCode style
# Using dict and set for fast lookups and counting

# Exercise 1: Two Sum
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
print("Exercise 1 - Two Sum:")
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

# Exercise 2: Check Anagram
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count1 = {}
    count2 = {}
    for char in s1:
        count1[char] = count1.get(char, 0) + 1
    for char in s2:
        count2[char] = count2.get(char, 0) + 1
    return count1 == count2
print("\nExercise 2 - Check Anagram:")
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False

# Exercise 3: Single Number
def single_number(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num in count:
        if count[num] == 1:
            return num
    return None
print("\nExercise 3 - Single Number:")
print(single_number([2, 2, 1, 3, 3]))  # 1

# Exercise 4: Group Anagrams
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in groups:
            groups[key].append(s)
        else:
            groups[key] = [s]
    return list(groups.values())
print("\nExercise 4 - Group Anagrams:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [['eat','tea','ate'], ['tan','nat'], ['bat']]

# Exercise 5: Max Value Key
def max_value_key(d):
    if not d:
        return None
    max_key = next(iter(d))
    max_val = d[max_key]
    for k, v in d.items():
        if v > max_val:
            max_val = v
            max_key = k
    return max_key
print("\nExercise 5 - Max Value Key:")
print(max_value_key({"a": 10, "b": 5, "c": 15}))  # "c"

# Exercise 6: Count Frequency
def count_frequency(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return freq
print("\nExercise 6 - Count Frequency:")
print(count_frequency([1, 2, 2, 3, 1, 4]))  # {1: 2, 2: 2, 3: 1, 4: 1}

# Exercise 7: Check Equal Lists
def are_lists_equal(list1, list2):
    return set(list1) == set(list2)
print("\nExercise 7 - Check Equal Lists:")
print(are_lists_equal([1, 2, 3], [3, 2, 1]))  # True
print(are_lists_equal([1, 2, 2], [1, 2, 3]))  # False

# Exercise 8: Symmetric Difference
def find_symmetric_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.symmetric_difference(set2))
print("\nExercise 8 - Symmetric Difference:")
print(find_symmetric_difference([1, 2, 3], [2, 4, 5]))  # [1, 3, 4, 5]

# Exercise 9: Most Frequent Number
def find_most_frequent(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    most_frequent_num = [k for k, v in freq.items() if v == max_freq][0]
    return most_frequent_num, max_freq
print("\nExercise 9 - Most Frequent Number:")
print(find_most_frequent([1, 2, 2, 3, 2, 4]))  # (2, 3)

# Exercise 10: Subarray Sum K
def has_subarray_sum(nums, k):
    sum_dict = {0: -1}  # Initialize with 0 sum at index -1
    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum - k in sum_dict:
            return True
        sum_dict[curr_sum] = i
    return False
print("\nExercise 10 - Subarray Sum K:")
print(has_subarray_sum([1, 4, 2, 3], 5))  # True
print(has_subarray_sum([1, 2, 3], 10))    # False

# Exercise 11: Pairs with Sum <= Target
def find_pairs_with_sum_leq(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] <= target:
                pairs.append((i, j))
    return pairs
print("\nExercise 11 - Pairs with Sum <= Target:")
print(find_pairs_with_sum_leq([1, 5, 3, 2], 6))  # [(0, 2), (0, 3), (1, 3)]

# Exercise 12: Count Words
def count_words(text):
    words = text.lower().split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq
print("\nExercise 12 - Count Words:")
print(count_words("The cat and the dog AND the cat"))  # {'the': 2, 'cat': 2, 'and': 2, 'dog': 1}

# Exercise 13: Count Common Elements
def count_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1.intersection(set2))
print("\nExercise 13 - Count Common Elements:")
print(count_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # 2

# Exercise 14: Create Dict from Lists
def create_dict_from_lists(keys, values):
    if len(keys) != len(values):
        return {}
    return dict(zip(keys, values))
print("\nExercise 14 - Create Dict from Lists:")
print(create_dict_from_lists(['a', 'b', 'c'], [1, 2, 3]))  # {'a': 1, 'b': 2, 'c': 3}

# Exercise 15: Diff Char Frequency
def diff_char_frequency(s1, s2):
    freq = {}
    for char in s1:
        freq[char] = freq.get(char, 0) + 1
    for char in s2:
        freq[char] = freq.get(char, 0) - 1
    return {k: v for k, v in freq.items() if v != 0}
print("\nExercise 15 - Diff Char Frequency:")
print(diff_char_frequency("hello", "hellp"))  # {'o': 1, 'p': -1}