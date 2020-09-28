import json
import numbers

def collect_nested_dicts(json_dict):
  occurrence_dict = []

  def find_nested_dicts(json_element):
      hasDictInside = False
      if type(json_element) is dict:
        for inner_element in json_element:
          # Look at every object in dictionary. If it is a nested dict find nested dicts inside it
          if (type(json_element[inner_element]) is dict):
            hasDictInside = True
            find_nested_dicts(json_element[inner_element])
        # If object is dict but doesn't have dicts inside we should still add it
        if (hasDictInside == False):
          occurrence_dict.append(json_element)

  def remove_unique_values(data):
    for index in range(len(data) - 1, -1, -1):
        if data.count(data[index]) == 1:
            del data[index]
    return data

  def remove_duplicated_values(data):
    data_without_duplicates = []
    for dict_ in data:
      if dict_ not in data_without_duplicates:
        data_without_duplicates.append(dict_)
    return data_without_duplicates

  find_nested_dicts(json_dict)

  # Find all nested dict and then leave only those which were found several times
  return remove_duplicated_values(remove_unique_values(occurrence_dict))

# Replace nested dict with it's id
def update_json(json_dict, key, new_value):
  for inner_element in json_dict:
    if (type(json_dict[inner_element]) is dict):
      update_json(json_dict[inner_element], key, new_value)
    if (inner_element == key):
      json_dict[inner_element] = new_value

def create_json_without_nested_dicts(json_dict, nested_dicts):
  replaced_json = {}

  def replace_nested_dicts(json_dict, recursion=False):
    if type(json_dict) is dict:
      # Look at every object in dictionary
        for inner_element in json_dict:
          if (recursion == False):
            replaced_json[inner_element] = json_dict[inner_element]
          # If inner object is dictionary and it's in list with nested dicts replace it with id
          if (type(json_dict[inner_element]) is dict):
            if (json_dict[inner_element] in nested_dicts):
              update_json(replaced_json, inner_element, json_dict[inner_element]["id"])
            # If dict is not nested look at it further. Maybe it has nested dicts inside
            else:
              replace_nested_dicts(json_dict[inner_element], recursion=True)

  replace_nested_dicts(json_dict)
  return replaced_json

def optimize_json(json_dict):
  external_data = []
  # Save nested dicts in order to write them in external table later
  nested_dicts = collect_nested_dicts(json_dict=json_dict)
  for nested_dict in nested_dicts:
    external_data.append(nested_dict)
  optimized_json = create_json_without_nested_dicts(json_dict, nested_dicts)
  # While data has nested dicts we should optimize it
  while (nested_dicts):
    nested_dicts = collect_nested_dicts(json_dict=optimized_json)
    if (nested_dicts):
      for nested_dict in nested_dicts:
        external_data.append(nested_dict)
    optimized_json = create_json_without_nested_dicts(optimized_json, nested_dicts)
  return optimized_json, external_data

def get_memory_usage(data):
  bool_cost = 32
  character_cost = 16
  number_cost = 64
  object_padding = 64
  object_entry_padding = 32

  def calculate_memory_usage(json_dict, memory_usage):
    if type(json_dict) is dict:
      memory_usage += object_padding
      for inner_element in json_dict:
        # Calculate entry size like padding and key size and then add value size
        memory_usage = memory_usage + object_entry_padding + len(inner_element) * character_cost
        memory_usage = calculate_memory_usage(json_dict[inner_element], memory_usage)
    if type(json_dict) is list and (len(json_dict) != 0):
      memory_usage += object_padding
      for inner_element in json_dict:
        memory_usage = calculate_memory_usage(inner_element, memory_usage)
    # Boolen is considered as instance of numbers.Number so check for not being bool
    if isinstance(json_dict, numbers.Number) and type(json_dict) is not bool:
      memory_usage += number_cost
    if type(json_dict) is str:
      memory_usage = memory_usage + len(json_dict) * character_cost
    if type(json_dict) is bool:
      memory_usage += bool_cost
    return memory_usage
          
  memory_usage = calculate_memory_usage(data, 0)
  return memory_usage / 8

with open('data.json') as json_file:
    data = json.load(json_file)

before_optimization = get_memory_usage(data)
print(before_optimization)

results = optimize_json(data)

after_optimization = get_memory_usage(results[0])
print(after_optimization)

external_memory = get_memory_usage(results[1])
print(external_memory)

print("Memory gain", before_optimization - (after_optimization + external_memory))

with open('external.json', 'w') as external_data_file:
    json.dump(results[1], external_data_file)

with open('new_data.json', 'w') as external_data_file:
    json.dump(results[0], external_data_file)