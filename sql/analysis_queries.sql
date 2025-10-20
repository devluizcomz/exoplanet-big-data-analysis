
-- ==========================================
-- ANÁLISES AVANÇADAS DE EXOPLANETAS
-- ==========================================

USE exoplanets;

-- ==========================================
-- 1. QUANTOS CANDIDATOS HABITÁVEIS?
-- ==========================================
SELECT 
    'Total Earth 2.0 Candidates (Score >= 3)' as metric,
    COUNT(*) as value
FROM earth_candidates;

-- ==========================================
-- 2. PLANETA MAIS SIMILAR À TERRA
-- ==========================================
SELECT 
    pl_name,
    hostname,
    ROUND(pl_rade, 2) as earth_radii,
    ROUND(pl_eqt, 2) as temp_kelvin,
    ROUND(pl_eqt - 273.15, 1) as temp_celsius,
    ROUND(sy_dist, 2) as distance_parsecs,
    ROUND(sy_dist * 3.26, 1) as distance_lightyears,
    habitability_score
FROM earth_candidates
WHERE habitability_score = 4
ORDER BY sy_dist
LIMIT 1;

-- ==========================================
-- 3. DISTRIBUIÇÃO POR CATEGORIA
-- ==========================================
SELECT 
    planet_category,
    count as total_planets,
    ROUND(count * 100.0 / SUM(count) OVER(), 2) as percentage
FROM category_stats
ORDER BY count DESC;

-- ==========================================
-- 4. TOP 5 MÉTODOS DE DESCOBERTA
-- ==========================================
SELECT 
    discoverymethod,
    total_planets,
    ROUND(avg_radius, 2) as avg_earth_radii,
    ROUND(avg_temp, 2) as avg_temp_kelvin
FROM discovery_stats
ORDER BY total_planets DESC
LIMIT 5;

-- ==========================================
-- 5. TOP 10 CANDIDATOS MAIS PRÓXIMOS
-- ==========================================
SELECT 
    pl_name,
    hostname,
    ROUND(sy_dist * 3.26, 1) as distance_lightyears,
    ROUND(pl_eqt - 273.15, 1) as temp_celsius,
    ROUND(pl_rade, 2) as earth_radii,
    habitability_score
FROM earth_candidates
ORDER BY sy_dist
LIMIT 10;