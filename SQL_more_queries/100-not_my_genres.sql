--  list all genres not linked to the show Dexter.
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
    SELECT tv_show_genres.genre_id 
    FROM tv_show_genres
    RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = "Dexter" 
)
GROUP BY tv_genres.name
ORDER BY tv_genres.name ASC;