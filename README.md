🌦️ OpsPulse — Weather Data Pipeline

A simple but complete end-to-end data pipeline project built in Python.
Fetches real weather data, saves it, cleans it, summarises it, charts it and tests it — all automated.


🎯 Business Problem
Every hour, weather stations around the world generate thousands of data points.
But raw data is messy, inconsistent and hard to read.
OpsPulse solves this by:

Automatically pulling live weather data from the internet
Saving it safely to disk before touching it
Cleaning and transforming it into something useful
Producing a clear daily summary report
Making sure everything works with automated tests


🏗️ Project Architecture
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

📁 Project Structure
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

🛠️ Tools & Technologies
ToolPurpose🐍 PythonCore programming language📓 Jupyter NotebookInteractive development environment🌐 RequestsFetches data from the Open-Meteo API🐼 PandasCleans, transforms and summarises data📊 MatplotlibCreates temperature and rain charts✅ PytestRuns automated tests🌤️ Open-Meteo APIFree weather API — no signup, no key needed

📊 What the Pipeline Produces
Raw Data (168 rows — 7 days x 24 hours)
timetemperature_2mprecipitationwindspeed_10m2025-06-01T00:0018.20.012.42025-06-01T01:0017.81.210.1............
Daily Summary (7 rows — one per day)
datemin_tempavg_tempmax_temptotal_rainmax_windrainy_hrs2025-06-0114.219.826.13.428.552025-06-0215.121.328.70.022.10.....................

🚀 How to Run This Project
Step 1 — Clone or download this repo
Click the green Code button above → Download ZIP → unzip it
Step 2 — Open Jupyter Notebook
Open Anaconda Navigator → Launch Jupyter Notebook → navigate to this folder
Step 3 — Open the notebook
Click on OpsPulse_Simple.ipynb
Step 4 — Run all cells
Click Kernel → Restart & Run All
That's it! All files will be generated automatically inside the weather_data/ folder.

✅ Automated Tests
3 tests written using Pytest that validate:
TestWhat it checkstest_columns_existAll required data columns are presenttest_rain_flagRain flag correctly identifies rainy hourstest_csv_saveCSV file saves and loads with correct data
All 3 tests pass.

📈 Key Learnings from This Project

✅ How to call a real public API and handle the response
✅ How to save raw data before transforming it (best practice)
✅ How to use Pandas for real data cleaning and transformation
✅ How to aggregate data into meaningful summaries
✅ How to write automated tests to validate your pipeline
✅ End-to-end thinking — from raw API data to final report


🌐 Data Source
Open-Meteo — https://open-meteo.com
Free, open-source weather API. No signup. No API key. No cost.
Data: NYC coordinates (40.7128° N, 74.0060° W), 7-day hourly forecast.

👤 Author
Built with curiosity and lots of coffee ☕
Feel free to fork, star and build on top of this!

⭐ If you found this useful
Give this repo a star ⭐ — it helps others find it too!
