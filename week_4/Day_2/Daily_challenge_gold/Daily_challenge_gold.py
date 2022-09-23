#Daily Challenge Gold
print("Daily Challenge of Birthdate:\n")

age = input("Enter your brithdate: DD/MM/YYYY : \t")
print('Your birthdate = ',age)
age=age[6:len(age)]
print('Your year of born is =',age)
y=int(age)
age=2022 - int(age)
print('Your age is = ',age)
age=str(age)[-1]
age=int(age)
val=int((13-age)/2)
print(val)
print('the number of candles = ',age)
for i in range(3):
    print(' ',end='')
for i in range(val):
    print('-',end='')
for i in range(age):
    print('i',end='')
for i in range(val):
    print('-',end='')
for i in range(3):
    print(' ',end='')
print(' ')
for i in range(3):
    print(' ',end='')
print('|:H:a:p:p:y:|')
for i in range(2):
    print(' ',end='')
for i in range(1):
    print(' ',end='')
print('|           |')
for i in range(0):
    print(' ',end='')
for i in range(19):
    print(' ',end='')
print('')
print('|^^^^^^^^^^^^^^^^^|')
print('|:B:i:r:t:h:d:a:y:|')
print('|                 |')
print('|                 |')
print('~~~~~~~~~~~~~~~~~~|')