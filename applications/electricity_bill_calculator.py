a=int(input("Enter number of units:"))
if a<=100:
   print("No charge")
elif a>=100and a<=200:
   cost1=(a-100)*5
   print("Total cost is:",cost1)
elif a>200:
   cost2=(a-200)*10+(a-100)*5-(a-200)*5
   print("Total cost is:",cost2)
   
   
#output  
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 program16.py
Enter number of units:350
Total cost is: 2000
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$""" 

 
  
