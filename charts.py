import io
import pandas as pd
import requests
import time
import tqdm


def week_dates(date, weekday=0):
    week_start = date - pd.DateOffset(weekday=weekday, weeks=1)
    week_end = date + pd.DateOffset(weekday=weekday, weeks=0)
    return week_start, week_end


def get_chart(date, region='en', freq='daily', chart='top200'):
    chart = 'regional' if chart == 'top200' else 'viral'
    date = pd.to_datetime(date)
    if date.year < 2017:
        raise ValueError('No chart data available from before 2017')
    if freq == 'weekly':
        start, end = week_dates(date, weekday=4)
        date = f'{start.date()}--{end.date()}'
    else:
        date = f'{date.date()}'
    url = f'https://spotifycharts.com/{chart}/{region}/{freq}/{date}/download'
    data = io.StringIO(requests.get(url).text)
    try:
        df = pd.read_csv(data)
        df = header_handler(df) # Remove Spotify's notice from DataFrame
    except pd.errors.ParserError:
        df = None
        print(data)
    return df


def get_charts(start, end, region='en', freq='daily', chart='top200', sleep=1):
    sample = 'D' if freq == 'daily' else 'W'
    dfs = []
    for date in tqdm.tqdm(pd.date_range(start=start, end=end, freq=sample)):
        df = get_chart(date, region=region, freq=freq, chart=chart)
        if df is not None:
            df['date'] = date
            dfs.append(df)
            time.sleep(sleep)
    return pd.concat(dfs)


def header_handler(df):
    find_row = df[df.columns[0]] == 'Position'
    if True in find_row:
        column_names = df[find_row].values.tolist()
        drop_row = df.index[find_row].tolist()
        df = df.drop(drop_row)
        df.columns = column_names
        df = df.dropna() # Drop row with Spotify's notice
        df = df.reset_index(drop=True)
    return df 


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--start_date', required=True,
        help='A date defining the start day for the chart.')
    parser.add_argument(
        '--outfile', required=True,
        help='Save the results in this file.')
    parser.add_argument(
        '--end_date',
        help='A date defining the end day for the chart.')
    parser.add_argument(
        '--region',
        default='global',
        help='A region defined for the chart.')
    parser.add_argument(
        '--freq',
        choices=['daily', 'weekly'],
        default='daily',
        help='Use timestamps on a weekly or daily frequency.')
    parser.add_argument(
        '--chart',
        choices=['top200', 'viral'],
        default='top200',
        help='The type of chart to retrieve.')
    args = parser.parse_args()
    
    if args.end_date is not None:
        df = get_charts(args.start_date, args.end_date, region=args.region,
                        freq=args.freq, chart=args.chart)
    else:
        df = get_chart(args.start_date, region=args.region, freq=args.freq,
                       chart=args.chart)
    df.to_csv(args.outfile)
