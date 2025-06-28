### ui_components.py
import streamlit as st
import pandas as pd
from typing import List, Optional


def array_ui_filter(df: pd.DataFrame, filters: List[str]) -> pd.DataFrame:
    filtered_df = df.copy()
    for col in filters:
        unique_vals = sorted(df[col].dropna().unique())
        selected = st.multiselect(f"Select {col}", unique_vals, default=unique_vals)
        filtered_df = filtered_df[filtered_df[col].isin(selected)]
    return filtered_df


def safe_melt(
    df: pd.DataFrame,
    id_vars: List[str],
    value_vars: Optional[List[str]] = None,
    var_name: str = "variable",
    value_name: str = "value",
) -> pd.DataFrame:
    """
    Performs a safe, readable melt (unpivot) on a DataFrame.

    - Use `value_vars` when you want to be explicit about which columns to melt.
      If not provided, all columns not in `id_vars` will be melted by default.
    - Use `var_name` and `value_name` when you want to rename the result columns:
        • var_name  → becomes the name of the column holding the old column headers
        • value_name → becomes the name of the column holding the values

    Args:
        df (pd.DataFrame): The DataFrame to melt
        id_vars (List[str]): Columns to keep as identifiers (not melted)
        value_vars (Optional[List[str]]): Columns to melt (default = all non-id_vars)
        var_name (str): Name for new 'variable' column
        value_name (str): Name for new 'value' column

    Returns:
        pd.DataFrame: Melted long-format DataFrame
    """
    # Validate id_vars
    missing_ids = [col for col in id_vars if col not in df.columns]
    if missing_ids:
        raise ValueError(f"Missing id_vars in DataFrame columns: {missing_ids}")

    # Auto-detect value_vars if not supplied
    if value_vars is None:
        value_vars = [col for col in df.columns if col not in id_vars]
    else:
        # Validate value_vars
        missing_vals = [col for col in value_vars if col not in df.columns]
        if missing_vals:
            raise ValueError(f"Missing value_vars in DataFrame columns: {missing_vals}")

    return pd.melt(
        df,
        id_vars=id_vars,
        value_vars=value_vars,
        var_name=var_name,
        value_name=value_name,
    )
