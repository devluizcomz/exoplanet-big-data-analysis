# 🏗️ Architecture Documentation

## System Architecture Overview

This document describes the technical architecture of the Exoplanet Big Data Analysis project.

---

## 📊 Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     DATA INGESTION LAYER                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  NASA Exoplanet Archive API                                │
│  ↓                                                          │
│  Python Download Script (01_download_data.py)              │
│  ↓                                                          │
│  Local Storage (data/raw/exoplanets_raw.csv)               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                   DISTRIBUTED STORAGE LAYER                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  HDFS (Hadoop Distributed File System)                     │
│  ├── /user/exoplanets/raw/                                 │
│  └── /user/exoplanets/processed/                           │
│                                                             │
│  Block Size: 128MB                                         │
│  Replication Factor: 3                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                  PROCESSING & COMPUTE LAYER                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Apache Spark 3.x                                          │
│  ├── Spark Core: Distributed processing                    │
│  ├── Spark SQL: Structured data processing                 │
│  └── DataFrame API: High-level transformations             │
│                                                             │
│  Processing Script: 02_spark_analysis.py                   │
│                                                             │
│  Key Operations:                                           │
│  • Data cleaning & validation                              │
│  • Feature engineering (habitability score)                │
│  • Aggregations & statistics                               │
│  • Parquet format conversion                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                    DATA WAREHOUSE LAYER                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Apache Hive                                               │
│  ├── External Tables                                       │
│  ├── Parquet Storage Format                               │
│  └── SQL Query Interface                                   │
│                                                             │
│  Tables:                                                   │
│  • exoplanets_enriched                                     │
│  • earth_candidates                                        │
│  • discovery_stats                                         │
│  • category_stats                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                   ANALYSIS & INSIGHTS LAYER                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SQL Queries (analysis_queries.sql)                        │
│  Python Visualizations (03_visualizations.py)              │
│  ↓                                                          │
│  Insights & Reports                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🐳 Docker Infrastructure

### Container Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    Docker Network                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────┐  ┌────────────────┐               │
│  │  NameNode      │  │  DataNode      │               │
│  │  (HDFS Master) │  │  (HDFS Worker) │               │
│  │  Port: 9870    │  │                │               │
│  └────────────────┘  └────────────────┘               │
│                                                          │
│  ┌────────────────┐  ┌────────────────┐               │
│  │ Spark Master   │  │ Spark Worker   │               │
│  │ Port: 8080     │  │                │               │
│  └────────────────┘  └────────────────┘               │
│                                                          │
│  ┌────────────────┐                                     │
│  │  Hive Server   │                                     │
│  │  Port: 10000   │                                     │
│  └────────────────┘                                     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Container Specifications

| Container | Image | Ports | Resources |
|-----------|-------|-------|-----------|
| NameNode | bde2020/hadoop-namenode:2.0.0 | 9870, 9000 | 1GB RAM |
| DataNode | bde2020/hadoop-datanode:2.0.0 | - | 2GB RAM |
| Spark Master | bde2020/spark-master:3.1.1 | 8080, 7077 | 1GB RAM |
| Spark Worker | bde2020/spark-worker:3.1.1 | - | 2GB RAM |
| Hive Server | bde2020/hive:2.3.2 | 10000 | 2GB RAM |

---

## 📦 Data Model

### Raw Data Schema

```
exoplanets_raw.csv
├── pl_name: STRING          # Planet name
├── hostname: STRING         # Host star name
├── discoverymethod: STRING  # Detection method
├── disc_year: INT          # Discovery year
├── pl_orbper: DOUBLE       # Orbital period (days)
├── pl_rade: DOUBLE         # Planet radius (Earth radii)
├── pl_bmasse: DOUBLE       # Planet mass (Earth masses)
├── pl_eqt: DOUBLE          # Equilibrium temperature (K)
├── st_teff: DOUBLE         # Stellar temperature (K)
├── st_rad: DOUBLE          # Stellar radius (Solar radii)
├── st_mass: DOUBLE         # Stellar mass (Solar masses)
└── sy_dist: DOUBLE         # System distance (parsecs)
```

### Enriched Data Schema

```
exoplanets_enriched.parquet
├── [All raw columns]
├── is_earth_size: INT          # 1 if 0.5-2.0 Earth radii
├── is_habitable_temp: INT      # 1 if 200-350K
├── is_sun_like_star: INT       # 1 if 4000-7000K
├── is_nearby: INT              # 1 if <1000 parsecs
├── habitability_score: INT     # Sum of above (0-4)
└── planet_category: STRING     # Rocky/Super-Earth/Neptune/Jupiter
```

---

## ⚙️ Processing Pipeline

### Stage 1: Data Ingestion
- **Tool**: Python + Requests library
- **Source**: NASA Exoplanet Archive TAP API
- **Format**: CSV
- **Size**: ~5MB (5,600+ records)

### Stage 2: Data Upload
- **Tool**: HDFS CLI
- **Destination**: `/user/exoplanets/raw/`
- **Replication**: 3x

### Stage 3: Spark Processing
- **Executor Memory**: 2G
- **Executor Cores**: 2
- **Number of Executors**: 2-4
- **Operations**:
  - Data validation & cleaning
  - Feature engineering
  - Aggregations
  - Parquet conversion

### Stage 4: Hive Table Creation
- **Table Type**: External
- **Storage Format**: Parquet
- **Partitioning**: None (small dataset)
- **Compression**: Snappy

### Stage 5: Analysis
- **Tool**: Hive SQL + Python
- **Queries**: Ad-hoc analytical queries
- **Output**: Insights & visualizations

---

## 🔧 Technology Choices

### Why Hadoop?
- **Distributed storage**: Scalable for large datasets
- **Fault tolerance**: Data replication
- **Industry standard**: Relevant for real-world scenarios

### Why Spark?
- **In-memory processing**: 100x faster than MapReduce
- **DataFrame API**: Intuitive data manipulation
- **Unified engine**: Batch + streaming capabilities

### Why Hive?
- **SQL interface**: Familiar query language
- **Data warehouse**: Structured analytical queries
- **Integration**: Works seamlessly with HDFS & Spark

### Why Docker?
- **Reproducibility**: Same environment everywhere
- **Quick setup**: No complex installation
- **Isolation**: Clean development environment

### Why Parquet?
- **Columnar storage**: Efficient for analytics
- **Compression**: 80% smaller than CSV
- **Performance**: Fast read/write operations

---

## 🚀 Performance Considerations

### Optimization Strategies

1. **Data Format**
   - Use Parquet instead of CSV (4-5x faster queries)
   - Enable Snappy compression

2. **Spark Configuration**
   - Tune executor memory based on data size
   - Use appropriate number of partitions
   - Cache frequently accessed DataFrames

3. **Hive Optimization**
   - Use external tables for flexibility
   - Avoid complex JOINs on large tables
   - Use EXPLAIN for query optimization

4. **Storage**
   - HDFS block size: 128MB (default)
   - Replication factor: 3 for small clusters

---

## 📊 Scalability

### Current Setup (Small Dataset)
- **Data size**: ~5MB CSV → ~1MB Parquet
- **Records**: 5,600+
- **Processing time**: <1 minute

### Future Scalability
This architecture scales to:
- **Millions of records**: Add more DataNodes & Workers
- **Terabytes of data**: Increase cluster size
- **Complex analytics**: Add more processing nodes

---

## 🔐 Security Considerations

For production deployment:
- Enable Kerberos authentication
- Configure HDFS permissions
- Use SSL/TLS for data in transit
- Implement role-based access control (RBAC)

---

## 📝 Best Practices Applied

✅ **Separation of concerns**: Each layer has single responsibility  
✅ **Containerization**: Easy deployment & reproducibility  
✅ **Version control**: All code in Git  
✅ **Documentation**: Comprehensive architecture docs  
✅ **Data formats**: Use efficient formats (Parquet)  
✅ **Idempotency**: Scripts can be re-run safely  
✅ **Logging**: Proper error handling & logging  
✅ **Testing**: Data validation at each stage  

---

## 🔗 Related Documentation

- [Data Dictionary](data-dictionary.md)
- [Analysis Insights](insights.md)
- [Main README](../README.md)

---

*Last updated: 2025-10-20*
