from internetspeedtwitterbot import InternetSpeedTwitterBot

PROMISED_DOWN = 100
PROMISED_UP  = 30

pilot = InternetSpeedTwitterBot()

print(pilot.receiving, pilot.sending)
pilot.get_internet_speed()
print(pilot.receiving, pilot.sending)

text = f"down = {PROMISED_DOWN}, up = {PROMISED_UP} \n receiving = {pilot.receiving}, sending = {pilot.sending}"
pilot.tweet_at_provider(text)

