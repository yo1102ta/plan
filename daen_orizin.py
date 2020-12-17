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

P = [[0 for a in range(2)] for b in range(20)]

P2 = [[0 for a in range(2)] for b in range(8)]

M1 = [[0 for a in range(2)] for b in range(20)]
M2 = [[0 for a in range(2)] for b in range(8)]

#print (P)

r=10
stride=40
h=20
c=5
C=0
C2=5

print("startX="+str(Sx))
print("startY="+str(Sy))
print("h="+str(h))
print("r="+str(r))
print("stride="+str(stride))
print("resolution="+str(c))

Rx1=Sx
Ry1=Sy+r
Rx2=Sx+stride
Ry2=Sy+r

i=0

while 5+i<=13:
    P[5+i][0]=Sx+C
    P[5+i][1]=Sy+h


    i+=1
    C+=c

j=0
rad1=240
while j<=4:
    rad = math.radians(rad1) #45°の時のラジアンを求める
    x= r * math.cos(rad) #x座標を求める
    y = r * math.sin(rad) #y座標を求める
    #x=int(x)
    #y=int(y)

    P[j][0]=x+Rx1
    P[j][1]=y+Ry1
    j+=1
    rad1-=30

k=14
rad2=60
while k<=19:
    rad = math.radians(rad2) #45°の時のラジアンを求める
    x= r * math.cos(rad) #x座標を求める
    y = r * math.sin(rad) #y座標を求める
    #x=int(x)
    #y=int(y)

    P[k][0]=x+Rx2
    P[k][1]=y+Ry2
    k+=1
    rad2-=30

l=0
while l<=7:
    P2[l][0]=Sx+stride-C2
    P2[l][1]=Sy

    l+=1
    C2+=c

print("P(x,y)")
print (P)
print("P2(x,y)")
print(P2)

print("P_all(x,y)")
print(P+P2)
m=0
while m<=19:
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
