from brownie import accounts, interface, CurveClaim


def main():
    user = accounts.load(input('brownie account: '))

    crv = interface.CurveToken('0xD533a949740bb3306d119CC777fa900bA034cd52')
    minter = interface.CurveMinter('0xd061D61a4d941c39E5453435B6345Dc261C2fcE0')
    claim = CurveClaim.at('0x87B132af10D6c7237B2cf51B207F7777e901b770')

    if not minter.allowed_to_mint_for(claim, user):
        minter.toggle_approve_mint(claim, {'from': user})

    all_gauges = [
        '0x7ca5b0a2910B33e9759DC7dDB0413949071D7575', '0xFA712EE4788C042e2B7BB55E6cb8ec569C4530c1',
        '0x69Fb7c45726cfE2baDeE8317005d3F94bE838840', '0xA90996896660DEcC6E997655E065b23788857849',
        '0x64E3C23bfc40722d3B649844055F1D51c1ac041d', '0xB1F2cdeC61db658F091671F5f199635aEF202CAC',
        '0x705350c4BcD35c9441419DdD5d2f097d7a55410F',
    ]
    gauges = [gauge for gauge in all_gauges if interface.CurveGauge(gauge).balanceOf(user) > 0]
    gauges += ['0x0000000000000000000000000000000000000000' for _ in range(8 - len(gauges))]

    claimable = claim.claimable.call(user, gauges)
    print(f'Claimable CRV: {claimable / 1e18:,.2f}')

    if claimable > 0:
        claim.claim(gauges, {'from': user})

    print(f'CRV balance: {crv.balanceOf(user) / 1e18:,.2f}')
