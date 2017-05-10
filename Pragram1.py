'''
Write a python program to find and display the product of three positive integer values based on the rule mentioned below:

It should display the product of the three values except when one of the integer value is 7. In that case, 7 should not be included in the product and the values to its left also should not be included.
If there is only one value to be considered, display that value itself. If no values can be included in the product, display -1.

Note: Assume that if 7 is one of the positive integer values, then it will occur only once. Refer the sample I/O given below.

Sample Input
Expected Output
1, 5, 3
15
3, 7, 8
8
7, 4, 3
12
1, 5, 7
-1
'''

def addition(number1,number2,number3):
 number=[number1,number2,number3]
 print number
 try:
  i=number.index(7)
 except ValueError:
  i=-1
 if i!=-1:
  if i==1:
   print number[2]
  elif i==0:
   print number2*number3
  elif i==2:
   print '-1'
 else:
  print number1*number2*number3
  
  
 
 
if __name__=='__main__':
 number1=input('Enter first:')
 number2=input('Enter second:')
 number3=input('Enter third:')
 addition(number1,number2,number3)
