#coding: UTF-8
import sys
sys.path.append('..\\..\\Rcb4Lib') #Rcb4Libの検索パスを追加

from Rcb4BaseLib import Rcb4BaseLib            #Rcb4BaseLib.pyの中のRcb4BaseLibが使えるように設定
import time                   #timeが使えるように宣言

rcb4 = Rcb4BaseLib()      #rcb4をインスタンス(定義)
        
rcb4.open('COM9',1250000,1.3)  #(portName,bundrate,timeout(s))


print(rcb4.getSinglePos(0,1))   #ID0番、SIOピン1番の角度を取得

data=[[0,1],[1,1]]

rcb4.setServoPos(data,20)

frm=50

rcb4.setSingleServo(7,1,10000,frm)
rcb4.setSingleServo(7,2,5000,frm)



for i in range(5):
    time.sleep(1)
    rcb4.setSingleServo(8,1,5000,frm)
    rcb4.setSingleServo(8,2,7500,30)
    print(rcb4.getSinglePos(0,1))
    time.sleep(1)
    rcb4.setSingleServo(8,1,7500,frm)
    rcb4.setSingleServo(8,2,10000,frm)
    print(rcb4.getSinglePos(0,1))

time.sleep(1)
rcb4.setSingleServo(8,2,7500,frm)
# rcb4.setSingleServo(0,1,7500,5)
rcb4.motionPlay(2)

#ACKコマンドを送ってRCB4と接続できるか確認
if rcb4.checkAcknowledge() == True:
    print ('checkAcknowledge OK')
    print ('Version    -->' ,rcb4.Version)   
else:
    print ('\n\ncheckAcknowledge error')


rcb4.close()