# Day 5: Two Pointers exercises with LeetCode style
# Using two pointers for efficient array/string operations

# Exercise 1: Valid Palindrome (Ignore non-alphanumeric, case-insensitive)
def is_palindrome(s):
    # Clean string: lowercase, alphanumeric only
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

print("Exercise 1 - Valid Palindrome:")
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False

# Exercise 2: Merge Two Sorted Lists (Return merged sorted list)
def merge_two_lists(l1, l2):
    merged = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    merged.extend(l1[i:])
    merged.extend(l2[j:])
    return merged

print("\nExercise 2 - Merge Two Sorted Lists:")
print(merge_two_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]

# Exercise 3: Remove Duplicates from Sorted Array (Return new length)
def remove_duplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[write_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index

print("\nExercise 3 - Remove Duplicates from Sorted Array:")
nums = [1, 1, 2, 2, 3]
length = remove_duplicates(nums)
print(f"New length: {length}, Array: {nums[:length]}")  # New length: 3, Array: [1, 2, 3]

# Exercise 4: Two Sum II - Input Array Is Sorted (Return indices)
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

print("\nExercise 4 - Two Sum II - Sorted:")
print(two_sum_sorted([2, 7, 11, 15], 9))  # [1, 2]

# Exercise 5: Container With Most Water (Max area between lines)
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

print("\nExercise 5 - Container With Most Water:")
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49

# Exercise 6: 3Sum (Find unique triplets summing to 0)
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

print("\nExercise 6 - 3Sum:")
print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]

# Exercise 7: Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

print("\nExercise 7 - Longest Substring Without Repeating:")
print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))    # 1

# Exercise 8: Trapping Rain Water (Total water trapped)
def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

print("\nExercise 8 - Trapping Rain Water:")
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6