# 📖 Data Dictionary

Complete reference for all data fields used in the Exoplanet Analysis project.

---

## 📊 Source: NASA Exoplanet Archive

**Official Documentation**: https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html

---

## 🌍 Planetary Properties

### Basic Identification

| Column | Type | Description | Example | Unit |
|--------|------|-------------|---------|------|
| `pl_name` | STRING | Planet name | Kepler-442 b | - |
| `hostname` | STRING | Host star name | Kepler-442 | - |
| `discoverymethod` | STRING | Detection method | Transit, Radial Velocity | - |
| `disc_year` | INT | Year of discovery | 2015 | year |
| `disc_facility` | STRING | Discovery facility | Kepler | - |

### Orbital Properties

| Column | Type | Description | Example | Unit |
|--------|------|-------------|---------|------|
| `pl_orbper` | DOUBLE | Orbital period | 112.3 | days |
| `pl_orbsmax` | DOUBLE | Orbit semi-major axis | 0.4 | AU |
| `pl_orbeccen` | DOUBLE | Orbital eccentricity | 0.04 | - |
| `pl_orbincl` | DOUBLE | Orbital inclination | 89.7 | degrees |

### Physical Properties

| Column | Type | Description | Example | Unit |
|--------|------|-------------|---------|------|
| `pl_rade` | DOUBLE | Planet radius | 1.34 | Earth radii |
| `pl_radj` | DOUBLE | Planet radius | 0.119 | Jupiter radii |
| `pl_bmasse` | DOUBLE | Planet mass (best) | 2.36 | Earth masses |
| `pl_bmassj` | DOUBLE | Planet mass (best) | 0.0074 | Jupiter masses |
| `pl_dens` | DOUBLE | Planet density | 5.2 | g/cm³ |

### Temperature

| Column | Type | Description | Example | Unit |
|--------|------|-------------|---------|------|
| `pl_eqt` | DOUBLE | Equilibrium temperature | 233 | Kelvin |
| `pl_eqt_earth_equivalent` | DOUBLE | Temperature in Celsius | -40 | °C |

---

## ⭐ Stellar Properties (Host Star)

### Basic Properties

| Column | Type | Description | Example | Unit |
|--------|------|-------------|---------|------|
| `st_spectype` | STRING | Spectral type | K2V | - |
| `st_teff` | DOUBLE | Stellar temperature | 4402 | Kelvin |
| `st_rad` | DOUBLE | Stellar radius | 0.61 | Solar radii |
| `st_mass` | DOUBLE | Stellar mass | 0.61 | Solar masses |
| `st_logg` | DOUBLE | Surface gravity | 4.63 | log10(cm/s²) |
| `st_age` | DOUBLE | Stellar age | 2.9 | Gyr |

### Luminosity & Magnitude

| Column | Type | Description | Example | Unit |
|--------|------|-------------|---------|------|
| `st_lum` | DOUBLE | Stellar luminosity | 0.17 | log(Solar) |
| `st_optmag` | DOUBLE | Optical magnitude | 14.8 | mag |

---

## 🌌 System Properties

| Column | Type | Description | Example | Unit |
|--------|------|-------------|---------|------|
| `sy_snum` | INT | Number of stars | 1 | - |
| `sy_pnum` | INT | Number of planets | 1 | - |
| `sy_mnum` | INT | Number of moons | 0 | - |
| `sy_dist` | DOUBLE | Distance from Earth | 370 | parsecs |
| `sy_dist_lightyears` | DOUBLE | Distance (converted) | 1206 | light-years |
| `sy_gaiamag` | DOUBLE | Gaia magnitude | 14.3 | mag |

---

## 🔭 Discovery & Publication

| Column | Type | Description | Example | Unit |
|--------|------|-------------|---------|------|
| `disc_pubdate` | DATE | Publication date | 2015-01-06 | YYYY-MM-DD |
| `disc_locale` | STRING | Discovery locale | Space | - |
| `disc_telescope` | STRING | Discovery telescope | Kepler | - |
| `disc_instrument` | STRING | Discovery instrument | Kepler CCD Array | - |

---

## 🆕 Engineered Features (Added by Processing)

### Habitability Indicators

| Column | Type | Description | Logic | Range |
|--------|------|-------------|-------|-------|
| `is_earth_size` | INT | Similar to Earth size | `pl_rade BETWEEN 0.5 AND 2.0` | 0 or 1 |
| `is_habitable_temp` | INT | Temperature in habitable zone | `pl_eqt BETWEEN 200 AND 350` | 0 or 1 |
| `is_sun_like_star` | INT | Host star similar to Sun | `st_teff BETWEEN 4000 AND 7000` | 0 or 1 |
| `is_nearby` | INT | Reasonably close to Earth | `sy_dist < 1000` | 0 or 1 |
| `habitability_score` | INT | Total habitability score | Sum of above 4 indicators | 0-4 |

### Planet Categories

| Column | Type | Description | Logic |
|--------|------|-------------|-------|
| `planet_category` | STRING | Planet type classification | Based on `pl_rade` |

**Category Definitions**:
- **Rocky (like Earth)**: `pl_rade < 1.25`
- **Super-Earth**: `1.25 <= pl_rade < 2.0`
- **Neptune-like**: `2.0 <= pl_rade < 6.0`
- **Jupiter-like**: `pl_rade >= 6.0`

---

## 📏 Unit Conversions

### Common Conversions Used

| From | To | Conversion Factor |
|------|-----|-------------------|
| Parsecs | Light-years | 1 pc = 3.26156 ly |
| Kelvin | Celsius | °C = K - 273.15 |
| Kelvin | Fahrenheit | °F = (K - 273.15) × 9/5 + 32 |
| Earth radii | km | 1 R⊕ = 6,371 km |
| Jupiter radii | km | 1 R♃ = 69,911 km |
| Earth masses | kg | 1 M⊕ = 5.972 × 10²⁴ kg |
| AU | km | 1 AU = 149,597,871 km |

---

## 🎯 Detection Methods

### Discovery Method Descriptions

| Method | Description | Percentage |
|--------|-------------|------------|
| **Transit** | Planet passes in front of star, causing brightness dip | ~75% |
| **Radial Velocity** | Star wobbles due to planet's gravity | ~20% |
| **Direct Imaging** | Direct observation of planet | ~3% |
| **Microlensing** | Gravitational lensing effect | ~1% |
| **Transit Timing** | Variations in transit timing | ~1% |
| **Astrometry** | Star's position shifts | <1% |
| **Pulsation Timing** | Timing variations in pulsar signals | <1% |

---

## 🌡️ Temperature Reference Points

### Habitability Temperature Range

| Temperature (K) | Temperature (°C) | Description |
|-----------------|------------------|-------------|
| 200 | -73 | Lower bound of habitability zone |
| 273 | 0 | Water freezing point |
| 288 | 15 | Earth's average temperature |
| 310 | 37 | Human body temperature |
| 350 | 77 | Upper bound of habitability zone |
| 373 | 100 | Water boiling point |

---

## 🔬 Data Quality Indicators

### Null Values Handling

| Column | Null Handling | Reason |
|--------|---------------|--------|
| `pl_rade` | Required | Essential for size classification |
| `pl_eqt` | Required | Essential for habitability |
| `st_teff` | Required | Essential for star classification |
| `pl_bmasse` | Optional | Not all planets have mass estimates |
| `pl_orbper` | Optional | Not critical for basic analysis |

### Data Validation Rules

1. **Radius**: `pl_rade > 0` and `pl_rade < 100`
2. **Temperature**: `pl_eqt > 0` and `pl_eqt < 5000`
3. **Distance**: `sy_dist > 0`
4. **Year**: `disc_year >= 1992` and `disc_year <= 2025`

---

## 📊 Aggregated Tables

### discovery_stats

| Column | Type | Description |
|--------|------|-------------|
| `discoverymethod` | STRING | Detection method |
| `total_planets` | BIGINT | Count of planets |
| `avg_radius` | DOUBLE | Average planet radius |
| `avg_temperature` | DOUBLE | Average equilibrium temp |

### category_stats

| Column | Type | Description |
|--------|------|-------------|
| `planet_category` | STRING | Planet type |
| `count` | BIGINT | Number of planets |
| `avg_temp` | DOUBLE | Average temperature |
| `closest_distance` | DOUBLE | Nearest planet distance |

### earth_candidates

| Column | Type | Description |
|--------|------|-------------|
| `pl_name` | STRING | Planet name |
| `hostname` | STRING | Host star |
| `pl_rade` | DOUBLE | Planet radius |
| `pl_eqt` | DOUBLE | Temperature |
| `sy_dist` | DOUBLE | Distance |
| `habitability_score` | INT | Score (3 or 4) |
| `disc_year` | INT | Discovery year |

---

## 📝 Notes on Data Quality

### Known Limitations

1. **Missing Data**: Not all planets have complete information
2. **Estimation Methods**: Some values are estimates with uncertainties
3. **Discovery Bias**: Transit method favors large, close-in planets
4. **Historical Data**: Older discoveries may have less accurate measurements

### Data Sources

- **Primary**: NASA Exoplanet Archive (https://exoplanetarchive.ipac.caltech.edu/)
- **Updated**: Monthly with new discoveries
- **Missions**: Kepler, TESS, ground-based surveys

---

## 🔗 External References

- [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)
- [TAP Service Documentation](https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html)
- [Column Definitions](https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html)

---

*Last updated: 2025-10-20*