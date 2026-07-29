import random

#Creation of an unopened board.
D1=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D2=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D3=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D4=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D5=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D6=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D7=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D8=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D9=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D10=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D11=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D12=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D13=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D14=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D15=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D16=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D17=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D18=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D19=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
D20=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]

#Merging in to a 2D list for easier selection.
DALL=[D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20]
for lizt in DALL:
    print(lizt)


#Asking user to choose a box.
ch1=int(input("Enter row= "))
ch2=int(input("Enter column= "))
#Changing values according to indexing rules(to use in 2D list).
ch1=ch1-1
ch2=ch2-1
#Creating lists to store values.
L1=[]
L2=[]
L3=[]
L4=[]
L5=[]
L6=[]
L7=[]
L8=[]
L9=[]
L10=[]
L11=[]
L12=[]
L13=[]
L14=[]
L15=[]
L16=[]
L17=[]
L18=[]
L19=[]
L20=[]
#Randomly choosing number of bombs in each list/row.
n1=random.randint(1,3)
n2=random.randint(1,3)
n3=random.randint(1,3)
n4=random.randint(1,3)
n5=random.randint(1,3)
n6=random.randint(1,3)
n7=random.randint(1,3)
n8=random.randint(1,3)
n9=random.randint(1,3)
n10=random.randint(1,3)
n11=random.randint(1,3)
n12=random.randint(1,3)
n13=random.randint(1,3)
n14=random.randint(1,3)
n15=random.randint(1,3)
n16=random.randint(1,3)
n17=random.randint(1,3)
n18=random.randint(1,3)
n19=random.randint(1,3)
n20=random.randint(1,3)

#User-defined function to add bombs and non-bomb places into the list.
def randomiser(L,n):
    ran=random.randint(0,19)
    for i in range(ran):
        L.append("_")
    L.append("*")
    for i in range(19-ran):
        L.append("_")

    for j in range(n-1):
        ran2=random.randint(0,19)

        if ran2==ran:
            ran2=random.randint(0,19)
            L[ran2]="*"
        else:
            L[ran2]="*"   
randomiser(L1,n1)
randomiser(L2,n2)
randomiser(L3,n3)
randomiser(L4,n4)
randomiser(L5,n5)
randomiser(L6,n6)
randomiser(L7,n7)
randomiser(L8,n8)
randomiser(L9,n9)
randomiser(L10,n10)
randomiser(L11,n11)
randomiser(L12,n12)
randomiser(L13,n13)
randomiser(L14,n14)
randomiser(L15,n15)
randomiser(L16,n16)
randomiser(L17,n17)
randomiser(L18,n18)
randomiser(L19,n19)
randomiser(L20,n20)

ALL=[L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20] #2D list for easier selection

#First click cannot be a bomb. Removing bomb if it appears on first click.
if ALL[ch1][ch2]=='*':
    ALL[ch1][ch2]='_'

#Minesweeper indicates bombs with numbers showing how many bombs are adjacent to it.
#Counting bombs and adding numbers to the lists.

for i in range(20):
    for j in range(20):
        if ALL[i][j]=="*": #Checking if chosen block is a bomb.
            try:
                if ALL[i][j-1]=="*": #If the place next to it is a bomb, 
                    pass #it is passed.
                elif ALL[i][j-1]=="_": #If the place next to it isn't a bomb,
                    ALL[i][j-1]=1 #We replace it with a numeric value to add on to it later.
            except IndexError:
                pass
            try:
                if ALL[i][j+1]=="*":
                    pass
                elif ALL[i][j+1]=="_":
                    ALL[i][j+1]=1
            except IndexError:
                pass
            try:
                if ALL[i+1][j]=="*":
                    pass
                elif ALL[i+1][j]=="_":
                    ALL[i+1][j]=1
                elif ALL[i+1][j] in [1,2,3]:
                    ALL[i+1][j]+=1
                elif ALL[i+1][j]==4:
                    pass
            except IndexError:
                pass
            try:
                if ALL[i+1][j-1]=="*":
                    pass
                elif ALL[i+1][j-1]=="_":
                    ALL[i+1][j-1]=1
                elif ALL[i+1][j-1] in [1,2,3]:
                    ALL[i+1][j-1]+=1
                elif ALL[i+1][j-1]==4:
                    pass
            except IndexError:
                pass
            try:
                if ALL[i+1][j+1]=="*":
                    pass
                elif ALL[i+1][j+1]=="_":
                    ALL[i+1][j+1]=1
                elif ALL[i+1][j+1] in [1,2,3]:
                    ALL[i+1][j+1]+=1
                elif ALL[i+1][j+1]==4:
                    pass
            except IndexError:
                pass
            try:
                if ALL[i-1][j]=="*":
                    pass
                elif ALL[i-1][j]=="_":
                    ALL[i-1][j]=1
                elif ALL[i-1][j] in [1,2,3]:
                    ALL[i-1][j]+=1
                elif ALL[i-1][j]==4:
                    pass
            except IndexError:
                pass
            try:
                if ALL[i-1][j-1]=="*":
                    pass
                elif ALL[i-1][j-1]=="_":
                    ALL[i-1][j-1]=1
                elif ALL[i-1][j-1] in [1,2,3]:
                    ALL[i-1][j-1]+=1
                elif ALL[i-1][j-1]==4:
                    pass
            except IndexError:
                pass
            try:
                if ALL[i-1][j+1]=="*":
                    pass
                elif ALL[i-1][j+1]=="_":
                    ALL[i-1][j+1]=1
                elif ALL[i-1][j+1] in [1,2,3]:
                    ALL[i-1][j+1]+=1
                elif ALL[i-1][j+1]==4:
                    pass
            except IndexError:
                pass

ALL=[L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20]
for wt in range(20):
    for wt2 in range(20):
        if ALL[wt][wt2] in [1,2,3,4]:
            ALL[wt][wt2] = str(ALL[wt][wt2]) #Converting all numeric values to string.

#Number of mines in the board.
bcount=0
for l in ALL:
    for b in l:
        if b=='*':
            bcount+=1

#Number of clean boxes in the board.
cleancount=400-bcount


#Opening the DALL board according to user's choice.
#Swapping out items of list DALL with list ALL's items.
nval=ALL[ch1][ch2]
DALL[ch1][ch2]=nval

#Number of clean boxes user has opened.
lclean=1

#3X3 opening around the chosen box.
try:
    if ch2-1<0: #To avoid negative indexing, we pass if the value becomes negative.
        pass
    elif ALL[ch1][ch2-1] not in '*': #If the nearby boxes are not bombs, we open it
        nval=ALL[ch1][ch2-1] #by swapping out the boxes in list DALL.
        DALL[ch1][ch2-1]=nval
        lclean+=1 #adding to lclean when a new clean box is opened.
except IndexError:
    pass

try:
    if ALL[ch1][ch2+1] not in '*':
        nval=ALL[ch1][ch2+1]
        DALL[ch1][ch2+1]=nval
        lclean+=1
except IndexError:
    pass

try:
    if ch1-1<0:
        pass
    elif ALL[ch1-1][ch2] not in '*':
        nval=ALL[ch1-1][ch2]
        DALL[ch1-1][ch2]=nval
        lclean+=1
except IndexError:
    pass

try:
    if ch1-1<0 or ch2-1<0:
        pass
    elif ALL[ch1-1][ch2-1] not in '*':
        nval=ALL[ch1-1][ch2-1]
        DALL[ch1-1][ch2-1]=nval
        lclean+=1
except IndexError:
    pass

try:
    if ch1-1<0:
        pass
    elif ALL[ch1-1][ch2+1] not in '*':
        nval=ALL[ch1-1][ch2+1]
        DALL[ch1-1][ch2+1]=nval
        lclean+=1
except IndexError:
    pass

try:
    if ALL[ch1+1][ch2] not in '*':
        nval=ALL[ch1+1][ch2]
        DALL[ch1+1][ch2]=nval
        lclean+=1
except IndexError:
    pass

try:
    if ch2-1<0:
        pass
    elif ALL[ch1+1][ch2-1] not in '*':
        nval=ALL[ch1+1][ch2-1]
        DALL[ch1+1][ch2-1]=nval
        lclean+=1
except IndexError:
    pass


try:
    if ALL[ch1+1][ch2+1] not in '*':
        nval=ALL[ch1+1][ch2+1]
        DALL[ch1+1][ch2+1]=nval
        lclean+=1
except IndexError:
    pass


#5x5 opening around the 3x3 if there no bomb in the 3x3 opening.
try:
    if ALL[ch1][ch2-1] not in '*' and ALL[ch1][ch2+1] not in '*' and ALL[ch1-1][ch2] not in '*' and ALL[ch1-1][ch2-1] not in '*' and ALL[ch1-1][ch2+1] not in '*' and ALL[ch1+1][ch2] not in '*' and ALL[ch1+1][ch2-1] not in '*' and ALL[ch1+1][ch2+1] not in '*':
        try:
            if ch2-2<0:
                pass
            elif ALL[ch1][ch2-2] not in '*':
                nval=ALL[ch1][ch2-2]
                DALL[ch1][ch2-2]=nval
                lclean+=1
        except IndexError:
            pass
    
        try:
            if ch1-2<0:
                pass
            elif ALL[ch1][ch2+2] not in '*':
                nval=ALL[ch1][ch2+2]
                DALL[ch1][ch2+2]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch1-2<0:
                pass
            elif ALL[ch1-1][ch2-2] not in '*':
                nval=ALL[ch1-1][ch2-2]
                DALL[ch1-1][ch2-2]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch1-2<0:
                pass
            elif ALL[ch1-1][ch2+2] not in '*':
                nval=ALL[ch1-1][ch2+2]
                DALL[ch1-1][ch2+2]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch1-2<0:
                pass
            elif ALL[ch1+1][ch2-2] not in '*':
                nval=ALL[ch1+1][ch2-2]
                DALL[ch1+1][ch2-2]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch1-2<0:
                pass
            elif ALL[ch1+1][ch2+2] not in '*':
                nval=ALL[ch1+1][ch2+2]
                DALL[ch1+1][ch2+2]=nval
                lclean+=1
        except IndexError:
            pass
        
        try:
            if ch1-2<0:
                pass
            elif ALL[ch1-2][ch2] not in '*':
                nval=ALL[ch1-2][ch2]
                DALL[ch1-2][ch2]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch1-2<0 or ch2-2<0:
                pass
            elif ALL[ch1-2][ch2-2] not in '*':
                nval=ALL[ch1-2][ch2-2]
                DALL[ch1-2][ch2-2]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch1-2<0:
                pass
            elif ALL[ch1-2][ch2+2] not in '*':
                nval=ALL[ch1-2][ch2+2]
                DALL[ch1-2][ch2+2]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch1-2<0:
                pass
            elif ALL[ch1-2][ch2-1] not in '*':
                nval=ALL[ch1-2][ch2-1]
                DALL[ch1-2][ch2-1]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch1-2<0:
                pass
            elif ALL[ch1-2][ch2+1] not in '*':
                nval=ALL[ch1-2][ch2-1]
                DALL[ch1-2][ch2-1]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch1-2<0:
                pass
            elif ALL[ch1+2][ch2-1] not in '*':
                nval=ALL[ch1+2][ch2-1]
                DALL[ch1+2][ch2-1]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch1-2<0:
                pass
            elif ALL[ch1+2][ch2+1] not in '*':
                nval=ALL[ch1+2][ch2+1]
                DALL[ch1+2][ch2+1]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ALL[ch1+2][ch2] not in '*':
                nval=ALL[ch1+2][ch2]
                DALL[ch1+2][ch2]=nval
                lclean+=1
        except IndexError:
            pass

        try:
            if ch2-2<0:
                pass
            elif ALL[ch1+2][ch2-2] not in '*':
                nval=ALL[ch1+2][ch2-2]
                DALL[ch1+2][ch2-2]=nval
                lclean+=1
        except IndexError:
            pass


        try:
            if ALL[ch1+2][ch2+2] not in '*':
                nval=ALL[ch1+2][ch2+2]
                DALL[ch1+2][ch2+2]=nval
                lclean+=1
        except IndexError:
            pass
        
except IndexError: #Python raises index error when the values are 1 or 20 in the list conditions
    if ch1==1:
        if ALL[ch1][ch2-1] not in '*' and ALL[ch1][ch2+1] not in '*' and ALL[ch1+1][ch2] not in '*' and ALL[ch1+1][ch2-1] not in '*' and ALL[ch1+1][ch2+1] not in '*':
            try:
                if ch2-2<0:
                    pass
                elif ALL[ch1][ch2-2] not in '*':
                    nval=ALL[ch1][ch2-2]
                    DALL[ch1][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass
    
            try:
                if ALL[ch1][ch2+2] not in '*':
                    nval=ALL[ch1][ch2+2]
                    DALL[ch1][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ALL[ch1+2][ch2] not in '*':
                    nval=ALL[ch1+2][ch2]
                    DALL[ch1+2][ch2]=nval
                    lclean+=1
            except IndexError:
                pass
    
            try:
                if ch2-2<0:
                    pass
                elif ALL[ch1+2][ch2-2] not in '*':
                    nval=ALL[ch1+2][ch2-2]
                    DALL[ch1+2][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ALL[ch1+2][ch2+2] not in '*':
                    nval=ALL[ch1+2][ch2+2]
                    DALL[ch1+2][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass
    if ch2==1:
        if ALL[ch1][ch2+1] not in '*' and ALL[ch1-1][ch2] not in '*' and ALL[ch1-1][ch2+1] not in '*' and ALL[ch1+1][ch2] not in '*' and ALL[ch1+1][ch2+1] not in '*':
            try:
                if ALL[ch1][ch2+2] not in '*':
                    nval=ALL[ch1][ch2+2]
                    DALL[ch1][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-2][ch2] not in '*':
                    nval=ALL[ch1-2][ch2]
                    DALL[ch1-2][ch2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-2][ch2+2] not in '*':
                    nval=ALL[ch1-2][ch2+2]
                    DALL[ch1-2][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ALL[ch1+2][ch2] not in '*':
                    nval=ALL[ch1+2][ch2]
                    DALL[ch1+2][ch2]=nval
                    lclean+=1
            except IndexError:
                pass
    
            try:
                if ALL[ch1+2][ch2+2] not in '*':
                    nval=ALL[ch1+2][ch2+2]
                    DALL[ch1+2][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass
    if ch1==20:
        if ALL[ch1][ch2-1] not in '*' and ALL[ch1][ch2+1] not in '*' and ALL[ch1-1][ch2] not in '*' and ALL[ch1-1][ch2-1] not in '*' and ALL[ch1-1][ch2+1] not in '*':
            try:
                if ch2-2<0:
                    pass
                elif ALL[ch1][ch2-2] not in '*':
                    nval=ALL[ch1][ch2-2]
                    DALL[ch1][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ALL[ch1][ch2+2] not in '*':
                    nval=ALL[ch1][ch2+2]
                    DALL[ch1][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-2][ch2] not in '*':
                    nval=ALL[ch1-2][ch2]
                    DALL[ch1-2][ch2]=nval
                    lclean+=1
            except IndexError:
                pass
    
            try:
                if ch1-2<0 or ch2-2<0:
                    pass
                elif ALL[ch1-2][ch2-2] not in '*':
                    nval=ALL[ch1-2][ch2-2]
                    DALL[ch1-2][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-2][ch2+2] not in '*':
                    nval=ALL[ch1-2][ch2+2]
                    DALL[ch1-2][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass
    if ch2==20:
        if ALL[ch1][ch2-1] not in '*' and ALL[ch1-1][ch2] not in '*' and ALL[ch1-1][ch2-1] not in '*' and ALL[ch1+1][ch2] not in '*' and ALL[ch1+1][ch2-1] not in '*':
            try:
                if ch2-2<0:
                        pass
                elif ALL[ch1][ch2-2] not in '*':
                    nval=ALL[ch1][ch2-2]
                    DALL[ch1][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-2][ch2] not in '*':
                    nval=ALL[ch1-2][ch2]
                    DALL[ch1-2][ch2]=nval
                    lclean+=1
            except IndexError:
                pass
    
            try:
                if ch1-2<0 or ch2-2<0:
                    pass
                elif ALL[ch1-2][ch2-2] not in '*':
                    nval=ALL[ch1-2][ch2-2]
                    DALL[ch1-2][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ALL[ch1+2][ch2] not in '*':
                    nval=ALL[ch1+2][ch2]
                    DALL[ch1+2][ch2]=nval
                    lclean+=1
            except IndexError:
                pass
    
            try:
                if ch2-2<0:
                    pass
                elif ALL[ch1+2][ch2-2] not in '*':
                    nval=ALL[ch1+2][ch2-2]
                    DALL[ch1+2][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass

print("------------------------------------------------------------")
for lizt in DALL:
    print(lizt)

#-----------------------------------------------------------------------------
#Repeating until user clicks on a bomb.

while True:
    ch1=int(input("Enter row= ")) #Repetitive choosing of boxes.
    ch2=int(input("Enter column= "))
    ch1=ch1-1
    ch2=ch2-1
    if ALL[ch1][ch2]=='*': #if the chosen box is a bomb,
        for lizt in ALL:
            print(lizt)
        print("Oops! You stepped on a mine :(")
        break #the while loop is broken.
    else:                #if not, it continues until the user clicks on a bomb.
        nval=ALL[ch1][ch2]
        DALL[ch1][ch2]=nval
        lclean+=1
    try:                
        if ch2-1<0:
            pass
        elif ALL[ch1][ch2-1] not in '*':
            nval=ALL[ch1][ch2-1]
            DALL[ch1][ch2-1]=nval
            lclean+=1
    except IndexError:
        pass

    try:
        if ALL[ch1][ch2+1] not in '*':
            nval=ALL[ch1][ch2+1]
            DALL[ch1][ch2+1]=nval
            lclean+=1
    except IndexError:
        pass

    try:
        if ch1-1<0:
            pass
        elif ALL[ch1-1][ch2] not in '*':
            nval=ALL[ch1-1][ch2]
            DALL[ch1-1][ch2]=nval
            lclean+=1
    except IndexError:
        pass

    try:
        if ch1-1<0 or ch2-1<0:
           pass
        elif ALL[ch1-1][ch2-1] not in '*':
            nval=ALL[ch1-1][ch2-1]
            DALL[ch1-1][ch2-1]=nval
            lclean+=1
    except IndexError:
        pass

    try:
        if ch1-1<0:
            pass
        elif ALL[ch1-1][ch2+1] not in '*':
            nval=ALL[ch1-1][ch2+1]
            DALL[ch1-1][ch2+1]=nval
            lclean+=1
    except IndexError:
        pass

    try:
        if ALL[ch1+1][ch2] not in '*':
            nval=ALL[ch1+1][ch2]
            DALL[ch1+1][ch2]=nval
            lclean+=1
    except IndexError:
        pass

    try:
        if ch2-1<0:
            pass
        elif ALL[ch1+1][ch2-1] not in '*':
            nval=ALL[ch1+1][ch2-1]
            DALL[ch1+1][ch2-1]=nval
            lclean+=1
    except IndexError:
        pass


    try:
        if ALL[ch1+1][ch2+1] not in '*':
            nval=ALL[ch1+1][ch2+1]
            DALL[ch1+1][ch2+1]=nval
            lclean+=1
    except IndexError:
        pass
    try:
        if ALL[ch1][ch2-1] not in '*' and ALL[ch1][ch2+1] not in '*' and ALL[ch1-1][ch2] not in '*' and ALL[ch1-1][ch2-1] not in '*' and ALL[ch1-1][ch2+1] not in '*' and ALL[ch1+1][ch2] not in '*' and ALL[ch1+1][ch2-1] not in '*' and ALL[ch1+1][ch2+1] not in '*':
            try:
                if ch2-2<0:
                    pass
                elif ALL[ch1][ch2-2] not in '*':
                    nval=ALL[ch1][ch2-2]
                    DALL[ch1][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass
        
            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1][ch2+2] not in '*':
                    nval=ALL[ch1][ch2+2]
                    DALL[ch1][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-1][ch2-2] not in '*':
                    nval=ALL[ch1-1][ch2-2]
                    DALL[ch1-1][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-1][ch2+2] not in '*':
                    nval=ALL[ch1-1][ch2+2]
                    DALL[ch1-1][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1+1][ch2-2] not in '*':
                    nval=ALL[ch1+1][ch2-2]
                    DALL[ch1+1][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass
    
            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1+1][ch2+2] not in '*':
                    nval=ALL[ch1+1][ch2+2]
                    DALL[ch1+1][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass
        
            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-2][ch2] not in '*':
                    nval=ALL[ch1-2][ch2]
                    DALL[ch1-2][ch2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0 or ch2-2<0:
                    pass
                elif ALL[ch1-2][ch2-2] not in '*':
                    nval=ALL[ch1-2][ch2-2]
                    DALL[ch1-2][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-2][ch2+2] not in '*':
                    nval=ALL[ch1-2][ch2+2]
                    DALL[ch1-2][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-2][ch2-1] not in '*':
                    nval=ALL[ch1-2][ch2-1]
                    DALL[ch1-2][ch2-1]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1-2][ch2+1] not in '*':
                    nval=ALL[ch1-2][ch2-1]
                    DALL[ch1-2][ch2-1]=nval
                    lclean+=1
            except IndexError:
                pass
    
            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1+2][ch2-1] not in '*':
                    nval=ALL[ch1+2][ch2-1]
                    DALL[ch1+2][ch2-1]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch1-2<0:
                    pass
                elif ALL[ch1+2][ch2+1] not in '*':
                    nval=ALL[ch1+2][ch2+1]
                    DALL[ch1+2][ch2+1]=nval
                    lclean+=1
            except IndexError:
                pass
    
            try:
                if ALL[ch1+2][ch2] not in '*':
                    nval=ALL[ch1+2][ch2]
                    DALL[ch1+2][ch2]=nval
                    lclean+=1
            except IndexError:
                pass

            try:
                if ch2-2<0:
                    pass
                elif ALL[ch1+2][ch2-2] not in '*':
                    nval=ALL[ch1+2][ch2-2]
                    DALL[ch1+2][ch2-2]=nval
                    lclean+=1
            except IndexError:
                pass


            try:
                if ALL[ch1+2][ch2+2] not in '*':
                    nval=ALL[ch1+2][ch2+2]
                    DALL[ch1+2][ch2+2]=nval
                    lclean+=1
            except IndexError:
                pass

#When if statment's conditions are out of indexing range:
    except IndexError:
        if ch1==1:
            if ALL[ch1][ch2-1] not in '*' and ALL[ch1][ch2+1] not in '*' and ALL[ch1+1][ch2] not in '*' and ALL[ch1+1][ch2-1] not in '*' and ALL[ch1+1][ch2+1] not in '*':
                try:
                    if ch2-2<0:
                        pass
                    elif ALL[ch1][ch2-2] not in '*':
                        nval=ALL[ch1][ch2-2]
                        DALL[ch1][ch2-2]=nval
                        lclean+=1
                except IndexError:
                    pass
    
                try:
                    if ALL[ch1][ch2+2] not in '*':
                        nval=ALL[ch1][ch2+2]
                        DALL[ch1][ch2+2]=nval
                        lclean+=1
                except IndexError:
                    pass

                try:
                    if ALL[ch1+2][ch2] not in '*':
                        nval=ALL[ch1+2][ch2]
                        DALL[ch1+2][ch2]=nval
                        lclean+=1
                except IndexError:
                    pass
    
                try:
                    if ch2-2<0:
                        pass
                    elif ALL[ch1+2][ch2-2] not in '*':
                        nval=ALL[ch1+2][ch2-2]
                        DALL[ch1+2][ch2-2]=nval
                        lclean+=1
                except IndexError:
                    pass

                try:
                    if ALL[ch1+2][ch2+2] not in '*':
                        nval=ALL[ch1+2][ch2+2]
                        DALL[ch1+2][ch2+2]=nval
                        lclean+=1
                except IndexError:
                    pass
        if ch2==1:
            if ALL[ch1][ch2+1] not in '*' and ALL[ch1-1][ch2] not in '*' and ALL[ch1-1][ch2+1] not in '*' and ALL[ch1+1][ch2] not in '*' and ALL[ch1+1][ch2+1] not in '*':
                try:
                    if ALL[ch1][ch2+2] not in '*':
                        nval=ALL[ch1][ch2+2]
                        DALL[ch1][ch2+2]=nval
                        lclean+=1
                except IndexError:
                    pass

                try:
                    if ch1-2<0:
                        pass
                    elif ALL[ch1-2][ch2] not in '*':
                        nval=ALL[ch1-2][ch2]
                        DALL[ch1-2][ch2]=nval
                        lclean+=1
                except IndexError:
                    pass

                try:
                    if ch1-2<0:
                        pass
                    elif ALL[ch1-2][ch2+2] not in '*':
                        nval=ALL[ch1-2][ch2+2]
                        DALL[ch1-2][ch2+2]=nval
                        lclean+=1
                except IndexError:
                    pass

                try:
                    if ALL[ch1+2][ch2] not in '*':
                        nval=ALL[ch1+2][ch2]
                        DALL[ch1+2][ch2]=nval
                        lclean+=1
                except IndexError:
                    pass
    
                try:
                    if ALL[ch1+2][ch2+2] not in '*':
                        nval=ALL[ch1+2][ch2+2]
                        DALL[ch1+2][ch2+2]=nval
                        lclean+=1
                except IndexError:
                    pass
        if ch1==20:
            if ALL[ch1][ch2-1] not in '*' and ALL[ch1][ch2+1] not in '*' and ALL[ch1-1][ch2] not in '*' and ALL[ch1-1][ch2-1] not in '*' and ALL[ch1-1][ch2+1] not in '*':
                try:
                    if ch2-2<0:
                        pass
                    elif ALL[ch1][ch2-2] not in '*':
                        nval=ALL[ch1][ch2-2]
                        DALL[ch1][ch2-2]=nval
                        lclean+=1
                except IndexError:
                    pass
    
                try:
                    if ALL[ch1][ch2+2] not in '*':
                        nval=ALL[ch1][ch2+2]
                        DALL[ch1][ch2+2]=nval
                        lclean+=1
                except IndexError:
                    pass

                try:
                    if ch1-2<0:
                        pass
                    elif ALL[ch1-2][ch2] not in '*':
                        nval=ALL[ch1-2][ch2]
                        DALL[ch1-2][ch2]=nval
                        lclean+=1
                except IndexError:
                    pass
    
                try:
                    if ch1-2<0 or ch2-2<0:
                        pass
                    elif ALL[ch1-2][ch2-2] not in '*':
                        nval=ALL[ch1-2][ch2-2]
                        DALL[ch1-2][ch2-2]=nval
                        lclean+=1
                except IndexError:
                    pass

                try:
                    if ch1-2<0:
                        pass
                    elif ALL[ch1-2][ch2+2] not in '*':
                        nval=ALL[ch1-2][ch2+2]
                        DALL[ch1-2][ch2+2]=nval
                        lclean+=1
                except IndexError:
                    pass
        if ch2==20:
            if ALL[ch1][ch2-1] not in '*' and ALL[ch1-1][ch2] not in '*' and ALL[ch1-1][ch2-1] not in '*' and ALL[ch1+1][ch2] not in '*' and ALL[ch1+1][ch2-1] not in '*':
                try:
                    if ch2-2<0:
                        pass
                    elif ALL[ch1][ch2-2] not in '*':
                        nval=ALL[ch1][ch2-2]
                        DALL[ch1][ch2-2]=nval
                        lclean+=1
                except IndexError:
                    pass

                try:
                    if ch1-2<0:
                        pass
                    elif ALL[ch1-2][ch2] not in '*':
                        nval=ALL[ch1-2][ch2]
                        DALL[ch1-2][ch2]=nval
                        lclean+=1
                except IndexError:
                    pass
    
                try:
                    if ch1-2<0 or ch2-2<0:
                        pass
                    elif ALL[ch1-2][ch2-2] not in '*':
                        nval=ALL[ch1-2][ch2-2]
                        DALL[ch1-2][ch2-2]=nval
                        lclean+=1
                except IndexError:
                    pass

                try:
                    if ALL[ch1+2][ch2] not in '*':
                        nval=ALL[ch1+2][ch2]
                        DALL[ch1+2][ch2]=nval
                        lclean+=1
                except IndexError:
                    pass
    
                try:
                    if ch2-2<0:
                        pass
                    elif ALL[ch1+2][ch2-2] not in '*':
                        nval=ALL[ch1+2][ch2-2]
                        DALL[ch1+2][ch2-2]=nval
                        lclean+=1
                except IndexError:
                    pass



    for lizt in DALL:
        print(lizt)
    if lclean==cleancount: #if the number of clean boxes chosen by the user is equal
        #to the number of clean boxes,  
        print("CONGRATS! You've won!") #the user has won the game.
        break

