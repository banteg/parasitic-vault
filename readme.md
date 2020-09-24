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

Deployed at [`0xE929d7af8CEdA5D6002568110675B82D3fA84BA3`](https://etherscan.io/address/0xE929d7af8CEdA5D6002568110675B82D3fA84BA3#code)

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

    function quote(
        address token_in,
        address token_out,
        uint256 amount_in
    ) external view returns (uint256);
}
```
Vyper interface:
```python
interface UniswapWrapper:
    def swap(token_in: address, token_out: address, amount_in: uint256, min_amount_out: uint256, to: address) -> bool: nonpayable
    def quote(token_in: address, token_out: address, amount_in: uint256) -> uint256: view
```
