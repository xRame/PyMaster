import requests

def get_token(msg):
	return {'token': msg.text.split('\n')[-1].split(' ')[-1]}

def start():
	auth = {'Authorization': 'Bearer a9811ec669145955881bc4d773673ea52a35d0b49936e29a2a32acc5f99f8ba6'}
	url_start = 'https://validator-2020.awesomestuff.in/race/start'
	url_move = 'https://validator-2020.awesomestuff.in/race/action/move'
	url_overcharge = 'https://validator-2020.awesomestuff.in/race/action/overcharge'
	url_recharge = 'https://validator-2020.awesomestuff.in/race/action/recharge'
	url_slow = 'https://validator-2020.awesomestuff.in/race/action/slow'
	start_info = requests.get(url_start, headers = auth)
	token = get_token(start_info)
	print(start_info.text)

	def race(do,token):
		r = requests.post(do,headers=auth, data = token)
		print(r.text)
		return get_token(r)


	for i in range(10):
		token = race(url_move, token)


start()

