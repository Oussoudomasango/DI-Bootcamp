-- Daily challenge Part 2
/*
--1
CREATE TABLE Book(
	book_id SERIAL PRIMARY KEY,
	title VARCHAR (50) NOT NULL,
	author VARCHAR (50) NOT NULL
);
--2
INSERT INTO Book(title,author)
VALUES ('Alice In Wonderland', 'Lewis Carroll'),
	   ('Harry Potter','J.K Rowling'),
	   ('To kill a mockingbird','Harper Lee');
--3
CREATE TABLE Student(
	student_id SERIAL PRIMARY KEY,
	name VARCHAR (50) NOT NULL UNIQUE,
	age INTEGER,
	CHECK(age<=15)
);
--4
INSERT INTO Student (name,age)
VALUES ('John',12),
	   ('Layer',11),
	   ('Patrick',10),
	   ('Bob',14);
--5
CREATE TABLE Library(
	book_id INTEGER NOT NULL,
	student_id INTEGER NOT NULL,
	PRIMARY KEY (book_id,student_id),
	FOREIGN KEY (book_id) REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
	borrowed_date DATE
);	 */  
--6
/*
INSERT INTO Library (book_id,student_id,borrowed_date)
VALUES 
	--(
	--(SELECT book_id FROM Book WHERE title='Alice In Wonderland' AND author='Lewis Carroll' ),
	--(SELECT student_id FROM student WHERE name = 'John'),
	--'15/02/2022'
	--),
	(
	(select book_id from Book where title='To kill a mockingbird'),
	  (select student_id from student where name='Bob'),
	  '03/03/2021'
	),	  
	(
	(select book_id from Book where title='Alice In Wonderland'),
	  (select student_id from student where name='Layer'),
	  '23/05/2021'
	),
	(
		  (select book_id from Book where title='Harry Potter'),
	  (select student_id from student where name='Bob'),
	  '12/08/2021'
	);
*/
--7
select * from library;
--
select s.name,b.title from Student s
join Library l on s.student_id=l.student_id
join Book b on l.book_id=b.book_id;
--
select s.age from Student s
join Library l on s.student_id=l.student_id
join Book b on l.book_id=b.book_id
where b.title='Alice In Wonderland';
--
delete from student where student.name='Layer';
