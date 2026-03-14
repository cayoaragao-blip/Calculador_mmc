# Menor Múltiplo Comum
Este projeto implementa um algoritmo eficiente para calcular o Mínimo Múltiplo Comum (MMC) de um conjunto de números.

## Funcionamento do Algoritmo
A lógica baseia-se na propriedade matemática que relaciona o MMC ao Máximo Divisor Comum (MDC). O cálculo é realizado em duas etapas principais:

1. Cálculo do MDC
Para encontrar o MMC de dois números, o algoritmo primeiro calcula o MDC utilizando o Algoritmo de Euclides, que é baseado em divisões sucessivas até que o resto seja zero.

2. Extensão para Múltiplos Números
Para conjuntos com mais de dois valores, o algoritmo utiliza uma abordagem iterativa:

Calcula o MMC dos dois primeiros números.

Armazena o resultado em uma variável acumuladora.

Calcula o MMC entre essa variável e o próximo número do conjunto.

Repete o processo até percorrer todos os elementos.

## 🛠️ Tecnologias e Conceitos 
Python 3.x e Lógica Matemática - Algoritmo de Euclides e Menor Múltiplo Comum📋

### Pré-requisitos: 
Python instalado; Git; Gerenciador de pacotes (pip);