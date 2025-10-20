-- ==========================================
-- CRIAR TABELAS HIVE PARA ANÁLISE
-- ==========================================

-- Criar database
CREATE DATABASE IF NOT EXISTS exoplanets;
USE exoplanets;

-- ==========================================
-- 1. Tabela de planetas enriquecidos
-- ==========================================
CREATE EXTERNAL TABLE IF NOT EXISTS planets_enriched (
    pl_name STRING,
    hostname STRING,
    discoverymethod STRING,
    disc_year INT,
    disc_facility STRING,
    pl_orbper DOUBLE,
    pl_rade DOUBLE,
    pl_bmasse DOUBLE,
    pl_eqt DOUBLE,
    st_teff DOUBLE,
    st_rad DOUBLE,
    st_mass DOUBLE,
    sy_dist DOUBLE,
    sy_snum INT,
    sy_pnum INT,
    is_earth_size INT,
    is_habitable_temp INT,
    is_sun_like_star INT,
    is_nearby INT,
    habitability_score INT,
    planet_category STRING
)
STORED AS PARQUET
LOCATION '/user/exoplanets/processed/planets_enriched';

-- ==========================================
-- 2. Tabela de candidatos habitáveis
-- ==========================================
CREATE EXTERNAL TABLE IF NOT EXISTS earth_candidates (
    pl_name STRING,
    hostname STRING,
    pl_rade DOUBLE,
    pl_eqt DOUBLE,
    sy_dist DOUBLE,
    habitability_score INT
)
STORED AS PARQUET
LOCATION '/user/exoplanets/processed/earth_candidates';

-- ==========================================
-- 3. Estatísticas por método de descoberta
-- ==========================================
CREATE EXTERNAL TABLE IF NOT EXISTS discovery_stats (
    discoverymethod STRING,
    total_planets BIGINT,
    avg_radius DOUBLE,
    avg_temp DOUBLE
)
STORED AS PARQUET
LOCATION '/user/exoplanets/processed/discovery_stats';

-- ==========================================
-- 4. Estatísticas por categoria
-- ==========================================
CREATE EXTERNAL TABLE IF NOT EXISTS category_stats (
    planet_category STRING,
    count BIGINT
)
STORED AS PARQUET
LOCATION '/user/exoplanets/processed/category_stats';

-- Mostrar tabelas criadas
SHOW TABLES;