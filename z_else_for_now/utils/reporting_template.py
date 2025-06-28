"""reporting.py template"""

import pandas as pd


def get_high_sales(df: pd.DataFrame, threshold: float = 1800) -> pd.DataFrame:
    return df[df["net_sales"] > threshold]


def report_high_sales_console(df: pd.DataFrame, threshold: float = 1800) -> None:
    high_sales = get_high_sales(df, threshold)
    if not high_sales.empty:
        for _, row in high_sales.iterrows():
            print(f"Store {row['store_no']} has high sales")
    else:
        print("NONE had high sales")


def export_high_sales_to_excel(df: pd.DataFrame, threshold: float, path: str) -> None:
    high_sales = get_high_sales(df, threshold)
    if high_sales.empty:
        print("Export skipped: no high sales")
    else:
        high_sales.to_excel(path, index=False)
        print(f"Exported high sales to {path}")
