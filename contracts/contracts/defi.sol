// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DefiBank {


    address public constant Admin = 0xB268C07881a418D0BcADCF7204CeBc6D68A54904;
    address public constant USD = 0x0B1B1D5481d05B0C0a1e5008DB55f87E64d03D18;
    address public constant soren = 0xC07FEc71bbc111C6fC9C33da2cbEA586469b9097;

    mapping(address => uint256) balances;
    event Deposit(address user, address token, uint256 amount);
    event WithDraw(address user, address token, uint256 amount);

    /* constructor(){

        start_time = block.timestamp;
        end_time = start_time + 7 days;
    }*/

    function deposit(uint256 amount) public payable{

        require(amount >= 100000000000000000000, 'The amount should be more than 100 USD');
        
        bool success = IERC20(USD).transferFrom(msg.sender, address(this), amount);
        require(success == true, "transfer failed!");

        balances[msg.sender] += amount;
        emit Deposit(msg.sender, USD, amount);
        
    }


    function withdraw() public payable{

        require(balances[msg.sender] > 0, 'insufficient balance');
        //require(block.timestamp >= end_time, 'too early');

        uint256 balance = balances[msg.sender];
        balances[msg.sender] = 0;

        IERC20(USD).transfer(msg.sender, balance);
        IERC20(soren).transfer(msg.sender, balance / 100);
        emit WithDraw(msg.sender, USD, balance);
    }


    function getbalance(address user) public view returns(uint256){

        return balances[user];
    }
}