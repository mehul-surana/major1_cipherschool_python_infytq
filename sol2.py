n=int(input())
records=[]
for i in range(n):
  name=input()
  score=float(input())
  records.append([name,score])
records.sort(key=lambda records:records[1])

a=[]
for i in range(n):
    if records[i][1]!=records[0][1]:
        a.append(records[i][0])
        for j in range(i+1,n):
            if records[j][1]==records[i][1]:
                a.append(records[j][0])
            else:
                break
        break
    else:
        continue
a.sort()
for i in a:
    print(i)


  
  
  
