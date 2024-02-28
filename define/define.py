import pandas as pd


def load_data(url):
    df = pd.read_csv(url)
    return df


def table(df):
    dct = {}
    for i in df.columns:
        mean = df[i].mean()
        count = df[i].count()
        dct[i] = {'Mean': mean, 'Count': count}
    return pd.DataFrame.from_dict(dct)
