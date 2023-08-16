-- Use RIGHT JOIN
SELECT a.title, b.genre_id 
FROM tv_show_genres b 
RIGHT JOIN tv_shows a 
ON b.show_id = a.id
WHERE b.show_id IS NULL
ORDER BY a.title, b.genre_id ASC;
