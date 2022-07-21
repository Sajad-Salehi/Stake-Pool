from brownie import Token, DefiBank, accounts

def main():

    account = accounts.load('dev1')
    
    #token_addrs = Token.deploy({'from': account})
    #print(f"your token address: {token_addrs}")

    contract = DefiBank.deploy({'from': account})
    print(f'your contract deployed at {contract}')

    #defibank address: 0x51A4ACef234c5b9E682F6d2584E1e41Cb6645C76
    #usd token address: 0x0B1B1D5481d05B0C0a1e5008DB55f87E64d03D18