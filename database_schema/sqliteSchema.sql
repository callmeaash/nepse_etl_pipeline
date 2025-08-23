CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS ohlc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER NOT NULL,
    date TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    ltp REAL,
    volume INTEGER,
    amount REAL,
    FOREIGN KEY(stock_id) REFERENCES stocks(id) ON DELETE CASCADE
);