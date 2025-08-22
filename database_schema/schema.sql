CREATE DATABASE "stocks_ohlc";

CREATE TABLE "stocks"(
    "id" SERIAL PRIMARY KEY,
    "symbol" VARCHAR(10) UNIQUE NOT NULL
);


CREATE TABLE "ohlc"(
    "id" SERIAL PRIMARY KEY,
    "stock_id" INTEGER REFERENCES "stocks"("id") ON DELETE CASCADE,
    "date" DATE,
    "open" NUMERIC(20, 2),
    "high" NUMERIC(20, 2),
    "low" NUMERIC(20, 2),
    "close" NUMERIC(20, 2),
    "ltp" NUMERIC(20, 2),
    "volume" INTEGER,
    "amount" NUMERIC(20, 2)
);