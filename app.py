# Criar um programa que leia a cotação do dóllar e avise quando for menor que R$5,10 e envie um email automatico para que eu possa saber dessa maravilha

import requests # pegar a informação você quer
import smtplib
import email.message # enviar um aviso - email


def enviar_email(cotacao):
    corpo_email = f"""
    <p>Bom dia, Askerzim. Hoje o dólar está abaixo ou igual a R$5.10. Cotação atual: R${cotacao:.2f}, ou seja, está na hora de comprar!</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Dólar está hoje abaixo de R$5.10"
    msg['From'] = 'seu-email'
    msg['To'] = 'seu-email'
    password = 'dzyfxalduwfsyphe'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587') #acessar o servidor do email
    s.starttls() #criar conf de segurança
    s.login(msg['From'], password) #faz o login no seu email
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8')) #envia para seu próprio email
    print('Email enviado')


requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
dados = requisicao.json()
cotacao = float((dados)['USDBRL']['bid'])
print(cotacao)


if cotacao < 5.10:
    enviar_email(cotacao)
