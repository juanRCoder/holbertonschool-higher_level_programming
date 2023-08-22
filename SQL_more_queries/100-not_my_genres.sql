-- list all genres not linked to the show 'Dexter'.
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
	ON tvtv__show_genres.show_id = tv_shows.id
WHERE tv_genres.name NOT IN (
	SELECT tv_genres.name
	FROM tv_genres
	JOIN tv_show_genres
		ON tv_genres.id = tv_show_genres.genre_id
	JOIN tv_shows 
		ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_show.title = 'Dexter')
ORDER BY tv_gender.name ASC;
