import json
import pandas as pd
import sys

MONTH_DICT = {
    "01": "january",
    "02": "february",
    "03": "march",
    "04": "april",
    "05": "may",
    "06": "june",
    "07": "july",
    "08": "august",
    "09": "september",
    "10": "october",
    "11": "november",
    "12": "december",
}


def get_month_report(sp_data, month: str, year: str = ""):
    if month not in MONTH_DICT:
        raise ValueError(
            f"Invalid month: {month}. Must be two-digit string from '01' to '12'"
        )

    # Get month name for filename
    month_name = MONTH_DICT[month]

    data = [d for d in sp_data if f"-{month}-" in d["endTime"]]
    df = pd.DataFrame(data)
    df["minsPlayed"] = df["msPlayed"].apply(lambda d: d / 60000)

    df = df.rename(
        columns={
            "dateTime": "Date",
            "trackName": "Track",
            "artistName": "Artist",
            "minsPlayed": "Minutes Played",
        }
    )
    df = df.groupby(["Track", "Artist"]).agg({"Minutes Played": "sum"}).reset_index()
    df["Minutes Played"] = df["Minutes Played"].apply(lambda d: round(d, 1))
    df.sort_values(by=["Minutes Played"], inplace=True, ascending=False)
    df.to_csv(
        rf"\out\{month_name}.csv",
        mode="w+",
        index=False,
    )


if __name__ == "__main__":
    data = []
    spotify_data_paths = sys.argv[1:]
    month=spotify_data_paths[-1]
    try:
        for data in spotify_data_paths:
            with open(data, "r", encoding="utf-8") as f:
                data = json.load(f)
        data.extend(data)
    except Exception as e:
        print(f"Invalid Data Path. See Error:\n{e}")

    # Example
    get_month_report(data, month)
