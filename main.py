def pizza_price():


  requsted_toppings = input(""")

  requsted_toppings = requsted_toppings.upper()
  print(f"You requsted: {requsted_toppings}")

  base_price = 15
  toppings_price = 0
  calculated_toppings = []

  for topping in requsted_toppings:

  if topping in calculated_toppings:
      continue
