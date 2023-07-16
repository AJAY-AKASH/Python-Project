--Create the customer table--
create table IF NOT EXISTS customer (
cus_id int primary key, name varchar(20),age int, gender varchar(2),journey_date date,
	arrival_place varchar(20),depature_place varchar(20),phone int);

--Insert the values in customer table--
insert into customer values
(1,'Ajay',23,'M','2023-06-22','Chennai','Trichy',9361295),
(2,'Akash',23,'M','2023-07-23','kanjipuram','Trichy',9361775),
(3,'Gifty',22,'F','2023-06-22','Chennai','Trichy',8471295),
(4,'Aparna',21,'F','2023-07-23','perampalur','Madurai',98737495);

--View the Customer Table--
select * from customer;

--Create Bus_Booking Table--

create table if not exists bus_booking(
book_id int primary key,cus_id int,arival_time time NOT NULL,depature_time time NOT NULL,
foreign key(cus_id) references customer(cus_id)on delete cascade);


--Insert the values in Booking--
insert into bus_booking values
(501,1,'06:50','11:00'),
(502,2,'04:30','09:00'),
(503,3,'03:00','08:00'),
(504,4,'04:00','07:30');

--view the Bus_booking table--

select * from bus_booking;

--Create Bus Table--
create table if not exists bus(
book_id int,bus_number int primary key,food varchar(10),
foreign key(book_id) references bus_booking(book_id)on delete cascade);

--Insert values in Bus Table--
insert into bus values
(501,1234,'yes'),
(502,2345,'No'),
(503,1237,'NO'),
(504,2348,'YES');

--Select the values from Bus--
select * from bus;

--create the Invoice Table--

create table if not exists invoice(
invoice_id int,book_id int,bus_number int,total_amount int,
payment_status varchar(10),journey_date date,
foreign key(bus_number)references bus(bus_number)on delete cascade);

--Insert values to Invoice--

insert into invoice values
(3456,501,1234,450,'complete','2023-06-22'),
(3445,502,2345,600,'Complete','2023-07-23'),
(3654,503,1234,450,'Complete','2023-06-22'),
(3245,504,2345,600,'Pending','2023-07-23');

--select the values from invoice--

select * from invoice;

--Alter the invoice table --

alter table invoice rename column bus_number to bus_no;