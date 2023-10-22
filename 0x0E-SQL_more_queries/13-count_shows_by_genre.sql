--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS `genre`, COUNT(tv_shows_genres.genre_id) AS `number_of_shows`
FROM tv_genres RIGHT JOIN tv_shows_genres
ON tv_genres.id = tv_shows_genres.genre_id
GROUP BY genre
ORDER By number_of_shows DESC;
