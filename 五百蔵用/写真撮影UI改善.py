import sys
import tkinter as tk
from PIL import Image, ImageTk
import urllib.request as req
import os
import cv2
if __name__=="__main__":

    root = tk.Tk()

    # ウインドウのタイトルを定義する
    root.title(u'Buttonを使ってみる')

    # ここでウインドウサイズを定義する
    root.geometry('1080x1920')

    cap = cv2.VideoCapture(0)
    
    if cap.isOpened() is False:
        raise("IO Error")

    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

    while True:

        ret, image = cap.read()

        if ret == False:
            continue

        cv2.imshow("Capture", image)
       
        if cv2.waitKey(33) >= 0:
            cv2.imwrite("image.png", image)
            break
            
    cv2.destroyAllWindows()
    
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()
    root.mainloop()