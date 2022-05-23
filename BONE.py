# Setting up packages etc 
from ast import Return
import json
from web3 import Web3
from datetime import timezone
import datetime
from decimal import Decimal

percent = chr(37)

# Fill in your infura API key here to connect to ETHEREUM node - NOTE THIS LINK WILL NOT WORK (YOU NEED YOUR OWN FROM https://infura.io/)
infura_url = 'https://mainnet.infura.io/v3/d6187bf3540244ad99f60866819672f5'

# Set up web 3 connection 
web3 = Web3(Web3.HTTPProvider(infura_url))

#constructing a BLOCK # time stamp 
block = (web3.eth.blockNumber)

# ISO 8606 time format 
now = datetime.datetime.utcnow().replace(microsecond=0).isoformat()

# first we setup the necessary contract 
# https://www.dextools.io/app/ether/pair-explorer/0xefb47fcfcad4f96c83d4ca676842fb03ef20a477
# TOKEN CONTRACT: https://etherscan.io/address/0x9813037ee2218799597d83d4a5b6f3b6778218d9#code
# TOKEN TRACKER: https://etherscan.io/token/0x9813037ee2218799597d83d4a5b6f3b6778218d9
SHIBASWAP_BONE_contract_address = Web3.toChecksumAddress('0x9813037ee2218799597d83D4a5B6F3b6778218d9')
SHIBASWAP_BONE_contract_abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"delegator","type":"address"},{"indexed":true,"internalType":"address","name":"fromDelegate","type":"address"},{"indexed":true,"internalType":"address","name":"toDelegate","type":"address"}],"name":"DelegateChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"delegate","type":"address"},{"indexed":false,"internalType":"uint256","name":"previousBalance","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newBalance","type":"uint256"}],"name":"DelegateVotesChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DELEGATION_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAIN_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint32","name":"","type":"uint32"}],"name":"checkpoints","outputs":[{"internalType":"uint32","name":"fromBlock","type":"uint32"},{"internalType":"uint256","name":"votes","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"}],"name":"delegate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"delegateBySig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegator","type":"address"}],"name":"delegates","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getCurrentVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPriorVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"numCheckpoints","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
    )
contract = web3.eth.contract(address=SHIBASWAP_BONE_contract_address, abi=SHIBASWAP_BONE_contract_abi)

# second we check the total supply of $BONE minted, converting into ETHER denomination and writing in millions to 2 decimal places
supply = contract.functions.totalSupply().call()
supply_wei = round(web3.fromWei(supply, 'ether')/1000000,2)

# next we look at BuryBone contract. This is the amount of $BONE staked - as it is a holder - and call the balance of function
# CONTRACT: https://etherscan.io/address/0xf7a0383750fef5abace57cc4c9ff98e3790202b3#code
# tBONE WALLET ADDRESS: https://etherscan.io/address/0xf7a0383750fef5abace57cc4c9ff98e3790202b3
# tBONE TOKEN TRACKER: https://etherscan.io/token/0xf7a0383750fef5abace57cc4c9ff98e3790202b3
bury_BONE_address = '0xf7a0383750fef5abace57cc4c9ff98e3790202b3'


# then we look at the BoneLocker contract. This is the amountof $BONE rewards to be claimed
# CONTRACT: https://etherscan.io/address/0xa404f66b9278c4ab8428225014266b4b239bcdc7#code
# WALLET ADDRESS: https://etherscan.io/address/0xa404f66b9278c4ab8428225014266b4b239bcdc7
unwoofed_BONE_address =  '0xa404f66b9278c4ab8428225014266b4b239bcdc7'


# then we look at the TopDog contract. This is the contract responsible for minting and distirbute to rewards pools
# CONTRACT: https://etherscan.io/address/0x94235659cf8b805b2c658f9ea2d6d6ddbb17c8d7#code
# WALLET ADDRESS: https://etherscan.io/address/0x94235659cf8b805b2c658f9ea2d6d6ddbb17c8d7
TOPDOG_BONE_address =  '0x94235659cf8b805b2c658f9ea2d6d6ddbb17c8d7'

# then we look at the set of LP pools / amount of $BONE in LP pairs
# # SSLP TOKEN TRACKER: https://etherscan.io/token/0xefb47fcfcad4f96c83d4ca676842fb03ef20a477#balances 
# https://www.dextools.io/app/ether/pair-explorer/0x6de1f2ddf595139fc196ff98c14dfdb4d6b3fab0
# CONTRACT: https://etherscan.io/address/0xefb47fcfcad4f96c83d4ca676842fb03ef20a477#code

# THIS IS THE BONE/WETH pair 
# WALLET ADDRESS: https://etherscan.io/address/0xefb47fcfcad4f96c83d4ca676842fb03ef20a477
WETH_BONE_address = '0xefb47fcfcad4f96c83d4ca676842fb03ef20a477'

# SHIB/BONE pair
# WALLET ADDRESS: https://etherscan.io/address/0xff64cb7ba5717a10dabc4be3a41acd2c2f95ee22
SHIB_BONE_address = '0xff64cb7ba5717a10dabc4be3a41acd2c2f95ee22'

# LEASH/BONE pair
# WALLET ADDRESS: https://etherscan.io/address/0xf6badfb9b0ab2f8f3fd8225ef1ea12fa689ad1a7  
LEASH_BONE_address = '0xf6badfb9b0ab2f8f3fd8225ef1ea12fa689ad1a7'


# THEN THERE ARE SOME OTHER CONTRACTS

# MULTI TOKEN LOCKER
# WALLET ADDRESS: https://etherscan.io/address/0x4bb0cdd7c906151347ad915af07f6af50c9028f7#code
MTL_BONE_address = '0x4bb0cdd7c906151347ad915af07f6af50c9028f7'

# GNOSIS SAFE
# wallet ADDRESS = https://etherscan.io/address/0xc9f512da761e121c2ff06abe3e7e13ba5752bbd8
GNOSIS_BONE_address = '0xc9f512da761e121c2ff06abe3e7e13ba5752bbd8'

# GNOSIS SAFE
# wallet ADDRESS = https://etherscan.io/address/0x38e1d4314a38c60c6ab3b98b0a89a4411d839d44
GNOSIS_2_BONE_address = '0x38e1d4314a38c60C6ab3b98b0a89a4411D839d44'

# CONTRACT: https://etherscan.io/address/0x44c652d679d99bb406167de9651d2535850fb479#code
# wALLET ADDRESS: https://etherscan.io/address/0x44c652d679d99bb406167de9651d2535850fb479
DEV_BONE_address = '0x44c652d679d99bb406167de9651d2535850fb479'

# then looking at the BONE MERKLE DISTRIB

# CONTRACT: https://etherscan.io/address/0x205c41bf932a34e14fea6b9b25585b3a5903aeeb#code
# WALLET ADDRESS: https://etherscan.io/address/0x205c41bf932a34e14fea6b9b25585b3a5903aeeb
MERKLE_BONE_address = '0x205c41bf932A34E14fea6b9B25585b3A5903aEeB'

# xshib BONE MERKLE DISTRIB
# CONTRACT: https://etherscan.io/address/0xa2c14852974afE7755eA824260Ca5dF03B816458#code
# WALLET ADDRESS: https://etherscan.io/address/0xa2c14852974afE7755eA824260Ca5dF03B816458
xshib_MERKLE_BONE_address = '0xa2c14852974afE7755eA824260Ca5dF03B816458'

# xleash BONE MERKLE DISTRIB
# CONTRACT: https://etherscan.io/address/0x9495A029Ce34983C0bF0c45EE8214021E95dA26A#code
# WALLET ADDRESS: https://etherscan.io/address/0x9495A029Ce34983C0bF0c45EE8214021E95dA26A
xleash_MERKLE_BONE_address = '0x9495A029Ce34983C0bF0c45EE8214021E95dA26A'
 
# tbone BONE MERKLE DISTRIB
# CONTRACT: https://etherscan.io/address/0xBaAa2B1F770c8AA0f86203C77A6b01E8315b3238#code
# WALLET ADDRESS: https://etherscan.io/address/0xBaAa2B1F770c8AA0f86203C77A6b01E8315b3238 
tbone_MERKLE_BONE_address = '0xBaAa2B1F770c8AA0f86203C77A6b01E8315b3238' 

# THEN THERE ARE SOME EXCHANGES (MEXC AND HOBIT)

# wALLET ADDRESS: https://etherscan.io/address/0x3cc936b795a188f0e246cbb2d74c5bd190aecf18
MEXC_3_BONE_address = '0x3cc936b795a188f0e246cbb2d74c5bd190aecf18'

# wALLET ADDRESS: https://etherscan.io/address/0x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88
MEXC_BONE_address = '0x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88'

# wALLET ADDRESS: https://etherscan.io/address/0x562680a4dc50ed2f14d75bf31f494cfe0b8d10a1
HOTBIT_BONE_address = '0x562680a4dc50ed2f14d75bf31f494cfe0b8d10a1'

# KNOWN BURNT BONE
# WALLET ADDRESS = https://etherscan.io/address/0xdead000000000000000042069420694206942069
burnt_BONE_address = '0xdead000000000000000042069420694206942069'

# creating list of relevant addresses
my_ADDRESSES = [bury_BONE_address, unwoofed_BONE_address, TOPDOG_BONE_address, 
                WETH_BONE_address, SHIB_BONE_address, LEASH_BONE_address, 
                MTL_BONE_address, GNOSIS_BONE_address, GNOSIS_2_BONE_address, DEV_BONE_address, 
                MERKLE_BONE_address, xshib_MERKLE_BONE_address, xleash_MERKLE_BONE_address, tbone_MERKLE_BONE_address, 
                MEXC_3_BONE_address, MEXC_BONE_address, HOTBIT_BONE_address, 
                burnt_BONE_address]

# iterating balanceOf function through elements in address
bone_balance = []

for i in my_ADDRESSES:
    format = Web3.toChecksumAddress(i)
    balance = contract.functions.balanceOf(format).call()
    j = (round(web3.fromWei(balance, 'ether')/1000000,2))
    bone_balance.append(j)

for i,j in zip(my_ADDRESSES, bone_balance):
    print (i,j)

# changing class from decimal.Decimal to float
balance_FLOAT = []

for i in bone_balance:
    j = "{0:f}".format(i)
    k = float(j)
    balance_FLOAT.append(k)

bury_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(bury_BONE_address)])

unwoofed_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(unwoofed_BONE_address)])

TOPDOG_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(TOPDOG_BONE_address)])

WETH_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(WETH_BONE_address)])

SHIB_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(SHIB_BONE_address)])

LEASH_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(LEASH_BONE_address)])

MTL_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(MTL_BONE_address)])

GNOSIS_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(GNOSIS_BONE_address)])

GNOSIS_2_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(GNOSIS_2_BONE_address)])

DEV_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(DEV_BONE_address)])

MERKLE_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(MERKLE_BONE_address)])

xshib_MERKLE_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(xshib_MERKLE_BONE_address)])

xleash_MERKLE_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(xleash_MERKLE_BONE_address)])

tbone_MERKLE_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(tbone_MERKLE_BONE_address)])

MEXC_3_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(MEXC_3_BONE_address)])

MEXC_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(MEXC_BONE_address)])

HOTBIT_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(HOTBIT_BONE_address)])

burnt_BONE_balance = (balance_FLOAT[my_ADDRESSES.index(burnt_BONE_address)])

# maximum dikuted supply of $BONE is 250 million tokens 
DS = (round(250000000/1000000,2))

print('For those who are not in #💬│bone, here are some supply facts for you.') 
print('As of ' + now + ' (Block #: ' + str(block) + ')' + ', looking at the various $BONE (BONE SHIBASWAP) supply metrics:') 
