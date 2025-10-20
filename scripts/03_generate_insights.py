#!/usr/bin/env python3
"""
Gerar insights detalhados dos dados de exoplanetas usando Spark SQL
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

print("=" * 70)
print("📊 GERANDO INSIGHTS DOS EXOPLANETAS")
print("=" * 70)
print()

# Criar Spark Session
spark = SparkSession.builder \
    .appName("Exoplanet Insights") \
    .getOrCreate()

# Ler dados processados
print("📖 Carregando dados processados...")
planets = spark.read.parquet("hdfs://namenode:9000/user/exoplanets/processed/planets_enriched")
candidates = spark.read.parquet("hdfs://namenode:9000/user/exoplanets/processed/earth_candidates")
print("✅ Dados carregados!")
print()

# ==========================================
# INSIGHT 1: Total de candidatos habitáveis
# ==========================================
print("=" * 70)
print("🌍 INSIGHT 1: CANDIDATOS A 'EARTH 2.0'")
print("=" * 70)
total_candidates = candidates.count()
score_4 = candidates.filter(col('habitability_score') == 4).count()
score_3 = candidates.filter(col('habitability_score') == 3).count()

print(f"Total de candidatos (score >= 3): {total_candidates}")
print(f"  • Score perfeito (4/4): {score_4}")
print(f"  • Score alto (3/4): {score_3}")
print()

# ==========================================
# INSIGHT 2: Planeta mais similar à Terra
# ==========================================
print("=" * 70)
print("🎯 INSIGHT 2: PLANETA MAIS SIMILAR À TERRA")
print("=" * 70)
best_candidate = candidates.filter(col('habitability_score') == 4) \
    .orderBy('sy_dist') \
    .select(
        'pl_name',
        'hostname',
        round('pl_rade', 2).alias('earth_radii'),
        round('pl_eqt', 2).alias('temp_kelvin'),
        round(col('pl_eqt') - 273.15, 1).alias('temp_celsius'),
        round('sy_dist', 2).alias('distance_parsecs'),
        round(col('sy_dist') * 3.26, 1).alias('distance_lightyears')
    ).first()

if best_candidate:
    print(f"Nome: {best_candidate['pl_name']}")
    print(f"Estrela: {best_candidate['hostname']}")
    print(f"Tamanho: {best_candidate['earth_radii']} raios terrestres")
    print(f"Temperatura: {best_candidate['temp_celsius']}°C ({best_candidate['temp_kelvin']}K)")
    print(f"Distância: {best_candidate['distance_lightyears']} anos-luz ({best_candidate['distance_parsecs']} parsecs)")
print()

# ==========================================
# INSIGHT 3: Distribuição por categoria
# ==========================================
print("=" * 70)
print("📊 INSIGHT 3: DISTRIBUIÇÃO POR TIPO DE PLANETA")
print("=" * 70)
category_dist = planets.groupBy('planet_category') \
    .count() \
    .orderBy(desc('count'))

category_dist.show(truncate=False)

total_planets = planets.count()
print("Percentuais:")
for row in category_dist.collect():
    pct = (row['count'] / total_planets) * 100
    print(f"  • {row['planet_category']}: {row['count']} ({pct:.1f}%)")
print()

# ==========================================
# INSIGHT 4: Métodos de descoberta
# ==========================================
print("=" * 70)
print("🔭 INSIGHT 4: MÉTODOS DE DESCOBERTA")
print("=" * 70)
methods = planets.groupBy('discoverymethod') \
    .agg(
        count('*').alias('total'),
        round(avg('pl_rade'), 2).alias('avg_radius')
    ) \
    .orderBy(desc('total'))

methods.show(10, truncate=False)
print()

# ==========================================
# INSIGHT 5: Top 10 mais próximos
# ==========================================
print("=" * 70)
print("🛸 INSIGHT 5: TOP 10 CANDIDATOS MAIS PRÓXIMOS")
print("=" * 70)
nearest = candidates.select(
    'pl_name',
    'hostname',
    round(col('sy_dist') * 3.26, 1).alias('distance_ly'),
    round(col('pl_eqt') - 273.15, 1).alias('temp_c'),
    round('pl_rade', 2).alias('earth_radii'),
    'habitability_score'
).orderBy('distance_ly').limit(10)

nearest.show(10, truncate=False)
print()

# ==========================================
# INSIGHT 6: Estatísticas gerais
# ==========================================
print("=" * 70)
print("📈 INSIGHT 6: ESTATÍSTICAS GERAIS")
print("=" * 70)
stats = planets.select(
    round(avg('pl_rade'), 2).alias('avg_radius'),
    round(avg('pl_eqt'), 2).alias('avg_temp'),
    round(min('sy_dist'), 2).alias('closest_distance'),
    round(max('sy_dist'), 2).alias('farthest_distance')
).first()

print(f"Raio médio dos planetas: {stats['avg_radius']} raios terrestres")
print(f"Temperatura média: {stats['avg_temp']}K ({stats['avg_temp'] - 273.15:.1f}°C)")
print(f"Sistema mais próximo: {stats['closest_distance']} parsecs ({stats['closest_distance'] * 3.26:.1f} anos-luz)")
print(f"Sistema mais distante: {stats['farthest_distance']} parsecs ({stats['farthest_distance'] * 3.26:.0f} anos-luz)")
print()

print("=" * 70)
print("✅ ANÁLISE COMPLETA!")
print("=" * 70)

spark.stop()