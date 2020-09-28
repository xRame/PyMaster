import requests

def get_token(msg):
	return msg.text.split('\n')[-1].split(' ')[-1]

response = requests.get('https://validator-2020.awesomestuff.in/race/start', headers={'Authorization': 'Bearer a9811ec669145955881bc4d773673ea52a35d0b49936e29a2a32acc5f99f8ba6'})


r = requests.post('https://validator-2020.awesomestuff.in/race/action/overcharge',headers={'Authorization': 'Bearer a9811ec669145955881bc4d773673ea52a35d0b49936e29a2a32acc5f99f8ba6'}, data = {'token':'a6f3c47e47d8967dbf07ef0eb69bdd96'})

print(r.content)
r = requests.post('https://validator-2020.awesomestuff.in/race/action/move',headers={'Authorization': 'Bearer a9811ec669145955881bc4d773673ea52a35d0b49936e29a2a32acc5f99f8ba6'}, data = {'token':'a37bb404c4d207269bf4dab84ac28c9d'})
print(r.text.split('\n')[-1])
print(get_token(r))
response1 = requests.get('https://validator-2020.awesomestuff.in/race/state?token=a6f3c47e47d8967dbf07ef0eb69bdd96',headers={'Authorization': 'Bearer a9811ec669145955881bc4d773673ea52a35d0b49936e29a2a32acc5f99f8ba6'})
print(response.content)
print(response1.content)
