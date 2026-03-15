import sqlite3
from typing import List
from models.listing import Listing

DB_PATH = "data/listings.db"


def init_db():

    conn = sqlite3.connect(DB_PATH)

    with open("db/schema.sql") as f:
        conn.executescript(f.read())

    conn.close()


def insert_listings(listings: List[Listing]):

    conn = sqlite3.connect(DB_PATH)

    rows = [
        (
            l.source,
            l.title,
            l.price,
            l.area,
            l.city,
            l.district,
            l.rooms,
            l.url,
        )
        for l in listings
    ]

    conn.executemany(
        """
        INSERT INTO listings
        (source, title, price, area, city, district, rooms, url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)

        ON CONFLICT(source, url) DO UPDATE SET
            price = excluded.price,
            area = excluded.area
        """,
        rows,
    )

    conn.commit()
    conn.close()