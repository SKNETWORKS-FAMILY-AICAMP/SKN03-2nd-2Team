import cleansing_movies
import get_movies_raw_data


def main():
    get_movies_raw_data.main()
    cleansing_movies.main()


if __name__ == "__main__":
    main()
