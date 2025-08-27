from api import get_token, get_questions
from utils import apresentar_regras
from game import jogar

# Ponto de entrada do programa
if __name__ == "__main__":
    try:
        apresentar_regras()

        token = get_token()

        perguntas_response = get_questions(token, 30, 'easy')
        perguntas_easy = perguntas_response['results']

        perguntas_response = get_questions(token, 30, 'medium')
        perguntas_medium = perguntas_response['results']

        perguntas_response = get_questions(token, 30, 'hard')
        perguntas_hard = perguntas_response['results']

        todas_perguntas = perguntas_easy + perguntas_medium + perguntas_hard

        jogar(todas_perguntas)

    except Exception as e:
        print(f"\nNão foi possível iniciar o jogo: {str(e)}")
