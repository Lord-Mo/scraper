# UK Open Tenders Scraper

This repository contains a simple Python script for scraping open tenders from the UK Contracts Finder website.

## Requirements

- Python 3.8+
- [`requests`](https://pypi.org/project/requests/)
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)

Install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper with one or more service keywords. When no keywords are
provided, the script searches for tenders related to **software testing**,
**digital health**, **EPR benefit realisation**, and **CRM development**.

```bash
python scrape_open_tenders.py --pages 2
```

You can provide your own keywords, for example:

```bash
python scrape_open_tenders.py "cyber security" "data analytics"
```

The script prints the title, closing date, and URL for each tender found for
each keyword.

## Notes

- The script queries the publicly available search interface at `https://www.contractsfinder.service.gov.uk`. Be mindful of the website's terms of use and do not overwhelm the service with excessive requests.
- Pagination is handled via the `--pages` argument. Increase this value to fetch additional pages of results.
