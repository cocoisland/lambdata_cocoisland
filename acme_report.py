import random
from acme import Product

prodlist=[]

def generate_products():
   adjective=['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
   noun=['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
   total_prod = random.randint(3,10)
   for _ in range(total_prod):
      new_name = random.choice(adjective) + ' ' + random.choice(noun)
      new_prod = Product(new_name).name
      #new_prod.set_price = random.randint(5,100)
      #new_prod.set_weight = random.randint(5,100)
      prodlist.append(new_prod)

def inventory_report():
   print('New Product list:\n'+ str(prodlist))
   

if __name__ == '__main__':
   generate_products()
   inventory_report()


