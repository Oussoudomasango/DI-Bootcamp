-- Daily challenge partie 1
--1
/*
CREATE TABLE customer (
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL
);*/
/*
CREATE TABLE customer_profile (
	profile_id INTEGER NOT NULL,
	isLoggedIn BOOL DEFAULT FALSE,
	PRIMARY KEY (profile_id),
	CONSTRAINT customer_id FOREIGN KEY (profile_id) REFERENCES customer(customer_id)
);*/
--2
/*
INSERT INTO customer (first_name, last_name)
VALUES ('John','Doe'),
	   ('Jerome','Lalu'),
	   ('Lea','Rive');*/
--3
/*	   
INSERT INTO customer_profile(profile_id, isLoggedIn)
VALUES (1,TRUE),
	   (2,FALSE);*/
--4
SELECT first_name FROM customer c inner join customer_profile AS cp
ON c.customer_id=cp.profile_id;
SELECT c.first_name,cp.isLoggedIn FROM customer c LEFT OUTER JOIN customer_profile As cp
ON c.customer_id=cp.profile_id;
SELECT COUNT(*) FROM customer c INNER JOIN customer_profile AS cp
ON c.customer_id=cp.profile_id WHERE cp.isLoggedIn!=TRUE;

	   
	   
	   
	   
