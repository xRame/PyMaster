import requests

def get_token(msg):
	token = msg.text.split('\n')[-1].split(' ')[-1]
	# print('TOKEN: ',token)
	# print(msg.content)
	return {'token': token}

def start():
	auth = {'Authorization': 'Bearer a9811ec669145955881bc4d773673ea52a35d0b49936e29a2a32acc5f99f8ba6'}
	url_start = 'https://validator-2020.awesomestuff.in/race/start'
	url_move = 'https://validator-2020.awesomestuff.in/race/action/move'
	url_overcharge = 'https://validator-2020.awesomestuff.in/race/action/overcharge'
	url_recharge = 'https://validator-2020.awesomestuff.in/race/action/recharge'
	url_slow = 'https://validator-2020.awesomestuff.in/race/action/slow'
	url_none = 'https://validator-2020.awesomestuff.in/race/action/none'
	speed = 62
	speedd = 62
	energy = 492
	car = 80
	boat = 71
	move_cost = 54
	charge = 112
	charge_lastas = 8
	recharge = 25
	recharge_restores = 317
	slow = 49
	slow_lasts = 9
	energy_total = 0
	finish = 937
	charge_now = 0
	slow_now = 0
	turns = 1

	start_info = requests.get(url_start, headers = auth)
	token = get_token(start_info)
	print(start_info.text)

	r = requests.post(url_recharge,headers=auth, data = 'd9bbd5038d39c8c55e05ce214d95cbd')
	print(r.text)

	def race(do,token):
		# print('action: ',do, ' token: ', token)
		r = requests.post(do,headers=auth, data = token)
		print(r.text)
		return get_token(r)

	# token = race(url_slow, token)
	# energy-=slow
	# energy_total+=slow

	# for i in range(10):
	# 	token = race(url_move, token)

	turns = 0

	while finish > 0:
		print('Turn: ',turns)
		if charge_now <= 0 and energy >= charge+recharge and finish - speedd*4 > 0:
			token = race(url_overcharge, token)
			
			charge_now = charge_lastas
			energy-=charge
			energy_total+=charge
			turns+=1
			speed*=2
			#print('chargig: ',charge_now, ', road: ', finish,', energy: ',energy ,',turns: ', turns,', total nrg: ',energy_total)
			continue
		else:
			charge_now-=1
		if charge_now <= 0:
			charge_now=0
			speed = 62
		if (energy-move_cost>recharge) or (energy>move_cost and finish-speed < 0 ):
			token = race(url_move, token)
			energy-=move_cost
			finish-=speed
			energy_total+=move_cost
			turns+=1
			print('chargig: ',charge_now, ', road: ', finish,', energy: ',energy ,',turns: ', turns,', total nrg: ',energy_total)
			continue
		print('RECHARGE')
		token = race(url_recharge, token)
		energy_total+=recharge
		energy+=recharge_restores
		token = race(url_none, token)

		# token = race(url_slow, token)
		# energy-=slow
		# energy_total+=slow

		token = race(url_overcharge, token)
		energy-=charge
		energy_total+=charge
		speed*=1.5
		charge_now=8
		turns+=1	

	print('total nrg: ',energy_total)
	print('me: ',turns)		

# auth = {'Authorization': 'Bearer a9811ec669145955881bc4d773673ea52a35d0b49936e29a2a32acc5f99f8ba6'}
# r = requests.get( 'https://validator-2020.awesomestuff.in/race/state?token=260effe0ccdd37df29a9a3bdff6957db' ,headers=auth)	
# r = requests.post('https://validator-2020.awesomestuff.in/race/action/move', headers=auth, data = {'token': '756ff316aaf2382874e4163829961183'})
# print(r.text)
# r = requests.post('https://validator-2020.awesomestuff.in/race/action/move', headers=auth, data = {'token': '57ce1dafb9179dbf2176bf8e8cb95e4d'})
# print(r.text)
# r = requests.post('https://validator-2020.awesomestuff.in/race/action/move', headers=auth, data = {'token': 'fce3645e9d04f7faf21f4750da2a81c0'})
# print(r.text)
start()

