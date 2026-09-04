# SYN Scan

Esse programa faz um scan das portas desejadas de um computador e permite saber quais portas estão abertas usando a biblioteca de manipulação de pacotes Scapy.

## Instalação

Recomendo que crie um ambiente virtual python para instalar o Scapy.

```
python -m venv .venv
source .venv/bin/activate # Linux/macOS
.venv\Scripts\activate # Windows
pip install scapy
```

## Como usar

Procure no programa a variavel "ip", "porta_inicio" e "porta_fim" e digite, respectivamente o IP alvo do seu scan, a porta de onde o scan começará e a de onde ele terminará.

```python
# Exemplo
ip = "192.168.34.10" 
porta_inicio = 1     
porta_fim = 443
```

O programa precisa rodar com o sudo/root. No terminal, rode:

```
sudo python3 synScan.py
```

## O que esperar quando rodar:
O programa vai mostrar todas as respostas das portas selecionadas. Procure pela flag da resposta na área ###[ TCP ]###, se for RA a porta esta fechada, se for SA está aberta.
Por ultimo, na ultima linha, mostrará uma lista das portas abertas.

## Atenção!
O uso desse código para fins maliciosos é completamente proibido. Ele foi feito com propositos acadêmicos e deve permanecer com esse propósito.
