def loan(loanType,loanAmt,salary,emi,balance,accNu):
 carbankstd=36
 housebankstd=60
 businessbankstd=84
 carbankstdloan=500000
 housebankstdloan=6000000
 businessbankstdloan=7500000
 acc1=str(accNu)
 
 if acc1.startswith('1') and len(acc1)<5:
     flag=1
if salary>25000:     

 if loanType=='car':

  if emi<=carbankstd and loanAmt<=carbankstdloan and balance>100000 and flag==1:
   print accNu
   print carbankstdloan
   print loanAmt
   print carbankstd

if salary>50000:
 if loanType=='house':

  if emi<=housebankstd and loanAmt<=housebankstdloan and balance>100000 and flag==1:
   print accNu
   print housebankstdloan
   print loanAmt
   print housebankstd

if salary>75000:
 if loanType=='business':

  if emi<=businessbankstd and loanAmt<=businessbankstdloan and balance>100000 and flag==1:
   print accNu
   print businessbankstdloan
   print loanAmt
   print businessbankstd


if __name__=='__main__':
 loanType=input('Type:')
 loanAmt=input('Amt:')
 salary=input('Salary:')
 emi=input('Emi:')
 balance=input('Balance:')
 accNu=input('Account Number:')
 
 loan(loanType,loanAmt,salary,emi,balance,accNu)