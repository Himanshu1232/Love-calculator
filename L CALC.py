name1="eddneiwfwfkfmnfwo"
name2="weifjwfewfjwfepwe"
fname=name1+name2
print(fname)
fname=fname.lower()
total=0
total+=fname.count('t')
total+=fname.count('r')
total+=fname.count('u')
total+=fname.count('e')
print(total)
love=0
love+=fname.count('l')
love+=fname.count('o')
love+=fname.count('v')
love+=fname.count('e')
print(love)
score=int(str(total)+str(love))
print("score=",score)
if score>=70 and score<=100:
    print("your score is",score,"your love life will be great")
else:
    print("your score is",score,"your love life will be ok")
