import os
import cv2
import utils

image = cv2.imread("image_5.png")
chars = utils.extract_char(image)

for char in chars:
    cv2.imshow('Image',char[1])
    input = cv2.waitKey(0)
    resized = cv2.resize(char[1],(20,20))

    if input >= 48 and input <= 57:
        name = str(input - 48)
        file_count = len(next(os.walk('./training_data/'+name+'/'))[2])
        cv2.imwrite('./training_data/'+str(input-48)+'/'+ str(file_count+1)+'.png',resized)
    elif input == ord('a') or input == ord('b') or input == ord('c'):
        name = str(input - ord('a')+10)
        file_count = len(next(os.walk('./training_data/'+name+'/'))[2])
        cv2.imwrite('./training_data/'+str(input-48)+'/'+ str(file_count+1)+'.png',resized)