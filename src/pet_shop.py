# WRITE YOUR FUNCTIONS HERE

# Make a function that return the pet shop name.
def get_pet_shop_name(pet_shop):
  return pet_shop['name']

# get the total cash
def get_total_cash(pet_shop):
  return pet_shop['admin']['total_cash']

# Add to the dict
def add_or_remove_cash(pet_shop, add):
  pet_shop['admin']['total_cash'] += add
  return pet_shop['admin']['total_cash']

# get the pets that have been sold
def get_pets_sold(pet_shop):
  return pet_shop['admin']['pets_sold']

# increase the amount of sold pets
def increase_pets_sold(pet_shop, add):
  pet_shop['admin']['pets_sold'] += add
  return pet_shop['admin']['pets_sold']

# Find out all the stock
def get_stock_count(pet_shop):
  return len(pet_shop['pets'])

# Get the pet breed
def get_pets_by_breed(pet_shop, breed):
    pet_search = []
    for pet in pet_shop['pets']:
        if pet['breed'] == breed:
            pet_search.append(pet)
    return pet_search

# Find by the pet name
def find_pet_by_name(pet_shop, name):
  for pet in pet_shop["pets"]:
    if pet["name"] == name:
      return pet
  return None

# Remove the name entered 
def remove_pet_by_name(pet_shop, name):
  pet_remove = find_pet_by_name(pet_shop, name)
  pet_shop["pets"].remove(pet_remove)

# # Add a pet to the dict
def add_pet_to_stock(pet_shop, new_pet):
  pet_shop["pets"].append(new_pet)
  return get_stock_count(pet_shop)

# Get the customer cash
def get_customer_cash(customer):
  return customer["cash"]

# Now let's take the customer cash
def remove_customer_cash(customer, remove):
  customer["cash"] -= remove
  return customer["cash"]

# Find out how many pets they have
def get_customer_pet_count(customer):
  pets = customer["pets"]
  return len(pets)

# Now let's add a pet
def add_pet_to_customer(customer, name):
  customer["pets"].append(name)
  return get_customer_pet_count(customer)
  
# ------------------------------------------------------------
#                      OPTIONAL 
# Make a function that checks if they can afford the pet
def customer_can_afford_pet(customer, pet_shop):
  if customer["cash"] >= pet_shop["price"]:
    return True
  else:
    return False

#-------------------------------------------------------------

#                      OPTIONAL 

def sell_pet_to_customer(pet_shop, name, customer):
  """Find the pet, Sell the pet, Get the cash, Get the total cash"""
  # Is if the name is in the pet_shop
  if name in pet_shop["pets"]:
    can_buy = customer_can_afford_pet(customer, name)

    # If they can afford it run this: 
    if can_buy == True:
      pet_shop["pets"].remove(name)

      # Add to the customer list
      customer["pets"].append(name)

      # Add sold to the admin list
      pet_shop["admin"]["pets_sold"] += 1

      # Add the cost to the total admin cash 
      pet_shop["admin"]["total_cash"] += name["price"]

      # Take it away from the customers cash 
      customer["cash"] -= name["price"]
    else:
      return "You can't but this"

# If we don't have the pet(name)
  else:
    return "We don't have this pet"




