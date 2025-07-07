# API Python (Flask) - Provedora de Dados

Esta é a API de dados principal do projeto, desenvolvida em Python utilizando o microframework Flask. Ela fornece endpoints para gerenciar usuários, produtos, pedidos, estoque e validações.

## Dependências

Certifique-se de que o Python 3.x está instalado.
A única dependência Python necessária é o Flask.

## Como Rodar a API

1.  **Navegue até a pasta `api_python/`:**
    Abra o terminal (ou o terminal integrado do PyCharm) e vá para o diretório `api_python/`.

    ```bash
    cd sua_pasta_principal/api_python/
    ```

2.  **Instale o Flask:**
    É altamente recomendado usar um ambiente virtual (`venv`). Se você usa o PyCharm, ele geralmente cria um automaticamente. Ative-o antes de instalar:

    ```bash
    # Se você ainda não tem um ambiente virtual e quer criar um:
    python -m venv .venv
    # Para ativar o ambiente virtual (Windows PowerShell):
    .venv\Scripts\Activate.ps1
    # Para ativar o ambiente virtual (Windows CMD):
    .venv\Scripts\activate.bat
    # Para ativar o ambiente virtual (macOS/Linux):
    source .venv/bin/activate
    ```
    Depois de ativar, instale o Flask:

    ```bash
    pip install Flask
    ```

3.  **Execute a API:**
    ```bash
    python app_python.py
    ```

**A API Python estará rodando em:** `http://127.0.0.1:5000`
