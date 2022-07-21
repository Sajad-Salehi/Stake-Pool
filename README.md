# Stake-Pool
A simple Stake Pool Smart Contract using Solidity, Python and Flask<br>

## Prerequisites

Please install or have installed the following:

- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)
- [metamask](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjtl7Oi6N_4AhWei_0HHbjzDH4QjBB6BAgHEAE&url=https%3A%2F%2Fmetamask.io%2Fdownload%2F&usg=AOvVaw049ASZIf5umKu9KN8vjUeH)

## Installation

[Install virtualenv](https://virtualenv.pypa.io/en/latest/installation.html), if you haven't already. Here is a simple way to install venv.

```bash
python -m pip install --user virtualenv
python -m virtualenv --help
```

Or, if that doesn't work, via pipx
```bash
pipx install virtualenv
virtualenv --help
```
Create a Virtual Environments and active venv
```bash
python3 -m virtualenv venv
cd venv/bin
source activate
```

After that you need install flask, web3.py and ipfs that we're going to use it to store our metadata 
```bash
pip install web3
pip install flask
pip install eth-brownie
```


# Usage
Clone this repository and deploy the smart contract
```bash
cd contracts
brownie run scripts/deploy.py --network <"NETWORK">
```

now go to build/contracts, copy json files and save it in src directory
then you can run your Dapp
```bash
flask run
```

#Resources
See my article in Medium: https://medium.com/@sajadsolidity/how-to-connect-flask-app-to-a-smart-contract-4a843b0a97fd
