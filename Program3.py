def salary(level,currentsal):
 if level==3:
  incentives=currentsal*(0.15)
  print incentives
  newsal=currentsal+incentives
 elif level==4:
  incentives=currentsal*(0.07)
  newsal=currentsal+incentives  
 elif level==5:
  incentives=currentsal*(0.05)
  newsal=currentsal+incentives  
 else:
  newsal=currentsal
 return newsal

if __name__=='__main__':
 level=input('Enter Level:')
 currentsal=input('Enter Current salary:') 
 newsal=salary(level,currentsal)
 print newsal
