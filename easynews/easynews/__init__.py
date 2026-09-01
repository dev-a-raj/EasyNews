import feedparser
import urllib.parse


class EasyNews:
    def __init__(
        self,
        language="en",
        country="IN",
        edition="en",
        max_results=10
    ):
        self.language = language
        self.country = country
        self.edition = edition
        self.max_results = max_results

    def search(self, keyword):
        safe_keyword = urllib.parse.quote(keyword)

        url = (
            f"https://news.google.com/rss/search?"
            f"q={safe_keyword}"
            f"&hl={self.language}-{self.country}"
            f"&gl={self.country}"
            f"&ceid={self.country}:{self.edition}"
        )

        feed = feedparser.parse(url)

        articles = []

        for entry in feed.entries[:self.max_results]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": getattr(entry, "published", None),
                "source": (
                    entry.source.title
                    if hasattr(entry, "source")
                    else "Unknown"
                )
            })

        return articles
