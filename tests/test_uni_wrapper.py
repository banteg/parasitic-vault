import brownie


def test_uni_wrapper(a, UniswapWrapper, interface, chain):
    user = a[0]
    infinite = 2 ** 256 - 1
    wrapper = UniswapWrapper.deploy({'from': user})
    weth = interface.ERC20('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')
    dai = interface.ERC20('0x6B175474E89094C44Da98b954EedeAC495271d0F')
    yfi = interface.ERC20('0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e')
    # wrap weth
    user.transfer(weth, '2 ether')
    assert weth.balanceOf(user) == '2 ether'
    # fail on no weth allowance
    with brownie.reverts():
        wrapper.swap(weth, dai, '1 ether', 0, user, {'from': user})
    # swap to dai
    weth.approve(wrapper, infinite, {'from': user})
    wrapper.swap(weth, dai, '1 ether', 0, user, {'from': user})
    # check we spent weth and got dai
    assert weth.balanceOf(user) == '1 ether'
    amount_in = dai.balanceOf(user)
    assert amount_in > 0
    # fail on no dai allowance
    with brownie.reverts():
        wrapper.swap(dai, yfi, amount_in, 0, user, {'from': user})
    # swap to yfi
    dai.approve(wrapper, infinite, {'from': user})
    wrapper.swap(dai, yfi, amount_in, 0, user, {'from': user})
    # check we spent dai and got yfi
    assert dai.balanceOf(user) == 0
    assert yfi.balanceOf(user) > 0
    # accidentally send yfi to contract
    yfi.transfer(wrapper, '1 gwei', {'from': user})
    assert yfi.balanceOf(wrapper) == '1 gwei'
    # recover it
    wrapper.dust(yfi, {'from': user})
    assert yfi.balanceOf(wrapper) == 0
