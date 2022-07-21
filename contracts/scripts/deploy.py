from brownie import Token, DefiBank, accounts

def main():

    account = accounts.load('dev1')
    
    #token_addrs = Token.deploy({'from': account})
    #print(f"your token address: {token_addrs}")

    contract = DefiBank.deploy({'from': account})
    print(f'your contract deployed at {contract}')

    #defibank address: 
    #usd token address: 
