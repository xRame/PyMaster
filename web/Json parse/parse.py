import json
import jsonf

def del_elem(key):
	data.pop(key)

def check_type(key):
	if issubclass(list, type(data[key])):
		print("list: ", key)
		size_list(data[key])
		pass
	elif issubclass(tuple, type(data[key])): 	
		print("tuple: ", key)
		pass
	elif issubclass(dict, type(data[key])): 	
		print("dict: ", key)
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

def empty_dict(key):
	print
	if len(data[key].keys()) == 0:
		return False

def size_list(l):
	print('size: ',len(l))
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
	check_type(key)
	#print(key, ' ',data[key], end = '\n\n')