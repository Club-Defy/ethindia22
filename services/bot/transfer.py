import base64
import json


def eth(to_address, amount):
    print(to_address, " -> ", amount)
    pass


def erc20(to_address, token_address, amount):
    return _get_url(to_address, token_address, amount)


def erc721(to_address, token_address, token_id):
    return _get_url(to_address, token_address, token_id)


def _get_url(to_address, token_address, token_id):
    return base64.urlsafe_b64encode(
        json.dumps(_get_return_value(to_address, token_address, token_id)).encode()).decode()


def _get_return_value(action, to_address, contract, value):
    return {
        'action': action,
        'collection_address': contract,
        'params': {
            'value': value,
            'to_address': to_address
        }
    }
