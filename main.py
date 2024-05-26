import os
from fastapi import FastAPI, File, UploadFile
import shutil
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model
import PIL
from ultralytics import YOLO

app = FastAPI()

'''
#Loading the classification model
model=load_model('app/densnet121.h5')
yolo_model=YOLO('D:\linked\Drone\drone_bestv4.pt')

# Create a directory to save uploaded and processed files
os.makedirs('uploads', exist_ok=True)
os.makedirs('Processed',exist_ok=True)
os.makedirs('video_uploads',exist_ok=True)
os.makedirs('video_Processed',exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}


#function to process the images file for classification
def classify_image(img):
        try:
            img = keras.preprocessing.image.load_img(img, target_size=(640, 640))
            x=keras.preprocessing.image.img_to_array(img)
            x=x/255
            x=np.expand_dims(x, axis=0)
            prediction= model.predict(x)
            prediction=np.argmax(prediction, axis=1)
            if prediction[0]==0:
                return "This images contains drone"
            else:
                return "This image does not have a drone"
        except Exception as e:             
             return "Facing an Error {}".format(e)
        
def video_process(video_file):
    # Run inference on the source
    results = model(video_file, save=True)

@app.post("/uploadfile/")
#This operation function takes file from the api end point and it save into local folder called uploads
async def create_upload_file(image: UploadFile):
    file_location=f"uploads/{image.filename}"
    processed_file_location=f"Processed/{image.filename}"
    with open(file_location,'wb') as file:
        shutil.copyfileobj(image.file,file)
    result=classify_image(file_location)
    shutil.move(file_location,processed_file_location)
        
    return {"filename": image.filename,"Operation Status":'File Successfully Uploaded',"Classification :":result}


@app.post("/uploadvideo/")
#This operation function takes file from the api end point and it save into local folder called uploads
async def create_upload_file(video: UploadFile):
    file_location=f"uploads/{video.filename}"
    processed_file_location=f"Processed/{video.filename}"
    with open(file_location,'wb') as file:
        shutil.copyfileobj(video.file,file)
    result=video_process(file_location)
    shutil.move(file_location,processed_file_location)
        
    return {"filename": video.filename,"Operation Status":'File Successfully Uploaded'}

    '''
@app.post('/name_file/')
async def file_called(file:UploadFile):
    name_of_file=file.filename
    first_part=str(name_of_file)
    first_part=first_part.split('.')[0]
    return {"first_part":first_part,"file name":file.filename}

