import json

def del_elem(fromd, key):
	fromd.pop(key)

def check_type(data, key):
	if issubclass(list, type(data[key])):
		print("list: ", key)
		size_list(data, key, data[key])
		pass
	elif issubclass(tuple, type(data[key])): 	
		print("tuple: ", key)
		pass
	elif issubclass(dict, type(data[key])): 	
		print("dict: ", key)
		size_dict(data, key)
		pass
	elif issubclass(bool, type(data[key])): 	
		print("bool: ", key)
	elif issubclass(int, type(data[key])): 	
		print("int: ", key)
	elif issubclass(str, type(data[key])): 	
		print("str: ", key,'size',len(data[key]))
	elif issubclass(float, type(data[key])): 	
		print("float: ", key)					
		pass	

def size_dict(data, keym):
	print('\n\n',keym)
	print('size: ', len(data[keym].keys()))
	if len(data[keym].keys()) == 0:
		return False
	else:
		print(data[keym].keys())
		for key in data[keym].keys():
			#print(key)
			check_type(data[keym], key)


def size_list(data, key, l):
	print('size: ',len(l))
	if len(l) == 0:
		return False
	if len(l)==1:
		 data[key]=l[0]
		print('!!!',key,' was replaced ')
			

def size_tuple(t):
	print('size: ',len(t))
	if len(l) == 0:
		return False

with open('data.json', 'r') as data_file:
    data = json.load(data_file)
keys = data.keys()
newd = {"tesas1t": "1"}
newd.update({"tesast": "2"})
print(issubclass(list, type(data["test"])))
print(len(data.keys()))

for key in data.keys():
	check_type(data, key)
	#print(key, ' ',data[key], end = '\n\n')
for key in data.keys():
	check_type(data, key)	