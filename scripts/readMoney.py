from brownie import accounts, network, NumberAdder, config


def get_account():
    if network.show_active() == "development":
        account = accounts[0]
    else:
        account = accounts.add(config['wallets']['from_key'])
    return account

def main():
    numberAdder = NumberAdder[-1]
    account = get_account()

    print(numberAdder.parties("Tanish"))
    print(numberAdder.parties("Tan"))