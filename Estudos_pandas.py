#Importando os pacotes
import pandas as pd
import matplotlib.pyplot as plt

#Lendo os arquivos
tv = pd.read_csv("planilha_vendas2.csv") #tv -> tabela de vendas
tm = pd.read_csv("tabela_mestre.csv") #tm -> tabela mestre

#Verificando a estrutura de dados
tv.info()
tm.info()

#Limpeza básica e corrigindo dados
pd.options.display.float_format = '{:,.2f}'.format #Mostrando como o Pandas deve imprimir os numero floats
tv['data_venda'] = pd.to_datetime(tv["data_venda"], dayfirst=True, errors='coerce') #Corrigindo o formato da data
tv['valor_frete'] = tv["valor_frete"].fillna(0.0) #Corrigindo o valor de frete na tabela de vendas
tv = tv.dropna(subset=['produto','quantidade'])#Limpando as linhas faltantes na tabela de vendas
tv['estado'] = tv['estado'].str.strip().str.upper() #Removendo espaços deixando tudo maiusculo na coluna "Estado"
correcoes = {'SPP': 'SP','PRR': 'PR'} #Dicionário: {'Valor Errado': 'Valor Certo'} com valores a serem substituidos
tv['estado'] = tv['estado'].replace(correcoes) #Correção sendo aplicada

#Unificando a identificação do cliente
tv = tv.rename(columns={'cpf': 'cpf/cnpj'}) #Ajustando o nome da coluna
tv['cpf/cnpj'] = tv['cpf/cnpj'].fillna(tv['cnpj']) #Unificando as colunas CPF e CNPJ
tv = tv.drop('cnpj', axis=1) #Excluindo a coluna de CNPJ

#Aplicando o merge nas planilhas
tm = tm.rename(columns={'nome do produto': 'produto'})
tm_unica = tm.drop_duplicates(subset=['produto'])
tu = tv.merge(tm_unica, on='produto', how='left')

#Fazendo o calculo de margem e lucro real
produtos_sem_cadastro = tu[tu['valor_custo'].isna()]
print(produtos_sem_cadastro['produto'].unique())
tu['lucro'] = tu['valor_total'] - (tu['valor_custo']*tu['quantidade'])
tu['margem_lucro'] = (tu['lucro']/tu['valor_total'])*100

#Dados extraidos da planilha unificada
crescimento = tu.groupby(tu['data_venda'].dt.year)['valor_total'].sum()
crescimento.index = crescimento.index.astype(int)

lucro = tu.groupby(tu['data_venda'].dt.year)['lucro'].sum()
lucro.index = crescimento.index.astype(int)

status_vendas_porc = (tu['status_venda'].value_counts(normalize=True))*100

clientes_vips = tu.groupby('cliente')['valor_total'].sum().sort_values(ascending=False).head()

#Funções para com as configurações padrões dos graficos
def grafico_horizontal(dados, tamanho, titulo, label_x, label_y):

    plt.figure(figsize=tamanho)

    dados.plot(kind='barh', color='#74c09c')

    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.xlabel(label_x, fontsize=12)
    plt.ylabel(label_y, fontsize=12)

    plt.gca().invert_yaxis()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig(f'{titulo}.png', dpi=300)
    plt.show()

def grafico_linha(dados,tamanho,espessura_linha,titulo,label_x,label_y):
    plt.figure(figsize=tamanho)

    plt.plot(dados.index, dados.values, marker='o', linestyle='-', linewidth=espessura_linha, color='#74c09c')

    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.xlabel(label_x, fontsize=12)
    plt.ylabel(label_y, fontsize=12)

    plt.xticks(dados.index)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig(f'{titulo}.png', dpi=300)
    plt.show()

#Chamando as funções para criação de graficos
grafico_linha(crescimento,(10,5),4,'Evolução de Faturamento Anual','Ano','Total Vendido em Bilhões(R$)')
grafico_linha(lucro,(10,5),4,'Evolução do Lucro Anual','Ano','Total de Lucro em Bilhões (R$)')
grafico_horizontal(status_vendas_porc,(10,5),'Status de vendas','Percentagem (%)','Status')
grafico_horizontal(clientes_vips,(15,5),'Ranking dos 5 melhores cliente','Valor Total em Milhões (R$)','Cliente')

print(tu.head())