#UI大改造v8
#-*- coding: utf8 -*-
import sys
import tkinter as tk
from PIL import Image, ImageTk
import urllib.request as req
import os
import cv2
# ボタンが押されたら呼び出される関数 Entryの中身をすべて削除します
def deleteEntry(self):
	print("deleteEntry")
	root.destroy()
    # Entryの中身をすべて削除します
"""
def finishPrg(self):
	print("finishPrg")
	sys.exit()
"""
def Restartmain(self):
	print("写真撮り直す")
	root.destroy()
	main()
def main():
	global root
	root = tk.Tk()
	root.geometry('900x400')
	root.title('IMG')
	img={}
	for i in range(1,4):
		if os.path.exists(str(i)+'.png'):
			img[i] = Image.open(open(str(i)+'.png', 'rb'))
			img[i].thumbnail((200, 200), Image.ANTIALIAS) #画像の大きさ最大値
			img[i] = ImageTk.PhotoImage(img[i])  # 表示するイメージを用意
		else :
			img[i] = Image.open(open(str(i)+'.jpg', 'rb'))
			img[i].thumbnail((200, 200), Image.ANTIALIAS) #画像の大きさ最大値
			img[i] = ImageTk.PhotoImage(img[i])  # 表示するイメージを用意
	################################
	canvas={}
	xx=0
	for i in range(1,4):
		canvas[i] = tk.Canvas(
			root, # 親要素をメインウィンドウに設定
			width=500,  # 幅を設定
			height=500 # 高さを設定
			#relief=tk.RIDGE  # 枠線を表示
			# 枠線の幅を設定
		)
		#PILでjpgを使用
		canvas[i].place(x=xx,y=0) #画像の座標
		xx=xx+300
		canvas[i].create_image(  # キャンバス上にイメージを配置
			0,  # x座標
			0,  # y座標
			image=img[i],  # 配置するイメージオブジェクトを指定
			tag="illust",  # タグで引数を追加する。
			anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
		)
	################################
	print("Button")
	# Buttonを設置してみる
	Button1 = tk.Button(text=u'これでOK')
	Button1.bind("<Button-1>", deleteEntry)        # ボタンが押されたときに実行される関数をバインドします
	Button1.place(x=350, y=230)
	# Buttonを設置してみる
	# Buttonを設置してみる
	Button2 = tk.Button(text=u'撮り直す')
	Button2.bind("<Button-1>", Restartmain)        # ボタンが押されたときに実行される関数をバインドします
	Button2.place(x=350, y=255)
	root.mainloop()

def main2():
	global root
	root = tk.Tk()
	root.geometry('900x400')
	root.title('IMG')

	img={}
    #png又はjpgファイルを開く
	for i in range(4,7):
		if os.path.exists(str(i)+'.png'):
			img[i] = Image.open(open(str(i)+'.png', 'rb'))
			img[i].thumbnail((200, 200), Image.ANTIALIAS) #画像の大きさ最大値
			img[i] = ImageTk.PhotoImage(img[i])  # 表示するイメージを用意
		else :
			img[i] = Image.open(open(str(i)+'.jpg', 'rb'))
			img[i].thumbnail((200, 200), Image.ANTIALIAS) #画像の大きさ最大値
			img[i] = ImageTk.PhotoImage(img[i])  # 表示するイメージを用意

	canvas={}
	xx=0
	for i in range(4,7):
		canvas[i] = tk.Canvas(
			root, # 親要素をメインウィンドウに設定
			width=500,  # 幅を設定
			height=500 # 高さを設定
			#relief=tk.RIDGE  # 枠線を表示
			# 枠線の幅を設定
		)
		#PILでjpgを使用
		canvas[i].place(x=xx,y=0) #画像の座標
		xx=xx+300
		canvas[i].create_image(  # キャンバス上にイメージを配置
			0,  # x座標
			0,  # y座標
			image=img[i],  # 配置するイメージオブジェクトを指定
			tag="illust",  # タグで引数を追加する。
			anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
		)
	################################
	# Buttonを設置してみる
	Button1 = tk.Button(text=u'消すボタン',)
	Button1.bind("<Button-1>", deleteEntry)        # ボタンが押されたときに実行される関数をバインドします
	Button1.place(x=350, y=255)
	root.mainloop()	

# main関数呼び出し
if __name__ == "__main__":
#	while True:
	main()#写真撮る
	main2()#撮った写真の確認
	#main3()#撮った写真　加工した画像の出力