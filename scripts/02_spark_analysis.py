#!/usr/bin/env python3
"""
Análise de Exoplanetas com Apache Spark
Processa dados da NASA e identifica candidatos a "Earth 2.0"
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

print("=" * 70)
print("🚀 EXOPLANET BIG DATA ANALYSIS WITH SPARK")
print("=" * 70)
print()

# Criar Spark Session
print("⚙️  Inicializando Spark Session...")
spark = SparkSession.builder \
    .appName("Exoplanet Analysis") \
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

print("✅ Spark Session iniciada!")
print(f"   Spark Version: {spark.version}")
print()

# Ler dados do HDFS
print("📖 Lendo dados do HDFS...")
df = spark.read.csv(
    "hdfs://namenode:9000/user/exoplanets/raw/exoplanets_raw.csv",
    header=True,
    inferSchema=True
)

print(f"✅ Dados carregados: {df.count():,} exoplanetas")
print()

# Mostrar schema
print("📋 Schema dos dados:")
df.printSchema()
print()

# Limpeza básica
print("🧹 Removendo valores nulos das colunas críticas...")
df_clean = df.filter(
    col('pl_rade').isNotNull() &
    col('pl_eqt').isNotNull() &
    col('st_teff').isNotNull()
)
print(f"✅ Após limpeza: {df_clean.count():,} planetas")
print()

# Feature Engineering - Criar Score de Habitabilidade
print("✨ Criando features de habitabilidade...")

df_enriched = df_clean.withColumn(
    "is_earth_size",
    when((col('pl_rade') >= 0.5) & (col('pl_rade') <= 2.0), 1).otherwise(0)
).withColumn(
    "is_habitable_temp",
    when((col('pl_eqt') >= 200) & (col('pl_eqt') <= 350), 1).otherwise(0)
).withColumn(
    "is_sun_like_star",
    when((col('st_teff') >= 4000) & (col('st_teff') <= 7000), 1).otherwise(0)
).withColumn(
    "is_nearby",
    when(col('sy_dist') < 1000, 1).otherwise(0)
).withColumn(
    "habitability_score",
    col('is_earth_size') + col('is_habitable_temp') + 
    col('is_sun_like_star') + col('is_nearby')
).withColumn(
    "planet_category",
    when(col('pl_rade') < 1.25, "Rocky")
    .when((col('pl_rade') >= 1.25) & (col('pl_rade') < 2.0), "Super-Earth")
    .when((col('pl_rade') >= 2.0) & (col('pl_rade') < 6.0), "Neptune-like")
    .when(col('pl_rade') >= 6.0, "Jupiter-like")
    .otherwise("Unknown")
)

print("✅ Features criadas!")
print()

# Análises
print("=" * 70)
print("📊 ANÁLISES E INSIGHTS")
print("=" * 70)
print()

# 1. Candidatos habitáveis
print("🌍 TOP 10 CANDIDATOS A 'EARTH 2.0':")
earth_candidates = df_enriched.filter(
    col('habitability_score') >= 3
).select(
    'pl_name', 'hostname', 'pl_rade', 'pl_eqt', 
    'sy_dist', 'habitability_score'
).orderBy(desc('habitability_score'), 'sy_dist')

earth_candidates.show(10, truncate=False)
print(f"Total de candidatos (score >= 3): {earth_candidates.count()}")
print()

# 2. Distribuição por categoria
print("📊 DISTRIBUIÇÃO POR CATEGORIA:")
category_stats = df_enriched.groupBy('planet_category').agg(
    count('*').alias('count')
).orderBy(desc('count'))
category_stats.show(truncate=False)
print()

# 3. Estatísticas por método de descoberta
print("🔭 PLANETAS POR MÉTODO DE DESCOBERTA:")
discovery_stats = df_enriched.groupBy('discoverymethod').agg(
    count('*').alias('total_planets'),
    round(avg('pl_rade'), 2).alias('avg_radius'),
    round(avg('pl_eqt'), 2).alias('avg_temp')
).orderBy(desc('total_planets'))
discovery_stats.show(10, truncate=False)
print()

# Salvar resultados no HDFS
print("💾 Salvando dados processados no HDFS...")

# Dados enriquecidos
df_enriched.write.mode("overwrite").parquet(
    "hdfs://namenode:9000/user/exoplanets/processed/planets_enriched"
)
print("✅ planets_enriched salvo")

# Candidatos habitáveis
earth_candidates.write.mode("overwrite").parquet(
    "hdfs://namenode:9000/user/exoplanets/processed/earth_candidates"
)
print("✅ earth_candidates salvo")

# Estatísticas
discovery_stats.write.mode("overwrite").parquet(
    "hdfs://namenode:9000/user/exoplanets/processed/discovery_stats"
)
print("✅ discovery_stats salvo")

category_stats.write.mode("overwrite").parquet(
    "hdfs://namenode:9000/user/exoplanets/processed/category_stats"
)
print("✅ category_stats salvo")

print()
print("=" * 70)
print("✅ PROCESSAMENTO COMPLETO!")
print("=" * 70)
print()
print("📌 Próximo passo: Criar tabelas no Hive")

spark.stop()