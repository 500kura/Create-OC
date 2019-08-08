#UI大改造v8
#-*- coding: utf8 -*-
import sys
import tkinter as tk
from PIL import Image, ImageTk
import urllib.request as req
import os
import cv2
import numpy as np
# ボタンが押されたら呼び出される関数 Entryの中身をすべて削除します
def deleteEntry(self):
	root.destroy()
    # Entryの中身をすべて削除します

def finish():
    print("finish")
    root.destroy()

#main0()関係
def takeFace(self):
    ret, image = c.read()
#    cv2.imshow("Capture", image)
    cv2.imwrite("image.jpg", image)
    c.release()
    cv2.destroyAllWindows()
    finish()

def capStart():
    print('camera-ON')
    try:
        global w, h, img
        w, h= c.get(cv2.CAP_PROP_FRAME_WIDTH), c.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('w:'+str(w)+'px+h:'+str(h)+'px')
    except:
        import sys
        print("error-----")
        print(sys.exec_info()[0])
        print(sys.exec_info()[1])
        '''終了時の処理はここでは省略します。
        c.release()
        cv2.destroyAllWindows()'''

def u():#update
    global img
    ret, frame =c.read()
    if ret:
        img=ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        canvas.create_image(w/2,h/2,image=img)
    else:
        print("u-Fail")
    root.after(1,u)

def main0():
    print("main0")
    global root,c
    root=tk.Tk()
    root.title("camera")
    root.geometry("720x490")
    root.resizable(width=False, height=False)
    c=cv2.VideoCapture(0)
    # Buttonを設置してみる
    Button1 = tk.Button(text=u'撮影します')
    Button1.bind("<Button-1>", takeFace)        
    Button1.place(x=300, y=460)

    global canvas
    canvas=tk.Canvas(root, width=640, height=460, bg="white")
    canvas.pack()
    capStart()
    u()
    root.mainloop()
    main()
#main0()関係終わり
###main()関係
def Restartmain(self):
    print("写真撮り直し")
    root.destroy()
    main0()
def main():
    print("main")
    global root
    root=tk.Tk()
    root.geometry('720x510')
    root.resizable(width=False, height=False)
    root.title('IMG')
    img={}
    img[1] = Image.open('image.jpg')
    img[1].thumbnail((640, 460), Image.ANTIALIAS) #画像の大きさ最大値
    img[1] = ImageTk.PhotoImage(img[1])# 表示するイメージを用意
    """
    for i in range(2,4):
        if os.path.exists(str(i)+'.png'):
            img[i] = Image.open(open(str(i)+'.png', 'rb'))
            img[i].thumbnail((200, 200), Image.ANTIALIAS) #画像の大きさ最大値
            img[i] = ImageTk.PhotoImage(img[i])  # 表示するイメージを用意
        else :
            img[i] = Image.open(open(str(i)+'.jpg', 'rb'))
            img[i].thumbnail((200, 200), Image.ANTIALIAS) #画像の大きさ最大値
            img[i] = ImageTk.PhotoImage(img[i])  # 表示するイメージを用意
    """
    ################################
    canvas={}
    canvas[1] = tk.Canvas(
		root, # 親要素をメインウィンドウに設定
		width=700,  # 幅を設定
		height=480 # 高さを設定
		#relief=tk.RIDGE  # 枠線を表示
		# 枠線の幅を設定
    )
	#PILでjpgを使用
    canvas[1].place(x=0,y=0)#画像の座標
    canvas[1].create_image(  # キャンバス上にイメージを配置
		50,  # x座標
		0,  # y座標
		image=img[1],  # 配置するイメージオブジェクトを指定
		tag="illust",  # タグで引数を追加する。
		anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
    )
	################################
	# Buttonを設置してみる
    Button1 = tk.Button(text=u'これでOK')
    Button1.bind("<Button-1>", deleteEntry)        # ボタンが押されたときに実行される関数をバインドします
    Button1.place(x=300, y=460)
    # Buttonを設置してみる
    # Buttonを設置してみる
    Button2 = tk.Button(text=u'撮り直す')
    Button2.bind("<Button-1>", Restartmain)        # ボタンが押されたときに実行される関数をバインドします
    Button2.place(x=300, y=485)
    root.mainloop()
#main()関係終わり
#main2()関係
def main2():
    print("main2")
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
#main2()関係終わり
# main関数呼び出し#写真撮る#撮った写真の確認
if __name__ == "__main__":
    cnt=0
    while True:
        main0()
#        main()
        main2()
        cnt=cnt+1
        if cnt == 2:
            break
#main3()#撮った写真　加工した画像の出力