import base64
import json
import math

from web3 import Web3

from config.config import w3, abi_erc20, baseUrl


def eth(to_address, amount):
    return _get_url('eth', to_address, '0x0', Web3.toWei(amount, 'ether'))


def erc20(to_address, token_address, amount):
    return _get_url('erc20', to_address, token_address, _get_base_amount(amount, token_address))


def erc721(to_address, token_address, token_id):
    return _get_url('erc721', to_address, token_address, token_id)

def erc20_approve(spender, amount, token_address):
    return _get_url('approve_erc20', spender, token_address, _get_base_amount(amount, token_address))

def _get_base_amount(amount, contract_address):
    return int(amount) * math.pow(10, w3.eth.contract(address=Web3.toChecksumAddress(contract_address),
                                                      abi=abi_erc20).functions.decimals().call())
def _get_url(action, to_address, token_address, token_id):
    return baseUrl + "q=" + base64.urlsafe_b64encode(
        json.dumps(_get_return_value(action, to_address, token_address, token_id)).encode()).decode()


def _get_return_value(action, to_address, contract, value):
    return {
        'action': action,
        'contract': Web3.toChecksumAddress(contract),
        'params': {
            'value': value,
            'to_address': Web3.toChecksumAddress(to_address)
        }
    }
