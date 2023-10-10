from flask import * 
import os 

import cv2 as cv
import numpy as np
import glob
import matplotlib.pyplot as plt

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("model.html")

@app.route('/success', methods = ['POST'])  
def success():
    if request.method == 'POST':
        f = request.files['file']

        if f:
            # Specify the directory where you want to save the uploaded images
            upload_directory = 'C:\\Users\\Asus ROG\\Desktop\\portfolio\\static\\images'

            # Ensure the directory exists; if not, create it
            if not os.path.exists(upload_directory):
                os.makedirs(upload_directory)

            # Construct the complete path including the filename
            image_path = os.path.join(upload_directory, f.filename)
            
            # Save the uploaded image
            f.save(image_path)
            parts = image_path.split('\\')

            # Extract the desired portion
            desired_part = '\\'.join(parts[-3:])  
            
            return render_template("success.html", name=f.filename, image_path=desired_part)
        




if __name__ == "__main__": 
    app.run(debug=True)
    