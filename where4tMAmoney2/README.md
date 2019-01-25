# watchtower
Script to watch ETH addresses for balance changes and abnormal activity

## Contracts: currently disabled because filtering for contract events is not possible when connecting to web3 through Infura
This module can track events of deployed contracts from the `fiat_gateway` repo. To do so, the contract ABI's in `./contracts/` must match the deployed contract ABI's

## Deployment
Currently, I am running this script as a scheduled 'one-off' worker on [Heroku](https://devcenter.heroku.com/articles/scheduler). 

## Requirements
- dotenv file stores global API keys and ETH addresses to track
- whitelist.py stores relevant phone numbers
- Heroku for deployment
- Twilio for an easy way to text numbers programmatically