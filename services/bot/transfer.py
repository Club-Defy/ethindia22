def eth(to_address, amount):
    print(to_address, " -> ", amount)
    pass


def erc20(to_address, token_address, amount):
    print("transfer " + amount + " " + token_address + " to " + to_address)
    pass

def erc721(to_address, token_address, token_id):
    print("transfer " + token_id + " " + token_address + " to " + to_address)
    pass
