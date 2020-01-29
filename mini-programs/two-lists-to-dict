column_names = ['id', 'color', 'style']
column_values = [1, 'red', 'bold']

# 1. Convert two lists into a dictionary with zip and the dict constructor
name_to_value_dict = dict(zip(column_names, column_values))

# 2. Convert two lists into a dictionary with a dictionary comprehension
name_to_value_dict = {key:value for key, value in zip(column_names, column_values)}

# 3. Convert two lists into a dictionary with a loop
name_value_zip = zip(column_names, column_values)
name_to_value_dict = {}
for key, value in name_value_zip: 
  if key in name_to_value_dict: 
    pass # Insert logic for handling duplicate keys 
  else: 
    name_to_value_dict[key] = value

print(name_to_value_dict)

