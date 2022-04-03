from brownie import USDC, SorenToken, DefiBank, config, accounts
from dotenv import load_dotenv
load_dotenv()

def main():
    
    account = accounts.load('mywallet')
    DefiBank.deploy({'from': account}, publish_source=True)
    
    
    