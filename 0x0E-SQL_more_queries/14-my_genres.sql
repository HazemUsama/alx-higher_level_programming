-- lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres JOIN tv_show_genres
ON tv_genres.id = (
	SELECT id
	FROM tv_shows
	WHERE tv_shows.name = "Dexter"
)
