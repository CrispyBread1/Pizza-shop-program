from db.run_sql import run_sql

from models.pizza import Pizza
from models.pizza_shop import Pizza_shop
import repositories.pizza_shop_repositorie as pizza_shop_repositorie

def save(pizza):
    sql = "INSERT INTO pizzas (name, toppings, pizza_shop_id, spice_lvl) VALUES(%s, %s, %s, %s) RETURN * "
    values = [pizza.name, pizza.toppings, pizza.pizza_shop.id, pizza.spice_lvl]
    results = run_sql(sql, values)
    id = results[0]['id']
    pizza.id = id
    return pizza

    