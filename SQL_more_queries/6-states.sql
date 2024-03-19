-- crteate database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- select database
USE hbtn_0d_usa;

-- create table
CREATE TABLE
    IF NOT EXISTS states (
        id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL
    );
