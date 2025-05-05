# 🐺 Bots Oficiais da FURIA

<div align="center">
  <img src="https://furia.gg/wp-content/uploads/2023/12/logo-furia-1.png" alt="Logo FURIA" width="200"/>
  
  ## 🤖 Os Bots Oficiais da Maior Torcida do Brasil!
</div>

---

## 📁 Estrutura do Projeto

```
Furia/
├── telegram_bot/           # Bot do Telegram
│   ├── furia_bot.py       # Código principal
│   ├── requirements.txt   # Dependências do Telegram
│   └── .env              # Configurações (token)
│
└── discord_bot/           # Bot do Discord
    ├── furia_discord_bot.py  # Código principal
    ├── requirements.txt   # Dependências do Discord
    └── .env              # Configurações (token)
```

---

## 🤖 Bot do Telegram

### 🎮 Comandos Disponíveis

| Comando | Descrição | Emoji |
|---------|-----------|-------|
| `/start` | Inicia o bot e mostra os comandos disponíveis | 🚀 |
| `/jogos` | Mostra a agenda de partidas da FURIA | 📅 |
| `/estatisticas` | Mostra estatísticas do time (K/D, mapas favoritos, etc.) | 📊 |
| `/curiosidades` | Mostra fatos divertidos sobre a FURIA | 🤔 |
| `/campeonatos` | Mostra informações sobre os campeonatos | 🏆 |
| `/fun` | Mostra memes e conteúdo divertido | 😂 |

### ⚙️ Como Configurar

1. **Acesse o diretório:**
```bash
cd telegram_bot
```

2. **Instale as dependências específicas do Telegram:**
```bash
pip install -r requirements.txt
```

3. **Configure o token:**
   - Crie/edite o arquivo `.env`
   - Adicione seu token do Telegram:
   ```
   TELEGRAM_TOKEN=seu_token_aqui
   ```

4. **Execute o bot:**
```bash
python3 furia_bot.py
```

