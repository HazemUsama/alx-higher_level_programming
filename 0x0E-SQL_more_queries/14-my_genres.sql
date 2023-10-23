-- lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genres_id
WHERE tv_show_genres.name = "Dexter"
