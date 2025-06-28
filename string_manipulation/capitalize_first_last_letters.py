str =input("Enter the string:")
s = str.split()
print(s)
for i in s:
    a = i[0].upper()+i[1:-1]+i[-1].upper()
    
    print(a,end=" ") 

#output
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program34.py
Enter the string:i am a student
['i', 'am', 'a', 'student']
II AM AA StudenT pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ 
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program34.py
Enter the string:python programming
['python', 'programming']
PythoN ProgramminG pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$"""














