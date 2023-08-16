-- lists all cities contained in the database hbtn_0d_usa
-- Use inner loop
-- Each record displays: cities.id - cities.name - states.name
SELECT a.id AS id, a.name AS name, b.name AS name
FROM cities a
INNER JOIN states b ON a.state_id = b.id
ORDER BY a.id ASC;
