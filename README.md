## Blood Pressure Prediction API and VIsualizer

### Overview

This project provides:

1. **Trained Blood Pressure ML models**: Trained both systolic (SBP) and diastolic blood pressure (DBP) predicting models for real-time BP trend prediction.
2. **Blood Pressure Prediction API**: A backend service that serves real-time predicted values for systolic (SBP) and diastolic (DBP) blood pressure via an HTTP endpoint.
3. **Visualizer Dashboard**: A user-friendly dashboard built using Plotly Dash to visualize blood pressure value trends in real-time.

### **Features**
- Real-time fetching of blood pressure prediction data via API.
- Dynamic and interactive visualization of SBP and DBP trends.
- Monitor recent data with a rolling window of the latest 50 data points.
- Easy to extend for additional features like average values, rates of change, etc.

----
### How to Implement

**1. Backend: Blood Pressure Predicion API**

The backend API provides blood pressure readings (SBP and DBP).

#### Requirements

- Python 3.8+ installed.
- A library to serve the API (e.g., FastAPI or Flask)

#### Setting up the Backend

1. **Install Dependencies**
   
```
pip install fastapi uvicorn httpx
```

2. **Run the API server**: Use the following command in your terminal to start the backend server
```
uvicorn main:app --reload --host 127.0.0.1 --port=8000
```
The API will now be available at http://127.0.0.1:8000/predict

Example Response:
``` json
   {
       "sbp": [120],
       "dbp": [80]
   }
```

**2. Frontend: Real-Time Blood Pressure Visualizer**

The frontend visualizer monitors SBP and DBP trends dynamically and visualizes them using a Plotly Dash application.

#### Requirements

- Python 3.8+ installed.
- Required libearies dash, plotly, httpx.

1. **Installed Dependencies:**
```
pip install dash plotly httpx
```

2. **Run the Dashboard:**Start the dashboard visualizer by running the following command:
```
python dash_app.py
```
The visualizer will be available at http://127/0.0.1:8050

----
### **Usage**
1. **Start the Backend API:**
    - Open your terminal and run `python main.py` to start the API server.
    - The API will serve blood pressure data at `http://127.0.0.1:8000/predict_bp_endpoint`.

2. **Start the Visualizer:**
    - Open another terminal and run `python app.py` to start the Dash application.
    - Open your browser and navigate to `http://127.0.0.1:8050` to view the real-time trends.

3. **Real-Time Monitoring:**
    - Observe the SBP and DBP predictions on the dashboard, which update every second with new data fetched from the API.
----
### **Project Structure**
The project files are organized as follows:
``` 
. 
├── main.py          # Backend API for Blood Pressure Predictions
├── app.py           # Frontend Real-Time Visualization Dashboard
└── README.md        # Project Documentation
```
----
### **Dataset**

Physionet mimic-IV waveform 0.1.0

----
### **Models Performance**

----
### **Demo Screenshot**

----
### **License**
This project is licensed under the MIT License.
