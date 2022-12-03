import base64
import json
import math

from web3 import Web3

from config.config import w3, abi_erc20, baseUrl, address_by_erc20_symbol


def eth(to_address, amount):
    return _get_url('eth', to_address, '0x0000000000000000000000000000000000000000', Web3.toWei(amount, 'ether'))


def erc20(to_address, token_address, amount):
    token = _get_erc20_address(token_address)
    return _get_url('erc20', to_address, token,
                    int(amount) * math.pow(10, w3.eth.contract(address=Web3.toChecksumAddress(token),
                                                               abi=abi_erc20).functions.decimals().call()))


def erc721(to_address, token_address, token_id):
    return _get_url('erc721', to_address, token_address, token_id)


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


def _get_erc20_address(token_name):
    token = str.upper(token_name)
    if token not in address_by_erc20_symbol:
        return token_name
    return address_by_erc20_symbol[token]
