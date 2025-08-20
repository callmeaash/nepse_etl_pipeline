import pandas as pd
import logging

logger = logging.getLogger(__name__)


def transform_data(raw_data: pd.DataFrame) -> tuple:
    """
    Transform and clean the data to load into the database
    """

    # Convert the data type of columns in right type
    logger.info("Convert the data into correct format")
    raw_data["date"] = pd.to_datetime(raw_data["date"])

    # Fill the missing values, if any
    logger.info("Fill missing values if exists")
    for col in raw_data.columns[2:]:
        raw_data[col].fillna(raw_data[col].mean(), inplace=True)

    # Selecting the last day records of each stock
    logger.info("Select the last day record of each stock")
    clean_data = (
        raw_data.sort_values("date", ascending=False)
        .groupby("symbol", as_index=False)
        .first()
    )

    # Adding the technical indicators to the raw dataframe
    logger.info("Calculate the techincal indicators")
    raw_data["per_change"] = (
        raw_data.sort_values("date")
        .groupby("symbol")["close"]
        .transform(lambda x: x.pct_change() * 100)
    )
    ema_12 = (
        raw_data.sort_values("date")
        .groupby("symbol")["close"]
        .transform(lambda x: x.ewm(span=12, adjust=False).mean())
    )
    ema_26 = (
        raw_data.sort_values("date")
        .groupby("symbol")["close"]
        .transform(lambda x: x.ewm(span=26, adjust=False).mean())
    )
    raw_data["MACD"] = ema_12 - ema_26
    raw_data["MACD_signal"] = (
        raw_data.sort_values("date")
        .groupby("symbol")["MACD"]
        .transform(lambda x: x.ewm(span=9, adjust=False).mean())
    )

    period = 14
    raw_data["RSI_14"] = raw_data.sort_values('date').groupby("symbol")["close"].transform(
        lambda x: 100 - (100 / (1 + (
            (
                x.diff()
                .clip(lower=0)
                .rolling(window=period, min_periods=period)
                .mean()
            ) / (
                    -x.diff()
                    .clip(upper=0)
                    .rolling(window=period, min_periods=period)
                    .mean()
                )
            )))
        )
    cols_to_round = ['per_change', 'MACD', 'MACD_signal', 'RSI_14']
    raw_data[cols_to_round] = raw_data[cols_to_round].round(2)

    technical_data = raw_data.sort_values('date').groupby('symbol', group_keys=False).apply(lambda x: x.head(len(x) - 20))

    # Return the clean data and technical data
    logger.info(f"clean_data df contains {len(clean_data)} rows")
    logger.info(f"technical_df contains {len(technical_data)} rows")
    logger.info('Return clean_data and technical_data as tuple')
    return (clean_data, technical_data)


