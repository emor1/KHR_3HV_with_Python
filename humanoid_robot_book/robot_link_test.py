"""
ヒューマノイドロボットで紹介されているようなリンク構造を表わすデータフィールドをPythonで記述するテスト

"""
import numpy as np

class uLinks:
    def __init__(self,name,sister,chiled):
        self.name=name          #自分の名前
        self.sister=sister      #妹リンク
        self.chiled=chiled      #子リンク

        # ,mother,P,R,v,W,q,dq,ddq,a,b,vertex,face,m,c,I
        # self.mother=mother      #親リンク
        # self.P=P                #ワールド座標系での位置
        # self.R=R                #ワールド座標系での姿勢
        # self.v=v                #ワールド座標系での速度
        # self.W=W                #ワールド座標系での角速度ベクトル
        # self.q=q                #関節位置
        # self.dq=dq              #関節速度
        # self.ddq=ddq            #関節加速度
        # self.a=a                #関節軸ベクトル
        # self.b=b                #相対位置
        # self.vertex=vertex      #形状
        # self.face=face          #接続情報
        # self.m=m                #質量
        # self.c=c                #重心位置（自リンク相対）
        # self.I=I                #リンク構造のデータフィールド

#ロボットのデータ構造
all_link=   [
            ["BODY", 0 - 1, 2 - 1],
            ["RARM", 4 - 1, 3 - 1],
            ["RHAND", 0 - 1, 0 - 1],
            ["LARM", 6 - 1, 5 - 1],
            ["LHAND", 0 - 1, 0 - 1],
            ["RLEG", 8 - 1, 7 - 1],
            ["RFOOT", 0 - 1, 0 - 1],
            ["LLEG", 0 - 1, 9 - 1],
            ["LFOOT", 0 - 1, 0 - 1]
]
links=[]
print(all_link[0])


#ロボットのリンクをそれぞれインスタンス化してlinksリストに代入
def setup():
    for i in range(len(all_link)):
        links.append(uLinks(all_link[i][0],all_link[i][1],all_link[i][2]))

#リンクの名前を全て表示する関数
def PrintLinkName(j):
    if j>=0:
        print("j=",j," : ",links[j].name)
        #再帰呼び出しにより表示
        PrintLinkName(links[j].chiled)
        PrintLinkName(links[j].sister)

#リンクの質量の合計を求める関数
def TotalMass(j):
    m=0
    if j==0:
        m=0
    else:
        m=links[j].m+TotalMass(links[j].sister)+TotalMass(links[j].chiled)
    return m


if __name__=="__main__":
    setup()
    print(links[links[links[0].chiled].chiled].name)
    PrintLinkName(0)