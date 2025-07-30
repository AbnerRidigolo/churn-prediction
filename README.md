# 🔁 Churn Prediction (Clientes que Cancelam)

## 📌 Objetivo
Identificar quais clientes estão propensos a cancelar o serviço, com base em variáveis de uso e perfil.

## 🗂️ Sobre o Projeto
Este projeto utiliza dados do Kaggle (Telco Customer Churn) para prever a rotatividade de clientes (churn). Envolve análise temporal, tratamento de desbalanceamento de classes, explicação dos trade-offs entre métricas, e entrega de um dashboard interativo para visualização de insights.

## 🔍 Etapas do Projeto
### 1. Análise e Engenharia de Features
- Criação de variáveis baseadas em tempo de uso, últimas ações e comportamento do cliente.
- Conversão de colunas categóricas e normalização de dados.

### 2. Lidar com Dados Desbalanceados
- Aplicação de SMOTE ou ajuste de thresholds para lidar com a desproporção entre churn e não churn.

### 3. Modelagem e Avaliação
- Métricas: F1-score, Recall, AUC
- Discussão dos trade-offs entre priorizar recall ou F1-score

### 4. Dashboard Interativo (Extra)
- Dashboard com Plotly Dash para análise de churn, principais variáveis e filtros dinâmicos.

## 📊 Dataset
- Nome: Telco Customer Churn  
- Fonte: [Kaggle Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## 💡 Tecnologias Utilizadas
- Python 3.x
- Pandas, NumPy
- Scikit-learn, imbalanced-learn
- Plotly, Dash
- Matplotlib, Seaborn

## 📁 Estrutura dos Arquivos
📦churn-prediction  
 ┣ 📊 data/  
 ┃ ┗ telco_churn.csv  
 ┣ 📈 notebooks/  
 ┃ ┣ 01_preprocessing.ipynb  
 ┃ ┣ 02_model_training.ipynb  
 ┃ ┗ 03_metrics_and_tradeoffs.ipynb  
 ┣ 📊 dashboard/  
 ┃ ┗ app.py  
 ┣ README.md  
 ┗ requirements.txt  

## ✅ Resultados
- Técnicas de balanceamento melhoraram o recall e o F1-score do modelo.
- Dashboard interativo permite visualizar churn por contrato, tipo de pagamento, tempo de uso e mais.

