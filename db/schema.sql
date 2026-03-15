CREATE TABLE IF NOT EXISTS listings (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    source TEXT NOT NULL,
    title TEXT,
    price INTEGER,
    area REAL,
    city TEXT,
    district TEXT,
    rooms INTEGER,
    url TEXT,

    scraped_at TEXT DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(source, url)

);