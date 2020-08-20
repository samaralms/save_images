import cv2
import os, os.path

cam = cv2.VideoCapture(0)
#este es un comentario
#est es
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
        img_name = "opencv_frame_{}.png".format(img_counter)
        path = '/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder'
        cv2.imwrite(os.path.join(path,img_name), frame)
        print("{} written!".format(img_name))
        img_counter += 1

        path, dirs, files = next(os.walk("/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder"))
        file_count = len(files)
        print(file_count)
        os.path = '/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder'
        if file_count > 5:
            # os.remove("/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder/")
            print(files)
            files.sort(key=os.path.getmtime)
            print(files)
            os.remove('/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder/'+files[len(files)-1])
            
           
        # files = os.listdir('/home/samara/Desktop/OPTIMOTION2/Proyectos_Relevantes/guardar_img/img_folder')
        # for file in files[1:]:
        #     os.remove(file)


cam.release()

cv2.destroyAllWindows()