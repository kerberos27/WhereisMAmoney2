from getBalance import textBalanceOwner, textBalanceValidator
import whitelist
import time

def loop_main(poll_interval):
	# Who will receive the alerts
	recipients = [whitelist.KERBEROS]
	while True:
		textBalanceOwner(recipients)
		textBalanceValidator(recipients)
		time.sleep(poll_interval)

def main():
	loop_main(2)

main()
