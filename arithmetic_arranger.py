from curses.ascii import isdigit
import math 
def arithmetic_arranger(s,h=False):
  
  m=""
  m1,m2,m3,m4=[],[],[],[]
  x1,x2,x3=[],[],[]
  if len(s) > 5 : 
    return ("Error: Too many problems.")
  if s[-1] == True:
    h=True
  r=[]
  for i in s:
    x=i.split(" ")
    x1.append(x[0])
    x2.append(x[1])
    x3.append(x[2])
    if x[1] not in ["+","-"] :
      return ("Error: Operator must be '+' or '-'.")
      
    if len(x[0]) > 4 or len(x[2]) > 4 :
      return "Error: Numbers cannot be more than four digits."
      
    if not( x[0].isdigit() and x[2].isdigit() ) :
        return ("Error: Numbers must only contain digits.")
        
    if x[1]=="+" :
      r.append(str(int(x[0])+int(x[2])))
    elif x[1]=="-":
      r.append(str(int(x[0])-int(x[2])))
  for i in range(len(r)):
    if max(len(x1[i]),len(x3[i]))==x1[i]:
      m1.append("  "+x1[i])
    else:
      m1.append("  "+" "*(len(x3[i])-len(x1[i]))+x1[i])
  m+="    ".join(m1)+"\n"
  for i in range(len(r)):
    if max(len(x1[i]),len(x3[i]))==x3[i]:
      m2.append(x2[i]+" "+x3[i])
    else:
      m2.append(x2[i]+" "+" "*(len(x1[i])-len(x3[i]))+x3[i])
  m+="    ".join(m2)+"\n"
  for i in range(len(r)):
    m3.append("-"*(2+max(len(x1[i]),len(x3[i]))))
  m+="    ".join(m3)+"\n"
  if h:
    for i in range(len(r)):
      m4.append(abs(2+max(len(x1[i]),len(x3[i]))-len(r[i]))*" "+r[i])
    m+="    ".join(m4)
  else : 
      m=m[:-1]

  return m
