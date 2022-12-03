from ens import ENS
from web3 import Web3
from web3.auto.infura import (
    build_http_headers)
from web3.providers.auto import load_provider_from_uri


def get_ens(node_address):
    _headers = build_http_headers()

    w3 = Web3(load_provider_from_uri(node_address, _headers))
    ens = ENS.fromWeb3(w3)

    from web3.middleware import geth_poa_middleware

    ens.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    return ens
