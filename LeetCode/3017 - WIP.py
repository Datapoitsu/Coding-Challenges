## ----- Count the Number of Houses at a Certain Distance II ----- ##
#Written By: Aarni Junkkala
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        L = [0] * n
        pairs = int(n * (n / 2 - 0.5))
        #for i in range(n):
            #L[i] = n - i - 1
        
        if x + y > n:
            x = n - x + 1
            y = n - y + 1 
        #print(x,y)
        for i in range(n-1):
            for k in range(i+1,n):
                #Etsi matka
                Suora = k-i - 1
                Oikopolku = min(abs(i-(x-1)) + abs(k-(y-1)),abs(k-(x-1)) + abs(i-(y-1)))
                #print("i:",i,"k:",k,"oik:",Oikopolku,"Suo:",Suora)
                L[min(Suora,Oikopolku)] += 1
        return L

if __name__ == "__main__":
    a = Solution()
    for i in range(7):
        print(0,i,a.countOfPairs(7,0,i))
    
    print("#Dist 2")
    for i in range(1,6):
        print(i,i+2,a.countOfPairs(7,i,i+2))
    
    print("#Dist 3")
    for i in range(1,5):
        print(i,i+3,a.countOfPairs(7,i,i+3))