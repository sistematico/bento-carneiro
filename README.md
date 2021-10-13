# Bento Carneiro

![Bento Carneiro](https://raw.githubusercontent.com/sistematico/bento-carneiro/main/assets/img/bento_carneiro.jpg "Bento Carneiro")  

*O vampiro brasileiro*

Um bot anti-spam para Telegram usando o wrapper [python-telegram-bot](https://python-telegram-bot.org).

## Começando

1- Instale o python-telegram-bot: `pip install python-telegram-bot`
2- Copie o arquivo `systemd/bentocarneiro.service` para `/etc/systemd/system/`
3- Clone este repositório: `mkdir /var/bentocarneiro/ && git clone https://github.com/sistematico/bento-carneiro.git /var/bentocarneiro/bot`
4- Crie um usuário para rodar o bot: `useradd -r -d /var/bentocarneiro -s /bin/bash bentocarneiro`
5- Corrija as permissões se necessário: `sudo chown -R bentocarneiro:bentocarneiro /var/bentocarneiro`
6- Recarregue as unidades do systemd: `sudo systemd daemon-reload`
7- Crie o arquivo `/var/bentocarneiro/bot/config/config.py` com o seu token no formato: `TOKEN='SEU_TOKEN_AQUI'`(para saber como gerar um token para seu bot consulte o [@BotFather](https://t.me/botfather))
8- Inicie o serviço: `sudo systemctl --now enable bentocarneiro`
