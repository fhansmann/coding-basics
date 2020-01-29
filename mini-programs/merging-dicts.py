yusuke_power = {"Yusuke Urameshi": "Spirit Gun"}
hiei_power = {"Hiei": "Jagan Eye"}
powers = dict()

# Iteration
for dictionary in (yusuke_power, hiei_power): 
  for key, value in dictionary.items(): 
    powers[key] = value

# Dictionary Comprehension
powers = {key: value for d in (yusuke_power, hiei_power) for key, value in d.items()}

# Copy and update
powers = yusuke_power.copy()
powers.update(hiei_power)

# Dictionary unpacking
powers = {**yusuke_power, **hiei_power}

