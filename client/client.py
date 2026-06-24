import socket
import base64

# CONFIGURAÇÃO DO RADMIN VPN:
# Substitua o IP abaixo pelo IP do Radmin do computador que está rodando o servidor.
IP_ALVO = '127.0.0.1' 
PORTA_ALVO = 9999

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        cliente.connect((IP_ALVO, PORTA_ALVO))
        print(f"Conectado ao servidor {IP_ALVO}:{PORTA_ALVO} com sucesso!\n")
    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")
        return

    print("=== MENU DE ENVIO ===")
    print("1 - Enviar Mensagem de forma INSEGURA (Texto Claro)")
    print("2 - Enviar Mensagem de forma OFUSCADA (Simulação - Base64)")
    print("Digite 'sair' para registrar e encerrar.\n")

    while True:
        opcao = input("Escolha o modo (1 ou 2): ").strip()
        
        if opcao.lower() == 'sair':
            break
            
        if opcao not in ['1', '2']:
            print("Opção inválida! Escolha 1 ou 2.")
            continue
            
        mensagem = input("Digite a mensagem que deseja transmitir: ")
        
        # Evita problemas de separação de strings no servidor
        if ":" in mensagem:
            print("Por razões didáticas do protocolo, não utilize ':' na mensagem.")
            continue
        
        if opcao == '1':
            pacote = f"INSEGURO:{mensagem}"
            print(f"[Transmitindo] Enviando em texto claro: '{mensagem}'")
            
        elif opcao == '2':
            # Variável corrigida aqui:
            mensagem_ofuscada = base64.b64encode(mensagem.encode('utf-8')).decode('utf-8')
            pacote = f"SEGURO:{mensagem_ofuscada}"
            print(f"[Transmitindo] O dado trafegando na rede será: '{mensagem_ofuscada}'")
            
        # Envia o pacote estruturado através do Socket TCP
        cliente.send(pacote.encode('utf-8'))
        
        # Recebe a resposta do servidor
        resposta = cliente.recv(1024).decode('utf-8')
        print(f"[Servidor respondeu]: {resposta}\n")

    print("Encerrando conexão.")
    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()