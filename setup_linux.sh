#!/usr/bin/env bash
# Prepara este proyecto en Linux (Debian/Ubuntu).
# Uso: bash setup_linux.sh
set -e

sudo apt update
sudo apt install -y git python3 python3-venv python3-pip python3-tk

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if command -v code >/dev/null 2>&1; then
    while read -r ext; do
        [ -n "$ext" ] && code --install-extension "$ext"
    done < vscode-extensions.txt
else
    echo "VS Code no esta en el PATH. Instala las extensiones con Settings Sync."
fi

echo "Listo. Activa el entorno con: source .venv/bin/activate"
