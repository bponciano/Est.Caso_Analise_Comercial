# 📊 Análise de Vendas e Performance Comercial

> Pipeline de tratamento, integração e análise de dados de vendas com geração de indicadores estratégicos.  
> Demonstra limpeza de dados, merge entre tabelas, cálculo de métricas financeiras e visualização analítica.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge)

## 🎯 Objetivo do Projeto

Construir um fluxo completo de tratamento e análise de dados comerciais a partir de duas bases distintas:

- Planilha de vendas (dados transacionais)
- Tabela mestre de produtos (dados de custo)

O projeto foi desenvolvido para simular um cenário real de análise empresarial, onde é necessário:

- Corrigir inconsistências
- Padronizar dados
- Integrar múltiplas fontes
- Calcular métricas financeiras
- Gerar visualizações estratégicas

O foco está na construção de um pipeline analítico estruturado e replicável.

## 🏗 Arquitetura da Solução
```
Planilha de Vendas (CSV)
+
Tabela Mestre de Produtos (CSV)
↓
Limpeza e Padronização
↓
Unificação de Identificação (CPF/CNPJ)
↓
Merge entre Bases
↓
Cálculo de Métricas (Lucro, Margem)
↓
Agregações Analíticas
↓
Visualização com Matplotlib
```

## ⚙️ Stack Tecnológica

- Python 3
- Pandas
- Matplotlib
- CSV (dados estruturados)

## 🔄 Pipeline de Dados

### 1️⃣ Leitura e Diagnóstico Inicial
- Importação dos arquivos CSV
- Verificação da estrutura com `.info()`
- Inspeção de tipos e valores nulos

---

### 2️⃣ Limpeza e Padronização

- Conversão de datas com `pd.to_datetime`
- Tratamento de valores nulos (`fillna`)
- Remoção de registros incompletos (`dropna`)
- Padronização textual (`strip`, `upper`)
- Correção de inconsistências com dicionário de substituição
- Formatação de floats para melhor visualização

---

### 3️⃣ Normalização de Identificador

- Padronização de CPF/CNPJ em uma única coluna
- Eliminação de redundâncias estruturais
- Garantia de chave única de cliente

---

### 4️⃣ Integração entre Bases

- Renomeação estratégica de colunas
- Remoção de duplicidades na tabela mestre
- Aplicação de `merge` (left join)
- Identificação de produtos sem cadastro de custo

---

### 5️⃣ Engenharia de Métricas

Cálculos implementados:

- **Lucro**  
```python
lucro = valor_total - (valor_custo * quantidade)
```
- **Margem de Lucro (%)**  
```python
margem = (lucro / valor_total) * 100
```
---

### 6️⃣ Agregações Analíticas

- Crescimento anual de faturamento
- Evolução anual de lucro
- Distribuição percentual por status de venda
- Ranking dos 5 principais clientes (VIP)

Uso de:

- `groupby`
- `sum`
- `value_counts(normalize=True)`
- `sort_values`

---

### 7️⃣ Visualização de Dados

Funções personalizadas para:

- Gráfico de linha (evolução temporal)
- Gráfico de barras horizontal (ranking e distribuição)

Características:
- Padronização visual
- Exportação automática em PNG
- Configuração de grid e layout profissional

## 🧠 Conceitos Aplicados

- Data Cleaning
- Data Wrangling
- Data Normalization
- Feature Engineering
- Data Integration (Join/Merge)
- Análise de Performance Comercial
- Visualização Estratégica
- Cálculo de Indicadores Financeiros
- Pensamento orientado a negócio

## 📊 Aplicações Analíticas

- Análise de crescimento anual
- Identificação de clientes estratégicos
- Monitoramento de margem e lucratividade
- Avaliação de performance comercial
- Base para dashboards executivos
- Suporte à tomada de decisão

## 🚀 Evoluções Futuras

- Automatização do pipeline com funções modulares
- Criação de dashboard interativo (Power BI / Streamlit)
- Implementação de testes de qualidade de dados
- Deploy como API analítica
- Integração com banco de dados relacional
- Criação de relatórios automatizados

## 👨‍💻 Autor

**Breno Ponciano**  
Foco em Engenharia e Análise de Dados