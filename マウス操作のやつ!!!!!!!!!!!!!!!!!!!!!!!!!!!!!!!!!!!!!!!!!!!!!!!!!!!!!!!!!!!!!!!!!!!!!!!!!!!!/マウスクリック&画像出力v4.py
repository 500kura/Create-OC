#for分でimg代入v4
#-*- coding: utf8 -*-
import sys
import tkinter as tk
from PIL import Image, ImageTk
import urllib.request as req

# ボタンが押されたら呼び出される関数
def deleteEntry(event):
    # Entryの中身をすべて削除します
    root.destroy()

root = tk.Tk()
root.geometry('900x400')
root.title('IMG')

img={}
for i in range(1,4):
	img[i] = Image.open(open(str(i)+'.JPG', 'rb'))
	img[i].thumbnail((200, 200), Image.ANTIALIAS) #画像の大きさ最大値
	img[i] = ImageTk.PhotoImage(img[i])  # 表示するイメージを用意
	

################################
  
canvas1 = tk.Canvas(
    root, # 親要素をメインウィンドウに設定
    width=500,  # 幅を設定
    height=500 # 高さを設定
    #relief=tk.RIDGE  # 枠線を表示
    # 枠線の幅を設定
)
canvas1.place(x=0, y=0)  # メインウィンドウ上に配置
canvas1.create_image(  # キャンバス上にイメージを配置
    0,  # x座標
    0,  # y座標
    image=img[1],  # 配置するイメージオブジェクトを指定
    tag="illust",  # タグで引数を追加する。
    anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
)

################################
#PILでjpgを使用

canvas2 = tk.Canvas(
    root, # 親要素をメインウィンドウに設定
    width=500,  # 幅を設定
    height=500 # 高さを設定
    #relief=tk.RIDGE  # 枠線を表示
    # 枠線の幅を設定
)
canvas2.place(x=300, y=0)  # メインウィンドウ上に配置
canvas2.create_image(  # キャンバス上にイメージを配置
    0,  # x座標
    0,  # y座標
    image=img[2],  # 配置するイメージオブジェクトを指定
    tag="illust",  # タグで引数を追加する。
    anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
)
################################
#PILでjpgを使用

canvas3 = tk.Canvas(
    root, # 親要素をメインウィンドウに設定
    width=500,  # 幅を設定
    height=500 # 高さを設定
    #relief=tk.RIDGE  # 枠線を表示
    # 枠線の幅を設定
)
canvas3.place(x=600, y=0)  # メインウィンドウ上に配置
canvas3.create_image(  # キャンバス上にイメージを配置
    0,  # x座標
    0,  # y座標
    image=img[3],  # 配置するイメージオブジェクトを指定
    tag="illust",  # タグで引数を追加する。
    anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#

# Buttonを設置してみる
Button1 = tk.Button(text=u'何も起こらないボタン')
Button1.pack()
Button1.place(x=350, y=230)
# Buttonを設置してみる
Button2 = tk.Button(text=u'消すボタン',)
Button2.bind("<Button-1>", deleteEntry)        # ボタンが押されたときに実行される関数をバインドします
Button2.pack()
Button2.place(x=350, y=255)

root.mainloop()