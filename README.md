# 📊 TCS Stock Market Analysis Dashboard (Power BI)

## 🚀 Project Overview

This repository contains a **Power BI dashboard** that analyzes historical stock price data of **Tata Consultancy Services (TCS)** from 2020 to 2026.  
The dashboard includes interactive visuals, trend insights, and detailed tables that help understand price movement patterns, volatility, yearly growth, and more.

📌 This project is ideal for **aspiring Data Analysts / BI professionals** who want to showcase skills in Power BI, data preparation, DAX, and visual storytelling.

---

## 📁 Repository Contents

```
TCS-Stock-Market-Analysis-PowerBI/
│
├── TCS_Stock_Dashboard.pbix ← Power BI report
├── data/
│ └── TCS_Combined_2020_2026.csv ← Clean dataset used in the report
├── screenshot_*.png ← Dashboard preview images
└── README.md ← Project documentation
```


---

### 📷 Dashboard Preview

#### 📊 Main Dashboard View
![Main Dashboard](Screenshot/Main%20Dashboard%20View.png)

#### 📈 Trend Analysis View
![Trend Analysis](Screenshot/Trend%20Analysis%20View.png)

#### 📋 Detailed Table View
![Detailed Table](Screenshot/Detailed%20Stock%20Table%20View.png)

---

## 🛠 Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Power BI Desktop** | Dashboard visualization |
| **DAX** | Calculated measures and aggregations |
| **CSV / Excel** | Source data storage |
| **GitHub** | Version control and portfolio |

---

## 📈 Features & Insights

### 📌 Core Visualizations

- **Yearly Performance** – Compare stock price trends year-by-year  
- **Quarterly Insights** – Analyze how each quarter performed  
- **Open vs Close** – Patterns between opening and closing prices  
- **High vs Low** – Daily price range analysis  
- **Volume Trends** – Impact of trade volume on price movement  
- **Interactive Slicers** – Filter by Year, Quarter, and Date

---

## 📊 Data Description

The dataset includes the following columns:

| Column | Description |
|--------|-------------|
| `Date` | Trading date |
| `Open` | Opening price |
| `High` | Highest price during the day |
| `Low` | Lowest price during the day |
| `Close` | Closing price |
| `Volume` | Number of shares traded |

Data is sourced from **Yahoo Finance** and cleaned for analysis.

---

## ⚙️ How to Use

### 🔹 Option 1: Open in Power BI Desktop

1. Download the `.pbix` file.
2. Open it in **Power BI Desktop**.
3. Navigate through the report pages.
4. Use slicers to interact with the visuals.

### 🔹 Option 2: Refresh with Your Own Data

1. Store your time-series file in the `data/` folder.
2. Make sure it has the same column format (`Date, Open, High, Low, Close, Volume`).
3. In Power BI Desktop, go to **Transform Data** → update the query to use your CSV.

---

## 📌 DAX Calculations & Measures Used

Some key measures used in this dashboard include:

- **Average Close Price**
- **Total Volume**
- **Yearly / Quarterly aggregations**
- **Custom filters using date slicers**

Each visual is backed by structured data modeling and relationships to support drill-down and interactive filtering.

---

## 🧠 Key Learnings

By completing this project, you demonstrate:

✔ Skill in data cleaning and preparation  
✔ Ability to use Power BI visuals effectively  
✔ Understanding of time-series stock data  
✔ Use of DAX for custom insights  
✔ Creation of interactive and user-friendly dashboards

---

## 🚀 Next Enhancements (Optional)

You can extend this project by adding:

✅ Technical indicators (MA20, EMA, RSI, MACD)  
✅ Machine learning-based price forecasting  
✅ Deployment to Power BI Service  
✅ Publish dashboard to public web link

---

## 📚 References

- Yahoo Finance (Historical Stock Data)  
- Microsoft Power BI Official Documentation

---

## 👨‍💻 Author

**Aviral Goyal**  
Aspiring Data Analyst | Power BI Developer  

🔗 LinkedIn: [Aviral Goyal](https://www.linkedin.com/in/avviiiral/)

---

🎉 _Thank you for visiting this project!_  
If you find it useful or want to learn how it was built, **feel free to message me.**
