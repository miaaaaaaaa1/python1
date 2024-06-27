#1

#2
l = int(input("Enter lenght of the line:"))
s = str(input("Enter the simbol:"))
for i in range(l):
    print(s)  

#3

num = int(input("Enter the number:"))
if(num>0):
    print("Number is positive")
elif(num<0):
    print("Number is negative")
elif(num==0):
    print("Number is equal to zero")
elif (num==7):
    break
print("Good bye!")

#4

num1 = int(input("Enter the number:"))
max_num = max(num1)
min_num = min(num1)
sum = (num1)

if num == 7:
            print("Good bye!")
            break

print("Sum:", sum)
print("Maximum:", max_num)
print("Minimum:", min_num)