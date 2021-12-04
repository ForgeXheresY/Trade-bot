import json
import httplib2
import urllib

from Keys import API_key, API_secret, ETH_wallet_address, DAI_id
from coinbase.wallet.client import Client
client = Client(API_key,API_secret)

account = client.get_account(DAI_id)

#dai deposit wallet values
DAI_amount = float( str( account['balance'] ).replace('DAI','') )
CAD_balance = float( str( account['native_balance'] ).replace('CAD','') )

#price of tokens relative to ETH or dai
ex_rate= str(client.get_exchange_rates(currency='DAI')['rates'])
# price = ex_rate['ETH']



# add data to json file to be the backbone of database
f = open("data.json", "a")
f.write(ex_rate)
f.close()

#open and read the file after the appending:
f = open("data.json", "r")
# print(f.read())
f.close()

# send DAI to ETH wallet(trading wallet)
# tx = client.send_money(DAI_id, to= ETH_wallet_address, amount='10', currency='DAI', idem='8316dd16-0c08')
# print(tx)
