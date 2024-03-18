-- select db
USE hbtn_0c_0;

-- convert db to utf8mb4_unicode_ci
ALTER TABLE `first_table` CONVERT TO CHARACTER
SET
    utf8mb4 COLLATE utf8mb4_unicode_ci;
