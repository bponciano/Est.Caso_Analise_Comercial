# 📊 Análise de Vendas e Performance Financeira

Este projeto consiste em um script Python desenvolvido para processar, limpar e analisar dados de vendas comerciais. O objetivo é transformar planilhas brutas em insights visuais sobre faturamento, lucro e comportamento dos clientes.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge)

## 🎯 Objetivo do Projeto

Automatizar o processo de consolidação de dados de vendas (extraídos de CSVs), realizar o tratamento de erros comuns em bases de dados reais (como datas mal formatadas e estados duplicados) e gerar relatórios gráficos para tomada de decisão.

## ⚙️ Funcionalidades

### 1. Coleta e Limpeza de Dados (ETL)
- **Importação:** Leitura de arquivos CSV (`planilha_vendas2.csv` e `tabela_mestre.csv`).
- **Tratamento de Tipos:** Conversão de colunas de datas e formatação de floats.
- **Correção de Dados:**
  - Preenchimento de valores nulos (ex: frete).
  - Remoção de registros incompletos.
  - Padronização de strings (ex: correção de siglas de estados 'SPP' -> 'SP').
- **Unificação de Identificadores:** Fusão inteligente das colunas de CPF e CNPJ em uma única coluna identificadora.

### 2. Enriquecimento de Dados
- **Merge de Tabelas:** Cruzamento da tabela de vendas com a tabela mestre de produtos para obter o custo unitário.
- **Cálculos Financeiros:**
  - Cálculo do **Lucro Real** (Valor Total - (Custo * Quantidade)).
  - Cálculo da **Margem de Lucro** percentual.

### 3. Visualização de Dados
Utilização da biblioteca `Matplotlib` para gerar gráficos estratégicos:
- 📈 **Evolução de Faturamento Anual:** Gráfico de linha.
- 💰 **Evolução do Lucro Anual:** Gráfico de linha comparativo.
- 📊 **Status das Vendas:** Gráfico de barras horizontais (Percentual de vendas concluídas vs. canceladas/pendentes).
- 🏆 **Top 5 Clientes VIP:** Ranking dos clientes que geraram maior receita.

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Pandas:** Para manipulação e análise tabular.
- **Matplotlib:** Para criação dos gráficos estáticos.

## 🚀 Como Executar

1. Clone este repositório:


```markdown
git clone [https://github.com/bponciano/Est.Caso_Analise_Comercial](https://github.com/bponciano/Est.Caso_Analise_Comercial)
```

2. Instale as dependências necessárias:
 
```markdown
 pip install pandas matplotlib
```

3. Certifique-se de que os arquivos planilha_vendas2.csv e tabela_mestre.csv estejam na mesma pasta do script.

4. Execute o arquivo Python:

```markdown
python analise_vendas.py
```
## 📂 Estrutura dos Arquivos

```python
├── analise_vendas.py     # Script principal
├── planilha_vendas2.csv  # Base de dados de vendas (Input)
├── tabela_mestre.csv     # Base de dados de produtos/custos (Input)
├── grafico.png           # Output gerado pelas funções de plotagem
└── README.md             # Documentação
```


Desenvolvido por:
## Breno Ponciano.