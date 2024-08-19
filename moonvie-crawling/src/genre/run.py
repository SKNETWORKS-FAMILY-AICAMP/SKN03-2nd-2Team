import cleansing_movies
import get_movies_raw_data
import get_genre


def main():
    get_movies_raw_data.main()
    cleansing_movies.main()
    get_genre.main()


if __name__ == "__main__":
    main()
