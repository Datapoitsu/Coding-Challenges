## -- 1000-digit Fibonacci number -- ##
#Written By: Aarni Junkkala

#Problem:
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

#My Thoughts:
#Same thing, again and again... still kinda nice problem.

fibo = [1,1]
while len(str(fibo[-1])) < 1000:
    fibo.append(fibo[-1] + fibo[-2])
print(len(fibo))