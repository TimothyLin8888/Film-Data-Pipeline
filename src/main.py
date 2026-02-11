from imdb_web_scraper import imdb_web_scraper
from update_google_sheet import write


def main():
    start_cell = "A2"
    movie_data = imdb_web_scraper()
    start_rank = 1
    end_rank = 100
    # print("Movie data keys:", movie_data.keys())
    # for key, values in movie_data.items():
    #     print(f"{key}: {len(values)} items")

    sliced_data = {}
    for key, values in movie_data.items():
        sliced_data[key] = values[start_rank - 1 : end_rank]
    write(sliced_data, start_cell)


if __name__ == "__main__":
    main()