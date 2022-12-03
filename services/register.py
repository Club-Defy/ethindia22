import os
import yaml
from pathlib import Path
import config.config
from threading import Lock

lock = Lock()


def register_discord_id(address, discord_id):
    mapping_file = config.config.id_address_map_file
    directory_name = os.path.dirname
    mapping_file_path = os.path.join(directory_name(directory_name(__file__)), mapping_file)

    if not os.path.exists(mapping_file_path): Path(mapping_file_path).touch()

    stream = open(mapping_file_path, 'r')
    data = yaml.safe_load(stream)
    if data is None:
        data = {discord_id: address}
    else:
        data[discord_id] = address

    with lock:
        with open(mapping_file, 'w') as yaml_file:
            yaml_file.write(yaml.dump(data))
