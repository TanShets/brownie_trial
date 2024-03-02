from brownie import NumberAdder, accounts

def test_num_add():
    account = accounts[0]
    numberAdder = NumberAdder.deploy({'from': account})

    assert numberAdder.parties("Tanish") == ('', 0)
    assert numberAdder.parties("Tan") == ('', 0)

    tran1 = numberAdder.registerParty("Tanish", {'from': account})
    tran1.wait(1)
    tran2 = numberAdder.registerParty("Tan", {'from': account})
    tran2.wait(1)

    tran1 = numberAdder.loadMoney('Tanish', 2500, {'from': account})
    tran1.wait(1)
    tran2 = numberAdder.loadMoney('Tan', 250, {'from': account})
    tran2.wait(1)

    assert numberAdder.parties('Tanish')[1] == 2500
    assert numberAdder.parties('Tan')[1] == 250

    tran1 = numberAdder.transact('Tanish', 'Tan', 500, 1, {'from': account})
    tran1.wait(1)

    assert numberAdder.parties('Tanish')[1] == 2000
    assert numberAdder.parties('Tan')[1] == 750