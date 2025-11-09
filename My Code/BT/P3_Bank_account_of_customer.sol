// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Program: Bank Account Smart Contract
// Aim: To create a smart contract that allows users to deposit, withdraw,
// and check their balance securely on the blockchain.

// --- Contract Declaration ---
contract BankAccount {

    // Step 1: State variables
    address public customer;          // To store the account owner's address
    uint256 private balance;          // To store the customer's balance (private for security)

    // Step 2: Constructor
    // Logic: When contract is deployed, the deployer becomes the account owner
    constructor() {
        customer = msg.sender;        // msg.sender is the address that deployed the contract
        balance = 0;                  // Initially, balance is set to 0
    }

    // Step 3: Deposit function
    // Logic: Function to allow the customer to deposit Ether into the account
    function deposit() public payable {
        require(msg.sender == customer, "Only the account owner can deposit.");  
        // 'msg.value' contains the amount of Ether sent with the transaction
        require(msg.value > 0, "Deposit amount must be greater than zero.");
        balance += msg.value;          // Add deposited amount to balance
    }

    // Step 4: Withdraw function
    // Logic: Function to allow the customer to withdraw Ether from their account
    function withdraw(uint256 amount) public {
        require(msg.sender == customer, "Only the account owner can withdraw.");
        require(amount <= balance, "Insufficient balance.");
        
        balance -= amount;             // Deduct the withdrawal amount from balance
        payable(msg.sender).transfer(amount);  // Send Ether back to customer
    }

    // Step 5: Show Balance function
    // Logic: Function to view current balance in the account
    function getBalance() public view returns (uint256) {
        require(msg.sender == customer, "Only the account owner can view balance.");
        return balance;                // Return the stored balance
    }
}
