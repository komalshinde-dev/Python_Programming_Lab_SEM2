
String = input('Enter the string :')
count = 0
String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count+=1
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))
    
#output    
""'pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program24.py
"""Enter the string :hello world"""
"""Total vowels are :3
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$"""




