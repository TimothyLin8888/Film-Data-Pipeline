from bs4 import BeautifulSoup
import requests
from config import IMDB_URL
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
def format_votes(votes):
    """Convert a large number to a human-readable format like 3.2M or 973K"""
    if votes is None:
        return "N/A"
    if votes >= 1_000_000:
        return f"{votes / 1_000_000:.1f}M"
    elif votes >= 1_000:
        return f"{votes / 1_000:.0f}K"
    else:
        return str(votes)

def imdb_web_scraper():
    response = requests.get(IMDB_URL, headers=headers)
    if response.status_code == 200:
        print("Page fetched successfully!")
    else:
        raise RuntimeError(f"Failed to retrieve page, status code: {response.status_code}d")

    soup = BeautifulSoup(response.content, "html.parser")
    movieData = soup.find('script', id='__NEXT_DATA__')

    '''
    Things that I probably want:
    - Movie Title
    - Release Year
    - Rating
    - Movie Rank on the IMDb list
    - Number of Ratings could be nice
    '''
    # movieName = []
    # movieYear = []
    # rating = []
    # movieRank = []
    movie_data = {
        "Title": [], 
        "Year": [], 
        "Rating": [],
        "Votes": []
        }

    if movieData:
        jsonData = json.loads(movieData.string)
        movies = jsonData['props']['pageProps']['pageData']['chartTitles']['edges']
        for movie in movies:
            node = movie["node"]
            # rank = movie['currentRank']
            # movie_data["Rank"].append(rank)

            title = movie['node']['titleText']['text']
            movie_data["Title"].append(title)

            year = movie['node']['releaseYear']['year']
            movie_data["Year"].append(year)

            ratings_summary = node.get("ratingsSummary", {})
            movie_data["Rating"].append(ratings_summary.get("aggregateRating"))
            movie_data["Votes"].append(format_votes(ratings_summary.get("voteCount")))
    else:
        raise RuntimeError("IDMb data not found")

    return movie_data


if __name__ == "__main__":
    movie_data = imdb_web_scraper()

    print(f"{'Rank':<5} {'Title':<35} {'Year':<6} {'Rating':<6}")
    print("-" * 55)

    for rank, title, year, rate, votes in zip(
        movie_data["Rank"],
        movie_data["Title"],
        movie_data["Year"],
        movie_data["Rating"],
        movie_data["Votes"]
    ):
        print(f"{rank:<5} {title:<35} {year:<6} {rate: <3} {votes}")