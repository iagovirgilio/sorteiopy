# SorteioPy

A aplicação, feita em Django, carrega um arquivo no formato xlsx, conta a quantidade de linhas no arquivo, escolhe uma linha aleatória e exibe os dados das células da linha escolhida.

O arquivo deve conter duas colunas (A e B), onde a primeira linha vem os títulos das colunas. Como no exemplo abaixo:

| Título1 | Título2 |
|---------|---------|
| cod 1   | dado 1  |
| cod 2   | dado 2  |

Caso a linha sorteada seja a segunda o resultado impresso será:
"cod1 - dado1"

**Use especificamente as colunas A e B da planilha.**
