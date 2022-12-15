from flask import render_template, Blueprint, redirect, request
from models.pizza_shop import Pizza_shop
from repositories import pizza_repository
from repositories import pizza_shop_repository
# from models.pizza import pizza

pizza_shop_blueprint = Blueprint("pizza_shop", __name__)

@pizza_shop_blueprint.route("/pizza")
def index():
    pizzas = pizza_repository.select_all()
    return render_template("pizza/index.html", all_pizzas = pizzas)

