# TCP Port Scanner

Este é um simples scanner de portas TCP desenvolvido em Python com uma interface gráfica construída usando Tkinter. Ele permite que você escaneie portas TCP em um host específico (endereço IP ou nome de domínio) e exibe quais portas estão abertas, juntamente com o serviço associado, se conhecido.

## Requisitos

- Python 3.x
- Tkinter (geralmente já incluído com a instalação do Python)

## Como Executar

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/tcp-port-scanner.git
    cd tcp-port-scanner
    ```

2. Certifique-se de ter o Python 3 instalado. Você pode verificar a versão instalada executando:

    ```bash
    python3 --version
    ```

3. Execute o script:

    ```bash
    python3 port-scanner.py
    ```

4. A interface gráfica será exibida. Insira o host (endereço IP ou nome de domínio) que deseja escanear, o intervalo de portas (Start Port e End Port), e clique em "Start Scan" para iniciar o escaneamento.

## Exemplos de Uso

- **Escanear o localhost**:

    - Host: `127.0.0.1`
    - Start Port: `1`
    - End Port: `1024`

- **Escanear um domínio público**:

    - Host: `scanme.nmap.org`
    - Start Port: `1`
    - End Port: `1000`
