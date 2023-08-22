-- list all cities of the database.
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name 
FROM cities
JOIN states ON cities.states_id = states.id
ORDER BY cities.id ASC;
