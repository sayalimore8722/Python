def delivery(ftype,quantity,km):
 costtillsix=9
 cost=0
 if ftype=='V' or 'v':
  if km>6:
    remain=km-6
    partialcost=remain*6
    cost=partialcost+costtillsix+(120*quantity)
  elif km>3:
    remain=km-3
    partialcost=remain*3
    cost=partialcost+(120*quantity)
    
 elif ftype=='N' or 'n':
  if km>6:
    remain=km-6
    partialcost=remain*6
    cost=partialcost+costtillsix+(150*quantity)
  elif km>3:
    remain=km-3
    partialcost=remain*3
    cost=(150*quantity)+partialcost
 return cost

if __name__=='__main__':
 type=input('Enter food type:')
 quantity=input('Enter quantity:')
 km=input('Enter km:')
 amount=delivery(type,quantity,km)
 print amount

  
