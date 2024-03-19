-- create db
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- GRANT select privilege 
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
