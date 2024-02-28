import pandas as pd


def table(df):
    dct = {}
    for i in df.columns:
        mean = df[i].mean()
        count = df[i].count()
        dct[i] = {'Mean': mean, 'Count': count}
    return pd.DataFrame.from_dict(dct)


def graphical_summary(df):
    summary_dict = {}
    for i in df.columns:
        mean = round(df[i].mean(), 2)
        dev = round(df[i].std(), 2)
        variance = round(df[i].var(), 2)
        skewness = round(df[i].skew(), 2)
        kurtosis = round(df[i].kurtosis(), 2)
        n = df[i].count()
        minimum = round(df[i].min(), 2)
        first_quartile = round(df[i].quantile(0.25), 2)
        median = round(df[i].quantile(0.5), 2)
        third_quartile = round(df[i].quantile(0.75), 2)
        maximum = round(df[i].max(), 2)

        summary_dict[i] = {"Mean": mean, "StDev": dev, "Var": variance, "Skewness": skewness, "Kurtosis": kurtosis, "N": n,
                           "Minimum": minimum, "1st Quartile": first_quartile, "Median": median,
                           "3rd Quartile": third_quartile, "Maximum": maximum}

    return pd.DataFrame.from_dict(summary_dict)
