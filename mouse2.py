import cv2
import mediapipe as mp
import pyautogui

video = cv2.VideoCapture(0)

my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
index_y = 0
while True: #video için frame yakalayan bir döngü oluşturdum
    _, resim = video.read()
    resim = cv2.flip(resim, 1)
    frame_height, frame_width, _ = resim.shape #kare boyutlarını elde edince height ve width değişkenlerine atıyoruz.
    rgb_frame = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)#(blue green red ) formatından (red green blue) formatına dönüşüm
    output = my_hands.process(rgb_frame)
    hands = output.multi_hand_landmarks #el tespitinde çıkan sonuçları atama

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(resim, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=resim, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                if id == 4:
                    cv2.circle(img=resim, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 30:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)
    cv2.imshow('Virtual Mouse', resim)
    cv2.waitKey(1)