# Show do Bitcoin

Um jogo de perguntas e respostas inspirado no programa de TV **Show do Milhão**, mas com prêmios em **Bitcoin virtual**.  
O objetivo é acumular **1 BTC** respondendo corretamente às questões.

---

## Regras do jogo
- Cada pergunta possui **4 alternativas**, apenas uma está correta.
- São **10 perguntas** no total, divididas em dificuldades:
  - 3 fáceis
  - 3 médias
  - 4 difíceis
- O jogador pode:
  - **Pular** até 3 perguntas por partida.
  - **Desistir** a qualquer momento e levará **50%** do prêmio acumulado.
  - Errar uma pergunta significa perder quase tudo: você fica apenas com **10%** do prêmio acumulado até o momento.
- O prêmio máximo é de **1 BTC virtual**.

---

## Estrutura do projeto
Show_do_Bitcoin/
│── api.py # Funções para buscar perguntas na API Open Trivia DB
│── game.py # Lógica principal do jogo (fluxo, prêmios, pulos, desistência)
│── utils.py # Constantes e funções auxiliares (regras, exibição de perguntas)
│── main.py # Ponto de entrada do jogo

---

## Requisitos
- Python **3.8+**
- Conexão com a internet (as perguntas são buscadas da API [Open Trivia DB](https://opentdb.com/))
- Nenhuma biblioteca externa é necessária

---

## Como jogar
1. Clone este repositório ou extraia os arquivos:
   ```bash
   git clone https://github.com/SEU_USUARIO/Show_do_Bitcoin.git
   cd Show_do_Bitcoin

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
