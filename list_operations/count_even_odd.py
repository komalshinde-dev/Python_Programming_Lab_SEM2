list1= [10, 21, 4, 45, 66, 93, 1]
 

even_count, odd_count = 0,0

for num in list1:

    if not num & 1:
        even_count += 1
    else:
        odd_count += 1
 

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


#output
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program37.py
Even numbers in the list:  3
Odd numbers in the list:  4
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$""" 





