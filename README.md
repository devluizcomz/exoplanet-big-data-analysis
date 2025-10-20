# 🪐 Hunting for Earth 2.0: Big Data Analysis of 5,600+ Exoplanets

<p align="center">
  <img src="images/cover-image.png" alt="Exoplanet Analysis" width="800"/>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![NASA Data](https://img.shields.io/badge/Data-NASA%20Exoplanet%20Archive-blue)](https://exoplanetarchive.ipac.caltech.edu/)
[![Apache Spark](https://img.shields.io/badge/Apache-Spark-orange)](https://spark.apache.org/)
[![Hadoop](https://img.shields.io/badge/Apache-Hadoop-green)](https://hadoop.apache.org/)

> **"Using Big Data technologies to search for potentially habitable worlds among thousands of confirmed exoplanets"**

---

## 🎯 Project Overview

This project applies **Big Data technologies** (Hadoop, Spark, Hive) to analyze over **5,600 confirmed exoplanets** from NASA's Exoplanet Archive, identifying potentially habitable worlds and uncovering fascinating patterns in planetary systems across our galaxy.

### 🌟 Key Highlights

- 📊 **5,600+ exoplanets** analyzed from NASA Kepler & TESS missions
- 🌍 **Habitability scoring system** based on Earth-like characteristics
- 🔭 **Multi-dimensional analysis**: size, temperature, orbital period, host star properties
- 📈 **Temporal analysis**: Discovery trends from 1992 to 2025
- 🚀 **Scalable pipeline**: Hadoop + Spark + Hive for big data processing

---

## 🏗️ Architecture

```
┌─────────────────┐
│   NASA API      │
│ Exoplanet Data  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│      HDFS       │
│  Distributed    │
│    Storage      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Apache Spark   │
│   Processing    │
│ Feature Eng.    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Apache Hive    │
│  Data Warehouse │
│  SQL Queries    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Insights &    │
│ Visualizations  │
└─────────────────┘
```

---

## 🔬 Methodology

### Habitability Score (0-4)

Each exoplanet receives a score based on four criteria:

1. **Earth-like Size** (0.5 - 2.0 Earth radii)
2. **Habitable Temperature** (200K - 350K / -73°C to 77°C)
3. **Sun-like Host Star** (4000K - 7000K)
4. **Reasonable Distance** (< 1000 parsecs / ~3,260 light-years)

**Score 3-4**: Strong candidates for habitability 🌍  
**Score 2**: Potentially interesting  
**Score 0-1**: Unlikely to be habitable

---

## 📊 Key Findings

### 🌍 Top Earth 2.0 Candidates

| Planet Name | Distance (ly) | Radius (Earth=1) | Temp (°C) | Score |
|------------|---------------|------------------|-----------|-------|
| *[To be filled after analysis]* | - | - | - | 4 |

### 📈 Discovery Trends

- **Total confirmed exoplanets**: 5,600+
- **Kepler mission contribution**: ~70% of all discoveries
- **Potentially habitable candidates**: [TBD]
- **Closest habitable candidate**: [TBD] light-years away

### 🔭 Detection Methods

- **Transit method**: Most effective (~75%)
- **Radial velocity**: ~20%
- **Direct imaging**: ~3%
- **Microlensing & others**: ~2%

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Apache Hadoop** | Distributed storage (HDFS) |
| **Apache Spark** | Large-scale data processing |
| **Apache Hive** | Data warehousing & SQL queries |
| **Python** | Data pipeline & visualizations |
| **Docker** | Containerized environment |
| **Pandas** | Data manipulation |
| **Matplotlib/Seaborn** | Visualizations |

---

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.8+
- 8GB+ RAM
- 20GB+ disk space

### Quick Start

```bash
# Clone repository
git clone https://github.com/[your-username]/exoplanet-big-data-analysis.git
cd exoplanet-big-data-analysis

# Start Hadoop/Spark cluster
cd docker
docker-compose up -d

# Download NASA data
python scripts/01_download_data.py

# Upload to HDFS
hdfs dfs -put data/raw/exoplanets_raw.csv /user/exoplanets/raw/

# Run Spark analysis
spark-submit scripts/02_spark_analysis.py

# Create Hive tables
beeline -u jdbc:hive2://localhost:10000 -f sql/create_tables.sql

# Run analysis queries
beeline -u jdbc:hive2://localhost:10000 -f sql/analysis_queries.sql
```

---

## 📁 Project Structure

```
exoplanet-big-data-analysis/
├── data/                   # Raw & processed data
├── scripts/                # Python processing scripts
├── sql/                    # Hive SQL queries
├── docker/                 # Docker configuration
├── docs/                   # Technical documentation
├── images/                 # Visualizations & screenshots
└── linkedin/               # Marketing materials
```

---

## 📖 Documentation

- [Architecture Details](docs/architecture.md)
- [Data Dictionary](docs/data-dictionary.md)
- [Analysis Insights](docs/insights.md)

---

## 🎓 Learning Outcomes

This project demonstrates:

- ✅ **Big Data pipeline design** for real-world datasets
- ✅ **Distributed computing** with Hadoop & Spark
- ✅ **Data warehousing** with Hive
- ✅ **Feature engineering** for scientific data
- ✅ **SQL optimization** for analytical queries
- ✅ **Docker containerization** for reproducibility

---

## 📊 Results & Insights

> **[Results will be added after completing the analysis]**

Preview of what we'll discover:
- How many potentially habitable exoplanets exist?
- Which star systems are most promising?
- How has exoplanet discovery evolved over time?
- What makes a planet "Earth-like"?

---

## 🤝 Contributing

This is a personal learning project, but suggestions and feedback are welcome! Feel free to open an issue or reach out.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **NASA Exoplanet Archive** for providing open access to exoplanet data
- **Apache Software Foundation** for Hadoop, Spark, and Hive
- **Kepler & TESS missions** for revolutionary exoplanet discoveries

---

## 📬 Contact

**Luiz Heming**  
💼 LinkedIn: [linkedin.com/in/luizheming](https://linkedin.com/in/luizheming)  
🐙 GitHub: [github.com/[your-username]](https://github.com/[your-username])

---

<p align="center">
  <i>🌌 Exploring the universe, one dataset at a time</i>
</p>

<p align="center">
  Made with ❤️ and ☕ | Powered by Big Data
</p>