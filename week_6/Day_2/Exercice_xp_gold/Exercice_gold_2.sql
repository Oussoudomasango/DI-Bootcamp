-- UPDATE
--1
UPDATE students SET birth_date='02/11/1998' WHERE first_name IN ('Marc','Lea') AND last_name='Benichou'; 
--2
UPDATE students SET last_name='Guez' WHERE first_name='David';
--DELETE
--3
DELETE FROM students WHERE last_name='Benichou' And first_name='Lea';
--COUNT
--1
SELECT count(first_name) FROM students;
--2
SELECT count(first_name) FROM students WHERE birth_date > '2000/01/01'; 
--INSERT/ALTER
--1
--ALTER TABLE students ADD COLUMN math_grade INTEGER;
--2
UPDATE students SET math_grade=80 WHERE id=1;
--3
UPDATE students SET math_grade=90 WHERE id IN (2,4);
--4 
UPDATE students SET math_grade=80 WHERE id=6;
--5
SELECT count(first_name) FROM students WHERE math_grade>83;
--6
--INSERT INTO students VALUES(8,'Omer', 'Simpson', (SELECT birth_date FROM students WHERE last_name='Simpson' AND first_name='Omer'),70);
--7 Bonus

--Sum
--1
SELECT sum(math_grade) FROM students;
--SELECT * FROM students;