import math
import numpy
import matplotlib.pyplot as plt

fig = plt.figure()

#脚スタート
Sx = 0
Sy = -190

#Linkの長さ
L1 = 108.454
L2 = 116.473

P = [[0 for a in range(2)] for b in range(16)]

P2 = [[0 for a in range(2)] for b in range(8)]

M1= [[0 for a in range(2)] for b in range(16)]
M2 = [[0 for a in range(2)] for b in range(8)]

#print (P)

w=40
h=20
c=5
c1=0
c2=0
c3=0
c4=0
print("startX="+str(Sx))
print("startY="+str(Sy))
print("h="+str(h))
print("w="+str(w))
#print("stride="+str(stride))
print("resolution="+str(c))


i=0
while i<=23:
    if i<=3:
        c1+=c
        P[i][0]=Sx
        P[i][1]=Sy+c1


    elif i>3 and i<=11 :
        c2+=c
        P[i][0]=Sx+c2
        P[i][1]=Sy+h


    elif i>11 and i<=15 :
        c3+=c
        P[i][0]=Sx+w
        P[i][1]=Sy+h-c3

    elif i>15 and i<=23 :
        c4+=c
        P2[i-16][0]=Sx+w-c4
        P2[i-16][1]=Sy


    i+=1


print("P(x,y)")
print (P)
print("P2(x,y)")
print(P2)
print("P_all(x,y)")
print(P+P2)

m=0
while m<=15:
    if P[m][0]==0:
        P[m][0]+=0.000000001
#逆運動学計算↓
    L3 = math.sqrt((P[m][0]*P[m][0]) + (P[m][1]*P[m][1]))
    fai2 = math.acos(((L1*L1) + (L2*L2) - ( L3 * L3)) / (2*L1*L2))
    tht2 = math.pi - fai2
    fai1 = math.acos(((L1*L1) + (L3 * L3) - (L2*L2)) / (2*L1*L3))
    fai0 = math.atan(P[m][1] / P[m][0])
    tht1 = math.atan2(P[m][1] , P[m][0]) - fai1
	#角度計算↓
    deg1 = math.degrees(tht1)
    deg2 = math.degrees(tht2)

    M1[m][0]=(round(deg1)+90)
    M1[m][1]=(round(deg2))

    m+=1

print("foot(ang1,ang2)")
print(M1)

m=0
while m<=7:
    if P2[m][0]==0:
        P2[m][0]+=0.000000001
#逆運動学計算↓
    L3 = math.sqrt((P2[m][0]*P2[m][0]) + (P2[m][1]*P2[m][1]))
    fai2 = math.acos(((L1*L1) + (L2*L2) - ( L3 * L3)) / (2*L1*L2))
    tht2 = math.pi - fai2
    fai1 = math.acos(((L1*L1) + (L3 * L3) - (L2*L2)) / (2*L1*L3))
    fai0 = math.atan(P2[m][1] / P2[m][0])
    tht1 = math.atan2(P2[m][1] , P2[m][0]) - fai1
	#角度計算↓
    deg1 = math.degrees(tht1)
    deg2 = math.degrees(tht2)

    M2[m][0]=(round(deg1)+90)
    M2[m][1]=(round(deg2))

    m+=1

print("foot2(ang1,ang2)")
print(M2)

print("foot_all(ang1,ang2)")
print(M1+M2)
