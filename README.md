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

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|--------|
| Python | Core programming language |
| Jupyter Notebook | Interactive development |
| Requests | API data fetching |
| Pandas | Data cleaning & transformation |
| Matplotlib | Data visualization |
| Pytest | Automated testing |
| Open-Meteo API | Free weather data source |

---

## 📊 Output Generated

### Raw Data (168 hourly records)

| time | temperature_2m | precipitation | windspeed_10m |
|------|----------------|---------------|----------------|
| 2025-06-01T00:00 | 18.2 | 0.0 | 12.4 |
| 2025-06-01T01:00 | 17.8 | 1.2 | 10.1 |
| ... | ... | ... | ... |

---

### Daily Summary (7 rows)

| date | min_temp | avg_temp | max_temp | total_rain | max_wind | rainy_hours |
|------|----------|----------|----------|-------------|----------|-------------|
| 2025-06-01 | 14.2 | 19.8 | 26.1 | 3.4 | 28.5 | 5 |
| 2025-06-02 | 15.1 | 21.3 | 28.7 | 0.0 | 22.1 | 0 |
| ... | ... | ... | ... | ... | ... | ... |

---

## 🚀 How to Run

1. Clone or download this repository  
2. Open Jupyter Notebook  
3. Navigate to project folder  
4. Open `OpsPulse_Simple.ipynb`  
5. Run all cells:


All outputs will be generated automatically inside `weather_data/`.

---

## ✅ Automated Tests

The pipeline includes 3 Pytest checks:

| Test | What it validates |
|------|------------------|
| test_columns_exist | Required columns are present |
| test_rain_flag | Rain detection logic is correct |
| test_csv_save | Data is saved and loaded correctly |

All tests must pass for pipeline integrity.

---

## 📈 Key Learnings

- Working with real-world APIs  
- Safe handling of raw data (before transformation)  
- Data cleaning using Pandas  
- Feature engineering (rain flags, wind categorization)  
- Aggregating time-series data  
- Writing automated tests for data pipelines  
- Building an end-to-end data workflow  

---

## 🌐 Data Source

Open-Meteo API  
https://open-meteo.com  

- Free and open-source  
- No API key required  
- Data: 7-day hourly forecast (NYC coordinates)

---

## 👤 Author

Built as a hands-on data engineering project focusing on real-world pipeline design and automation.

---

## ⭐ If you like this project

Give it a star ⭐ — it helps others discover it too!
