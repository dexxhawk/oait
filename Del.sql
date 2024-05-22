
DELETE FROM Analytics WHERE TRUE;
DELETE FROM Metadata WHERE TRUE;
DELETE FROM Video WHERE TRUE;
DELETE FROM "User" WHERE TRUE;
DELETE FROM Playlist WHERE TRUE;
DELETE FROM "Comment" WHERE TRUE;
DELETE FROM Genre WHERE TRUE;

DELETE FROM user_comment WHERE TRUE;
DELETE FROM user_playlist WHERE TRUE;
DELETE FROM user_video WHERE TRUE;
DELETE FROM video_comment WHERE TRUE;
DELETE FROM video_genre WHERE TRUE;
DELETE FROM video_playlist WHERE TRUE;

ALTER SEQUENCE analytics_analytics_id_seq RESTART WITH 1;
ALTER SEQUENCE metadata_metadata_id_seq RESTART WITH 1;
ALTER SEQUENCE video_video_id_seq RESTART WITH 1;
ALTER SEQUENCE "User_user_id_seq" RESTART WITH 1;
ALTER SEQUENCE playlist_playlist_id_seq RESTART WITH 1;
ALTER SEQUENCE "Comment_comment_id_seq" RESTART WITH 1;
ALTER SEQUENCE genre_genre_id_seq RESTART WITH 1;

ALTER SEQUENCE user_comment_user_comment_id_seq RESTART WITH 1;
ALTER SEQUENCE user_playlist_user_playlist_id_seq RESTART WITH 1;
ALTER SEQUENCE user_video_user_video_id_seq RESTART WITH 1;
ALTER SEQUENCE video_comment_video_comment_id_seq RESTART WITH 1;
ALTER SEQUENCE video_genre_video_genre_id_seq RESTART WITH 1;
ALTER SEQUENCE video_playlist_video_playlist_id_seq RESTART WITH 1;