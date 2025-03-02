from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
import base64
import json

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

# Create an instance that will be globally available
clApp = ClientApp()

@app.route("/train")
def train():
    os.system("python main.py")
    return "Training completed successfully"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST","GET"])
@cross_origin()
def predict():
    try:
        # Debug the request
        print("Request method:", request.method)
        print("Request content type:", request.content_type)
        
        # Handle JSON data with base64 image
        if request.content_type and 'application/json' in request.content_type:
            data = request.get_json()
            if not data or 'image' not in data:
                return jsonify({"error": "No image found in JSON data"}), 400
                
            # Decode the base64 image
            img_data = base64.b64decode(data['image'])
            with open(clApp.filename, 'wb') as f:
                f.write(img_data)
                
        # Handle multipart form data (file upload)
        elif "image" in request.files:
            image = request.files["image"]
            image.save(clApp.filename)
        else:
            return jsonify({"error": "No image found in request"}), 400
            
        # Run the detection
        os.system(f"cd yolov5 && python detect.py --weights ../artifacts/model_training/best.pt --img 416 --conf 0.4 --source ../{clApp.filename}")
        
        # Check if the output file exists
        output_path = "yolov5/runs/detect/exp/inputImage.jpg"
        if not os.path.exists(output_path):
            return jsonify({"error": "Detection failed - output image not found"}), 500
            
        # Read the file and encode to base64
        with open(output_path, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode('utf-8')
            
        result = {"image": encoded_string}
        
        # Clean up the runs directory
        os.system("rm -rf yolov5/runs")
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": f"Error: {str(e)}"}), 500

@app.route("/live", methods=["POST", "GET"])
@cross_origin()
def live_predict():
    try:
        os.system("cd yolov5 && python detect.py --weights ../artifacts/model_training/best.pt --img 416 --conf 0.4 --source 0")
        os.system("rm -rf yolov5/runs")
        return "camera live prediction started"
    except Exception as e:
        print(e)
        return "Error while starting live prediction"

if __name__ == "__main__":
    clApp = ClientApp()
    #app.run(host='0.0.0.0', port=8080) # AWS
    app.run(host='0.0.0.0', port=80) # Azure