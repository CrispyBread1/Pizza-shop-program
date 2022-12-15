import pdb
from models.pizza import Pizza
from models.pizza_shop import Pizza_shop

import repositories.pizza_repository as pizza_repository
import repositories.pizza_shop_repository as pizza_shop_repository

pizza_shop1 = Pizza_shop("You Want aPizza Me")
pizza_shop_repository.save(pizza_shop1)
pizza_shop2 = Pizza_shop("Pie Boy")
pizza_shop_repository.save(pizza_shop2)

pizza1 = Pizza("El Classico", "Pepperoni", pizza_shop1, "Burn your butt")
pizza_repository.save(pizza1)
pizza2 = Pizza("Hubba Bubba", "Hot Bacon",pizza_shop1, "Cunting Hot")
pizza_repository.save(pizza2)