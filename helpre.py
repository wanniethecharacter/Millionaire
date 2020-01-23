import random





def válogatós_függvény():
    percents= []
    percents.append(random.randrange(40, 89))
    percents.append(random.randrange(0, 100-percents[0]))
    percents.append(random.randrange(0, 100-percents[0]-percents[1]))
    percents.append(100-(percents[0]+percents[1]+percents[2]))
    if percents[0]+percents[1]+percents[2]+percents[3] != 100:
        print(" AUDIENCE HELP IS BROKEN!!!")
    return percents



percents=válogatós_függvény()
index=2
a_percent=0
b_percent=0
c_percent=0
d_percent=0
mylist=[a_percent,b_percent,c_percent,d_percent]
counter=0
for each in range(len(mylist)):
    if mylist[each]==mylist[index]:
        mylist[each]=percents[0]

    if mylist[each]!=válogatós_függvény()[0]:
        mylist[each]=percents[counter]
    counter+=1

if mylist[0]+ mylist[1]+ mylist[2]+ mylist[3]!=100:
    print("FUCK")
print(mylist)