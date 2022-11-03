--Part 1
--1
/*
CREATE TABLE purchases(
	purchases_id SERIAL PRIMARY KEY NOT NULL,
	customer_id INTEGER NOT NULL,
	items_id INTEGER NOT NULL,
	quantiy_purchased INTEGER NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customers(id),
	FOREIGN KEY (items_id) REFERENCES items(id)
);*/
/*
INSERT INTO purchases(customer_id, items_id, quantity_purchased)
VALUES (
(SELECT id FROM customers WHERE last_name='Scott' AND first_name='Scott'),
(SELECT id FROM items WHERE item_name='Fan'),1
);*/
/*
INSERT INTO purchases(customer_id, items_id, quantity_purchased)
VALUES (
	(SELECT id FROM customers WHERE last_name='Johnson' AND first_name='Melanie'),
	(SELECT id FROM items WHERE item_name='Large Desk'),10
);*/
/*
INSERT INTO purchases(customer_id, items_id, quantity_purchased)
VALUES (
	(SELECT id FROM customers WHERE last_name='Jones' AND first_name='Greg'),
	(SELECT id FROM items WHERE item_name='Small Desk'),2
);*/

--Part 2
--1.
--1.1
SELECT * FROM purchases;

--1.2
SELECT * FROM purchases pu INNER JOIN customers cu ON pu.items_id = cu.id;

--1.3
SELECT * FROM purchases  WHERE customer_id=5;

--1.4
SELECT * FROM purchases pu INNER JOIN items i ON pu.items_id=i.id WHERE i.item_name IN ('Large Desk', 'Small Desk') ;

--2
SELECT cu.first_name,cu.last_name, i.item_name FROM customers cu INNER JOIN purchases pu ON cu.id=pu.customer_id  INNER JOIN items i ON pu.items_id=i.id;

--3
INSERT INTO purchases(customer_id,quantity_purchased) VALUES((SELECT id FROM customers WHERE last_name='Jones' AND first_name='Sandra'),2);
-- sa ne marche pas parce qu'il y a une valeur null pour items_id. c'est comme s'il à payer 2 fois une choses qu'on ne connait pas.

