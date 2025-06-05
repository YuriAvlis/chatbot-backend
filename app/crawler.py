# Módulo de Leitura (Crawler simples) 
import requests
from bs4 import BeautifulSoup

def extrair_conteudo_do_site(url="https://www.jovemprogramador.com.br"):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  
  textos = soup.stripped_strings
  conteudo = "\n".join(textos)
  
  with open("data/content.txt", "w", encoding="utf-8") as f:
    f.write(conteudo)
    
    return "Conteúdo salvo em data/content.txt"
  
  