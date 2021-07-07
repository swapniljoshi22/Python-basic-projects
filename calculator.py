class cal:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        return self.x+self.y
    
    def sub(self):
        return self.x-self.y

    def mul(self):
        return self.x*self.y

    def div(self):
        return self.x/self.y
    


x=int(input("Enter your 1st value: "))
y=int(input("Enter your 2nd value: "))
obj=cal(x,y)


def abc():
    a=("1.Addition \n 2.Substraction \n 3.Multiply \n 4.Division")
    print(a)

abc()

w=int(input("Enter your choice:"))

if w==1:
    print("Addition is",obj.add())
elif w==2:
    print("Substraction is",obj.sub())
elif w==3:
    print("Multiply is",obj.mul())
elif w==4:
    print("Division is",obj.div())



    

        
        
