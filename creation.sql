CREATE TABLE IF NOT EXISTS Analytics
(
	Analytics_id SERIAL PRIMARY KEY,
	Popularity INTEGER NOT NULL,
	Average_viewing_time NUMERIC NOT NULL,
	Percentage_of_views_without_comments NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS Metadata
(
	Metadata_id SERIAL PRIMARY KEY,
	Format VARCHAR(64) NOT NULL,
	Resolution VARCHAR(9) NOT NULL,
	Sampling_rate NUMERIC NOT NULL,
	Bitrate INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Video
(
	Video_id SERIAL PRIMARY KEY,
	Title VARCHAR(256) NOT NULL,
	Description VARCHAR(5000),
	Creation_date TIMESTAMP NOT NULL,
	Rating NUMERIC NOT NULL,
	Visibility_status INTEGER NOT NULL,
	Analytics_id INTEGER NOT NULL,
	Metadata_id INTEGER NOT NULL,
	FOREIGN KEY (Analytics_id) REFERENCES Analytics (Analytics_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (Metadata_id) REFERENCES Metadata (Metadata_id) ON UPDATE CASCADE ON DELETE CASCADE ,
	Duration NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS "User"
(
	User_id SERIAL PRIMARY KEY,
	ROLE INTEGER NOT NULL,
	Login VARCHAR(64) UNIQUE NOT NULL,
	"Password" VARCHAR(64) NOT NULL,
	Email VARCHAR(64) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Playlist
(
	Playlist_id SERIAL PRIMARY KEY,
	Title VARCHAR(64),
	Creation_date TIMESTAMP,
	Duration NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS "Comment"
(
	Comment_id SERIAL PRIMARY KEY,
	Text VARCHAR(1000),
	Creation_date TIMESTAMP
);

CREATE TABLE IF NOT EXISTS GENRE
(
	Genre_id SERIAL PRIMARY KEY,
	Title VARCHAR(64) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS User_Video 
(
	User_Video_id SERIAL PRIMARY KEY,
	User_id INTEGER NOT NULL,
	Video_id INTEGER NOT NULL,
	FOREIGN KEY (User_id) REFERENCES "User" (User_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (Video_id) REFERENCES Video (Video_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS User_Playlist 
(
	User_Playlist_id SERIAL PRIMARY KEY,
	User_id INTEGER NOT NULL,
	Playlist_id INTEGER NOT NULL,
	FOREIGN KEY (User_id) REFERENCES "User" (User_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (Playlist_id) REFERENCES Playlist (PLaylist_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Video_Genre
(
	Video_Genre_id SERIAL PRIMARY KEY,
	Video_id INTEGER NOT NULL,
	Genre_id INTEGER NOT NULL,
	FOREIGN KEY (Video_id) REFERENCES Video (Video_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (Genre_id) REFERENCES Genre (Genre_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Video_Playlist
(
	Video_Playlist_id SERIAL PRIMARY KEY,
	Video_id INTEGER NOT NULL,
	Playlist_id INTEGER NOT NULL,
	FOREIGN KEY (Video_id) REFERENCES Video (Video_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (Playlist_id) REFERENCES Playlist (PLaylist_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS User_Comment
(
	User_Comment_id SERIAL PRIMARY KEY,
	User_id INTEGER NOT NULL,
	Comment_id INTEGER NOT NULL,
	FOREIGN KEY (User_id) REFERENCES "User" (User_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (Comment_id) REFERENCES "Comment" (Comment_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Video_Comment
(
	Video_Comment_id SERIAL PRIMARY KEY,
	Video_id INTEGER NOT NULL,
	Comment_id INTEGER NOT NULL,
	FOREIGN KEY (Video_id) REFERENCES Video (Video_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (Comment_id) REFERENCES "Comment" (Comment_id) ON UPDATE CASCADE ON DELETE CASCADE
);

