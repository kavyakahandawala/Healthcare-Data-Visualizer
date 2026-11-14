"""Create the visualizations for the freeCodeCamp medical data challenge."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


DATA_PATH = Path(__file__).resolve().with_name("medical_examination.csv")
CATEGORY_FEATURES = [
    "cholesterol",
    "gluc",
    "smoke",
    "alco",
    "active",
    "overweight",
]
CATEGORY_ORDER = sorted(CATEGORY_FEATURES)


def prepare_data(data: pd.DataFrame) -> pd.DataFrame:
    """Return a prepared copy with overweight and normalized risk features."""
    prepared = data.copy()
    bmi = prepared["weight"] / ((prepared["height"] / 100) ** 2)
    prepared["overweight"] = (bmi > 25).astype(int)

    for feature in ("cholesterol", "gluc"):
        prepared[feature] = (prepared[feature] > 1).astype(int)

    return prepared


if not DATA_PATH.is_file():
    raise FileNotFoundError(
        f"Medical examination data was not found at {DATA_PATH}. "
        "Place medical_examination.csv beside this script."
    )

df = prepare_data(pd.read_csv(DATA_PATH))


def draw_cat_plot():
    """Draw counts of healthy/unhealthy values split by cardio outcome."""
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=CATEGORY_FEATURES,
    )
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    chart = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
        order=CATEGORY_ORDER,
        hue_order=[0, 1],
    )
    fig = chart.fig
    fig.savefig(Path(__file__).resolve().with_name("catplot.png"))
    return fig


def draw_heat_map():
    """Draw the lower-triangle correlation heat map after cleaning outliers."""
    height_low, height_high = df["height"].quantile([0.025, 0.975])
    weight_low, weight_high = df["weight"].quantile([0.025, 0.975])
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= height_low)
        & (df["height"] <= height_high)
        & (df["weight"] >= weight_low)
        & (df["weight"] <= weight_high)
    ]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 12))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".1f",
        mask=mask,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )
    fig.savefig(Path(__file__).resolve().with_name("heatmap.png"))
    return fig
