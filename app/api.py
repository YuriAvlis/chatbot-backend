# Rota API
from flask import Blueprint, request, jsonify
from app.responder import responder_automatico

chatbot_api = Blueprint('chatbot_api', __name__)

@chatbot_api.route('/pergunta', mthods=['POST'])
def responder():
    data = request.json
    pergunta = data.get('pergunta', '')
    resposta = responder_automatico(pergunta)
    return jsonify({'resposta': resposta})


