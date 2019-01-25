import os

## read Heroku config vars
INFURA_API_KEY_MAIN = os.environ.get("e2d1efdcbc6a4618a570a799e5447ec2")
#GMAIL = os.environ.get("kerberosjoo28@gmail.com")
#GMAIL_AUTH_TOKEN = os.environ.get("gmail_AUTH_TOKEN")
 
TWILIO_SID = os.environ.get("ACad5e5812c122746e66d7e60b5517f6d9")
TWILIO_AUTH_TOKEN = os.environ.get("639a482f6819450cf843396489ad18ee")

## user wallets to monitor

# Owner of smart contracts
owner = os.environ.get("0x1fC88dE3dC1C2ab4C73E2CF4A2e571cB6cEF4bd8")
# Validator can set permissions on Regulator
validator = os.environ.get("4162348351D75349EDBD8121DEB86C1F4A0B09C53D92F39D30B735163F09E70A")
