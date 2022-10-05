-- Daily challenge
/*
CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);


SELECT * FROM SecondTab
*/

--1 ça ne va rien afficher car Null n'est pas une valeur
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );

--2 ça fait le compt de tout ce qui est dans le premier tableau et qui a un id différent de 5 donc ca donne 2. Car le Null n'est pas une valeur.
    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
--3 ça affiche le totale de ce qui n'a pas le même id du second tableau
	SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
--4 ça selection le id 5 dans le second tableau et regarde si les id du premier tableau sont identique, il ne les copies pas. ça donne 10 


