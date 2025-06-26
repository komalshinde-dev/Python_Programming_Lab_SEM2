num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))

if(num1>=num2)and(num1>=num3):
  largest=num1
elif(num2>=num1)and(num2>=num3):
  largest=num2
else:
  largest=num3
print("The largest number is:",largest)

#output
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program12.py
Enter first number:5
Enter second number:7
Enter third number:9
The largest number is: 9.0
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$""" 

