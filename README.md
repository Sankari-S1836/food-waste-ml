# 🆘 Code Red Hackathon – Food Waste Management System

## 🚨 About the Event

**Code Red** symbolizes *urgent action*. In this hackathon, our team addressed one of the world’s most pressing problems — **Food Waste** — with a dual-approach solution: a **Pantry Tracker Website** and a separate **Machine Learning model** to aid in waste prediction and prevent wastage of food effectively.

---

## 🍽️ Project Title: Smart Pantry Tracker – Reducing Food Waste with ML Support

### 🔍 Problem Statement

Globally, 1.3 billion tons of food go to waste every year. A large portion of this comes from domestic settings due to lack of tracking, over-purchasing, and poor planning. Our goal is to combat this using a web-based pantry system supported by ML insights to help users make better decisions.

---

## 💡 Key Features

### 🌐 Pantry Tracker Website (HTML-based Front-End)
- 🧑‍💻 **User Login & Registration** – Simple authentication
<img width="1135" height="826" alt="image (3)" src="https://github.com/user-attachments/assets/10085784-f64a-4756-986a-f14cbf96b88a" />

- 📦 **Add Pantry Items** – Name, quantity, and expiry date
- 🔄 **Update Stocks** – Adjust quantity when used
- 📅 **Track Expiry Dates** – See which items are nearing expiration
- 📊 **Dashboard View** – Lists current pantry contents visually

### 🧠 Machine Learning Module (Separate)
- 🤖 **ML Model**: Logistic Regression built in a separate environment
- 📁 **Input Data**: Custom dataset including quantity, expiry days, etc.
- 📈 **Output**: Predicts whether a food item is likely to be wasted (`is_wasted`)
- ⚠️ **Note**: This ML model is **not integrated into the web app**, but can assist future planning and visualization.

---

## 🛠️ Tech Stack

| Component     | Technology           |
|---------------|----------------------|
| Frontend      | HTML, CSS            |
| ML Model      | Python, scikit-learn |
| Data Handling | CSV (custom dataset) |

---

## 🧪 How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Sankari-S1836/food-waste-ml.git
   cd food-waste-ml
   
2.Open the index.html file in your browser:

Right-click → Open with → Any browser

Or double-click the file to launch the web page

3.Use the app:

📝 Register or log in as a user

🍎 Add food items with quantity and expiry date

📉 Update stock levels as you consume items

📊 View the dashboard to monitor expiry and reduce waste

4.🤖 For Machine Learning Model (Separate)
Open the file food.ipynb in:

Google Colab [recommended], or

Jupyter Notebook (if installed on your system)

Make sure the required CSV (food_waste_data_sample.csv) is in the same directory.

Run the notebook:

Train the Logistic Regression model

View prediction results for is_wasted column

Analyze the output to support food planning

🔔 The ML model currently runs separately and is not integrated with the HTML website. It's used for food waste analysis and prediction only.

### For Website:
1. Clone the repository:
   ```bash
   git clone https://github.com/Sankari-S1836/food-waste-ml
   cd food-waste-ml

## 👥 Team Members
1.Sankari.S
2.Roshini.S
3.Akshaya Sree.S

