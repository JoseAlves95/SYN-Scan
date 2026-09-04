# SYN Scan

Esse programa faz um scan das portas desejadas de um computador e permite saber quais portas estao abertas usando a biblioteca de manipulacao de pacotes Scapy.

## Instalacao

Recomendo que crie um ambiente virtual python para instalar o Scapy.

```
python -m venv .venv
source .venv/bin/activate # Linux/macOS
.venv\Scripts\activate # Windows
pip install scapy
```

## Como usar

Procure no programa a variavel "ip", "porta_inicio" e "porta_fim" e digite, respectivamente o IP alvo do seu scan, a porta de onde o scan comecara e a de onde ele terminara.

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
O programa vai mostrar todas as respostas das portas selecionadas. Procure pela flag da resposta na area ###[ TCP ]###, se for RA a porta esta fechada, se for SA esta aberta.
Por ultimo, na ultima linha, mostrara uma lista das portas abertas.

## Atencao
O uso desse codigo para fins maliciosos e completamente proibido. Ele foi feito para propositos academicos e deve permanecer com esse proposito.