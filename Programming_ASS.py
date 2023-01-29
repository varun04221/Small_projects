#function to calculate echelon form
def echelon(list,int):
    i=list[0]
    if i[int-1]==0:
        count=0
        while i[int-1]==0:
            list.append(i)
            list.remove(i)
            count+=1
            i=list[0]
            if count==len(list):
                global npr
                npr+=1
                break
    else:
        a=i[int-1]
        for j in range(1,len(list)):
            b=list[j][int-1]
            for k in range(len(list[j])):
                list[j][k]=list[j][k]-(b/a)*i[k]
        first_row=list[0]
        list.remove(first_row)
        global ans
        ans.append(first_row)

#function to make all the pivots=1
def scale(list):
    for i in range(len(list)):
        for j in list[i]:
            if j!=0:
                piv=j
                break
            else:
                piv=1
        list[i]=[i/piv for i in list[i]]

#function to convert echelon to RREF
def RREF(list):
    list=list[::-1]
    for i in range(len(list)-1):
        for j in list[i]:
            if j!=0:
                pivcol=list[i].index(j)
                break
            else:
                pivcol=None
        if type(pivcol)==int:
            for k in range(i+1,len(list)):
                list[k][pivcol]=0
    list=list[::-1]

ans=[]#output of echelon form
#INPUT
nrows=int(input("Please Enter the Number of Rows:"))
ncol=int(input("Please Enter the Number of Columns:"))
l=[]
faltu=[]
#Making matrix using enteries of user
for i in range(nrows):
    row=list(map(int,input("Please enter Enteries of Rows:").split()))
    l.append(row)

npr=0
i=len(ans)+1
#Making Echelon Form of matrix
while nrows>0:
    echelon(l,i)
    for j in l:
        if j==[0]*ncol:
            faltu.append(j)
    for m in faltu:
        if m in l:
            l.remove(m)
    nrows=len(l)
    i=len(ans)+1+npr

ans+=faltu

#Echelon form Done
#Now RREF
scale(ans)
RREF(ans)
print("*"*50)
print("RREF of given coefficient matrix is:")
for i in ans:
    print(i)
basic_variables=[]
final_answer=[]
for i in range(len(ans)):
    if ans[i]==[0]*ncol:
        pass
    else:
        flag=True
        kuchh=[]
        for j in range(len(ans[i])):
            if ans[i][j]==1 and flag:
                kuchh.append("x"+str(j+1))
                basic_variables.append("x"+str(j+1))
                flag=False
            elif ans[i][j]!=0:
                kuchh.append(str(-ans[i][j])+"x"+str(j+1))
        final_answer.append(kuchh)
print("*"*50)
all_variables=["x"+str(i) for i in range(1,ncol+1)]
free_variables=[i for i in all_variables if i not in basic_variables]
print("Basic variables are:",*basic_variables)
if len(free_variables)>0:
    print("Free Variables are:",*set(free_variables))
else:
    print("There are no free variables.")
print("*"*50)
print("Solutions are:")
for i in range(len(final_answer)):
    for j in range(1,len(final_answer[i])):
        if final_answer[i][j][0]!="-":
            final_answer[i][j]="+"+final_answer[i][j]

for i in final_answer:
    if len(i)>1:
        print(i[0],"=",*i[1:])
    else:
        print(i[0],"=",0)