#import speak
import face_recognition
import cv2
import numpy as np
import os
import re
from pygame import mixer
import datetime
import time
from gtts import gTTS
from playsound import playsound
# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)#"files/me.mp4"'rtsp://192.168.0.40/live.sdp'
cap=video_capture
ret,img=cap.read()
# Load a sample picture and learn how to recognize it.
#Инициализируем звуковое устройство
mixer.init()    
# Проигрываем полученный mp3 файл
from subprocess import call


Yuriy_image = face_recognition.load_image_file("files/Yuriy.jpg")
Yuriy_face_encoding = face_recognition.face_encodings(Yuriy_image)[0]

Dovgiy_image = face_recognition.load_image_file("files/Dovgiy.jpg")
Dovgiy_face_encoding = face_recognition.face_encodings(Dovgiy_image)[0]

Nastya_image = face_recognition.load_image_file("files/Nastya.jpg")
Nastya_face_encoding = face_recognition.face_encodings(Nastya_image)[0]

Dasha_image = face_recognition.load_image_file("files/Dasha.jpg")
Dasha_face_encoding = face_recognition.face_encodings(Dasha_image)[0]

LisoviyOksenVasilyevich_image = face_recognition.load_image_file("files/LisoviyOksenVasilyevich.jpg")
LisoviyOksenVasilyevich_face_encoding = face_recognition.face_encodings(LisoviyOksenVasilyevich_image)[0]
#Natasha_image = face_recognition.load_image_file("files/Natali.png")
#Natasha_face_encoding = face_recognition.face_encodings(Natasha_image)[0]
# Load a second sample picture and learn how to recognize it.

putin9999_image = face_recognition.load_image_file("files/putin9999.png")
putin9999_face_encoding = face_recognition.face_encodings(putin9999_image)[0]
p_image = face_recognition.load_image_file("files/p.jpg")
p_face_encoding = face_recognition.face_encodings(p_image)[0]
VitaliyLisoviy_image = face_recognition.load_image_file("files/VitaliyLisoviy.jpg")
VitaliyLisoviy_face_encoding = face_recognition.face_encodings(VitaliyLisoviy_image)[0]
Vadim_image = face_recognition.load_image_file("files/Vadim.jpg")
Vadim_face_encoding = face_recognition.face_encodings(Vadim_image)[0]
Anya_image = face_recognition.load_image_file("files/Anya.jpg")
Anya_face_encoding = face_recognition.face_encodings(Anya_image)[0]
u1_image = face_recognition.load_image_file("files/u1.png")
u1_face_encoding = face_recognition.face_encodings(u1_image)[0]
Obolonik_image = face_recognition.load_image_file("files/Natasha.png")
Natasha_face_encoding = face_recognition.face_encodings(Obolonik_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    Yuriy_face_encoding,
    Dovgiy_face_encoding,
    putin9999_face_encoding,
    Nastya_face_encoding,
    VitaliyLisoviy_face_encoding,
    p_face_encoding,
    Vadim_face_encoding,
    Dasha_face_encoding,
    Natasha_face_encoding,
    LisoviyOksenVasilyevich_face_encoding,
    u1_face_encoding,
    Anya_face_encoding,
    
]
known_face_names=[
    "Yuriy",
    "Dovgiy",
    "putin9999",
    "Nastya",
    "VitaliyLisoviy",
    "p",
    "Dasha",
    "Vadim",
    "Natasha",
    "LisoviyOksenVasilyevich",
    "u1",
    "Anya",

]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
i=0
y=0
y1=0
y2=0
y3=0
y4=0
y5=0
y6=0
y7=0
y8=0
y9=0
y10=0
y11=0
y12=0
y13=0
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read(0)

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time


    
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
           
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            #nameold="x"
            face_names.append(name)
            
            if name=="Yuriy" and y==0 :
                y=y+1 
                print(y)
                mixer.music.load("y.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
                
            # Устанвливаем текущим файлом y.mp3 и закрываем звуковое устройство
# Это нужно чтобы мы могли удалить предыдущий mp3 файл без колизий
            
                #mixer.stop
                #mixer.quit
                print(y+1)
                print(name)#-нашел имя++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                
                #speak()
                #playsound('y.mp3')
                #call(["cvlc", "--play-and-exit", "y.mp3"])
            elif name=="Dasha" and y2==0:
                y2=y2+1 
                print(name)
                #mixer.init()
                mixer.music.load("Dasha.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
                #speak()
            elif name=="putin9999" and y3==0:
                y3=y3+1 
                print(name)
                #mixer.init()
                mixer.music.load("putin.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
                #mixer.stop
                #mixer.quit
                print(name)
            elif name=="Nastya"and y4==0:
                y4=y4+1 
                print(name)
                #mixer.init()
                mixer.music.load("Nastya.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
                #mixer.stop
                #mixer.quit
            elif name =="VitaliyLisoviy" and y5==0:
                y5=y5+1 
                print(name)
                mixer.init()
                mixer.music.load("Vitaliy.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
            elif name =="Vadim" and y6==0:
                y6=y6+1
                print(name)
                #mixer.init()
                mixer.music.load("Vadim.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)   
            elif name =="Dovgiy" and y7==0:
                y7=y7+1
                print(name)
                #mixer.init()
                mixer.music.load("Dovgiy.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
            elif name =="Natasha" and y8==0:
                y8=y8+1
                print(name)
                #mixer.init()
                mixer.music.load("Obolonik1.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
                    
            elif name =="LisoviyOksenVasilyevich" and y9==0:
                y9=y9+1
                print(name)
                #mixer.init()
                mixer.music.load("LOV.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
            
            elif name =="Unknown" and y11==0:
                y11=y11+1
                print(y11)
                cv2.imwrite('unk/camera1.png',frame)
                i=i+1
                #mixer.init()
                mixer.music.load("Unknown.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
            elif name =="u" and y12==0:
                y12=y12+1
                print(y12)
                i=i+1
                #mixer.init()
                mixer.music.load("u.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
                    
            elif name =="Anya":
                y13=y13+1
                print(y13)
                i=i+1
                #mixer.init()
                mixer.music.load("Anya.mp3")
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1) 
    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.namedWindow("Video",cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("Video",580,700)

    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
