# Iniciar a API Flask

from flask import Flask
from app.api import chatbot_api

app = Flask(__name__)
app.register_blueprint(chatbot_api)

if __name__ == "__main__":
  app.run(debug=True)
