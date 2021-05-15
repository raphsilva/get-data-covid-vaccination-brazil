import pandas as pd
from time_format import date_to_datetime, datetime_to_str
from datetime import datetime


def detect_missing(df: pd.DataFrame()):
    mss = df.copy()
    mss = mss[mss['contagem'] > 1]

    ddp = df.copy()
    ddp = ddp[ddp['contagem'] == 1]
    ddp['contagem'] = 1
    del ddp['paciente_id']
    gb = list(ddp.columns)
    gb.remove('contagem')
    ddp = pd.DataFrame(ddp.groupby(gb).sum())

    return mss.reset_index(), ddp.reset_index()


def detect_wrong_date(df):
    print(df)
    print(df.columns)
    df['data_incorreta'] = False
    df[df['data'] < '2021-01-17'] = True
    df[df['data'] > datetime_to_str(datetime.now())] = True
    wr = df[df['data_incorreta']].copy()
    df = df[~df['data_incorreta']].copy()
    del df['data_incorreta']
    return wr, df


def separate_by_date(df):
    r = dict()
    df['data']
    gb = df.groupby('data')
    for g in gb:
        r[g[0]] = g[1]
    return r