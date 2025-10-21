# 🌍 Exoplanet Big Data Analysis: Hunting for Earth 2.0

![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
![Hadoop](https://img.shields.io/badge/hadoop-v3.3-yellow.svg)
![Spark](https://img.shields.io/badge/spark-v3.5-orange.svg)
![Hive](https://img.shields.io/badge/hive-v3.1-green.svg)
![Docker](https://img.shields.io/badge/docker-containerized-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> **Análise de 5,759 exoplanetas do NASA Exoplanet Archive usando Apache Hadoop, Spark e Hive para identificar candidatos habitáveis à "Terra 2.0"**

## 📊 Relatório Interativo
🚀 **[Ver Análise Completa (Relatório HTML)](https://fmlwhgoa.gensparkspace.com/)**

## 🎯 Principais Descobertas

- **5,759 exoplanetas** analisados do NASA Exoplanet Archive
- **65 candidatos habitáveis** identificados (1.13% do dataset)
- **3 planetas com score perfeito** de habitabilidade (4.0/4.0)
- **Kepler-442 b** como melhor candidato a "Terra 2.0"
- **71.4% das descobertas** usam método Transit

## 🏆 Top 3 Candidatos a Terra 2.0

| Posição | Planeta | Score | Raio (×Terra) | Temperatura | Distância |
|---------|---------|-------|---------------|-------------|-----------|
| 🥇 | **Kepler-442 b** | 4.0/4.0 | 1.34× | 233 K (-40°C) | 1,206 anos-luz |
| 🥈 | Kepler-62 f | 4.0/4.0 | 1.41× | 208 K (-65°C) | 1,200 anos-luz |
| 🥉 | Kepler-186 f | 4.0/4.0 | 1.17× | 188 K (-85°C) | 580 anos-luz |

## 🛠️ Stack Tecnológico

### Core Technologies
- **Apache Hadoop 3.3** - Distributed storage (HDFS)
- **Apache Spark 3.5** - Distributed processing (PySpark)
- **Apache Hive 3.1** - Data warehouse and SQL queries
- **Python 3.10** - Data processing and analysis
- **Docker** - Containerized environment

### Data Formats & Tools
- **Parquet** - Columnar storage format
- **PostgreSQL** - Hive Metastore
- **Jupyter Notebooks** - Interactive analysis
- **Matplotlib/Seaborn** - Data visualizations

## 🏗️ Arquitetura do Sistema

```
NASA Exoplanet Archive API
          ↓
    [Raw Data Ingestion]
          ↓
      HDFS Storage
          ↓
    Spark Processing
    (Feature Engineering)
          ↓
    Parquet Files (HDFS)
          ↓
    Hive External Tables
          ↓
   Analysis & Insights
```

## 📁 Estrutura do Projeto

```
exoplanet-big-data-analysis/
├── README.md                          # Este arquivo
├── docker/                           # Docker setup
│   ├── docker-compose.yml           # Orquestração de serviços
│   ├── hadoop.env                   # Configurações Hadoop
│   └── README.md                    # Documentação Docker
├── scripts/                         # Scripts de processamento
│   ├── 01_download_data.py          # Download dos dados
│   ├── 02_spark_analysis.py         # Processamento Spark
│   ├── 03_generate_insights.py      # Geração de insights
│   └── 04_create_visualizations.py  # Criação de gráficos
├── sql/                             # Scripts SQL
│   ├── create_tables.sql            # DDL Hive
│   └── analysis_queries.sql         # Consultas analíticas
├── data/                            # Dados do projeto
│   ├── raw/                         # Dados brutos
│   │   └── exoplanets_raw.csv       # Dataset NASA
│   └── processed/                   # Dados processados
│       ├── planets_enriched/        # Planetas com features
│       ├── earth_candidates/        # Candidatos habitáveis
│       ├── discovery_stats/         # Stats por método
│       └── category_stats/          # Stats por categoria
├── docs/                            # Documentação
│   ├── insights.md                  # Insights detalhados
│   ├── architecture.md              # Arquitetura técnica
│   └── data-dictionary.md           # Dicionário de dados
├── visualizations/                  # Gráficos gerados
│   ├── 01_discovery_methods.png     # Métodos descoberta
│   ├── 02_planet_categories.png     # Categorias planetas
│   ├── 03_top5_candidates.png       # Top 5 candidatos
│   ├── 04_general_stats.png         # Dashboard estatísticas
│   ├── 05_earth_comparison.png      # Comparação Terra
│   └── 06_journey_infographic.png   # Infográfico jornada
└── venv/                            # Python virtual environment
```

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
```bash
# Instalar Docker e Docker Compose
docker --version
docker-compose --version

# Instalar Python 3.10+
python --version
```

### 2. Clonar o Repositório
```bash
git clone https://github.com/yourusername/exoplanet-big-data-analysis.git
cd exoplanet-big-data-analysis
```

### 3. Setup do Ambiente Python
```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate   # Windows

# Instalar dependências
pip install requests pandas matplotlib seaborn jupyter pyspark
```

### 4. Iniciar Stack Big Data
```bash
cd docker
docker-compose up -d

# Verificar serviços
docker-compose ps
```

### 5. Executar Pipeline de Dados
```bash
# 1. Download dos dados
python scripts/01_download_data.py

# 2. Processamento Spark
docker exec -it spark-master /spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  /app/scripts/02_spark_analysis.py

# 3. Gerar insights
docker exec -it spark-master /spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  /app/scripts/03_generate_insights.py

# 4. Criar visualizações
python scripts/04_create_visualizations.py
```

### 6. Acessar Interfaces Web
- **Hadoop NameNode:** http://localhost:9870
- **Spark Master:** http://localhost:8080
- **Hive Server:** http://localhost:10002

## 🔬 Metodologia

### Habitability Score (0-4 pontos)
Desenvolvi um score customizado baseado em 4 critérios:

| Critério | Pontos | Range | Descrição |
|----------|--------|-------|-----------|
| Tamanho do Planeta | +1 | 0.5-2× Terra | Similar ao tamanho da Terra |
| Temperatura | +1 | 200-350 K | Faixa adequada para água líquida |
| Tipo de Estrela | +1 | 4500-7000 K | Estrela hospedeira tipo Sol |
| Distância da Terra | +1 | <500 parsecs | Relativamente próximo |

### Feature Engineering
```python
# Exemplo de cálculo do score
def calculate_habitability_score(planet):
    score = 0
    if 0.5 <= planet.radius <= 2.0: score += 1      # Tamanho
    if 200 <= planet.temperature <= 350: score += 1  # Temperatura  
    if 4500 <= planet.star_temp <= 7000: score += 1 # Estrela
    if planet.distance < 500: score += 1            # Distância
    return score
```

## 📈 Performance

- **Processamento:** ~5,759 exoplanetas em **segundos** (Spark in-memory)
- **Storage:** Dados comprimidos em formato Parquet (eficiência de armazenamento)
- **Escalabilidade:** Arquitetura preparada para datasets 100x maiores

## 📖 Documentação Adicional

- 📊 **[Insights Detalhados](docs/insights.md)** - Análises aprofundadas e descobertas
- 🏗️ **[Arquitetura Técnica](docs/architecture.md)** - Detalhes da implementação
- 📚 **[Dicionário de Dados](docs/data-dictionary.md)** - Descrição das variáveis

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:
1. Faça fork do projeto
2. Crie sua feature branch (`git checkout -b feature/nova-analise`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova análise'`)
4. Push para a branch (`git push origin feature/nova-analise`)
5. Crie um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Contato

**Luiz [Seu Sobrenome]** - [Seu Email]
- 💼 LinkedIn: [Seu LinkedIn]
- 🐱 GitHub: [Seu GitHub]
- 🌐 Portfolio: [Seu Site]

## 🙏 Agradecimentos

- 🌌 **NASA Exoplanet Archive** - Pelos dados públicos
- 🚀 **Apache Foundation** - Pelas ferramentas open source (Hadoop, Spark, Hive)
- 🐳 **Docker Community** - Pela containerização simplificada
- 👥 **Cloudera/Hortonworks** - Pela documentação e melhores práticas

---

⭐ **Se este projeto foi útil, considere dar uma estrela!** ⭐

**🌍 A busca por vida continua... e Big Data está acelerando nossas descobertas!** 🚀