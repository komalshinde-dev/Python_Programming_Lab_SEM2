num_rows = int(input("Enter the number of rows:"));
i = 1
for i in range(0, num_rows):
    for j in range(0, i+1):
        print("* ", end="")
    i= i + 1
    print()
    
#output   
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program25.py
Enter the number of rows:4
* 
* * 
* * * 
* * * * 
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$"""



