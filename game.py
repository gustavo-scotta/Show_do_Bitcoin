from typing import Dict, List
from utils import PRIZES, LEVELS, MAX_SKIPS, exibir_pergunta


def jogar(perguntas: List[Dict[str, any]]) -> None:
    """
    Controla o fluxo principal do jogo.

    O jogador deve responder perguntas de múltipla escolha com dificuldade
    crescente, podendo desistir a qualquer momento ou pular até um limite
    pré-definido. O prêmio acumulado depende do desempenho do jogador.
    """
    pulos_usados: int = 0
    premio_atual: float = 0.0
    perguntas_utilizadas: List[str] = []
    numero_pergunta: int = 0

    while numero_pergunta < len(PRIZES):
        dificuldade: str = LEVELS[numero_pergunta]

        # Seleciona uma pergunta ainda não utilizada
        pergunta = next(
            (p for p in perguntas if p['question'] not in perguntas_utilizadas and p['difficulty'] == dificuldade),
            None
        )

        if not pergunta:
            print("\nNão há mais perguntas disponíveis. O jogo será encerrado.")
            break

        perguntas_utilizadas.append(pergunta['question'])

        while True:
            alternativas = exibir_pergunta(pergunta, pulos_usados, premio_atual, numero_pergunta)
            resposta = input("\nDigite sua resposta (1-4), 'P' para pular ou 'D' para desistir: ").strip().upper()

            while resposta not in ['1', '2', '3', '4', 'P', 'D']:
                resposta = input("Opção inválida. Digite 1, 2, 3, 4, 'P' ou 'D': ").strip().upper()

            if resposta == 'D':
                premio_final = premio_atual * 0.5
                print(f"\nVocê desistiu do jogo. Prêmio conquistado: {premio_final:.2f} BTC")
                print(f"Pulos usados: {pulos_usados}")
                return

            if resposta == 'P':
                if pulos_usados < MAX_SKIPS:
                    pulos_usados += 1
                    print(f"\nVocê pulou a pergunta! Pulos usados: {pulos_usados}/{MAX_SKIPS}\n")
                    break
                else:
                    print("\nVocê já usou todos os seus pulos! Precisa responder esta pergunta.")
                    continue

            # Resposta do jogador
            indice_resposta = int(resposta) - 1
            resposta_selecionada = alternativas[indice_resposta]

            if resposta_selecionada == pergunta['correct_answer']:
                premio_atual += PRIZES[numero_pergunta]
                print("\nResposta correta! Você acumulou {:.1f} BTC\n".format(premio_atual))

                if numero_pergunta == len(PRIZES) - 1:
                    print("\nParabéns! Você ganhou o prêmio máximo de 1 BTC!")
                    print(f"Pulos usados: {pulos_usados}")
                    return

                numero_pergunta += 1
                break
            else:
                premio_final = premio_atual * 0.1
                print(f"\nResposta errada! A correta era: {pergunta['correct_answer']}")
                print(f"Você ganhou {premio_final:.2f} BTC.")
                print(f"Pulos usados: {pulos_usados}")
                return

    print(f"\nFim de jogo! Você acumulou {premio_atual:.2f} BTC.")
    print(f"Pulos usados: {pulos_usados}")
