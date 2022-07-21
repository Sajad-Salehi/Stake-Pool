import json
import os
import time
from web3 import Web3
from web3.middleware import geth_poa_middleware



def get_balance():

    contract_info = connect_web3('defibank')
    balance = contract_info['contract'].functions.getbalance(contract_info['wallet_address']).call()
    return balance // 10**18



def withdraw():

    contract_info = connect_web3('defibank')
    trx = contract_info['contract'].functions.withdraw().buildTransaction({

        "chainId": contract_info['rinkeby_chain_id'],
        "from": contract_info['wallet_address'],
        "nonce": contract_info['nonce']
    })

    sign_trx = contract_info['w3'].eth.account.sign_transaction(
        trx,
        private_key=contract_info['private_key']
    )

    trx_hash = contract_info['w3'].eth.send_raw_transaction(sign_trx.rawTransaction)
    trx_recipt = contract_info['w3'].eth.wait_for_transaction_receipt(trx_hash)
    time.sleep(5)
    return trx_hash



def deposit(amount):
    
    approve()
    contract_info = connect_web3('defibank')
    print(contract_info['nonce'], '\n')

    _amount = Web3.toWei(amount, 'ether')
    trx = contract_info['contract'].functions.deposit(_amount).buildTransaction({

        "chainId": contract_info['rinkeby_chain_id'],
        "from": contract_info['wallet_address'],
        "nonce": contract_info['nonce']
    })

    sign_trx = contract_info['w3'].eth.account.sign_transaction(
        trx,
        private_key=contract_info['private_key']
    )

    trx_hash = contract_info['w3'].eth.send_raw_transaction(sign_trx.rawTransaction)
    trx_recipt = contract_info['w3'].eth.wait_for_transaction_receipt(trx_hash)
    time.sleep(5)
    return trx_hash


def approve():


    token_info = connect_web3('token')
    print(token_info)
    max_amount = Web3.toWei(2**64-1,'ether')    
    spender = '0x51A4ACef234c5b9E682F6d2584E1e41Cb6645C76'

    tx = token_info['contract'].functions.approve(spender, max_amount).buildTransaction({
        'from': token_info['wallet_address'], 
        'nonce': token_info['nonce']
        })
        
    signed_tx = token_info['w3'].eth.account.signTransaction(tx, token_info['private_key'])
    tx_hash = token_info['w3'].eth.sendRawTransaction(signed_tx.rawTransaction)
    time.sleep(10)
    return token_info['w3'].toHex(tx_hash)



def connect_web3(contract_name):

    if contract_name == 'defibank':
        file = open('DefiBank.json')
        contract_address = '0x51A4ACef234c5b9E682F6d2584E1e41Cb6645C76'


    elif contract_name == 'token':
        file = open('Token.json')
        contract_address = '0x0B1B1D5481d05B0C0a1e5008DB55f87E64d03D18'

    data = json.load(file)
    abi = data["abi"]


    trx_info = {

        'w3': None,
        'nonce': None,
        'contract': None,
        'rinkeby_chain_id': 4,
        'contract_address': contract_address,
        'private_key': os.getenv('PRIVATE_KEY'),
        'provider_url': os.getenv('WEB3_PROVIDER'),
        'wallet_address': '0xB268C07881a418D0BcADCF7204CeBc6D68A54904'
    }

    # connecting to the infura http provier and create contract
    w3 = Web3(Web3.HTTPProvider(trx_info['provider_url']))
    trx_info['w3'] = w3
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    nonce = w3.eth.getTransactionCount(trx_info['wallet_address'])
    trx_info['nonce'] = nonce
    trx_info['contract_addres'] = contract_address
    contract = w3.eth.contract(address=contract_address, abi=abi)
    trx_info['contract'] = contract

    return trx_info


print(get_balance())