
from scapy.all import IP, TCP, ICMP, sr1, RandShort

portas_abertas = []

def hostOn(ip):
    """
    Manda um pacote ICMP para o ip (passado por parâmetro) destinatário  para testar a conexão (ping).
    Se chegar uma resposta retorna verdadeiro e o destinatário está online e o scan pode ser realizado.
    """
    pacote_icmp = IP(dst = ip) / ICMP()
    resposta = sr1(pacote_icmp, timeout = 1, verbose = 0)
    
    if resposta and resposta.haslayer(ICMP):
        return True
    else:
        return False


def synScan(ip, port):
    """
    Faz o escaneamento mandando pacotes com a flag S (SYN) para o ip e a porta passados como parâmetro
      e recebendo as respostas e mostrando com a função show().
    Se a resposta tiver a flag SA (SYN_ACK) a porta é adicionada a lista de portas abertas.
    Caso a resposta for do tipo RA (RST-ACK), a porta está fechada
    """
    pacote_syn = IP(dst = ip) / TCP(dport = port, sport = RandShort(), flags="S")
    resposta = sr1(pacote_syn, timeout = 1, verbose = 0)

    if resposta[TCP].flags == "SA":
        portas_abertas.append(port)

    return resposta.show()

ip = "192.168.18.112"  
porta_inicio = 1
porta_fim = 443

if hostOn(ip):
    print(f"Escaneando as portas do {ip}...")
    for i in range(porta_inicio, porta_fim + 1):
        print(f"\n--- Porta: {i} ----------------------------------\n")
        print(synScan(ip, i))
    print("Escaneameto acabou.")
    print(f"Portas abertas: {portas_abertas}")
else:
    print(f"Destinatário {ip} está off-line.")