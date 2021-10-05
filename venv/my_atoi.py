class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        atoi = 0
        sign = True
        s = s.strip()
        length = len(s)
        if length == 0:
            return atoi
        elif length == 1:
            if s.isdigit():
                atoi = int(s)
                return atoi
            else:
                return atoi
        else:
            i = 0
            temp = ''
            first_num = False
            for i in range(length):
                if s[i].isdigit() and not s[i] == 0:
                    first_num = True
                    temp += s[i]
                elif not i == length - 1 and s[i] == '-' :
                    if s[i+1].isdigit() and first_num == False:
                        sign = False
                    else:
                        break
                elif not i == length -1 and s[i] == '+':
                    if s[i+1].isdigit() and first_num == False:
                        sign = True
                    else:
                        break
                else:
                    break
            if temp == '':
                return atoi
            atoi = int(temp)
            if sign == True and atoi > 2**31-1:
                atoi = 2**31-1
            if sign == False and atoi > 2**31:
                atoi = 2**31
            if sign == False:
                atoi = -1*atoi
            return atoi

if __name__ == '__main__':
    str = '+-+1283472332'
    s = Solution()
    print(s.myAtoi(str))