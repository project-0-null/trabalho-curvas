# Teste Computacional - Ajuste de Curvas (Mínimos Quadrados)

Este repositório contém a resolução do Teste Computacional 1 (2025/2) do curso de **Engenharia Elétrica**.

## 📝 Sobre o Trabalho
[cite_start]O objetivo deste projeto é implementar algoritmos para o ajuste de funções não lineares utilizando o **Método dos Mínimos Quadrados** com **linearização**[cite: 3, 45].

[cite_start]Conforme solicitado nas instruções, o código foi desenvolvido em Python implementando manualmente a resolução do sistema linear (Eliminação de Gauss com pivoteamento), sem utilizar bibliotecas prontas de ajuste de curvas (como `polyfit` ou similar)[cite: 71, 114].

## 🚀 Problemas Resolvidos
O programa oferece um menu para resolver os dois casos propostos:

1.  [cite_start]**Problema 1 (Circuito RC):** Ajuste de modelo exponencial ($i = ae^{bt}$) para dados de corrente x tempo[cite: 74, 78].
2.  [cite_start]**Problema 2 (Volume de Árvores):** Ajuste de modelo de potência ($v = ax^b$) para dados de volume x diâmetro[cite: 85, 92].

## 🛠️ Como Executar
Execute o script principal. O programa exibirá os resultados numéricos (parâmetros $a$, $b$ e resíduos) e gerará os gráficos comparando os dados experimentais com a curva ajustada.
