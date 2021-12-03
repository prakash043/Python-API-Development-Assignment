CREATE DATABASE IF NOT EXISTS books_data;
USE books_data;
CREATE TABLE book (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    isbn varchar(50) NOT NULL,
    authors varchar(255) NOT NULL,
    country varchar(80) NOT NULL,
    number_of_pages int NOT NULL,
    publisher varchar(255) NOT NULL,
    release_date datetime,
    PRIMARY KEY (id)
);

