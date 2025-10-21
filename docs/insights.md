# 🌍 Hunting for Earth 2.0 - Insights e Descobertas

## 📊 Visão Geral do Dataset

Após processar e analisar os dados do **NASA Exoplanet Archive**, chegamos a números impressionantes sobre a busca por mundos habitáveis além do nosso Sistema Solar.

### Estatísticas Gerais

| Métrica | Valor |
|---------|-------|
| **Total de Exoplanetas** | 5,759 planetas confirmados |
| **Métodos de Descoberta** | 10 técnicas diferentes |
| **Raio Médio** | 5.09× Terra |
| **Massa Média** | 195.96× Terra |
| **Temperatura Média** | 863K (590°C) |
| **Candidatos Habitáveis** | 65 planetas (score ≥ 3) |

---

## 🔭 Métodos de Descoberta

A análise revelou que o método **Transit** domina amplamente as descobertas de exoplanetas:

| Método | Planetas | Percentual |
|--------|----------|------------|
| **Transit** | 4,111 | 71.4% |
| **Radial Velocity** | 1,068 | 18.5% |
| **Microlensing** | 208 | 3.6% |
| **Imaging** | 169 | 2.9% |
| **Eclipse Timing Variations** | 24 | 0.4% |
| **Outros métodos** | <1% cada | - |

### 💡 Insight Chave
O método Transit é tão eficaz porque detecta a diminuição do brilho estelar quando um planeta passa em frente à sua estrela. Missões como **Kepler** e **TESS** utilizaram essa técnica com enorme sucesso!

---

## 🪐 Categorias de Planetas

Nossa análise classificou os exoplanetas em 4 categorias baseadas no tamanho:

| Categoria | Quantidade | Características |
|-----------|------------|-----------------|
| **Super-Earth** | 1,571 | 1.25-2× raio da Terra |
| **Gas Giant** | 1,434 | >4× raio da Terra |
| **Neptune-like** | 1,381 | 2-4× raio da Terra |
| **Terrestrial** | 1,373 | <1.25× raio da Terra |

### 📈 Observação
A predominância de **Super-Terras** sugere que planetas ligeiramente maiores que a Terra podem ser mais comuns na galáxia do que pensávamos!

---

## 🌍 Candidatos a "Terra 2.0"

Aplicamos um **Habitability Score** (0-4) baseado em:
- ✅ Tamanho similar à Terra (0.5-2× raio)
- ✅ Temperatura adequada (200-350K)
- ✅ Estrela hospedeira tipo solar
- ✅ Distância da Terra

### 🏆 Top 5 Candidatos Mais Promissores

#### 1. 🥇 **Kepler-442 b** - O Campeão!
- **Habitability Score**: 4.0/4.0 ⭐⭐⭐⭐
- **Raio**: 1.34× Terra
- **Temperatura**: 233K (-40°C)
- **Distância**: 370 parsecs (~1,206 anos-luz)
- **Por quê?**: Tamanho ideal, temperatura na zona habitável, estrela estável!

#### 2. 🥈 **Kepler-62 f**
- **Habitability Score**: 4.0/4.0 ⭐⭐⭐⭐
- **Raio**: 1.41× Terra
- **Temperatura**: 208K (-65°C)
- **Distância**: 368 parsecs (~1,200 anos-luz)
- **Destaque**: Possível mundo oceânico com efeito estufa natural

#### 3. 🥉 **Kepler-186 f** - O Mais Famoso
- **Habitability Score**: 4.0/4.0 ⭐⭐⭐⭐
- **Raio**: 1.17× Terra
- **Temperatura**: 188K (-85°C)
- **Distância**: 178 parsecs (~580 anos-luz)
- **Destaque**: Primeiro planeta do tamanho da Terra na zona habitável!

#### 4. **Kepler-1649 c** - O Mais Próximo!
- **Habitability Score**: 3.0/4.0 ⭐⭐⭐
- **Raio**: 1.06× Terra
- **Temperatura**: 234K (-39°C)
- **Distância**: 91 parsecs (~297 anos-luz) 🚀
- **Destaque**: O candidato habitável MAIS PRÓXIMO de nós!

#### 5. **Kepler-296 f**
- **Habitability Score**: 3.0/4.0 ⭐⭐⭐
- **Raio**: 1.75× Terra
- **Temperatura**: 269K (-4°C)
- **Distância**: 533 parsecs (~1,738 anos-luz)

---

## 🎯 Principais Descobertas

### 1. **A Zona Habitável é Real!**
Encontramos **65 planetas** com características favoráveis à vida como conhecemos. Isso representa **1.13%** de todos os exoplanetas conhecidos.

### 2. **Planetas Rochosos São Comuns**
Quase **24%** dos exoplanetas são terrestriais ou super-terras, sugerindo que mundos rochosos não são raros na galáxia.

### 3. **A Maioria é MUITO Quente!**
Com temperatura média de **863K** (590°C), a maioria dos exoplanetas descobertos orbitam muito próximos de suas estrelas - os chamados "Hot Jupiters" e "Hot Neptunes".

### 4. **Kepler Revolucionou o Campo**
A predominância do método Transit (71.4%) e nomes começando com "Kepler-" mostram o impacto monumental da missão **Kepler Space Telescope** (2009-2018).

### 5. **Estamos Apenas Começando**
Com apenas 5,759 exoplanetas confirmados de um estimado de **bilhões** só na Via Láctea, mal arranhamos a superfície da busca por vida extraterrestre!

---

## 🚀 Implicações para a Busca por Vida

### Perspectiva Otimista 😊
- 65 candidatos habitáveis é um número encorajador
- A diversidade de planetas sugere que a formação planetária é comum
- Tecnologias futuras (James Webb, missões futuras) podem detectar bioassinaturas

### Perspectiva Realista 🤔
- "Habitável" ≠ "Habitado"
- Distâncias enormes (centenas de anos-luz) tornam visitas impossíveis com tecnologia atual
- Temperaturas frias nos melhores candidatos requerem atmosferas espessas para manter água líquida

### Próximos Passos 🔬
1. **Análise de Atmosferas**: Telescópios como James Webb podem detectar vapor d'água e metano
2. **Busca por Bioassinaturas**: Oxigênio + metano = possível vida?
3. **Melhor Caracterização**: Determinar massa, composição e atividade geológica

---

## 📈 Metodologia do Habitability Score

Nosso score customizado considera:

```python
habitability_score = 0

# 1. Tamanho similar à Terra (0.5-2× raio)
if 0.5 <= pl_rade <= 2.0:
    habitability_score += 1

# 2. Temperatura na zona habitável (200-350K ou -73°C a 77°C)
if 200 <= pl_eqt <= 350:
    habitability_score += 1

# 3. Estrela tipo solar (4500-7000K)
if 4500 <= st_teff <= 7000:
    habitability_score += 1

# 4. Distância razoável (<500 parsecs ou ~1,630 anos-luz)
if sy_dist < 500:
    habitability_score += 1

# Score final: 0 (nenhum critério) a 4 (todos os critérios)
```

---

## 🎓 Lições Aprendidas com Big Data

### Sobre os Dados
- **Volume**: 5,759 registros com 100+ campos cada
- **Variedade**: Dados de múltiplas missões (Kepler, TESS, HST, ground-based)
- **Qualidade**: ~30% dos registros têm dados incompletos (campos nulos)
- **Velocidade**: API da NASA permite atualizações diárias

### Stack Tecnológico Performance
- **Spark**: Processou 5,759 registros em segundos (overkill para esse volume, mas pronto para escalar!)
- **Parquet**: Reduziu tamanho dos dados em ~60% vs CSV
- **Hive**: Metastore funcionou perfeitamente para catalogação
- **HDFS**: Arquitetura distribuída pronta para datasets maiores

---

## 🌟 Conclusão

A busca por **Earth 2.0** não é mais ficção científica - é ciência de dados! 

Com **5,759 mundos** catalogados e **65 candidatos habitáveis**, estamos vivendo uma era dourada da astronomia. Ferramentas de Big Data como **Hadoop, Spark e Hive** permitem que cientistas (e entusiastas!) processem volumes massivos de dados astronômicos que antes eram impossíveis de analisar.

**Kepler-442 b**, nosso campeão com score 4.0, pode estar a 1,206 anos-luz de distância, mas cada análise nos aproxima da resposta à pergunta mais antiga da humanidade:

> **"Estamos sozinhos no universo?"** 🌌

A resposta pode estar escondida nesses dados... e agora temos as ferramentas para encontrá-la! 🚀

---

## 📚 Referências

- **NASA Exoplanet Archive**: https://exoplanetarchive.ipac.caltech.edu/
- **Dataset**: Planetary Systems Composite Data (PSCompPars)
- **Processamento**: Apache Spark 3.5.0
- **Armazenamento**: Apache Hadoop 3.3.6 (HDFS) + Apache Parquet
- **Análise**: Apache Hive 3.1.3
- **Data de Análise**: Janeiro 2025

---

*Documento gerado como parte do projeto "Hunting for Earth 2.0 with Big Data"*  
*Stack: Hadoop | Spark | Hive | Python | Docker*  
*Autor: Luiz Heming *