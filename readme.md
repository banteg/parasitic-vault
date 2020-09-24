# Parasitic Vault

A set of single-user yearn-like strategies

## CurveClaim

Approves the contract to mint from gauges on your behalf, claims vested and gauges rewards.

```python
$ brownie run curve_claim --network mainnet

```

## UniswapWrapper

A wrapper contract for UniswapRouter that doesn't require dynamic arrays.
It routes directly if one of the (token_in, token_out) is WETH, otherwise adds a WETH intermediate pair.

Deployed at [`0x6A99298240EF13e58688a8634E625d4E13974558`](https://etherscan.io/address/0x6a99298240ef13e58688a8634e625d4e13974558#code)

Solidity interface:
```solidity
interface UniswapWrapper {
    function swap(
        address token_in,
        address token_out,
        uint256 amount_in,
        uint256 min_amount_out,
        address to
    ) external returns (bool);
}
```
Vyper interface:
```python
interface UniswapWrapper:
    def swap(token_in: address, token_out: address, amount_in: uint256, min_amount_out: uint256, to: address) -> bool: nonpayable
```
