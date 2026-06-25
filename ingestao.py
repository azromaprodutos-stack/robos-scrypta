import os
import time
from supabase import create_client, Client

# Puxa as chaves secretas das configurações seguras do Railway
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ ERRO: Chaves do Supabase não encontradas nas variáveis de ambiente!")
    exit(1)

# Conecta ao banco de dados Scrypta
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def rodar_captura():
    print("🚀 Scrypta Engine: Iniciando captura automatizada dos dados...")
    
    # Esta estrutura vai simular a carga inicial para as 10 APIs
    dados_carga_inicial = [
        {
            "micro_vertical": "creatina",
            "codigo_ibge_municipio": "3550308",  # São Paulo - SP
            "preco_diesel_medio": 5.890,
            "bandeira_tarifaria_energia": "VERDE",
            "prazo_frete_correios_dias": 2,
            "custo_frete_base": 18.50,
            "hype_tiktok_score": 75.20,
            "busca_google_score": 68.40,
            "preco_medio_marketplace": 95.00,
            "volume_concorrentes_ativos": 142,
            "estoque_global_estimado": 4500,
            "volume_pix_regional": 1250000.00,
            # Scores iniciais simulando o cálculo que as MMs vão assumir depois
            "score_iem_margem": 45.20,
            "score_alpha_hype": 82.10,
            "probabilidade_ruptura_15d": 12.50,
            "probabilidade_explosao_demanda": 88.00
        }
    ]
    
    for registro in dados_carga_inicial:
        try:
            # O 'upsert' insere o dado ou atualiza se ele já existir no mesmo dia/nicho/cidade
            supabase.table("tabela_mestre_temporal").upsert(registro).execute()
            print(f"✅ Dados integrados com sucesso: {registro['micro_vertical']} em SP.")
        except Exception as e:
            print(f"❌ Falha ao injetar dados: {str(e)}")

if __name__ == "__main__":
    rodar_captura()
