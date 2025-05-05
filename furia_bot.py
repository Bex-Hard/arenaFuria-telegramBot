import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
from pathlib import Path

# Carregando variáveis de ambiente do diretório pai
dotenv_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path)

# Verificando se o token está presente
token = os.getenv('TELEGRAM_TOKEN')
if not token:
    print("Erro: Token do Telegram não encontrado no arquivo .env")
    print("Por favor, crie um arquivo .env com o token do seu bot")
    print("O arquivo deve estar em:", dotenv_path)
    exit(1)

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Dados de exemplo (em um caso real, isso viria de uma API ou banco de dados)
JOGOS = [
    "FURIA vs MIBR - 20/03/2024 - 19:00",
    "FURIA vs LOUD - 22/03/2024 - 20:00",
    "FURIA vs Imperial - 25/03/2024 - 18:00"
]

ESTATISTICAS = {
    "K/D": "1.25",
    "Mapas Favoritos": "Mirage, Inferno, Ancient",
    "Win Rate": "65%",
    "Headshot %": "45%"
}

CURIOSIDADES = [
    "A FURIA foi fundada em 2017",
    "O time tem uma das maiores torcidas do Brasil",
    "O mascote da FURIA é um lobo",
    "A FURIA já venceu vários campeonatos internacionais"
]

CAMPEONATOS = [
    "ESL Pro League - Em andamento",
    "BLAST Premier - Próxima etapa em abril",
    "IEM Rio - Qualificatórias em maio"
]

MEMES = [
    "https://i.imgur.com/example1.jpg",
    "https://i.imgur.com/example2.jpg",
    "https://i.imgur.com/example3.jpg"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia uma mensagem quando o comando /start é emitido."""
    await update.message.reply_text(
        "Olá! Eu sou o bot da FURIA! 🐺\n"
        "Use os seguintes comandos:\n"
        "/jogos - Ver agenda de partidas\n"
        "/estatisticas - Ver estatísticas do time\n"
        "/curiosidades - Saber fatos divertidos\n"
        "/campeonatos - Ver campeonatos atuais\n"
        "/fun - Ver memes e conteúdo divertido"
    )

async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia a agenda de jogos."""
    mensagem = "📅 Próximos jogos da FURIA:\n\n"
    for jogo in JOGOS:
        mensagem += f"• {jogo}\n"
    await update.message.reply_text(mensagem)

async def estatisticas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia as estatísticas do time."""
    mensagem = "📊 Estatísticas da FURIA:\n\n"
    for key, value in ESTATISTICAS.items():
        mensagem += f"{key}: {value}\n"
    await update.message.reply_text(mensagem)

async def curiosidades(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia curiosidades sobre a FURIA."""
    mensagem = "🤔 Curiosidades sobre a FURIA:\n\n"
    for curiosidade in CURIOSIDADES:
        mensagem += f"• {curiosidade}\n"
    await update.message.reply_text(mensagem)

async def campeonatos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia informações sobre os campeonatos."""
    mensagem = "🏆 Campeonatos da FURIA:\n\n"
    for campeonato in CAMPEONATOS:
        mensagem += f"• {campeonato}\n"
    await update.message.reply_text(mensagem)

async def fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia memes e conteúdo divertido."""
    mensagem = "😂 Memes e conteúdo divertido da FURIA:\n\n"
    for meme in MEMES:
        mensagem += f"{meme}\n"
    await update.message.reply_text(mensagem)

def main():
    """Inicia o bot."""
    # Cria a aplicação
    application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()

    # Adiciona os handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("jogos", jogos))
    application.add_handler(CommandHandler("estatisticas", estatisticas))
    application.add_handler(CommandHandler("curiosidades", curiosidades))
    application.add_handler(CommandHandler("campeonatos", campeonatos))
    application.add_handler(CommandHandler("fun", fun))

    # Inicia o bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 