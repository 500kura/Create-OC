#画像＆マウスできたああああああああああああ
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
root.geometry('1080x1920')
root.title('IMG')


canvas1 = tk.Canvas(
    root, # 親要素をメインウィンドウに設定
    width=500,  # 幅を設定
    height=500 # 高さを設定
    #relief=tk.RIDGE  # 枠線を表示
    # 枠線の幅を設定
)
 
canvas1.place(x=0, y=0)  # メインウィンドウ上に配置

img1 = Image.open(open('IMG_0004.JPG', 'rb'))
img1.thumbnail((500, 500), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)  # 表示するイメージを用意
  
#PILでjpgを使用
img1 = Image.open(open('無題.png', 'rb'))
img1.thumbnail((500, 500), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)  # 表示するイメージを用意

canvas1.create_image(  # キャンバス上にイメージを配置
    0,  # x座標
    0,  # y座標
    image=img1,  # 配置するイメージオブジェクトを指定
    tag="illust",  # タグで引数を追加する。
    anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
)
# Buttonを設置してみる
Button1 = tk.Button(text=u'何も起こらないボタン')
Button1.pack()
# Buttonを設置してみる
Button2 = tk.Button(text=u'消すボタン', width=50)
Button2.bind("<Button-1>", deleteEntry)        # ボタンが押されたときに実行される関数をバインドします
Button2.pack()

root.mainloop()