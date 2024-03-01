// SPDX-License-Identifier: MIT 

pragma solidity ^0.8.0;
pragma experimental ABIEncoderV2;

contract NumberAdder {
    uint256 private totalSum;

    struct Party {
        string _partyName;
        int256 totalAmount;
    }

    struct Transaction {
        Party owner;
        Party cpty;
        int256 amount;
    }

    mapping(string => Party) public parties;

    mapping(string => Transaction[]) transactions;

    function keepNum(uint256 _candidateSum) public {
        totalSum = _candidateSum;
    }

    function getParty(string memory party) public view returns(Party memory) {
        return parties[party];
    }

    function getTotalSum() public view returns(uint256) {
        return totalSum;
    }

    function registerParty(string memory name) public returns(string memory) {
        if(parties[name].totalAmount == 0){
            parties[name] = Party(name, -1);
            return "Success";
        }
        else {
            return "Party has already been registered";
        }
    }

    function loadMoney(string memory name, int256 balance) public returns(string memory){
        if(parties[name].totalAmount == -1 ){
            parties[name].totalAmount = balance;
            return "Success";
        }
        else{
            return "Failed";
        }
    }

    function addTransaction(string memory owner, string memory cpty, int256 amount) internal returns(bool) {
        Party memory ownerParty = parties[owner];
        Party memory cptyParty = parties[cpty];
        if(ownerParty.totalAmount == -1 || cptyParty.totalAmount == -1){
            return false;
        }
        transactions[owner].push(Transaction(ownerParty, cptyParty, amount));
        return true;
    }

    function transact(string memory owner, string memory cpty, int256 amount, uint256 direction) public returns(string memory) {
        string memory payer;
        string memory receiver;

        if(direction == 1){
            payer = owner;
            receiver = cpty;
        }
        else if(direction == 0) {
            payer = cpty;
            receiver = owner;
        }

        if(addTransaction(payer, receiver, amount) && addTransaction(receiver, payer, -amount)){
            parties[payer].totalAmount -= amount;
            parties[receiver].totalAmount += amount;
            return "Success";
        }
        else {
            return "Failed Transaction";
        }
    }

    function showTransactions(string memory owner) public view returns(Transaction[] memory){
        return transactions[owner];
    }
    
    function doubleAndGiveIt() public pure returns(uint256) {
        return 5555 * 32323;
    }
}