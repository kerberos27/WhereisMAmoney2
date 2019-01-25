from setupWeb3 import w3
from textdispatcher import text
import config

# Owner of smart contracts
owner = config.owner

# Validator can set permissions on Regulator
validator = config.validator

# Minter can mint new CUSD
minter = validator

# Return 1 if balance has increased, -1 if decreased, 0 if unchanged
def getBalance(address):
	latestBlock = w3.eth.blockNumber
	try:
		oldBalance = w3.fromWei(w3.eth.getBalance(address, block_identifier=latestBlock-1), 'ether')
	except:
		print('ERROR reading oldBalance')
		return
	try:
		newBalance = w3.fromWei(w3.eth.getBalance(address), 'ether')
	except:
		print('ERROR reading newBalance')
		return

	if newBalance < oldBalance:
		result = ({'delta':-1, 'new': newBalance, 'old': oldBalance})
		return result
	elif newBalance > oldBalance:
		result = ({'delta': 1, 'new': newBalance, 'old': oldBalance})
		return result
	else:
		result = ({'delta': 0, 'new': newBalance, 'old': oldBalance})
		return result


# Text recipients if owner balance has changed
def textBalanceOwner(recipients):
	deltaBalance = getBalance(owner)
	if deltaBalance is None:
		return
	latestBlock = w3.eth.blockNumber
	blockNumber = str('Block number: {}'.format(latestBlock))
	if deltaBalance['delta'] == 1:
		latestBlock = w3.eth.blockNumber
		ownerBalance = str("balance now {} ETH, old balance was {}\n".format(deltaBalance['new'], deltaBalance['old']))
		text('Owner ETH balance increased\n' + ownerBalance + blockNumber, recipients)
	elif deltaBalance['delta'] == -1:
		latestBlock = w3.eth.blockNumber
		ownerBalance = str("balance now {} ETH, old balance was {}\n".format(deltaBalance['new'], deltaBalance['old']))
		text('Owner ETH balance decreased' + ownerBalance + blockNumber, recipients)
	else:
		print('Owner ETH balance unchanged' + blockNumber)

# Text recipients if validator balance has changed
def textBalanceValidator(recipients):
	deltaBalance = getBalance(validator)
	if deltaBalance is None:
		return
	latestBlock = w3.eth.blockNumber
	blockNumber = str('Block number: {}'.format(latestBlock))
	if deltaBalance['delta'] == 1:
		latestBlock = w3.eth.blockNumber
		ownerBalance = str("balance now {} ETH, old balance was {}\n".format(deltaBalance['new'], deltaBalance['old']))
		text('Validator&Minter ETH balance increased\n' + ownerBalance + blockNumber, recipients)
	elif deltaBalance['delta'] == -1:
		latestBlock = w3.eth.blockNumber
		ownerBalance = str("balance now {} ETH, old balance was {}\n".format(deltaBalance['new'], deltaBalance['old']))
		text('Validator&Minter ETH balance decreased' + ownerBalance + blockNumber, recipients)
	else:
		print('Validator&Minter ETH balance unchanged' + blockNumber)

