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
<img width="350" height="600" alt="image (3)" src="https://github.com/user-attachments/assets/10085784-f64a-4756-986a-f14cbf96b88a" />

<img width="350" height="500" alt="image (2)" src="https://github.com/user-attachments/assets/33b77af5-cbbe-4c38-beb9-1e5dd22a1f59" />

- **Menus**- To navigate add,update,remove items and view dashboard
  
  <img width="350" height="600" alt="image (1)" src="https://github.com/user-attachments/assets/cca0df02-f958-4f78-987f-ecb8cb8383c0" />


- 📦 **Add Pantry Items** – Name, quantity, and expiry date
  
  <img width="350" height="600" alt="image (6)" src="https://github.com/user-attachments/assets/b67a2783-0c6e-4efc-9adf-4d6ab9ffa81e" />

- 🔄 **Update Stocks** – Adjust quantity when used
  
  <img width="350" height="600" alt="image (4)" src="https://github.com/user-attachments/assets/23bc11d9-5174-4059-b8b2-92df4c62629a" />

- 📅 **Remove items** – To delete the items that fot finished or entered incorrectly
  
  <img width="350" height="600" alt="image (5)" src="https://github.com/user-attachments/assets/ce394dfe-9983-44ee-8df2-f75cc1a5e9dd" />

- 📊 **Dashboard View** – Lists current pantry contents visually
  
  <img width="350" height="600" alt="image (7)" src="https://github.com/user-attachments/assets/5670df7c-f82f-40e7-b75e-ff69e5083223" />


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

