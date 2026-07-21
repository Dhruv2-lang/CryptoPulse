# 📈 CryptoPulse

An automated cryptocurrency analytics platform that collects live market data, stores it in a SQLite database, computes rolling analytics, and visualizes insights through an interactive Streamlit dashboard.

---

## 🚀 Overview

CryptoPulse is an end-to-end data engineering and analytics project built with Python. The application automatically fetches cryptocurrency prices on a scheduled basis using GitHub Actions, stores historical records in SQLite, performs analytical computations with Pandas, and presents the results through an interactive Streamlit dashboard.

The project demonstrates the complete lifecycle of a modern data pipeline:

- Data Collection
- Data Storage
- Data Processing
- Data Visualization
- Workflow Automation

---

## ✨ Features

- 📊 Interactive Streamlit dashboard
- 📈 Historical cryptocurrency price visualization
- 📉 Rolling volatility analysis
- 🗄 SQLite database for historical data storage
- ⚡ Automated hourly data collection
- 🔄 GitHub Actions workflow automation
- 🪙 Multi-cryptocurrency comparison
- 🎯 Dynamic filtering by selected coins and time window
- 📋 Raw dataset explorer

---

## 🏗️ System Architecture

```
                    CoinGecko API
                           │
                           ▼
              Automated Data Collection
                  (GitHub Actions)
                           │
                           ▼
                 Data Processing (Pandas)
                           │
                           ▼
                 SQLite Database Storage
                           │
                           ▼
              Streamlit Analytics Dashboard
                           │
                           ▼
        Interactive Charts • Metrics • Insights
```

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Dashboard | Streamlit |
| Database | SQLite |
| Data Processing | Pandas |
| Visualization | Plotly |
| Automation | GitHub Actions |
| API | CoinGecko API |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```
CryptoPulse/
│
├── .github/
│   └── workflows/
│       └── update_data.yml
│
├── data/
│   └── crypto.db
│
├── src/
│   ├── dashboard.py
│   ├── fetch_prices.py
│   ├── analytics.py
│   ├── database.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📊 Dashboard Modules

### Price Trends

Visualize historical cryptocurrency prices using interactive Plotly charts.

### Volatility Analysis

Analyze rolling volatility and compare market fluctuations across different cryptocurrencies.

### Raw Data

Inspect the underlying historical dataset stored in the SQLite database.

---

## ⚙️ Automated Workflow

The project automatically updates market data through GitHub Actions.

Workflow:

1. Fetch latest cryptocurrency prices from CoinGecko
2. Validate API response
3. Store data in SQLite
4. Compute rolling analytics
5. Commit updated database
6. Refresh dashboard

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/CryptoPulse.git
cd CryptoPulse
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Launch the dashboard

```bash
streamlit run src/dashboard.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 📸 Dashboard Preview

### Home Dashboard

> Add a screenshot here

```markdown
![Dashboard](images/dashboard.png)
```

### Price Trends

> Add a screenshot here

```markdown
![Price Trends](images/price-trends.png)
```

### Volatility Analysis

> Add a screenshot here

```markdown
![Volatility](images/volatility.png)
```

---

## 📈 Future Improvements

- Portfolio tracking
- Price prediction using Machine Learning
- Candlestick charts
- Market capitalization analytics
- Trading volume visualization
- Email or Telegram price alerts
- Docker deployment
- Cloud database integration

---

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Data Engineering
- REST API Integration
- ETL Pipelines
- Workflow Automation
- Time-Series Analytics
- Data Visualization
- Python Development
- SQLite Database Management
- GitHub Actions CI/CD

---

## 🤝 Contributing

Contributions are welcome.

If you would like to improve CryptoPulse:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request


---

## 👤 Author

**Dhruv Pratap Singh**

GitHub: https://github.com/your-username

---

⭐ If you found this project useful, consider starring the repository.
