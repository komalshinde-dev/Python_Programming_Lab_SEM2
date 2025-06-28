seconds=int(input("enter the seconds:"))
hour=seconds//3600
seconds%=3600
minutes=seconds//60
seconds%=60

print("The hours are:",hour)
print("The minutes are:",minutes)
print("The seconds are:",seconds)


#output
"""pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ python3 assignment1.py
enter the seconds:3666
The hours are: 1
The minutes are: 1
The seconds are: 6
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B3_57/SEM II$ """


