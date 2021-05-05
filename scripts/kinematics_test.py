#coding: UTF-8
import sys
import math
sys.path.append('..\\..\\Rcb4Lib')                  #Rcb4Libの検索パスを追加
from Rcb4BaseLib import Rcb4BaseLib                 #Rcb4BaseLib.pyの中のRcb4BaseLibが使えるように設定
import time                                         #timeが使えるように宣言
rcb4 = Rcb4BaseLib()                                #rcb4をインスタンス(定義)
rcb4.open('COM9',1250000,1.3)                       #(portName,bundrate,timeout(s))

import get_servos_pos                               #角度やポジションの計算のメソッドをインポート

length1=65
length2=length1*2
length3=length1*3

#逆運動学計算
def InverseKinematics(x,y):
    OP=math.sqrt(x**2+y**2)
    N=(length1**2+length2**2-OP**2)/(2*length1*length2)
    alpha=math.acos(N)
    try:
        beta=math.acos((length1**2+OP**2-length2**2)/(2*length1*length2))
    except ValueError:
        M=(length1**2+OP**2-length2**2)/(2*length1*length2)
        if M>1:
            print("Value over; deg = 1")
            beta=0
        else:
            print("Value is too small")
            beta=90

    ganma=math.acos(x/OP)
    deg1=math.degrees(ganma-beta)
    deg2=math.degrees(math.pi-alpha)
    return deg1,deg2

#順運動学計算
def ForwardKinematics(deg1,deg2):
    x=length1*math.cos(math.radians(deg1))+length2*math.cos(math.radians(deg1+deg2))
    y=length1*math.sin(math.radians(deg1))+length2*math.sin(math.radians(deg1+deg2))
    return x,y

def change_deg(n,deg):
    if n==7:
        deg=135+90-deg        #135度の地点を90度として計算(0度が後ろの方向へ)
    elif n==8:
        deg=deg+45+90         #135度の地点を90度として計算(270度が後ろの方向へ)
    return deg

# if rcb4.checkAcknowledge() == True:  #通信が返ってきたとき
def aaa():
    # deg1=0         #範囲は-45~225
    # deg2=90         #範囲は-45~225

    # X,Y=ForwardKinematics(deg1,deg2)

    for i in range(5):
        deg1,deg2=InverseKinematics(0,160-i*20)
    # deg1,deg2=InverseKinematics(0,140)

        deg1=change_deg(7,deg1)
        deg2=change_deg(8,deg2)
        print(deg1,deg2)

        rcb4.setSingleServo(7,1,get_servos_pos.calculate_pos(deg1),20)
        rcb4.setSingleServo(8,1,get_servos_pos.calculate_pos(deg2),20)
        time.sleep(1)


    time.sleep(5)

    for i in range(5):
        deg1,deg2=InverseKinematics(0,80+i*20)
    # deg1,deg2=InverseKinematics(0,140)

        deg1=change_deg(7,deg1)
        deg2=change_deg(8,deg2)
        print(deg1,deg2)

        rcb4.setSingleServo(7,1,get_servos_pos.calculate_pos(deg1),20)
        rcb4.setSingleServo(8,1,get_servos_pos.calculate_pos(deg2),20)
        time.sleep(1)


    rcb4.motionPlay(2)
# else:
#     print("Error : check the connection or a battery")

    rcb4.close()

aaa()