str=input("Enter a string:")
letter=False
digit=False
for i in str:
    if i.isalpha():
        letter=True
    elif i.isdigit():
        digit=True
        
if letter and digit:
   print("string contains both letters and digits")
else:
   print("string does not contain both letters and digits")
   
#output   
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program33.py
Enter a string:python3
string contains both letters and digits
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program33.py
Enter a string:abcd
string does not contain both letters and digits
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$""" 





   
   
   
   
