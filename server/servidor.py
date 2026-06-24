import socket
import threading
import base64
from datetime import datetime

IP_SERVIDOR = '0.0.0.0'  
PORTA = 9999

def lidar_com_cliente(conexao, endereco):
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Cliente conectado! Origem: IP {endereco[0]} na Porta {endereco[1]}")
    
    while True:
        try:
            dados_recebidos = conexao.recv(1024).decode('utf-8')
            
            if not dados_recebidos:
                break  
            
            # Validação para evitar quebra do servidor caso o pacote venha malformado
            if ':' not in dados_recebidos:
                continue
                
            modo, mensagem_corpo = dados_recebidos.split(':', 1)
            horario = datetime.now().strftime('%H:%M:%S')
            
            if modo == "INSEGURO":
                print(f"[{horario}] [TEXTO CLARO] {endereco[0]}:{endereco[1]} enviou: {mensagem_corpo}")
                resposta = f"Servidor recebeu seu texto claro às {horario}"
                
            elif modo == "SEGURO":
                print(f"[{horario}] [OFUSCADO - BASE64] Interceptado na rede como: {mensagem_corpo}")
                # Decodifica para mostrar o conteúdo original
                texto_original = base64.b64decode(mensagem_corpo.encode('utf-8')).decode('utf-8')
                print(f"[{horario}] [DECODIFICADO NO SERVIDOR] Conteúdo real: {texto_original}")
                resposta = f"Servidor decodificou seu dado (Base64) às {horario}"
            else:
                resposta = "Modo desconhecido."
            
            conexao.send(resposta.encode('utf-8'))
            
        except Exception as e:
            print(f"Erro na conexão com {endereco}: {e}")
            break

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Conexão encerrada com {endereco[0]}:{endereco[1]}")
    conexao.close()

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Permite reusar a porta imediatamente após fechar o servidor
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((IP_SERVIDOR, PORTA))
    servidor.listen()
    print(f"=== SERVIDOR DE SEGURANÇA DE REDE ATIVO ===")
    print(f"Ouvindo na porta {PORTA}... Aguardando conexões...\n")
    
    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conexao, endereco))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()