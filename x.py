# 1

start = int(input("Enter the first number:"))
finish = int(input("Enter the second number:"))
for i in range(start, finish):
 if(i%7==0):
    print(i)

#2

start1 = int(input("Enter the first number:"))
finish1 = int(input("Enter the second number:"))
for i in range(start1, finish1):
  print(i)
for i in range( finish1, start1, -1):
  print(i)
for i in range(start1, finish1):
  if(i%7==0):
    print(i)
count = 0
for i in range(start1, finish1):
 if (i%5==0):
  count += 1
  print(count)

#3

start2 = int(input("Enter the first number:"))
finish2 = int(input("Enter the second number:"))
for i in range(start2, finish2):
 if(i%3==0):
    print("Fizz")
 elif(i%5==0):
    print("Buzz")
 elif(i%3==0, i%5==0):
   print("Fizz Buzz")
 else:
   print(i)




