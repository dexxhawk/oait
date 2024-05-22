import psycopg2
from config import host, user, password, db_name
import insertion

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host, user=user, password=password, database=db_name
    )
    connection.autocommit = True

    # insertion.analytics_insertion(connection, 50)
    # insertion.metadata_insertion(connection, 50)

    video_set = insertion.video_insertion(connection, 500)
    user_set = insertion.user_insertion(connection, 500 * 2)
    playlist_set = insertion.playlist_insertion(connection, 1250)
    comment_set = insertion.comment_insertion(connection, 1000)
    genre_qty = insertion.genre_insertion(connection, 15)
    insertion.uservideo_insertion(connection, 1000, user_set, video_set)
    insertion.usercomment_insertion(connection, 1000, user_set, comment_set)
    insertion.userplaylist_insertion(connection, 1250, user_set, playlist_set)
    insertion.videocomment_insertion(connection, 1000, video_set, comment_set)
    insertion.videogenre_insertion(connection, 1000, video_set, genre_qty)
    insertion.videoplaylist_insertion(
        connection, 2500, len(video_set), len(playlist_set)
    )


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
