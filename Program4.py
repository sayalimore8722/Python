def currency_cal(currency,amount):
 if currency=='Euro' or 'euro':
  needed_cur=amount*0.01417
 elif currency=='Pound' or 'pound':
  needed_cur=amount*0.0100
 elif currency=='A doller':
  needed_cur=amount*0.02140
 elif currency=='C doller':
  needed_cur=amount*0.02027
 return needed_cur

if __name__=='__main__':
 currency=input('Enter Currency:')
 amount=input('Enter amount:')
 needed_cur=currency_cal(currency,amount)
 print needed_cur
