weight = 1.5

# Ground Shipping

if weight <= 2:
  cost_price = weight * 1.5 + 20
elif weight <= 6:
  const_price = weight * 3 + 20
elif weight <= 10:
  cost_price = weight * 4 + 20
else:
  cost_price = weight * 4.75 + 20

print('Ground Shipping: $', cost_price)

# Ground Shipping Premium

const_premium = 125

print('Ground Shipping Premium: $', const_premium)

# Dron Shipping 

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print('Dron Shipping: $', cost_drone)