num = int(input("Enter the list of series:"))
x=0
y=1
z=0
for i in range(num):
    print(z, end=" ")
    x = y
    y = z
    z = x+y
    
