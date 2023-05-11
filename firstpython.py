print('Welcome to the git Test \n==========================')
print('This is a program to determine if the year you were born is a leap year')
year=input(int('Enter the year to be determined if it is leap year or not: '))
if ( year%100!=0  and  year%4==0) or year%400==0 :
  print(year,' Is a leap year')
else:
  print('This is not a Leap year')
