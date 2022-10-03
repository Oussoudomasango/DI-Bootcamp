/*
CREATE TABLE actors (
actor_id SERIAL PRIMARY KEY,
first_name VARCHAR (50) NOT NULL,
last_name VARCHAR (100) NOT NULL,
age DATE NOT NULL,
number_oscars SMALLINT NOT NULL
);*/

/*
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);
*/


-- femme integrer
/*
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Mikassa','Ackerman','12/05/1983', 7);
*//*
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Ten','Kario','02/03/2000', 6);*/
/*
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Madara','Utchiua', '13/07/1590',20),
	  ('Suichi','Utchiua', '14/09/1880',50),
	  ('Hachirama','Senju', '10/06/1590',15);*/
--1.
SELECT COUNT(first_name) FROM actors;

--2.
-- chaque champ à été mis non null. la symtaxe ne va pas passer
INSERT INTO actors (first_name,last_name,age,number_oscars)
VALUES ('Orochimaru','','17/05/1950', 5);
SELECT * FROM actors;

