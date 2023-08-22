-- lists genres and numbers of shows..
SELECT tv_genres.name AS genre, COUNT(tv_show_geners.genre_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
GROUP BY tv_show_geners.genre_id 
ORDER BY number_of_shows DESC;
