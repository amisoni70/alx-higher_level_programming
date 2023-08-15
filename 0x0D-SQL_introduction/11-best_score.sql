-- Lists all records of the second_table
-- Results display both the score & name
-- Records ordered in descending order
SELECT `score`, `name`
FROM `second_table` WHERE score >= 10
ORDER BY `score` DESC;
