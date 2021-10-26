from agtuary import Agtuary

user = "test@agtuary.com"
psk = "supersecrete123"
at = Agtuary(email=user, password=psk)

print(at.periods)
print(at.subtypes)
