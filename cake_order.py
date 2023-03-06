"""
My cake shop is so popular, I'm adding some tables and hiring wait staff so folks can have a cute sit-down cake-eating experience.

I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe.
All the customer orders get combined into one list for the kitchen, where they should be handled first-come, first-served.

Recently, some customers have been complaining that people who placed orders after them are getting their food first. Yikes—that's not good for business!

To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
Each customer order (from either register) as it was finished by the kitchen. (served_orders)
Given all three lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it.

We'll represent each customer order as a unique integer.

As an example,

  Take Out Orders: [1, 3, 5]
 Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 4, 6, 5, 3]
would not be first-come, first-served, since order 3 was requested before order 5 but order 5 was served first.

But,

  Take Out Orders: [17, 8, 24]
 Dine In Orders: [12, 19, 2]
  Served Orders: [17, 8, 12, 19, 24, 2]
would be first-come, first-served.

"""

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
  take_out_orders_index = 0
  dine_in_orders_index = 0
  take_out_orders_max_index = len(take_out_orders) - 1
  dine_in_orders_max_index = len(dine_in_orders) - 1

  for order in served_orders:
      # If we still have orders in take_out_orders
      # and the current order in take_out_orders is the same
      # as the current order in served_orders
      if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
          take_out_orders_index += 1

      # If we still have orders in dine_in_orders
      # and the current order in dine_in_orders is the same
      # as the current order in served_orders
      elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
          dine_in_orders_index += 1

      # If the current order in served_orders doesn't match the current
      # order in take_out_orders or dine_in_orders, then we're not serving first-come,
      # first-served.
      else:
          return False

  # Check for any extra orders at the end of take_out_orders or dine_in_orders
  if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
      return False

  # All orders in served_orders have been "accounted for"
  # so we're serving first-come, first-served!
  return True