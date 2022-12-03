import json

import web3
import yaml
import os

with open(os.path.join(os.path.dirname(__file__), 'config.yml'), 'r') as file:
    ymlConfig = yaml.safe_load(file)
    env = ymlConfig["env"]
    health_check_response = ymlConfig["health_check_msg"]
    id_address_map_file = ymlConfig["id_address_mapping_filename"]
    baseUrl = ymlConfig["baseUrl"]

    w3 = web3.Web3(web3.HTTPProvider(ymlConfig['node_address']))
    bot_token = ymlConfig["bot"]["token"]

    with open(ymlConfig["abi_path"]["erc20"], 'r') as erc20:
        abi_erc20 = json.load(erc20)
    with open(ymlConfig["abi_path"]["erc721"], 'r') as erc721:
        abi_erc721 = json.load(erc721)
    with open(ymlConfig["address_by_erc20_symbol_file"], 'r') as address_by_symbol:
        file_name = address_by_symbol.name
        with open(file_name, 'r') as address_file:
            address_by_erc20_symbol = yaml.safe_load(address_file)
