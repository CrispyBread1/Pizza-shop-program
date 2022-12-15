from db.run_sql import run_sql

from models.pizza import Pizza
from models.pizza_shop import Pizza_shop

def save(pizza_shop):
    sql = "INSERT INTO pizza_shop (name) VALUES (%s) RETURNING *"
    values = [pizza_shop.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    pizza_shop.id = id
    return pizza_shop

def select_all():
    pizzas = []
    sql = "SELECT * FROM pizza"
    results = run_sql(sql)

    for row in results:
        pizza_shop = Pizza_shop(row['name'], row['id'])
        pizzas.append(pizza_shop)

    return pizzas

