import pandas as pd

df = pd.read_csv("../data/raw/contra_contacts_raw.csv")

df = df[df["AGE"] > 0]

df["DATE"] = pd.to_datetime(df["DT"], format="%m/%d/%y")

df.drop(
    columns=[
        "DT",
        "WK",
        "WEEK_START",
        "SCIENSANO_REQUEST_TICKET_NUMBER",
    ],
    inplace=True,
)

df["AGE_CATEGORY"] = pd.cut(
    x=df["AGE"],
    bins=[0, 18, 30, 50, 70, 90, 110],
    labels=["<18", "18-30", "30-50", "50-70", "70-90", "90+"],
)

df.to_csv("../data/processed/contra_contacts_processed.csv", index=False)
