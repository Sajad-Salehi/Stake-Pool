// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token is ERC20, Ownable {

    constructor() ERC20("USD", "USD"){

        _mint(msg.sender, 1000000000000000000000000);
    }
}