<<<<<<< HEAD
class Worker:

    def __init__(self,n,a,num,s):
    	self.Name=n
    	self.Age=a
    	self.NumberOfPlaseOfWork=num
    	self.Salary=s
    def Inf(self):
        return f'{self.Name} {self.Age} work in {self.NumberOfPlaseOfWork} division'



def GetName(self):
	 return {self.Name}



def GetSal(self):
	 return self.Salary



w1=Worker("William Bowers",24,0,2500)
w2=Worker('Thomas Hernandez',58,5,7000)
w3=Worker('Bryan Wilson',37,2,8760)
w4=Worker('Gregory House',45,9,5400)
w5=Worker('Steven Martin',68,12,10)


print('map')
a=[w1,w2,w3,w4,w5]
b = []
for i in range(5):
	b.append((GetName(a[i])))
print(b)


c1=GetSal(a[0])
c2=GetSal(a[1])
c3=GetSal(a[2])
c4=GetSal(a[3])
c5=GetSal(a[4])

print('reduce')
c=c1+c2+c3+c4+c5
print(c)
=======
class Worker:

    def __init__(self,n,a,num,s):
    	self.Name=n
    	self.Age=a
    	self.NumberOfPlaseOfWork=num
    	self.Salary=s
    def Inf(self):
        return f'{self.Name} {self.Age} work in {self.NumberOfPlaseOfWork} division'



def GetName(self):
	 return {self.Name}



def GetSal(self):
	 return self.Salary



w1=Worker("William Bowers",24,0,2500)
w2=Worker('Thomas Hernandez',58,5,7000)
w3=Worker('Bryan Wilson',37,2,8760)
w4=Worker('Gregory House',45,9,5400)
w5=Worker('Steven Martin',68,12,10)


print('map')
a=[w1,w2,w3,w4,w5]
b = []
for i in range(5):
	b.append((GetName(a[i])))
print(b)


c1=GetSal(a[0])
c2=GetSal(a[1])
c3=GetSal(a[2])
c4=GetSal(a[3])
c5=GetSal(a[4])

print('reduce')
c=c1+c2+c3+c4+c5
print(c)
>>>>>>> 0432194c9c9d05f957d69a83343c7f0daf363f82
