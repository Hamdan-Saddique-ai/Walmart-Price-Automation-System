# 🛒 Walmart Price Automation System
<img width="1024" height="1536" alt="Image" src="https://github.com/user-attachments/assets/821a9fe0-f9ce-489e-b5a3-d2fc1e4d3b64" />

A Python-based automation tool designed to simplify product pricing and link management for Walmart workflows. This project reads product data from Excel, updates prices with additional costs, and automates opening product URLs for review.

---

## 🚀 Features

✅ Automatically updates product prices  
✅ Adds fixed costs (label, packing, profit margin)  
✅ Handles invalid or missing data  
✅ Saves updated data into a new Excel file  
✅ Opens product links one-by-one for manual checking  
✅ Simple and beginner-friendly Python scripts  

---

## 🧠 How It Works

### 1️⃣ Price Calculation Script
- Reads Excel file
- Takes "Source Price"
- Adds:
  - Label Cost
  - Packing Cost
  - Profit Margin
- Saves updated prices into a new file

### 2️⃣ Link Automation Script
- Reads product URLs from Excel
- Opens each link in browser
- Waits for user confirmation before next link

---

## 📂 Project Structure


📁 Walmart-Price-Automation
│
├── calculate_prices.py # Price automation script
├── open_links_simple.py # Link opening script
├── input.xlsx # Input file (your product data)
├── output.xlsx # Generated output file
└── README.md # Documentation


---

## ⚙️ Requirements

Make sure you have Python installed, then install dependencies:

pip install pandas openpyxl
📊 Input Excel Format

Your Excel file should contain:

Source Price	Store's URL
100	https://...
200	https://...
💻 Usage
▶️ Run Price Automation
python calculate_prices.py

✔ This will:

Read Excel file
Update prices
Save output.xlsx
🌐 Run Link Automation
python open_links_simple.py

✔ This will:

Open product links one by one
Wait for user input before next
🧾 Cost Breakdown (Editable)

Inside calculate_prices.py:

LABEL_COST = 6
PACKING_COST = 5
PROFIT_MARGIN = 5

You can modify these values based on your needs.

## ⚠️ Notes
Ensure Excel file name matches script  
Close browser tab before pressing ENTER for next link   
Invalid prices are automatically skipped   
## 💡 Future Improvements   
GUI Interface (Tkinter / Web App)   
Automatic scraping of prices   
Bulk processing without manual input   
Integration with APIs   
## 👨‍💻 Author   

Hamdan Saddique

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!    
