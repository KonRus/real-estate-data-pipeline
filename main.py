from db.database import init_db, insert_listings
from scrapers.trojmiasto import scrape as scrape_trojmiasto


def main():

    init_db()

    listings = scrape_trojmiasto()

    insert_listings(listings)

    print(f"Saved {len(listings)} listings")


if __name__ == "__main__":
    main()