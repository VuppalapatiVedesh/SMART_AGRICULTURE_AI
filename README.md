# 🌱 Smart Agriculture AI (Crop Prediction System)

An AI-powered smart agriculture system that predicts the most suitable crop based on soil nutrients and environmental conditions. The system integrates real-time weather data and provides intelligent farming tips to support better agricultural decisions.

---

## 🚀 Features

✅ Crop prediction using Machine Learning  
✅ Real-time weather auto-fill (temperature & humidity)  
✅ Rainfall detection & smart estimation  
✅ Crop image display  
✅ Smart cultivation tips  
✅ Mobile-friendly interface  
✅ Cloud deployment ready  

---

## 🧠 Technologies Used

- Python  
- Flask  
- Scikit-learn (Random Forest Algorithm)  
- HTML & CSS  
- OpenWeatherMap API  

---

## 📊 Input Parameters

The system predicts crops using:

- Nitrogen (N)  
- Phosphorus (P)  
- Potassium (K)  
- Temperature  
- Humidity  
- Soil pH  
- Rainfall  

---

## 🌾 Output

✔ Recommended crop  
✔ Crop image  
✔ Farming tip  

---

## 🌦 Weather Integration

The system automatically fetches real-time weather data using the OpenWeatherMap API.

If rainfall data is unavailable, the system intelligently estimates rainfall based on humidity levels to ensure reliable predictions.

---

## ⚙️ How It Works

1. User enters soil parameters  
2. Click **Auto Fill Weather** (optional)  
3. System fetches real-time weather data  
4. Machine learning model predicts the best crop  
5. Result displayed with image & farming tip  

---

## 📱 Mobile Friendly

The interface is optimized for smartphones, ensuring usability for farmers in real-world outdoor environments.

---

## 🗂 Project Structure

```
smart-agriculture-ai
│
├── app.py
├── Procfile
├── requirements.txt
├── train_model.py
│
├── data/
│   └── crop_data.csv
|
├── model/
│   └── crop_model.pkl
│
├── static/
│   ├── images/
│   └── style.css
│
├── templates/
│   └── index.html
|
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository
```
git clone https://github.com/your-username/smart-agriculture-ai.git
cd smart-agriculture-ai
```

### 2️⃣ Create virtual environment
```
python -m venv venv
```

### 3️⃣ Activate environment

**Windows**
```
venv\Scripts\activate
```

**Mac/Linux**
```
source venv/bin/activate
```

### 4️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 5️⃣ Run the application
```
python app.py
```

### 6️⃣ Open in browser
```
http://127.0.0.1:5000
```

---

## 🌍 Deployment

This application can be deployed on cloud platforms like Render for live access.

🌍 Live Demo: https://your-link.onrender.com

---

## 🎯 Real-World Applications

- Smart farming decision support  
- Crop planning assistance  
- Agricultural advisory systems  
- Precision agriculture  

---

## 🚀 Future Enhancements

- Fertilizer recommendations  
- Pest & disease detection  
- Voice input for farmers  
- Offline mode for rural areas  
- Mobile app version  

---

## 👨‍💻 Author

**Vedesh**

---

## ⭐ If you found this project useful, consider giving it a star!
