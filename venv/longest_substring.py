# Finds the length of the longest substring of unique characters.
class Solution:
    # O(n^3)
    def find_substring(s : str) -> int:
        length = 0
        longest_string = ""
        substring = ""
        for i in range (len(s)):
            for j in range(i, len(s)):
                if not substring.__contains__(s[j]):
                   substring = "".join([substring, s[j]])
                   if len(substring) > length:
                       longest_string = substring
                       length = len(longest_string)
                else:
                    substring = ""
                    break
        print(longest_string)
        return length


    def fast_find_substring(s : str) -> int:
        length = 0
        longest_string = ""
        start = 0
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                start = max(start, seen[s[i]] + 1)
            seen[s[i]] = i
            if len(s[start : i]) >= length:
                longest_string = s[start:i + 1]
            length = max(length, i - start + 1)
        print(longest_string)
        return length

if __name__ == "__main__":
        string = "ABCDEFGHIJKlmnopQqrrsstt"
       # print(Solution.find_substring(string))
        print(Solution.fast_find_substring(string))