-- list all the cities of state California.
SELECT id, name FROM cities
WHERE state_id IN (
    SELECT id FROM states 
    WHERE name = 'California'
)
ORDER BY cities.id ASC;