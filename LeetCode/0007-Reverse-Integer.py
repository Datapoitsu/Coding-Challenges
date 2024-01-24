## ----- Reverse Integer ----- ##
#Written By: Aarni Junkkala

#Date 24.1.2024
#Runtime: 34 ms, Beats 82.77% of users with python3
#Memory: 16.61 MB, Beats 52.60% of users with python3

#Written into one line as a joke.

class Solution:
    def reverse(self, x: int) -> int:
        return (int(str(x)[::-1]) if int(str(x)[::-1]) < 2147483648 else 0) if str(x)[0] != "-" else int("-" + str(x)[1:][::-1]) if int(str(x)[1:][::-1]) < 2147483648 else 0
if __name__ == "__main__":
    a = Solution()
    print(a.reverse(123))