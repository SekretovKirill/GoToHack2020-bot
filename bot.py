from time import sleep
import requests
from requests.auth import HTTPBasicAuth
def buy(priceold, price, a):
    if price/priceold - 1 <-a or price/priceold - 1 >= 0.1 :
        print(price, priceold, a,price/priceold - 1 )
        return 's'
    elif price/priceold - 1 >a or price/priceold - 1<= -0.1:
        print(price, priceold, a,price/priceold - 1 )
        return 'b'
    else:
        return ' '
    
def des(priceold, price, l1,l2, i, pr):
    f = buy(priceold, price,0.3)
    h = requests.get('http://stonks.goto.msk.ru/api/robot/balance/', auth=HTTPBasicAuth(l1, l2)).json()['balance']
    if f == 's':
        requests.get('http://stonks.goto.msk.ru/api/robot/stocks/'+str(pr.json()[i]['id'])+ '/buy?number='+ str(int(h*0.3/pr.json()[i]['price'])), auth=HTTPBasicAuth(l1, l2)) 
        print('bought '+str(pr.json()[i]['id'])+' '+ str(int(h*0.5/pr.json()[i]['price'])) )
    elif f == 'b':
        requests.get('http://stonks.goto.msk.ru/api/robot/stocks/'+str(pr[i]['id'])+ '/sell?number='+ str(pr.json()[i]['stocks']), auth=HTTPBasicAuth(l1, l2)) 
        print('sold ' + str(pr.json()[i]['id']) + ' ' + str(pr.json()[i]['stocks']))
    return requests.get('http://stonks.goto.msk.ru/api/robot/stocks', auth=HTTPBasicAuth(l1,l2)).json()[i]['price']

def bot(priceold,l1, l2):
    pr = requests.get('http://stonks.goto.msk.ru/api/robot/stocks', auth=HTTPBasicAuth(l1,l2))
    for i in range(len(pr.json())):
        priceold[i] =des(priceold[i], pr.json()[i]['price'],l1,l2,i, pr)
    print('sleep')
    sleep(300)
    print('awake')
    bot(priceold,l1, l2)
print('Введите логин от аккаунта goto stonks:')
l1 = input()
print('Введите парль от аккаунта goto stonks:')
l2 = input()
answer = requests.get('http://stonks.goto.msk.ru/api/robot/stocks', auth=HTTPBasicAuth(l1, l2))
k = []
for i in answer.json():
    k.append(i['price'])
bot(k,l1, l2)

            