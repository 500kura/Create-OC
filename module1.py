import dlib
import cv2

from time import sleep

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("me", frame) # 確認用
    # ここに処理を追加していく ----
    dets = detector(frame[:, :, ::-1])
    if len(dets) > 0:
      parts = predictor(frame, dets[0]).parts()

    # 確認用 ---
      img = frame * 0
      for i in parts:
        cv2.circle(img, (i.x, i.y), 3, (255, 0, 0), -1)

      cv2.imshow("me", img)

      nose = parts[33].y - parts[27].y
      print("鼻 %d" %nose)
    # 確認用 ここまで ---
    # ここまで ----

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
