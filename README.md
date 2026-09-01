EasyNews

A simple and lightweight Python library for searching news using Google News RSS.

EasyNews is designed to make Google News RSS searches easy to use from Python without dealing with RSS URLs manually.

Features

- 🔎 Search Google News using keywords
- 🌍 Choose language and country
- 📰 Get article title, link, publication date, and source
- 📦 Lightweight dependency — uses "feedparser"
- 🐍 Supports Python 3.8+
- ⚡ Simple API

Installation

Install EasyNews from PyPI:

pip install easynews

Quick Start

from easynews import EasyNews

news = EasyNews()

articles = news.search("artificial intelligence")

for article in articles:
    print(article["title"])
    print(article["link"])
    print()

Configuration

You can customize the language, country, edition, and maximum number of results:

from easynews import EasyNews

news = EasyNews(
    language="en",
    country="IN",
    edition="en",
    max_results=10
)

Parameters

Parameter| Default| Description
"language"| ""en""| Language used for the Google News search
"country"| ""IN""| Country code
"edition"| ""en""| Google News edition
"max_results"| "10"| Maximum number of articles returned

Searching

Use the "search()" method with a keyword or search phrase:

articles = news.search("technology")

You can also search for multiple words:

articles = news.search("artificial intelligence India")

The method returns a list of dictionaries.

Article Format

Each article contains:

{
    "title": "Article title",
    "link": "https://...",
    "published": "Publication date",
    "source": "News source"
}

Available fields

- "title" — Article title
- "link" — Article URL
- "published" — Publication date, when provided by the feed
- "source" — News source, or ""Unknown"" when unavailable

Example

from easynews import EasyNews

news = EasyNews(max_results=5)

articles = news.search("Python")

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Source: {article['source']}")
    print(f"Published: {article['published']}")
    print(f"Link: {article['link']}")
    print("-" * 50)

How It Works

EasyNews uses the Google News RSS search feed.

When you call:

news.search("Python")

EasyNews creates the appropriate Google News RSS search URL, retrieves the feed, parses it using "feedparser", and returns the articles as Python dictionaries.

Requirements

- Python 3.8 or newer
- Internet connection
- "feedparser"

Dependency

EasyNews currently uses:

- ""feedparser"" (https://pypi.org/project/feedparser/) — for parsing RSS feeds

Limitations

EasyNews currently depends on Google News RSS being available and requires an internet connection to retrieve news.

Search results and available article information are provided by the Google News RSS feed and may vary depending on the search query, country, language, and Google News.

License

This project is open source.

See the repository for the applicable license.

Contributing

Contributions, suggestions, bug reports, and improvements are welcome.

If you find a problem or have an idea for EasyNews, feel free to open an issue or submit a pull request in the project's repository.

Author

EasyNews is developed as a simple Python library for making Google News RSS searches easier.

Links

- PyPI: "https://pypi.org/project/easynews/"
- GitHub: "https://github.com/dev-a-raj/EasyNews"

---

EasyNews — Search news easily with Python.
