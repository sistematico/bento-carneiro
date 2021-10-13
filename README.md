# Bento Carneiro

<p align="center">
  <img src="https://raw.githubusercontent.com/sistematico/bento-carneiro/main/assets/img/bento_carneiro.jpg" alt="Bento Carneiro" />
  <em>O vampiro brasileiro</em>
</p>

Um bot anti-spam para Telegram usando o wrapper [python-telegram-bot](https://python-telegram-bot.org).

## Uso

1. Instale o python-telegram-bot: `pip install python-telegram-bot`
2. Copie o arquivo `systemd/bentocarneiro.service` para `/etc/systemd/system/`
3. Clone este repositório: `mkdir /var/bentocarneiro/ && git clone https://github.com/sistematico/bento-carneiro.git /var/bentocarneiro/bot`
4. Crie um usuário para rodar o bot: `useradd -r -d /var/bentocarneiro -s /bin/bash bentocarneiro`
5. Corrija as permissões se necessário: `sudo chown -R bentocarneiro:bentocarneiro /var/bentocarneiro`
6. Recarregue as unidades do systemd: `sudo systemd daemon-reload`
7. Crie o arquivo `/var/bentocarneiro/bot/config/config.py` com o seu token no formato: `TOKEN='SEU_TOKEN_AQUI'`(para saber como gerar um token para seu bot consulte o [@BotFather](https://t.me/botfather))
8. Inicie o serviço: `sudo systemctl --now enable bentocarneiro`

## Contato

- lucas@archlinux.com.br

## Ajude

Se o meu trabalho foi útil de qualquer maneira, considere doar qualquer valor através do das seguintes plataformas:

[![LiberaPay](https://img.shields.io/badge/LiberaPay-gray?logo=liberapay&logoColor=white&style=flat-square)](https://liberapay.com/sistematico/donate) [![PagSeguro](https://img.shields.io/badge/PagSeguro-gray?logo=pagseguro&logoColor=white&style=flat-square)](https://pag.ae/bfxkQW) [![ko-fi](https://img.shields.io/badge/ko--fi-gray?logo=ko-fi&logoColor=white&style=flat-square)](https://ko-fi.com/K3K32RES9) [![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-gray?logo=buy-me-a-coffee&logoColor=white&style=flat-square)](https://www.buymeacoffee.com/sistematico) [![Open Collective](https://img.shields.io/badge/Open_Collective-gray?logo=opencollective&logoColor=white&style=flat-square)](https://opencollective.com/sistematico) [![Patreon](https://img.shields.io/badge/Patreon-gray?logo=patreon&logoColor=white&style=flat-square)](https://patreon.com/sistematico)

![GitHub Sponsors](https://img.shields.io/github/sponsors/sistematico?label=Github%20Sponsors)
