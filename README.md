# Sistema de Controle de Peças Industriais

## Descrição
Este projeto foi desenvolvido em Python para simular a automação do controle de qualidade de peças em uma linha de produção industrial.

O sistema permite cadastrar peças, verificar automaticamente se elas estão aprovadas ou reprovadas com base em critérios pré-definidos, armazenar peças aprovadas em caixas com capacidade máxima de 10 unidades e gerar um relatório final com os resultados do processo.

## Funcionalidades
- Cadastrar nova peça
- Listar peças aprovadas e reprovadas
- Remover peça cadastrada
- Listar caixas fechadas
- Gerar relatório final

## Regras de negócio
Uma peça será **aprovada** apenas se atender a todos os critérios abaixo:
- **Peso:** entre 95g e 105g
- **Cor:** azul ou verde
- **Comprimento:** entre 10cm e 20cm

Se a peça for aprovada:
- ela é armazenada na caixa atual
- quando a caixa atingir 10 peças, ela é fechada automaticamente
- uma nova caixa passa a ser utilizada

Se a peça for reprovada:
- ela é registrada na lista de peças reprovadas
- os motivos da reprovação ficam salvos para o relatório final

## Estrutura dos arquivos
- `main.py` → controla o fluxo principal do programa e o menu interativo
- `functions.py` → contém a lógica do sistema e as regras de negócio
- `interface.py` → reúne as funções de entrada e saída no terminal
- `README.md` → documentação do projeto

## Como executar o programa
### 1. Pré-requisitos
Tenha o **Python 3** instalado no computador.

### 2. Organize os arquivos
Deixe os arquivos abaixo na mesma pasta:
- `main.py`
- `functions.py`
- `interface.py`

### 3. Abra o terminal na pasta do projeto
No VS Code, você pode abrir o terminal com:
- **Terminal > New Terminal**

### 4. Execute o programa
Use um dos comandos abaixo:

```bash
python main.py
```

ou, se necessário:

```bash
python3 main.py
```

## Exemplo de uso
### Exemplo 1: peça aprovada
**Entrada:**
- ID: P001
- Peso: 100
- Cor: azul
- Comprimento: 15

**Saída:**
```text
Peça aprovada e armazenada na caixa atual.
```

### Exemplo 2: peça reprovada
**Entrada:**
- ID: P002
- Peso: 110
- Cor: vermelho
- Comprimento: 25

**Saída:**
```text
Peça reprovada: Peso fora do padrão (95g a 105g); Cor fora do padrão (azul ou verde); Comprimento fora do padrão (10cm a 20cm)
```

### Exemplo 3: fechamento automático da caixa
Ao cadastrar a décima peça aprovada:

```text
Peça aprovada e caixa fechada com 10 peças.
```

## Correção aplicada no código
Foi corrigida a função de remoção de peças.

Antes, ao remover uma peça aprovada, o sistema podia deixar a peça ainda registrada dentro de uma caixa fechada, causando inconsistência nos dados.

Agora, a remoção verifica corretamente:
- peças reprovadas
- peças aprovadas na caixa atual
- peças aprovadas dentro de caixas fechadas

## Observações
- O programa funciona apenas durante a execução atual.
- Ao fechar o programa, os dados não ficam salvos automaticamente.
- Para salvar dados no futuro, seria possível integrar arquivos, banco de dados ou sensores reais.

## Autor
Projeto desenvolvido para a disciplina de **Algoritmos e Lógica de Programação**.
