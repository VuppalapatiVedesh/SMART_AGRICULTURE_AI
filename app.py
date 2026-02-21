from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# load trained model
model = pickle.load(open("model/crop_model.pkl", "rb"))

# 🌿 smart crop tips
crop_tips = {
    "apple": "Apples grow best in cool climates with well-drained soil.",
    "banana": "Bananas require rich soil, high humidity, and regular watering.",
    "blackgram": "Black gram prefers warm temperatures and fertile soil.",
    "chickpea": "Chickpeas grow well in dry climates with low rainfall.",
    "coconut": "Coconut grows well in coastal sandy soil and humid climates.",
    "coffee": "Coffee requires shade, rainfall, and slightly acidic soil.",
    "cotton": "Cotton grows best in black soil with good drainage and sunlight.",
    "grapes": "Grapes need well-drained soil and plenty of sunlight.",
    "jute": "Jute requires high rainfall and humid climate.",
    "kidneybeans": "Kidney beans need moderate rainfall and fertile soil.",
    "lentil": "Lentils grow well in cool climates with low moisture.",
    "maize": "Maize requires warm weather and nutrient-rich soil.",
    "mango": "Mango trees thrive in tropical climates with well-drained soil.",
    "mothbeans": "Moth beans are drought-resistant and grow in dry regions.",
    "mungbean": "Mung beans grow best in warm weather and moderate rainfall.",
    "muskmelon": "Muskmelon requires sandy soil and warm climate.",
    "orange": "Oranges grow best in sunny weather and well-drained soil.",
    "papaya": "Papaya grows quickly in tropical climates with good sunlight.",
    "pigeonpeas": "Pigeon peas grow well in semi-arid climates.",
    "pomegranate": "Pomegranate thrives in dry climates and well-drained soil.",
    "rice": "Rice grows best in high humidity and water-rich soil.",
    "sugarcane": "Sugarcane requires hot climate and abundant water supply.",
    "watermelon": "Watermelon needs warm weather and sandy soil.",
    "wheat": "Wheat prefers cool weather and well-drained fertile soil."
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    values = [float(x) for x in request.form.values()]
    features = np.array([values])

    prediction = model.predict(features)[0].lower()

    # image handling
    image_file = prediction + ".jpg"
    image_path = os.path.join(app.root_path, "static", "images", image_file)

    if not os.path.exists(image_path):
        image_file = None

    # tip handling (guaranteed)
    tip_text = crop_tips.get(prediction, "Best grown under suitable soil and climate conditions.")

    return render_template(
        "index.html",
        prediction_text="Recommended Crop: " + prediction.capitalize(),
        crop_image=image_file,
        tip=tip_text
    )

if __name__ == "__main__":
    app.run(debug=True)
