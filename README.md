# 🌦️ OpsPulse — Weather Data Pipeline

A simple but complete end-to-end data pipeline project built in Python.  
It fetches real weather data, saves it, cleans it, summarises it, visualises it, and tests it — all automatically.

---

## 🎯 Business Problem

Every hour, weather stations around the world generate thousands of data points.  
But raw data is messy, inconsistent, and hard to interpret.

**OpsPulse solves this by:**

- Automatically pulling live weather data from the internet  
- Saving raw data safely before any processing  
- Cleaning and transforming data into usable format  
- Generating daily summary reports  
- Validating the pipeline using automated tests  

---

## 🏗️ Project Architecture

```
Internet (Open-Meteo API)
         │
         ▼
   fetch_weather()        ← pulls 168 hourly records for NYC
         │
         ▼
     save_raw()           ← saves weather.json + weather.csv (untouched)
         │
         ▼
    transform()           ← cleans columns, adds rain flag, wind category
         │
         ▼
  daily_summary()         ← collapses 168 rows into 7-day report
         │
         ▼
   visualise()            ← generates temperature + rain + wind charts
         │
         ▼
    pytest tests          ← validates schema, logic and file output
```
---
📁 Project Structure
```
opspulse/
│
├── 📓 OpsPulse_Simple.ipynb       ← main Jupyter notebook (run this)
├── 📄 README.md                   ← you are here
│
└── 📂 weather_data/
    ├── 📂 raw/
    │   ├── weather.json           ← original API response (untouched)
    │   └── weather.csv            ← same data in CSV format
    │
    └── 📂 processed/
        ├── daily_summary.csv      ← 7-day clean summary report
        ├── chart.png              ← temperature + rain + wind chart
        └── test_pipeline.py       ← all 3 pytest tests
```
---

🛠️ Tools & Technologies

Tool	Purpose

🐍 Python	Core programming language
📓 Jupyter Notebook	Interactive development environment
🌐 Requests	Fetches data from the Open-Meteo API
🐼 Pandas	Cleans, transforms and summarises data
📊 Matplotlib	Creates temperature and rain charts
✅ Pytest	Runs automated tests
🌤️ Open-Meteo API	Free weather API — no signup, no key needed
---
📊 What the Pipeline Produces
Raw Data (168 rows — 7 days x 24 hours)
time	temperature_2m	precipitation	windspeed_10m
2025-06-01T00:00	18.2	0.0	12.4
2025-06-01T01:00	17.8	1.2	10.1
...	...	...	...
Daily Summary (7 rows — one per day)
date	min_temp	avg_temp	max_temp	total_rain	max_wind	rainy_hrs
2025-06-01	14.2	19.8	26.1	3.4	28.5	5
2025-06-02	15.1	21.3	28.7	0.0	22.1	0
...	...	...	...	...	...	...
---
🚀 How to Run This Project
Step 1 — Clone or download this repo
Click the green Code button above → Download ZIP → unzip it
Step 2 — Open Jupyter Notebook
Open Anaconda Navigator → Launch Jupyter Notebook → navigate to this folder
Step 3 — Open the notebook
Click on OpsPulse_Simple.ipynb
Step 4 — Run all cells
Click Kernel → Restart & Run All
That's it! All files will be generated automatically inside the `weather_data/` folder.
---
✅ Automated Tests
3 tests written using Pytest that validate:
Test	What it checks
`test_columns_exist`	All required data columns are present
`test_rain_flag`	Rain flag correctly identifies rainy hours
`test_csv_save`	CSV file saves and loads with correct data
All 3 tests pass.
---
📈 Key Learnings from This Project
✅ How to call a real public API and handle the response
✅ How to save raw data before transforming it (best practice)
✅ How to use Pandas for real data cleaning and transformation
✅ How to aggregate data into meaningful summaries
✅ How to write automated tests to validate your pipeline
✅ End-to-end thinking — from raw API data to final report
---
🌐 Data Source
Open-Meteo — https://open-meteo.com  
Free, open-source weather API. No signup. No API key. No cost.  
Data: NYC coordinates (40.7128° N, 74.0060° W), 7-day hourly forecast.
---
👤 Author
Built with curiosity and lots of coffee ☕  
Feel free to fork, star and build on top of this!
---
⭐ If you found this useful
Give this repo a star ⭐ — it helps others find it too!
