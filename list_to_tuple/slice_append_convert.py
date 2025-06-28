l1=[]
n=int(input("Enter number of elements in the list greater than 5:"))
for i in range(n):
    l1.append(input(f"Enter the element {i+1}:"))
l2=l1[:5]
l2.append(20)
l2.append(25)
l2.append(30)
l2.append(l1[i])
tup=tuple(l2)
print (f"entered list:{l1}\n converted tuple:{tup}")

#output
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program39.py
Enter number of elements in the list greater than 5:6
Enter the element 1:4
Enter the element 2:8
Enter the element 3:10
Enter the element 4:50
Enter the element 5:20
Enter the element 6:30
entered list:['4', '8', '10', '50', '20', '30']
 converted tuple:('4', '8', '10', '50', '20', 20, 25, 30, '30')
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$""" 



 

    
