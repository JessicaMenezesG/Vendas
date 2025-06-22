# Analisador de Vendas

Este projeto em Python utiliza a biblioteca **pandas** para analisar dados de vendas a partir de um arquivo Excel.

## Funcionalidades

- Lê dados de vendas (produto, quantidade, preço unitário e data) de um arquivo Excel (`vendas.xlsx`)
- Calcula a receita por venda (quantidade x preço unitário)
- Gera um novo arquivo Excel com os dados analisados (`vendas_analisadas.xlsx`)
- Mostra no terminal:
  - Receita total
  - Produto mais vendido (quantidade)
  - Produto que mais gerou receita
  - Receita total por dia

## Como usar

1. Certifique-se de ter Python instalado (versão 3.10 ou superior recomendada)
2. Instale a biblioteca pandas (se ainda não tiver):

   ```bash
   pip install pandas openpyxl
