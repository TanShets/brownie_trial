from brownie import accounts, config, NumberAdder
import os

def temp_account():
    # account = accounts.load("sepolia_test")
    account = accounts.add(config['wallets']['from_key'])
    numberAdder = NumberAdder.deploy({"from": account})
    print(numberAdder)

    currentSum = numberAdder.getTotalSum()
    print(currentSum)
    transaction = numberAdder.registerParty("Tanish", {"from": account})
    transaction.wait(1)
    transaction = numberAdder.registerParty("Tan", {"from": account})
    transaction.wait(1)

    transaction = numberAdder.loadMoney("Tanish", 2500, {"from": account})
    transaction.wait(1)
    transaction = numberAdder.loadMoney("Tan", 250, {"from": account})
    transaction.wait(1)

    transaction = numberAdder.transact("Tanish", "Tan", 500, 1, {"from": account})
    transaction.wait(1)

    print(numberAdder.parties("Tanish"))
    print(numberAdder.parties("Tan"))



def main():
    temp_account()
    print("Hello world")