def maxArea(self, height: List[int]) -> int:
        water = 0
        head = 0
        tail = len(height) - 1

        for cnt in range(len(height)):

            width = abs(head - tail)

            if height[head] < height[tail]:   
                res = width * height[head]
                head += 1
            else:
                res = width * height[tail]
                tail -= 1

            if res > water:
                water = res

        return water

def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        for i in range(1,len(p)+1):
            if p[i-1] == '*':
                if i >= 2:
                    dp[0][i] = dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        return dp[len(s)][len(p)]

def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num