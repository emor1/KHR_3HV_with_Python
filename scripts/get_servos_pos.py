#coding: UTF-8
import sys
sys.path.append('..\\..\\Rcb4Lib') #Rcb4Libの検索パスを追加

from Rcb4BaseLib import Rcb4BaseLib            #Rcb4BaseLib.pyの中のRcb4BaseLibが使えるように設定
import time                   #timeが使えるように宣言

rcb4 = Rcb4BaseLib()      #rcb4をインスタンス(定義)
rcb4.open('COM9',1250000,1.3)  #(portName,bundrate,timeout(s))


length=65

#ポジションから角度を求める関数
def calculate_deg(pos):
    return (pos-3500)/29.6

#角度からポジションを求める関数
def calculate_pos(deg):
    degree=(deg*29.6)+3500
    return int(degree)

if rcb4.checkAcknowledge() == True:  #通信が返ってきたとき

    LLEG_J2=rcb4.getSinglePos(7,1)
    LLEG_J3=rcb4.getSinglePos(8,1)
    LLEG_J4=rcb4.getSinglePos(9,1)

    LLEG_J2=calculate_deg(LLEG_J2[1])
    LLEG_J3=calculate_deg(LLEG_J3[1])
    LLEG_J4=calculate_deg(LLEG_J4[1])

    print(LLEG_J2," deg")
    print(LLEG_J3," deg")
    print(LLEG_J4," deg")
    time.sleep(3)
    rcb4.motionPlay(2)
rcb4.close()