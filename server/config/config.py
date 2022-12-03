import yaml

with open('config.yml', 'r') as file:
    ymlConfig = yaml.safe_load(file)
    env = ymlConfig["env"]
    health_check_response = ymlConfig["health_check_msg"]
