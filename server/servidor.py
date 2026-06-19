import socket
import threading
import base64
from datetime import datetime

# Configurações do Servidor
IP_SERVIDOR = '0.0.0.0'  # Ouve em todas as placas de rede do computador
PORTA = 9999

def lidar_com_cliente(conexao, endereco):
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Clicente conectado com sucesso! Endereço: {endereco}")
    
    while True:
        try:
            # Recebe o pacote de dados (limite de 1024 bytes)
            dados_recebidos = conexao.recv(1024).decode('utf-8')
            
            if not dados_recebidos:
                break  # Se não houver dados, o cliente desconectou
            
            # Divide o pacote para entender o formato: "MODO:MENSAGEM"
            modo, mensagem_corpo = dados_recebidos.split(':', 1)
            horario = datetime.now().strftime('%H:%M:%S')
            
            if modo == "INSEGURO":
                print(f"[{horario}] [INSEGURO - TEXTO CLARO] {endereco} enviou: {mensagem_corpo}")
                resposta = f"Servidor recebeu seu texto claro às {horario}"
                
            elif modo == "SEGURO":
                print(f"[{horario}] [SEGURO - CAPTURADO EM BASE64] {endereco} enviou: {mensagem_corpo}")
                # Decodifica para mostrar o conteúdo original no terminal do servidor
                texto_original = base64.b64decode(mensagem_corpo.encode('utf-8')).decode('utf-8')
                print(f"[{horario}] [SEGURO - DESCRIPTOGRAFADO NO SERVIDOR] Conteúdo real: {texto_original}")
                resposta = f"Servidor decodificou seu dado seguro às {horario}"
            
            # Envia uma resposta de confirmação para o cliente
            conexao.send(resposta.encode('utf-8'))
            
        except Exception as e:
            break

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Conexão encerrada com {endereco}")
    conexao.close()

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((IP_SERVIDOR, PORTA))
    servidor.listen()
    print(f"=== SERVIDOR DE SEGURANÇA DE REDE ATIVO ===")
    print(f"Ouvindo na porta {PORTA}... Aguardando conexões...\n")
    
    while True:
        conexao, endereco = servidor.accept()
        # Cria uma thread para cada novo cliente que conectar
        thread = threading.Thread(target=lidar_com_cliente, args=(conexao, endereco))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()