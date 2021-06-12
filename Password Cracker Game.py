import random
x=[0,0,0,0,0]
y=[1,2,3,4,5]
def genX():
    x[0]=random.randint(1,5)
    x[1]=random.randint(1,5)
    x[2]=random.randint(1,5)
    x[3]=random.randint(1,5)
    x[4]=random.randint(1,5)
def genY():
    global y
    userInput1=input("Enter First Number (1-5): ")
    if userInput1 == "": userInput1=0
    userInput2=input("Enter Second Number (1-5): ")
    if userInput2 == "": userInput2=0
    userInput3=input("Enter Third Number (1-5): ")
    if userInput3 == "": userInput3=0
    userInput4=input("Enter Fourth Number (1-5): ")
    if userInput4 == "": userInput4=0
    userInput5=input("Enter Fifth Number (1-5): ")
    if userInput5 == "": userInput5=0
    y[0]=int(userInput1)
    y[1]=int(userInput2)
    y[2]=int(userInput3)
    y[3]=int(userInput4)
    y[4]=int(userInput5)
def compare(a):
    if x[a]==y[a]:
        print("0")
    else:
        print("X")  

if __name__ == '__main__': genX()
while y!=x:
    genY()
    compare(0)
    compare(1)
    compare(2)
    compare(3)
    compare(4)
    #print("x=",x)
    print("Your Guess: ",y)
    if y==x: break
    print("Guess Again?")

print('''

Code Broken, 
        
            Congratulations!

You Did it!
        
''')
print("Press return to exit")
input()
exit()


