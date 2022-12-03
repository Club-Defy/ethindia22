import base64
import json
import math
import os

import yaml
from web3 import Web3

from config.config import w3, abi_erc20, baseUrl, id_address_map_file, address_by_erc20_symbol


def eth(to_address, amount):
    return _get_url('eth', to_address, '0x0000000000000000000000000000000000000000', Web3.toWei(amount, 'ether'))


def erc20(to_address, token_address, amount):
    token = _get_erc20_address(token_address)
    return _get_url('erc20', to_address, token, _get_base_amount(amount, token))


def erc721(to_address, token_address, token_id):
    return _get_url('erc721', to_address, token_address, token_id)


def erc20_approve(spender, amount, token_address):
    return _get_url('approve_erc20', spender, token_address, _get_base_amount(amount, token_address))


def _get_base_amount(amount, contract_address):
    return int(float(amount) * math.pow(10, w3.eth.contract(address=Web3.toChecksumAddress(contract_address),
                                                 abi=abi_erc20).functions.decimals().call()))


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


def get_address_from_id(discord_id):
    mapping_file = id_address_map_file
    directory_name = os.path.dirname
    mapping_file_path = os.path.join(directory_name(directory_name(directory_name(__file__))), mapping_file)
    if not os.path.exists(mapping_file_path): return ""

    stream = open(mapping_file_path, 'r')
    data = yaml.safe_load(stream)
    if data is None:
        return ""
    else:
        return data[discord_id]


def _get_erc20_address(token_name):
    token = str.upper(token_name)
    if token not in address_by_erc20_symbol:
        return token_name
    return address_by_erc20_symbol[token]
