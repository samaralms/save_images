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
        

        path, dirs, files = next(os.walk("/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder"))
        file_count = len(files)
        #print(file_count)


        images = []
        nums = []
        max_v = 0
        min_v = 0
        for file in files:
            temp = file.split('_')
            nums.append(int(temp[2]))
            print(temp[2])
            images.append(file)
        print(nums)
        if nums:
            min_v = min(nums)
            max_v = max(nums)
        
        img_name = "opencv_frame_" + str(max_v + 1) + "_.png"
        path = '/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder'
        cv2.imwrite(os.path.join(path,img_name), frame)
        print("{} written!".format(img_name))
        
        
        
        if 6 == len(images):
            print("llegue al 6") 
            print("opencv_frame_"+ str(min_v) + "_.png")
            os.remove("/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder/"+ "opencv_frame_"+ str(min_v) + "_.png")



cam.release()

cv2.destroyAllWindows()



       
        