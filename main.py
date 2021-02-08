import os 
from mask import maske_olustur 
 
_path = "resim\\" 
    
images = [os.path.join(_path, f) for f in os.listdir(_path) if os.path.isfile(os.path.join(_path, f))]
for i in range(len(images)): 
    maske_olustur(images[i]) 
   
   