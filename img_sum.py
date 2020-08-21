import cv2
import os, os.path
import glob
import datetime
import time

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")



img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
         # SPACE pressed
        img_name = "opencv_frame_{}_.png".format(img_counter)
        path = '/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder'
        cv2.imwrite(os.path.join(path,img_name), frame)
        print("{} written!".format(img_name))
        img_counter += 1

        path, dirs, files = next(os.walk("/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder"))
        file_count = len(files)
        #print(file_count)


        images = []

        
        for file in files:
            images.append(file)
            print(images)
        

        list_of_list = []
        for img in images:
            list_of_list.append(img.split('_'))
            print(list_of_list)


        numbers_of_list = []
        
        for list_element in list_of_list:
            numbers_of_list.append(list_element[2])
            print(numbers_of_list)

        
        if 6 == len(numbers_of_list):
            print("llegue al 6") 
            print("opencv_frame_"+ str(min(numbers_of_list)) + "_.png")
            os.remove("/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder/"+ "opencv_frame_"+ str(min(numbers_of_list)) + "_.png")



cam.release()

cv2.destroyAllWindows()



       
        