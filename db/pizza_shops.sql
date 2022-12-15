DROP TABLE IF EXISTS pizza;
DROP TABLE IF EXISTS pizza_shop;

CREATE TABLE pizza_shop(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE pizza(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    toppings VARCHAR(255),
    spice_lvl VARCHAR(255),
    pizza_shop_id INT NOT NULL REFERENCES pizza_shop(id)
);
