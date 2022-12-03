import time
from web3 import Web3
import json
import base64
import math

from config.config import w3, abi_erc20, baseUrl, transaction_deadline_mins, uniswap_router_address, weth_address


def swap_erc20_to_erc20(from_amount, from_currency, to_currency):
    return _get_url('swap', uniswap_router_address, 0, _get_base_amount(from_amount, from_currency), 0,
                    [from_currency, to_currency], _fetch_deadline())


def swap_eth_to_erc20(from_amount, to_currency):
    return _get_url('swap_eth', uniswap_router_address, _get_base_amount(from_amount, weth_address), 0, 0,
                    [weth_address, to_currency],
                    _fetch_deadline())


def swap_erc20_to_eth(from_amount, from_currency):
    return _get_url('swap_erc20', uniswap_router_address, 0, _get_base_amount(from_amount, weth_address), 0,
                    [from_currency, weth_address],
                    _fetch_deadline())


def _get_base_amount(amount, contract_address):
    return int(float(amount) * math.pow(10, w3.eth.contract(address=Web3.toChecksumAddress(contract_address),
                                                            abi=abi_erc20).functions.decimals().call()))


def _fetch_deadline():
    return int(time.time()) + 60 * transaction_deadline_mins


def _get_url(action, contract_address, value, amount_in, amount_out_min, path, deadline):
    return baseUrl + "q=" + base64.urlsafe_b64encode(
        json.dumps(_get_return_value(action, contract_address, value, amount_in, amount_out_min, path,
                                     deadline)).encode()).decode()


def _get_return_value(action, contract_address, value, amount_in, amount_out_min, path, deadline):
    return {
        'action': action,
        'contract': contract_address,
        'params': {
            'amountIn': amount_in,
            'amountOutMin': amount_out_min,
            'path': path,
            'deadline': deadline,
            'value': value
        }
    }
