-- Lists all genres of the show Dexter.
SELECT tv_genres.name AS name
FROM tv_genres
INNER JOIN tv_shows ON tv_genres.id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;
