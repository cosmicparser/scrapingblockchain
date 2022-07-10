import requests
import re
import bs4
from bs4 import BeautifulSoup
import certifi
import pandas as pd
import requests, json, openpyxl


key = "WW8TF8W4DC4PRCQZY5D3VXIMKEA3JI4HUU"

url = "https://api.etherscan.io/api"

contractadress = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
startblock = "0"


def query(contractadress, startblock, number):
    querystring = {"module":"account","action":"tokennfttx","contractaddress":contractadress,
                   "sort":"asc","page":"2","startblock":startblock,"endblock":"99999999","apikey":key}


    response = requests.request("GET",url,params=querystring)

    #print(response.url)

    a = response.json()

    initiallist = []

    for i in a["result"]:
        print(i)
        initiallist.append(i)

    working = initiallist[1]


    print("lol")
    print(working)


    data = []
    for i in initiallist:
        tings = []
        for value in i:
            tings.append(i[value])

        print(len(tings))
        data.append(tings)




    df = pd.DataFrame(data, columns=['Blocknum', 'timestamp', 'hash', 'nonce', 'blockhash', 'from', 'contractadress', 'to', 'tokenid', 'tokenname', 'tokensymbol', 'tokendecimal', 'transactionindex', 'gas', 'gasprice', 'gasused',"cumulativegasused","input","confirmations"])
    path = r"C:\Users\User\Desktop\cryptoblock"+number+".xlsx"
    df.to_excel(path, index=False)
    block = tings[0]
    return block



for i in range(0,10):
    result = query("0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D","0","1")

