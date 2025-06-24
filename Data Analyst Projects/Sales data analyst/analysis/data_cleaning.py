import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df.dropna(inplace=True)
    df['Month'] = df['Date'].dt.to_period('M')
    return df
print("done")