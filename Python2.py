'''


You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z. The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins. How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1.

Sample Input
Expected Output
Available Rs. 1 coins
Available Rs. 5 notes
Amount to be made
Rs. 1 coins needed
Rs. 5 notes needed
2
4
21
1
4
11
2
11
1
2
3
3
19
-1
,,,



def change(one,five,total):
 fivers=total/5
 rest=total-(5*fivers)
 oners=rest/1
 
 if (one*1)<rest:
  print '-1'
 else:
  print oners
  print fivers

if __name__=='__main__':
 total=input('Enter Total:')
 five=input('Enter five:')
 one=input('Enter one:')
 change(one,five,total)
 
