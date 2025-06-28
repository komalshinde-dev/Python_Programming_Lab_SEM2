rows = int(input('Enter the number of rows:'))

for i in range(rows):
    # nested loop
    for j in range(i):
        print(i, end=' ')
    # new line after each row
    print('')
    
#output    
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program27.py
Enter the number of rows:6

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$""" 



