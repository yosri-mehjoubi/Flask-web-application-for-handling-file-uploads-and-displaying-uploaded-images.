from flask import * 
import os 

import cv2 as cv
import numpy as np
import glob
import matplotlib.pyplot as plt
import random

app = Flask(__name__)

def median_stack_filter(imgs):

    rows = imgs[0][:,:,0].shape[0]
    cols = imgs[0][:,:,0].shape[1]
    updated_img = np.zeros_like(imgs[0])
    channel = 3

    imgs = np.array(imgs)
    med = np.median(imgs, axis=0)
    return med.astype(int)

@app.route('/')
def home():
    return render_template("model.html")

@app.route('/success', methods = ['POST'])  
def success():
    if request.method == 'POST':
        f = request.files.getlist('file[]')
        print(f)

        files = []
        for file in f:
            files.append(os.path.join('static/imgs/'+ file.filename))

        for file in f:    
            if file:
                # Specify the directory where you want to save the uploaded images
                upload_directory = 'static/imgs/'

                # Ensure the directory exists; if not, create it
                if not os.path.exists(upload_directory):
                    os.makedirs(upload_directory)

                # Construct the complete path including the filename
                image_path = os.path.join(upload_directory, file.filename)
                
                # Save the uploaded image
                file.save(image_path)
                parts = image_path.split('\\')

                # Extract the desired portion
                desired_part = '\\'.join(parts[-3:])  
           
        read_images=[]
        for idx in range(len(f)):
            read_images.append(cv.imread(files[idx], 1))
        updated_image = median_stack_filter(read_images)
        cv.imwrite('static/results.png',updated_image)

        cache_bust = random.randint(1, 100000)
        return render_template("success.html", data=updated_image, file_path = 'static/imgs/results.png',cache_bust=cache_bust)
        




if __name__ == "__main__": 
    app.run(debug=True)
    