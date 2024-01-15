-- create second table in database
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- insert values in table created
INSERT INTO second_table (id, name, score)
VALUES (1, 'Jhon', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);