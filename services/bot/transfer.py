import base64

from web3 import Web3
import json


def convert_dict_to_base64(dict):
    return base64.b64encode(bytes(json.dumps(dict), 'utf-8')).decode('utf-8')


def eth(to_address, amount):
    data = {
        "action": "eth",
        "to": to_address.lower(),
        "value": Web3.toWei(amount, 'ether')
    }

    return convert_dict_to_base64(data)


def erc20(to_address, token_address, amount):
    print("transfer " + amount + " " + token_address + " to " + to_address)
    pass


def erc721(to_address, token_address, token_id):
    print("transfer " + token_id + " " + token_address + " to " + to_address)
    pass
