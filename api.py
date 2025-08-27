"""
Módulo api
----------

Este módulo é responsável pela comunicação com a API de perguntas 
(`https://tryvia.ptr.red/`). Ele gerencia a criação de tokens de sessão 
e a requisição de perguntas de múltipla escolha para o jogo.

Funções principais:
- get_token(): Obtém e retorna um token de sessão válido.
- get_questions(): Busca perguntas da API com base na quantidade e dificuldade.
"""

import requests
from typing import Dict, Any


def get_token() -> str:
    """
    Solicita um token de sessão à API.

    O token é necessário para realizar requisições subsequentes de perguntas
    sem repetir ou invalidar sessões.

    Returns
    -------
    str
        Token de sessão válido.

    Raises
    ------
    ConnectionError
        Se a requisição falhar ou a API não retornar um token válido.
    """
    response = requests.get('https://tryvia.ptr.red/api_token.php?command=request')

    # Verifica se a resposta foi bem-sucedida
    if response.status_code != 200 or response.json()['response_code'] != 0:
        raise ConnectionError("Não foi possível obter o token. Verifique sua conexão.")

    return response.json()['token']


def get_questions(token: str, qtd_questions: int, difficulty: str) -> Dict[str, Any]:
    """
    Busca perguntas da API com base na quantidade e dificuldade informadas.

    Parameters
    ----------
    token : str
        Token de sessão obtido via `get_token()`.
    qtd_questions : int
        Número de perguntas a serem buscadas.
    difficulty : str
        Dificuldade das perguntas (ex.: 'easy', 'medium', 'hard').

    Returns
    -------
    dict
        Dicionário contendo as perguntas retornadas pela API.

    Raises
    ------
    ConnectionError
        Se a requisição falhar ou a API não retornar perguntas válidas.
    """
    category = 0  # Categoria 0: Todas as categorias
    response = requests.get(
        f'https://tryvia.ptr.red/api.php'
        f'?amount={qtd_questions}'
        f'&category={category}'
        f'&type=multiple'
        f'&difficulty={difficulty}'
        f'&token={token}'
    )

    # Verifica se a resposta foi bem-sucedida
    if response.status_code != 200 or response.json()['response_code'] != 0:
        raise ConnectionError("Não foi possível obter as perguntas. Verifique sua conexão ou tente novamente.")

    return response.json() 
