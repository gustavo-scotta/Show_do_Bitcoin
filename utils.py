import random
from typing import Dict, List

PRIZES = [0.1] * 10
LEVELS = ['easy', 'easy', 'easy', 'medium', 'medium', 'medium', 'hard', 'hard', 'hard', 'hard']
MAX_SKIPS = 3

def apresentar_regras() -> None:
    """
    Exibe as regras do jogo de forma organizada e clara.
    """
    print("==================================================")
    print("=====      BEM-VINDO AO SHOW DO BITCOIN      =====")
    print("==================================================")
    print("\nRegras do jogo:")
    print("- Responda corretamente às perguntas até atingir o prêmio máximo de 1 BTC.")
    print("- Cada pergunta possui 4 alternativas e apenas uma está correta.")
    print("- Você pode pular até 3 perguntas por partida.")
    print("- Ao pular, você continua no mesmo nível de prêmio.")
    print("- Você pode desistir a qualquer momento e levará metade do prêmio conquistado.")
    print("- Se você errar uma resposta, receberá apenas 10% do valor conquistado até o momento.")
    print("\nVamos começar. Boa sorte!\n")

def exibir_pergunta(pergunta: Dict[str, List[str]], pulos_usados: int, premio_atual: float, numero_pergunta: int) -> List[str]:
    """
    Exibe a pergunta, as alternativas e a situação do jogo no momento.
    """
    alternativas = pergunta['incorrect_answers'] + [pergunta['correct_answer']]
    random.shuffle(alternativas)

    print("=" * 50)
    print(f"Pergunta {numero_pergunta + 1} - Valendo {PRIZES[numero_pergunta]:.1f} BTC")
    print(f"Prêmio acumulado: {premio_atual:.1f} BTC")
    print(f"Pulos usados: {pulos_usados} / 3")
    print("=" * 50)
    print(pergunta['question'])
    for idx, alternativa in enumerate(alternativas, 1):
        print(f"{idx}) {alternativa}")

    return alternativas
