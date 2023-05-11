print('testing github')
year=input(int('Enter the year to be determined if it is leap year or not: '))
if (year%100!=0 AND Year%4==0) OR year%400==0:
  print(year,' Is a leap year')
else:
  print('This is not a Leap year')
