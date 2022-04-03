// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DefiBank {

    uint256 startTime;
    uint256 endTime;

    address public Admin = 0x9515243Dfc19Df23B2877a411FAa6dB265bF8846;
    address public USDC = 0x5FdcF38f359c7408105dfA447590126591ba574f;
    address public soren = 0x4Fd2700fC5E38F60c0aa009cb1dbB3e311ed3E30;

    mapping(address => bool) deposeted;
    mapping(address => uint256) balances;

    event Stake(address staker, address token, uint256);
    event WithDraw(address staker, address token, uint256);
    event WithdrawInterest(address staker, address token, uint256);

    constructor(){

        startTime = block.timestamp;
        endTime = startTime + 7 days;
    
    }

    function stake(uint256 amount) public payable{

        require(block.timestamp >= startTime, 'too early');
        require(deposeted[msg.sender] == false, 'You can not invest twice');

        bool success = IERC20(USDC).transferFrom(msg.sender, address(this), amount);
        require(success == true, "transfer failed!");

        deposeted[msg.sender] = true;
        balances[msg.sender] += amount;

        emit Stake(msg.sender, USDC, amount);
        
    }

    function unstake() public payable{

        require(block.timestamp >= endTime, 'too early');
        require(balances[msg.sender] > 0, 'insufficient balance, You had unstaked your balance before');

        uint256 balance = balances[msg.sender];
        balances[msg.sender] = 0;

        IERC20(soren).transfer(msg.sender, balance / 100);
        IERC20(USDC).transfer(msg.sender, balance);

        emit WithDraw(msg.sender, USDC, balance);
        emit WithdrawInterest(msg.sender, soren, balance / 100);
    }

    function depositSoren(uint amount) public payable{

        require(msg.sender == Admin, "You can not have any access");
        IERC20(soren).transferFrom(msg.sender, address(this), amount);
    }

    function getbalance(address staker) public view returns(uint256){

        return balances[staker];
    }
}