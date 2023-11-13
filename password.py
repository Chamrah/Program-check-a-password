#Program that check password
def NbCMin(passe):
    min = passe
    for i in min:
        if("a"<=min<="z"):
          return len(min)

def NbCMaj(passe):
   max = passe
   for i in max:
      if("A"<=max<="Z"):
         return len(max)

def NbCAlpha(passe):
   alpha = passe
   for i in alpha:
      if(alpha!=str):
        return len(alpha)

def LongMaj(passe):
   LongMaj_X = 0
   LongMaj_Y = 0
   long = passe
   for i in long:
      if(i.isupper()):
         LongMaj_X = LongMaj_X + 1
         if(LongMaj_X > LongMaj_Y):
            LongMaj_Y = LongMaj_X
      else:
        LongMaj_X = 0
   return LongMaj_X
   
def LongMin(passe):
   LongMin_X = 0
   LongMin_Y = 0
   long = passe
   for i in long:
      if(i.isupper()):
         LongMin_X = LongMin_X + 1
         if(LongMin_X > LongMin_Y):
            LongMin_Y = LongMin_X
      else:
         LongMin_X = 0 
   return LongMin_X

def score(passe):
   score1 = 0
   score2 = 0
   score = 0
   
   score1 = (len(passe)*4 + (len(passe)-NbCMaj(passe))*2 + (len(passe)-NbCMin(passe))*3 + (NbCAlpha(passe)*5))
   score2 = (LongMaj(passe)*2) + (LongMin(passe)*2)
   score = score1 - score2
    
s = input("Enter your password : ")
x = score(s)
if(x<20):
   print("Very weak password")
elif(20 <= x < 40):
   print("Weak password")
elif(40 <= x < 80):
   print("Password is strong")
else:
   print("Password is very strong")
