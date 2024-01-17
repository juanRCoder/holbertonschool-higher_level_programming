-- lists all shows from hbtn_0d_tvshows_rate.
SELECT tv_shows.title, COALESCE(SUM(tv_show_ratings.rate), 0) AS 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;