from pathlib import Path
from typing import Optional

import pandas as pd
from pandas import DataFrame

from automation_factory import safe_package_sort
from constants import PackageStack


def package_classifier(data_frame: DataFrame) -> None:
    data_frame["Classification"] = data_frame.apply(
        lambda row: safe_package_sort(
            row["Width"], row["Height"], row["Length"], row["Mass"]
        ),
        axis=1,
    )

def calculate_volume(row: pd.Series) -> Optional[int]:
    if row["Classification"] == PackageStack.INVALID.name:
        return None
    return int(row["Width"]) * int(row["Height"]) * int(row["Length"])

def compute_volume(data_frame: DataFrame):
    data_frame["Volume"] = data_frame.apply(calculate_volume, axis=1)

def read_packages_from_csv(path: Path) -> DataFrame:
    df = pd.read_csv(path, usecols=[0, 1, 2, 3])
    df[["Width", "Height", "Length", "Mass"]] = df[["Width", "Height", "Length", "Mass"]].apply(pd.to_numeric, errors="coerce")
    package_classifier(df)
    compute_volume(df)

    return df

def total_by_class_summary(data_frame: DataFrame) -> None:
    total = len(data_frame)
    summary = data_frame["Classification"].value_counts()

    print(f"Total packages: {total}")
    for classification, count in summary.items():
        percent = (count / total) * 100
        print(f"{classification}: {percent:.2f}%")

def grouped_by_class_summary(data_frame: DataFrame) -> None:
    df_valid = data_frame[data_frame["Classification"] != PackageStack.INVALID.name]

    stats = df_valid.groupby("Classification").agg({
        "Mass": ["mean", "min", "max"],
        "Volume": ["mean", "min", "max"]
    }).round(2)

    print(stats)


def main():
    df = read_packages_from_csv(Path("packages.csv"))
    total_by_class_summary(df)
    grouped_by_class_summary(df)


if __name__ == "__main__":
    main()