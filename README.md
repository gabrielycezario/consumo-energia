# ⚡ Calculadora de Consumo de Energia

Este projeto é um sistema desenvolvido em **Python** que calcula o consumo mensal estimado de um aparelho elétrico e o custo aproximado de energia com base na potência e no tempo de uso diário.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

![Energy](https://img.shields.io/badge/Energia-Calculadora-yellow?style=for-the-badge)

## 🧮 Fórmula utilizada

O consumo mensal é calculado utilizando a seguinte fórmula:

**Consumo mensal (kWh) = (Potência (W) × Horas de uso por dia × 30) ÷ 1000**

Depois, o custo mensal é calculado considerando o valor de **R$ 0,75 por kWh**:

**Custo mensal = Consumo mensal × 0,75**

## ▶️ Como executar

1. Tenha o **Python** instalado no computador.
2. Abra o projeto no **Visual Studio Code**.
3. Abra o arquivo `app.py`.
4. Execute o programa pelo botão ▶️ ou pelo terminal.
5. Informe:
   - Nome do aparelho;
   - Potência em watts (W);
   - Tempo médio de uso diário em horas.

## 💡 Exemplo

```text
Digite o nome do aparelho: Geladeira
Digite a potência do aparelho em watts (W): 150
Digite o tempo médio de uso diário do aparelho: 10

Aparelho: Geladeira
Consumo estimado: 45.0
Custo estimado: R$33.75