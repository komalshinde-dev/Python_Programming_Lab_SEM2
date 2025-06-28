str=input("enter a string: ")
l=(len(str)//2)
if (str[ : :l]==str[l : :]):
   print("string is not a palindrome")
else:
   print("it is a palindrome")
if (str[ :l]==str[l: ]):
   print("string is symmetric")
else:
   print("it is not symmetric")
   
   
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program31.py
enter a string: khokho
it is a palindrome
string is symmetric
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program31.py
enter a string: madam
it is a palindrome
it is not symmetric
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$""" 



   
