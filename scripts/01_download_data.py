#!/usr/bin/env python3
"""
Script para download dos dados de exoplanetas da NASA
Fonte: NASA Exoplanet Archive
"""

import requests
import pandas as pd
from datetime import datetime
import sys

def download_exoplanet_data():
    """
    Baixa dados de exoplanetas do NASA Exoplanet Archive
    """
    
    print("=" * 60)
    print("🌌 NASA EXOPLANET DATA DOWNLOADER")
    print("=" * 60)
    print()
    
    # URL da API do NASA Exoplanet Archive
    base_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    
    # Query SQL para buscar dados da tabela 'ps' (Planetary Systems)
    query = """
    SELECT 
        pl_name,
        hostname,
        discoverymethod,
        disc_year,
        disc_facility,
        pl_orbper,
        pl_rade,
        pl_bmasse,
        pl_eqt,
        st_teff,
        st_rad,
        st_mass,
        sy_dist,
        sy_snum,
        sy_pnum
    FROM ps
    WHERE 
        pl_rade IS NOT NULL AND
        pl_eqt IS NOT NULL AND
        st_teff IS NOT NULL
    """
    
    params = {
        'query': query,
        'format': 'csv'
    }
    
    print("📡 Conectando ao NASA Exoplanet Archive...")
    print(f"🔗 URL: {base_url}")
    print()
    
    try:
        # Fazer requisição
        print("⏳ Baixando dados... (pode levar 10-30 segundos)")
        response = requests.get(base_url, params=params, timeout=60)
        response.raise_for_status()
        
        # Salvar CSV bruto
        output_file = "data/raw/exoplanets_raw.csv"
        with open(output_file, 'wb') as f:
            f.write(response.content)
        
        print("✅ Download completo!")
        print()
        
        # Ler e mostrar estatísticas
        df = pd.read_csv(output_file)
        
        print("=" * 60)
        print("📊 ESTATÍSTICAS DOS DADOS")
        print("=" * 60)
        print(f"📁 Arquivo salvo: {output_file}")
        print(f"📦 Tamanho do arquivo: {len(response.content) / 1024:.2f} KB")
        print(f"🌍 Total de exoplanetas: {len(df):,}")
        print(f"📋 Total de colunas: {len(df.columns)}")
        print()
        
        print("🔭 Métodos de descoberta:")
        discovery_counts = df['discoverymethod'].value_counts()
        for method, count in discovery_counts.head(5).items():
            print(f"   • {method}: {count:,} planetas")
        print()
        
        print("📅 Anos de descoberta:")
        print(f"   • Primeiro: {df['disc_year'].min():.0f}")
        print(f"   • Mais recente: {df['disc_year'].max():.0f}")
        print()
        
        print("📋 Primeiras 5 linhas:")
        print(df[['pl_name', 'hostname', 'pl_rade', 'pl_eqt', 'sy_dist']].head())
        print()
        
        print("=" * 60)
        print("✅ DOWNLOAD CONCLUÍDO COM SUCESSO!")
        print("=" * 60)
        print()
        print("📌 Próximo passo: Upload para HDFS")
        
        return 0
        
    except requests.exceptions.RequestException as e:
        print(f"❌ ERRO ao baixar dados: {e}")
        return 1
    except Exception as e:
        print(f"❌ ERRO inesperado: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(download_exoplanet_data())
