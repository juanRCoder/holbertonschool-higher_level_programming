-- lists all shows without the genre Comedy.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_show_genres.show_id 
    FROM tv_show_genres
    RIGHT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = "Comedy" 
)
GROUP BY tv_shows.title
ORDER BY tv_shows.title ASC;