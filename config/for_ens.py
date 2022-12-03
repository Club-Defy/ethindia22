from ens import ENS
from web3 import Web3
from web3.auto.infura import (
    build_http_headers, build_infura_url)
from web3.auto.infura.endpoints import INFURA_GOERLI_DOMAIN
from web3.providers.auto import load_provider_from_uri


def get_ens():
    _headers = build_http_headers()

    _infura_url = build_infura_url(INFURA_GOERLI_DOMAIN)

    w3 = Web3(load_provider_from_uri(_infura_url, _headers))
    ens = ENS.fromWeb3(w3)

    from web3.middleware import geth_poa_middleware

    ens.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    return ens
