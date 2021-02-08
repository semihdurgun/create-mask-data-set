import cv2,os 
from PIL import Image   

def maske_olustur(path):    
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml") 
    #https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt.xml 
    img = cv2.imread(path)
    im1 = Image.open(path) 
    im2 = Image.open("default-maske.png")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
     
    if  len(faces) != 1:
        im1.close()
        if os.path.exists(path):
            os.remove(path)
            return 
         
    for (x,y,w,h) in faces:
        print(x,y,w,h) 
        old = int(h/2)
        newsize = (int(w),int(h*12/20)) 
        area = (x-80,y-80,x+80+w,y+80+h) 
        im2 = im2.resize(newsize) 
        im3 = im1.copy()
        im1.paste( im2, (x, y+old),im2)  
    for (x,y,w,h) in faces:  
        saves(path,im1) 
        saves2(path,im3)        
    
def saves(path,im1) :
    path_splits = os.path.splitext(path[6:])
    new_face_path = "resim\\maskeli\\" + path_splits[0] + '-with-mask' + path_splits[1]
    im1.save(new_face_path) 
    print(f'Kaydediliyor.. {new_face_path}')
def saves2(path,im3) :
    path_splits = os.path.splitext(path[6:])
    new_face_path = "resim\\maskesiz\\" + path_splits[0] + '-without-mask' + path_splits[1]
    im3.save(new_face_path) 
    print(f'Kaydediliyor.. {new_face_path}')    
    
    
    