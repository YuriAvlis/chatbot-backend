# Módulo de Resposta
from app.interpreter import buscar_resposta

def responder_automatico(pergunta):
  try:
    with open("data/content.txt", "r", encodig="utf-8") as f:
      texto = f.read()
  except FileNotFoundError:
      return "Erro: conteudo ainda não foi carregado."
      
  resposta = buscar_resposta(pergunta, texto)
  
  if resposta:
    return resposta
  else:
      return "Desculpe, não encontrei uma resposta para sua pergunta."
    
  