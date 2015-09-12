__author__ = 't5'

num=int(input("enter the desired goal cell number:"));
#position=["right","front","top","below","back","left"]
rightleft=[1,4,6,3]
#rlPosition=["right","below","left","top"]
forback=[2,3,5,4]
#fbPositon=["front","top","back","below"]



def toRight():
     popword=rightleft.pop(len(rightleft)-1)
     rightleft.insert(0,popword)
     forback_syc()


def toForword():
    popword=forback.pop(0)
    forback.append(popword)
    rightleft_syc()

def toLeft():
    popword=rightleft.pop(0)
    rightleft.append(popword)
    forback_syc()

def toBackword():
    popword=forback.pop(len(forback)-1)
    forback.insert(0,popword)
    rightleft_syc()



def forback_syc():
    forback[1]=rightleft[3]
    forback[3]=rightleft[1]

def rightleft_syc():
    rightleft[1]=forback[3]
    rightleft[3]=forback[1]

def fun(n):
  return (1+n)*n/2


moveRightSteps=0
moveForwordSteps=0
moveLeftSteps=0
moveBackWordSteps=0



if(num<=0):
    print("Incorrect value, try again")
elif num==2:
    toRight()
else:
    i=1
    sum=0
    while(2*sum<num-1):
        i=i+1
        sum=fun(i)

    for k in range(1,i):
        if k%2!=0:
            for _ in range(k%4):
                moveRightSteps+=1
                toRight()
            for _ in range(k%4):
                moveForwordSteps+=1
                toForword()


        else:
            for _ in range(k%4):
                moveLeftSteps+=1
                toLeft()
            for _ in range(k%4):
                moveBackWordSteps+=1
                toBackword()

    spareStep=num-i*(i-1)-1

    if i%2!=0:
        if spareStep<=i:
            for _ in range(spareStep%4):
                moveRightSteps+=1
                toRight()
        else:
            for _ in range(i%4):
                moveRightSteps+=1
                toRight()
            for _ in range((spareStep-i)%4):
                moveForwordSteps+=1
                toForword()

    else:
        if spareStep<=i:
            for _ in range(spareStep%4):
                moveLeftSteps+=1
                toLeft()
        else:
            for _ in range(i%4):
                moveLeftSteps+=1
                toLeft()
            for _ in range((spareStep-i)%4):
                moveBackWordSteps+=1
                toBackword()

print('On cell {0}, {1} is at the top, {2} at the front, and {3} on the right.'.format(num,forback[1],forback[0],rightleft[0]))
