import requests
from bs4 import BeautifulSoup


def scrape_open_tenders(service_keyword: str, pages: int = 1):
    """Scrape open tenders from Contracts Finder for a given service keyword.

    Args:
        service_keyword: Keyword describing the service to search for.
        pages: Number of search result pages to retrieve.

    Returns:
        A list of dictionaries containing tender details.
    """
    base_url = "https://www.contractsfinder.service.gov.uk/Search/Results"
    tenders = []
    for page in range(1, pages + 1):
        params = {
            "page": page,
            "status": "Open",
            "keyword": service_keyword,
        }
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for notice in soup.select(".search-result"):  # each result block
            title_elem = notice.select_one("h2 a")
            closing_elem = notice.select_one("span.closing-date")
            if not title_elem:
                continue
            tender = {
                "title": title_elem.get_text(strip=True),
                "url": "https://www.contractsfinder.service.gov.uk" + title_elem["href"],
                "closing_date": closing_elem.get_text(strip=True) if closing_elem else None,
            }
            tenders.append(tender)
    return tenders


DEFAULT_KEYWORDS = [
    "software testing",
    "digital health",
    "epr benefit realisation",
    "crm development",
]


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Scrape open UK tenders for one or more service keywords"
    )
    parser.add_argument(
        "keywords",
        nargs="*",
        default=DEFAULT_KEYWORDS,
        help=(
            "Service keywords to search for. If omitted, a set of default "
            "keywords is used."
        ),
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Number of result pages to scrape for each keyword",
    )
    args = parser.parse_args()

    for keyword in args.keywords:
        print(f"### Results for: {keyword}\n")
        results = scrape_open_tenders(keyword, args.pages)
        for tender in results:
            print(f"{tender['title']} - {tender['closing_date']}")
            print(f"{tender['url']}\n")


if __name__ == "__main__":
    main()
