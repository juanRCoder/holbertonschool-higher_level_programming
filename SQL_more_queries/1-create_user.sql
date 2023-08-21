-- Create user 'user_0d_1' in MySQL server.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Grant all privileges to user.
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
-- Change the user's password to 'user_0d_1_pwd'.
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
