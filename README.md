# Chatbot NPL Livros

Este repositório contém um chatbot desenvolvido utilizando técnicas de Processamento de Linguagem Natural (NLP).

## Visão Geral

O objetivo deste projeto é criar um chatbot capaz de interagir com usuários de maneira natural e eficiente, utilizando modelos de NLP para entender e responder às perguntas com intuito de auxíliar o usuário na busca de livros. Os dados dos livros tem como fonte: [goodreads-livros](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks) encontrado na plataforma kaggle. No presente momento, o chat está provendo de respostas randômicas a diálogos de boas-vindas e realizando pesquisa por coluna colhidas do dataset.


## Requisitos

- Python 3.x
- IDE de sua preferência(foi utilizado o Visual Studio Code para realização do projeto).

## Estrutura do Projeto

- `chatbot.py`: Script principal que contém a lógica do chatbot.
- `favicon.ico`: Ícone do projeto.
- `.gitignore`: Arquivo para ignorar arquivos desnecessários no repositório.

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/dayviddouglas/chatbot_npl.git

2. Navegue até o diretório do projeto:
    ```bash
    cd chatbot_npl

3. Crie um ambiente virtual (venv):

No terminal, execute o seguinte comando:

```bash 
$ python -m venv venv
```

Ative o ambiente virtual:
```bash 
$ .\venv\Scripts\activate
```

4. Instale as dependências a partir do arquivo requirements.txt:
No terminal, execute o seguinte comando:

```bash 
$ pip install -r requirements.txt
```

5. Faça o download do modelo nlp dendo do ambiente virtual:

```bash 
$ python -m spacy download pt_core_news_sm
```

6. Para executar a aplicação:

```bash 
$ python chatbot.py
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Contato

- Email: [dayvid_douglas@hotmail.com](mailto:dayvid_douglas@hotmail.com)
- LinkedIn: [dayvid-douglas](https://www.linkedin.com/in/dayvid-douglas/)
- GitHub: [Dayvid Douglas](https://github.com/dayviddouglas)
   
