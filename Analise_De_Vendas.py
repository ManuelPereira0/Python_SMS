import pandas as pd
from twilio.rest import Client

account_sid = "fornecido pelo twilio"
auth_token = "fornecido pelo twilio"
client = Client(account_sid, auth_token)
#Passo  a passo da solução
#Abrir os 6 arquivos em excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel('{}.xlsx'.format(mes))
    if (tabela_vendas['Vendas'] > 55000).any():
        #.any = algum valor
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        #.loc = localizar na tabela
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        #.loc trás em tabela, .values 'tira' da tabela e trás o valor
        #f e .format são iguais
        message = client.messages.create(
            to= "Seu telefone",
            from_= "Telefone fornecido pelo twilio",
            body=f'No mês {mes} o vendedor(a) {vendedor} vendeu R${vendas}'
        )
        print(message.sid)
        
# Para cada arquivo:
#Verificar se algum valor na coluna Vendas é maior que 55.000
#Se for maior enviar um SMS com o nome, o mês e as vendas

