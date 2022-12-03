import yaml
import os

with open(os.path.join(os.path.dirname(__file__), 'config.yml'), 'r') as file:
    ymlConfig = yaml.safe_load(file)
    env = ymlConfig["env"]
    health_check_response = ymlConfig["health_check_msg"]

    bot_token = ymlConfig["bot"]["token"]
    erc20_abi_path = ymlConfig["abi_path"]["erc20"]
    erc721_abi_path = ymlConfig["abi_path"]["erc721"]
    swap_abi_path = ymlConfig["abi_path"]["swap"]
