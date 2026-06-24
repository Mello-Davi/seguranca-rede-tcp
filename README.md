# Segurança em Rede TCP

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![TCP](https://img.shields.io/badge/Protocol-TCP-green.svg)
![Status](https://img.shields.io/badge/Status-Acadêmico-orange.svg)

Projeto desenvolvido para a disciplina de **Segurança em Redes**, com o objetivo de demonstrar o funcionamento da comunicação cliente-servidor utilizando **Sockets TCP em Python**, comparando a transmissão de dados em **texto claro** e em **Base64**.

---

## Sobre o Projeto

O sistema consiste em um servidor TCP capaz de receber conexões simultâneas e um cliente que pode transmitir mensagens de duas formas:

### Modo Inseguro
A mensagem é enviada em texto claro pela rede.

**Exemplo:**

```text
INSEGURO:Olá servidor
```

### Modo Seguro
A mensagem é codificada em Base64 antes da transmissão.

**Exemplo:**

```text
SEGURO:T2zDoSBzZXJ2aWRvcg==
```

O servidor recebe o conteúdo, identifica o modo de transmissão e, quando necessário, realiza a decodificação da mensagem.

> Importante: Base64 não é criptografia. Seu uso neste projeto possui finalidade exclusivamente educacional para demonstrar a diferença visual entre dados legíveis e codificados durante a transmissão.

---

## Integrantes

- Bruno Fortuna Cabo
- Davi Rodrigues de Mello
- Gabriel Trindade Rosina de Faria
- João Vitor Dias Seigarro
- Lucas Surica

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Socket TCP
- Threading
- Base64
- Wireshark
- Git e GitHub

---

## Estrutura do Projeto

```text
SEGURANCA-REDE-TCP
│
├── client/
│   └── client.py
│
├── docs/
│   ├── screenshots-wireshark/
│   │   └── screenshotteste.txt
│   │
│   └── relatorio.pdf
│
├── server/
│   ├── logs.txt
│   └── servidor.py
│
└── README.md
```

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de que o Python está instalado.

### Verificar instalação

```bash
python --version
```

ou

```bash
python3 --version
```

Saída esperada:

```bash
Python 3.x.x
```

Caso não possua o Python instalado:

- Windows: https://www.python.org/downloads/
- Linux:

```bash
sudo apt update
sudo apt install python3
```

- macOS:

```bash
brew install python
```

---

## Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/Mello-Davi/seguranca-rede-tcp.git
```

```bash
cd seguranca-rede-tcp
```

---

### 2. Iniciar o Servidor

Abra um terminal e navegue até a pasta:

```bash
cd ./server/
```

Execute:

```bash
python servidor.py
```

ou

```bash
python3 servidor.py
```

Saída esperada:

```text
=== SERVIDOR DE SEGURANÇA DE REDE ATIVO ===
Ouvindo na porta 9999...
Aguardando conexões...
```

---

### 3. Iniciar o Cliente

Abra um segundo terminal e navegue até a pasta:

```bash
cd ./client/
```

Execute:

```bash
python client.py
```

ou

```bash
python3 client.py
```

Saída esperada:

```text
Conectado ao servidor 127.0.0.1:9999 com sucesso!
```

---

## Configuração de Rede

Por padrão, o cliente conecta localmente:

```python
IP_ALVO = '127.0.0.1'
```

Para conectar em outro computador da mesma rede, altere para o IP da máquina que está executando o servidor:

```python
IP_ALVO = '192.168.1.100'
```

---

## Fluxo de Comunicação

```text
┌─────────┐
│ Cliente │
└────┬────┘
     │
     │ INSEGURO:Mensagem
     │
     ▼
┌──────────┐
│ Servidor │
└──────────┘
```

ou

```text
┌─────────┐
│ Cliente │
└────┬────┘
     │
     │ SEGURO:TWVuc2FnZW0=
     │
     ▼
┌──────────┐
│ Servidor │
│ Decodifica
│ Base64
└──────────┘
```

---

## Análise com Wireshark

O projeto foi desenvolvido para possibilitar a captura e análise dos pacotes TCP utilizando o Wireshark.

Durante a captura é possível observar:

- Dados enviados em texto claro.
- Dados enviados em Base64.
- Estabelecimento da conexão TCP.
- Troca de mensagens entre cliente e servidor.
- Encerramento da conexão.

As evidências das capturas podem ser encontradas na pasta:

```text
docs/screenshots-wireshark/
```

---

## Conceitos Demonstrados

- Comunicação Cliente-Servidor
- Programação com Sockets
- Protocolo TCP
- Multithreading
- Codificação Base64
- Segurança da Informação
- Captura de Pacotes
- Análise de Tráfego de Rede

---

## Relatório

O relatório completo do projeto encontra-se em:

```text
docs/relatorio.pdf
```

---

## Licença

Este projeto foi desenvolvido exclusivamente para fins acadêmicos e educacionais.
