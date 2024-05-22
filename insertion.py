from data_generation import *

# def analytics_insertion(connection, qty=10):
#     with connection.cursor() as cursor:
#         for _ in range(qty):
#             inp = generate_analytics()
#             print(inp)
#             cursor.execute(
#                 f"INSERT INTO Analytics (Popularity, Average_viewing_time, Percentage_of_views_without_comments) "
#                 f"VALUES ({inp[0]}, {inp[1]}, {inp[2]})"
#             )
#         print("[INFO] Data was succefully inserted")

# def metadata_insertion(connection, qty=10):
#     with connection.cursor() as cursor:
#         for _ in range(qty):
#             inp = generate_metadata()
#             cursor.execute(
#                 f"INSERT INTO Metadata (Format, Resolution, Sampling_rate, Bitrate) "
#                 f"VALUES (\'{inp[0]}\', \'{inp[1]}\', {inp[2]}, {inp[3]})"
#             )
#         print("[INFO] Data was succefully inserted")


def video_insertion(connection, qty=10):
    with connection.cursor() as cursor:
        for i in range(qty):
            inp = generate_analytics()
            cursor.execute(
                f"INSERT INTO Analytics (Popularity, Average_viewing_time, Percentage_of_views_without_comments) "
                f"VALUES ({inp[0]}, {inp[1]}, {inp[2]})"
            )

            inp = generate_metadata()
            cursor.execute(
                f"INSERT INTO Metadata (Format, Resolution, Sampling_rate, Bitrate) "
                f"VALUES ('{inp[0]}', '{inp[1]}', {inp[2]}, {inp[3]})"
            )

            inp = generate_video()
            cursor.execute(
                f"INSERT INTO Video (Title, Description, Creation_date, Rating, Visibility_status, Analytics_id, Metadata_id, Duration) "
                f"VALUES ('{inp[0]}', '{inp[1]}', '{inp[2]}', {inp[3]}, {inp[4]}, {i + 1}, {i + 1}, {inp[7]})"
            )

        print("[INFO] Data was succefully inserted")
        return set(x + 1 for x in range(qty))


def user_insertion(connection, qty=10):
    with connection.cursor() as cursor:
        for _ in range(qty):
            inp = generate_user()
            cursor.execute(
                f'INSERT INTO "User" (Role, Login, "Password", Email) '
                f"VALUES ({inp[0]}, '{inp[1]}', '{inp[2]}', '{inp[3]}')"
            )
        print("[INFO] Data was succefully inserted")
        return set(x + 1 for x in range(qty))


def playlist_insertion(connection, qty=10):
    with connection.cursor() as cursor:
        for _ in range(qty):
            inp = generate_playlist()
            cursor.execute(
                f"INSERT INTO Playlist (Title, Creation_date, Duration) "
                f"VALUES ('{inp[0]}', '{inp[1]}', {inp[2]})"
            )
        print("[INFO] Data was succefully inserted")
        return set(x + 1 for x in range(qty))


def comment_insertion(connection, qty=10):
    with connection.cursor() as cursor:
        for _ in range(qty):
            inp = generate_comment()
            cursor.execute(
                f'INSERT INTO "Comment" (Text, Creation_date) '
                f"VALUES ('{inp[0]}', '{inp[1]}')"
            )
        print("[INFO] Data was succefully inserted")
        return set(x + 1 for x in range(qty))


def genre_insertion(connection, qty=10):
    with connection.cursor() as cursor:
        for _ in range(qty):
            inp = generate_genre()
            cursor.execute(f"INSERT INTO Genre (Title) " f"VALUES ('{inp}')")
        print("[INFO] Data was succefully inserted")
        return qty


def uservideo_insertion(connection, qty: int, user_set_orig: set, video_set_orig: set):
    user_set = user_set_orig.copy()
    video_set = video_set_orig.copy()
    with connection.cursor() as cursor:
        for _ in range(len(user_set)):
            user_id = user_set.pop()
            for i in range(faker.pyint(0, 4)):
                if not video_set:
                    break
                cursor.execute(
                    f"INSERT INTO User_Video (User_id, Video_id) "
                    f"VALUES ({user_id}, {video_set.pop()})"
                )
        print("[INFO] Data was succefully inserted")


def usercomment_insertion(
    connection, qty: int, user_set_orig: set, comment_set_orig: set
):
    user_set = user_set_orig.copy()
    comment_set = comment_set_orig.copy()
    with connection.cursor() as cursor:
        for _ in range(len(user_set)):
            user_id = user_set.pop()
            for i in range(faker.pyint(0, 100)):
                if not comment_set:
                    break
                cursor.execute(
                    f"INSERT INTO User_Comment (User_id, Comment_id) "
                    f"VALUES ({user_id}, {comment_set.pop()})"
                )
        print("[INFO] Data was succefully inserted")


def userplaylist_insertion(
    connection, qty: int, user_set_orig: set, playlist_set_orig: set
):
    user_set = user_set_orig.copy()
    playlist_set = playlist_set_orig.copy()
    with connection.cursor() as cursor:
        for _ in range(len(user_set)):
            user_id = user_set.pop()
            for i in range(faker.pyint(0, 5)):
                if not playlist_set:
                    break
                cursor.execute(
                    f"INSERT INTO User_Playlist (User_id, Playlist_id) "
                    f"VALUES ({user_id}, {playlist_set.pop()})"
                )
        print("[INFO] Data was succefully inserted")


def videocomment_insertion(
    connection, qty: int, video_set_orig: set, comment_set_orig: set
):
    video_set = video_set_orig.copy()
    comment_set = comment_set_orig.copy()
    with connection.cursor() as cursor:
        for _ in range(len(video_set)):
            video_id = video_set.pop()
            for i in range(faker.pyint(0, 100)):
                if not comment_set:
                    break
                cursor.execute(
                    f"INSERT INTO Video_Comment (Video_id, Comment_id) "
                    f"VALUES ({video_id}, {comment_set.pop()})"
                )
        print("[INFO] Data was succefully inserted")


def videogenre_insertion(connection, qty: int, video_set_orig: set, genre_qty: int):
    video_set = video_set_orig.copy()
    with connection.cursor() as cursor:
        for _ in range(len(video_set)):
            video_id = video_set.pop()
            for i in range(faker.pyint(1, 3)):
                cursor.execute(
                    f"INSERT INTO Video_Genre (Video_id, Genre_id) "
                    f"VALUES ({video_id}, {faker.pyint(1, genre_qty)})"
                )
        print("[INFO] Data was succefully inserted")


def videoplaylist_insertion(connection, qty: int, video_qty: set, playlist_qty: int):
    with connection.cursor() as cursor:
        for _ in range(video_qty):
            for i in range(faker.pyint(1, 3)):
                cursor.execute(
                    f"INSERT INTO Video_Playlist (Video_id, Playlist_id) "
                    f"VALUES ({faker.pyint(1, video_qty)}, {faker.pyint(1, playlist_qty)})"
                )
        print("[INFO] Data was succefully inserted")
