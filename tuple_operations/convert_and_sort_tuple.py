d=()
a=[]
b=int(input("Enter the total number of elements:"))

for i in range(0,b):
    c=int(input("Enter the elements:"))
    a.append(c)
d=tuple(a)
print(a)
print(d)
sort_t=tuple(sorted(d))
print(sort_t)

#output
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program38.py
Enter the total number of elements:5
Enter the elements:20
Enter the elements:50
Enter the elements:40
Enter the elements:10
Enter the elements:60
[20, 50, 40, 10, 60]
(20, 50, 40, 10, 60)
(10, 20, 40, 50, 60)
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$""" 




