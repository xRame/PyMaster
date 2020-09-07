import time

class Messenger:
	db = []
	requested_count = 0

	def send_message(self, user, text):
		timestamp = time.asctime()
		self.db.append({
			'user': user,
			'text': text,
			'timestamp': timestamp
			})
		
	def get_messages(self):
		return self.db	

	def get_new_messages(self):
		new_messages = self.db[self.requested_count:]
		self.requested_count += len(new_messages)
		return self.db		

msg = Messenger()	
msg.send_message({'name':'Nikita','soname':'Dimitiriev'},'hello')
print('all: ', msg.get_messages())
msg.send_message({'name':'Nikita','soname':'Dimitiriev'},'hello1')
msg.send_message({'name':'Nikita','soname':'Dimitiriev'},'hello2')
print('new: ',msg.get_new_messages())		
