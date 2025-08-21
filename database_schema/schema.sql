CREATE DATABASE "stocks_ohlc";

CREATE TABLE "stocks"(
    "id" SERIAL PRIMARY KEY,
    "symbol" VARCHAR(10) UNIQUE NOT NULL
);


CREATE TABLE "stocks_ohlc"(
    "id" SERIAL PRIMARY KEY,
    "stock_id" INTEGER REFERENCES "stocks"("id") ON DELETE CASCADE,
    "open" NUMERIC(10, 2),
    "high" NUMERIC(10, 2),
    "low" NUMERIC(10, 2),
    "close" NUMERIC(10, 2)
);