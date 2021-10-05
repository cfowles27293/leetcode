from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ''
        valid = True
        index = 0

        while valid:
            for element in range(len(strs)):
                if element == 0 and len(strs[element]) > index:
                    next_letter = strs[element][index]
                else:
                    if len(strs[element]) > index:
                        if strs[element][index] != next_letter:
                            valid = False
                            return prefix
                    else:
                        valid = False
                        return prefix
            prefix += next_letter
            index += 1
        return prefix

if __name__ == "__main__":
    s = Solution()
    strs = ["ab", "a"]
    result = s.longestCommonPrefix(strs)
    print(result)