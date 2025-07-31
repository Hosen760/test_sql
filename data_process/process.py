import pandas as pd

def choice_process(df: pd.DataFrame) -> pd.DataFrame:
    """
    对传入的 DataFrame 进行处理：
    1. 删除最后 7 行
    2. 重命名 '交易时间' 为 'date'，'收盘价' 为 'price'
    3. 设置 'date' 为索引
    4. 只保留 'price' 列

    参数:
        df (pd.DataFrame): 原始数据，必须包含 '交易时间' 和 '收盘价' 两列

    返回:
        pd.DataFrame: 处理后的 DataFrame，索引为 date，仅包含 price 列
    """
    df = df.iloc[:-7, :].copy()
    df.rename(columns={'交易时间': 'date', '收盘价': 'price'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df[['price']]
    return df


def wind_process(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(columns={'日期': 'date', '收盘价(元)': 'price'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df[['price']]
    return df



