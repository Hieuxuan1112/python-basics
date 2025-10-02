# Day 5: Two Pointers exercises with LeetCode style
# Using two pointers for efficient array/string operations

# Exercise 1: Valid Palindrome (Ignore non-alphanumeric, case-insensitive)
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

print("Exercise 1 - Valid Palindrome:")
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))

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
print(merge_two_lists([1, 3, 5], [2, 4, 6]))

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
print(f"New length: {length}, Array: {nums[:length]}")

# Exercise 4: Two Sum II - Input Array Is Sorted (Return indices)
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

print("\nExercise 4 - Two Sum II - Sorted:")
print(two_sum_sorted([2, 7, 11, 15], 9))

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
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))

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
print(three_sum([-1, 0, 1, 2, -1, -4]))

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
print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))

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
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# Exercise 9: Remove Duplicates from Sorted Array II (Allow up to 2 duplicates)
def remove_duplicates_ii(nums):
    if len(nums) < 3:
        return len(nums)
    write_index = 2
    for read_index in range(2, len(nums)):
        if nums[read_index] != nums[write_index - 1] or nums[read_index] != nums[write_index - 2]:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index

print("\nExercise 9 - Remove Duplicates from Sorted Array II:")
nums = [1, 1, 1, 2, 2, 3]
length = remove_duplicates_ii(nums)
print(f"New length: {length}, Array: {nums[:length]}")

# Exercise 10: Rotate Array (Rotate k steps to the right)
def rotate_array(nums, k):
    k = k % len(nums)
    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]

print("\nExercise 10 - Rotate Array:")
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(nums, k)
print(f"Array after rotating {k} steps: {nums}")

# Exercise 11: K Closest Points to Origin (Return k closest points)
def k_closest(points, k):
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]

print("\nExercise 11 - K Closest Points to Origin:")
points = [[1, 3], [-2, 2]]
k = 1
print(k_closest(points, k))

# Exercise 12: Subarray Product Less Than K
def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    count = 0
    product = 1
    left = 0
    for right in range(len(nums)):
        product *= nums[right]
        while product >= k and left <= right:
            product //= nums[left]
            left += 1
        count += right - left + 1
    return count

print("\nExercise 12 - Subarray Product Less Than K:")
print(num_subarray_product_less_than_k([10, 5, 2, 6], 100))

# Exercise 13: Partition Labels (Partition string into labels)
def partition_labels(s):
    last = {c: i for i, c in enumerate(s)}
    start, end = 0, 0
    result = []
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = end + 1
    return result

print("\nExercise 13 - Partition Labels:")
print(partition_labels("ababcbacadefegdehijhklij"))

# Exercise 14: Minimum Window Substring
def min_window(s, t):
    if not t or not s:
        return ""
    dict_t = {}
    for c in t:
        dict_t[c] = dict_t.get(c, 0) + 1
    required = len(dict_t)
    formed = 0
    l, r = 0, 0
    window_counts = {}
    ans = float("inf"), None, None
    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        while l <= r and formed == required:
            char = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

print("\nExercise 14 - Minimum Window Substring:")
print(min_window("ADOBECODEBANC", "ABC"))

# Exercise 15: Sliding Window Maximum (Max in each window of size k)
from collections import deque
def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    deq = deque()
    result = []
    for i in range(len(nums)):
        while deq and deq[0] < i - k + 1:
            deq.popleft()
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            result.append(nums[deq[0]])
    return result

print("\nExercise 15 - Sliding Window Maximum:")
print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))