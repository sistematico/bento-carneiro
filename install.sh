#!/usr/bin/env bash

[ "$EUID" -eq 0 ] && systemctl daemon-reload

if [ "$EUID" -eq 0 ]; then
    if ! id "bentocarneiro" &>/dev/null; then
        useradd -m -r -d /var/bentocarneiro -s /bin/bash bentocarneiro
        passwd bentocarneiro
    fi
fi

[ ! -f /etc/systemd/system/bentocarneiro.service ] && [ "$EUID" -eq 0 ] && cp etc/systemd/system/bentocarneiro.service /etc/systemd/system/
[ ! -f /etc/sudoers.d/96-bentocarneiro ] && [ "$EUID" -eq 0 ] && cp etc/sudoers.d/96-bentocarneiro /etc/sudoers.d/

[ "$EUID" -eq 0 ] && chmod 440 /etc/sudoers.d/96-bentocarneiro

if [ "$(systemctl is-active bentocarneiro)" == "inactive" ]; then
    [ "$EUID" -eq 0 ] && systemctl enable bentocarneiro || sudo systemctl enable bentocarneiro
fi

[ "$EUID" -eq 0 ] && systemctl restart bentocarneiro || sudo systemctl restart bentocarneiro