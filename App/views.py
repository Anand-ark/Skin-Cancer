from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.preprocessing import image
import joblib

import tensorflow as tf
model =load_model('./models/skin_cancer.h5')
img_height2,img_width2=224,224 # skincancer

def skin(request):
    return render(request, 'App/skin.html')
def upload2(request):#Malaria
    p2 = request.FILES['image'];
    fs2=FileSystemStorage()
    filePathname2=fs2.save(p2.name,p2);
    filePathname2=fs2.url(filePathname2)
    testimage='.'+filePathname2
    img=image.load_img(testimage,target_size=(img_height2,img_width2))
    x=image.img_to_array(img)
    x=np.array(img)
    x=x/255;
    x=x.reshape(1,img_height2,img_width2,3)
    ans=model.predict(x)
    if(ans[0]>0.5):
        ans='Your Skin is Infected'
    else:
        ans='Your Skin is Safe'
    context={'filepathname2':filePathname2,'pred2':ans}
    return render(request, 'App/skinout.html',context)




