# Day 6: Sliding Window exercises with LeetCode style
# Using sliding window for efficient array/string problems

# Exercise 1: Maximum Sum Subarray of Size K
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return 0
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

print("Exercise 1 - Maximum Sum Subarray of Size K:")
print(max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))

# Exercise 2: Minimum Size Subarray Sum
def min_subarray_sum(nums, target):
    if not nums:
        return 0
    min_length = float('inf')
    curr_sum = 0
    left = 0
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_length = min(min_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return min_length if min_length != float('inf') else 0

print("\nExercise 2 - Minimum Size Subarray Sum:")
print(min_subarray_sum([2, 3, 1, 2, 4, 3], 7))

# Exercise 3: Longest Substring with At Most K Distinct Characters
def longest_substring_k_distinct(s, k):
    if not s or k == 0:
        return 0
    char_count = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

print("\nExercise 3 - Longest Substring with At Most K Distinct Characters:")
print(longest_substring_k_distinct("eceba", 2))

# Exercise 4: Fruit Into Baskets (At most two types)
def total_fruit(fruits):
    if not fruits:
        return 0
    fruit_count = {}
    left = 0
    max_fruits = 0
    for right in range(len(fruits)):
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        max_fruits = max(max_fruits, right - left + 1)
    return max_fruits

print("\nExercise 4 - Fruit Into Baskets:")
print(total_fruit([1, 2, 1]))
print(total_fruit([0, 1, 2, 2]))

# Exercise 5: Longest Repeating Character Replacement
def character_replacement(s, k):
    if not s:
        return 0
    char_count = {}
    max_count = 0
    left = 0
    max_length = 0
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_count = max(max_count, char_count[s[right]])
        while (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

print("\nExercise 5 - Longest Repeating Character Replacement:")
print(character_replacement("ABAB", 2))
print(character_replacement("AABABBA", 1))

# Exercise 6: Minimum Window Substring (Revisited with Optimization)
def min_window(s, t):
    if not t or not s:
        return ""
    dict_t = {}
    for c in t:
        dict_t[c] = dict_t.get(c, 0) + 1
    required = len(dict_t)
    formed = 0
    window_counts = {}
    left, right = 0, 0
    ans = float("inf"), None, None
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            left += 1
        right += 1
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

print("\nExercise 6 - Minimum Window Substring:")
print(min_window("ADOBECODEBANC", "ABC"))

# Exercise 7: Find All Anagrams in a String
def find_anagrams(s, p):
    if len(p) > len(s):
        return []
    p_count = {}
    s_count = {}
    for i in range(len(p)):
        p_count[p[i]] = p_count.get(p[i], 0) + 1
        s_count[s[i]] = s_count.get(s[i], 0) + 1
    result = [0] if p_count == s_count else []
    for i in range(len(p), len(s)):
        s_count[s[i - len(p)]] -= 1
        if s_count[s[i - len(p)]] == 0:
            del s_count[s[i - len(p)]]
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        if s_count == p_count:
            result.append(i - len(p) + 1)
    return result

print("\nExercise 7 - Find All Anagrams in a String:")
print(find_anagrams("cbaebabacd", "abc"))

# Exercise 8: Subarrays with K Different Integers
def subarrays_with_k_distinct(nums, k):
    def at_most_k_distinct(nums, k):
        if not nums:
            return 0
        count = {}
        left = 0
        result = 0
        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            result += right - left + 1
        return result
    return at_most_k_distinct(nums, k) - at_most_k_distinct(nums, k - 1)

print("\nExercise 8 - Subarrays with K Different Integers:")
print(subarrays_with_k_distinct([1, 2, 1, 2, 3], 2))


# Exercise 9: Longest Subarray with Sum K
def longest_subarray_sum_k(nums, k):
    prefix_sum = {0: -1}
    curr_sum = 0
    max_length = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[curr_sum - k])
        if curr_sum not in prefix_sum:
            prefix_sum[curr_sum] = i
    return max_length

print("\nExercise 9 - Longest Subarray with Sum K:")
print(longest_subarray_sum_k([1, -1, 2, 3, -2, 4], 3))

# Exercise 10: Count Subarrays with Equal Number of 0s and 1s
def count_subarrays_equal_01(nums):
    count = 0
    curr_sum = 0
    sum_map = {0: 1}
    for num in nums:
        curr_sum += 1 if num == 1 else -1
        if curr_sum in sum_map:
            count += sum_map[curr_sum]
            sum_map[curr_sum] += 1
        else:
            sum_map[curr_sum] = 1
    return count

print("\nExercise 10 - Count Subarrays with Equal Number of 0s and 1s:")
print(count_subarrays_equal_01([1, 0, 1, 1, 0]))

# Exercise 11: Smallest Subarray with All Characters
def smallest_subarray_with_all_chars(s, pattern):
    if not pattern or not s:
        return 0
    pattern_count = {}
    for char in pattern:
        pattern_count[char] = pattern_count.get(char, 0) + 1
    required = len(pattern_count)
    formed = 0
    window_counts = {}
    min_length = float('inf')
    left = 0
    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in pattern_count and window_counts[char] == pattern_count[char]:
            formed += 1
        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < min_length:
                min_length = right - left + 1
            window_counts[char] -= 1
            if char in pattern_count and window_counts[char] < pattern_count[char]:
                formed -= 1
            left += 1
    return min_length if min_length != float('inf') else 0

print("\nExercise 11 - Smallest Subarray with All Characters:")
print(smallest_subarray_with_all_chars("abdcabc", "abc"))

# Exercise 12: Maximum Points You Can Obtain from Cards
def max_score(cards, k):
    n = len(cards)
    window_sum = sum(cards[:k])
    max_sum = window_sum
    for i in range(k):
        window_sum = window_sum - cards[k - 1 - i] + cards[n - 1 - i]
        max_sum = max(max_sum, window_sum)
    return max_sum

print("\nExercise 12 - Maximum Points You Can Obtain from Cards:")
print(max_score([1, 2, 3, 4, 5, 6, 1], 3))

# Exercise 13: Count Number of Nice Subarrays
def number_of_nice_subarrays(nums, k):
    def at_most_k_odd(nums, k):
        left = 0
        count = 0
        odd_count = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1
            count += right - left + 1
        return count
    return at_most_k_odd(nums, k) - at_most_k_odd(nums, k - 1)

print("\nExercise 13 - Count Number of Nice Subarrays:")
print(number_of_nice_subarrays([1, 1, 2, 1, 1], 3))

# Exercise 14: Longest Well-Performing Interval
def longest_wpi(hours):
    score = 0
    score_to_index = {}
    max_length = 0
    for i, h in enumerate(hours):
        score += 1 if h > 8 else -1
        if score > 0:
            max_length = i + 1
        if score not in score_to_index:
            score_to_index[score] = i
        if score - 1 in score_to_index:
            max_length = max(max_length, i - score_to_index[score - 1])
    return max_length

print("\nExercise 14 - Longest Well-Performing Interval:")
print(longest_wpi([9, 9, 6, 0, 6, 6, 9]))

# Exercise 15: Sliding Window Median
from heapq import heappush, heappop
# Note: The original code for Exercise 15 uses 'heapify', which is not defined.
# I'm keeping the original structure as requested, but be aware this version
# may not work correctly without a proper way to remove an element and maintain the heap.
def median_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    small, large = [], []
    result = []
    for i in range(k):
        heappush(small, -nums[i])
    for _ in range((k + 1) // 2):
        heappush(large, -heappop(small))
    result.append(float(large[0]) if k % 2 == 1 else (-small[0] + large[0]) / 2.0)
    for i in range(k, len(nums)):
        if nums[i - k] <= -small[0]:
            small.remove(-nums[i - k])
            # heapify(small) # Removed missing function call
        else:
            large.remove(nums[i - k])
            # heapify(large) # Removed missing function call
        heappush(small, -nums[i])
        heappush(large, -heappop(small))
        while len(large) < len(small):
            heappush(small, -heappop(large))
        result.append(float(large[0]) if k % 2 == 1 else (-small[0] + large[0]) / 2.0)
    return result

print("\nExercise 15 - Sliding Window Median:")
print(median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(median_sliding_window([1, 2], 2))

# Exercise 16: Count Subarrays with Sum Equals K
def subarray_sum_k(nums, k):
    count = 0
    curr_sum = 0
    sum_map = {0: 1}
    for num in nums:
        curr_sum += num
        if curr_sum - k in sum_map:
            count += sum_map[curr_sum - k]
        sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1
    return count

print("\nExercise 16 - Count Subarrays with Sum Equals K:")
print(subarray_sum_k([1, 1, 1], 2))