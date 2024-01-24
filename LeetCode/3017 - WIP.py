## ----- Count the Number of Houses at a Certain Distance II ----- ##
#Written By: Aarni Junkkala
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        L = [0] * n
        pairs = int(n * (n / 2 - 0.5))
        #for i in range(n): #Jos ei olisi oikopolkua
            #L[i] = n - i - 1
        
        if x + y > n:
            x = n - x + 1
            y = n - y + 1 
        x,y = min(x,y),max(x,y)

        for i in range(x):
            L[i] += x - i
        
        for i in range(0,n-y):
            L[i] += n-y-i-1
        
        for i in range(0,y-x):
            L[i] += y-x - i
        
        for i in range(n - (y-x)):
            print(i)
        
        #for i in range(n-1):
        #    for k in range(i+1,n):
        #        #Etsi matka
        #        Suora = k-i - 1
        #        Oikopolku = min(abs(i-(x-1)) + abs(k-(y-1)),abs(k-(x-1)) + abs(i-(y-1)))
        #        #print("i:",i,"k:",k,"oik:",Oikopolku,"Suo:",Suora)
        #        L[min(Suora,Oikopolku)] += 1
        return L

if __name__ == "__main__":
    a = Solution()
    b = 8
    
    print(a.countOfPairs(b,4,6))
    
    #print("#Dist 1-2")
    #print(1,1,a.countOfPairs(b,1,1))
    
    #for k in range(2,b):
    #    print("#Dist",k)
    #    for i in range(1,int((b - (k-1)) / 2) + 1):
    #        print(i,i+k,a.countOfPairs(b,i,i+k))