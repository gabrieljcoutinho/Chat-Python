import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carrega variáveis de ambiente
load_dotenv()

# Obtém a chave da API Gemini do arquivo .env
GEMINI_API = os.getenv("GEMINI_API")

# Configura a API do Google Gemini
genai.configure(api_key=GEMINI_API)

# Técnica de Prompt de Instrução: orienta o modelo sobre o tipo de resposta desejada
prompt_instrucao = (
    "Você é um agente de recomendação especializado em jogo do Ps5. "
    "Liste apenas os nomes dos produtos e ofereça uma breve descrição de cada um, "
    "focando em jogos de varias categorias."
)

# Cria o modelo generativo com instrução do sistema
modelo = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=prompt_instrucao
)

# Pergunta do usuário
pergunta = "Liste 5 jogos mais famosos."

try:
    # Gera resposta usando o modelo
    resposta = modelo.generate_content(pergunta)
    
    # Exibe a resposta gerada
    print(f'Resposta gerada:\n{resposta.text}')
    
except Exception as e:
    print(f"Erro ao gerar resposta: {e}")