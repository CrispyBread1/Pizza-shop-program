DROP TABLE IF EXISTS pizzas;
DROP TABLE IF EXISTS pizza_shops;

CREATE TABLE pizza_shops(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE pizzas(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    toppings VARCHAR(255),
    spice_lvl VARCHAR(255),
    pizza_shop_id INT NOT NULL REFERENCES pizza_shops(id)
);
