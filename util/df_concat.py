import pandas as pd

def concat(*args, start_min_date=True, end_max_date=True, interpolate=True):
    dfs = []
    mins_dates = []
    maxs_dates = []
    for path in args:
        df = pd.read_csv(path)
        date_col = 'DATE'
        for col in df.columns:
            if 'date' in col.lower():
                date_col = col
                break
        
        df[date_col] = pd.to_datetime(df[date_col])

        if start_min_date:
            mins_dates.append(df[date_col].min())
        if end_max_date:
            maxs_dates.append(df[date_col].max())

        df.set_index(date_col, inplace=True)
        dfs.append(df)

    if end_max_date:
        for df in dfs:
            df = df[(
                df.index <= min(maxs_dates))]
    n_dfs = []
    if start_min_date:
        for df in dfs:
            n_dfs.append(df[(
                df.index >= max(mins_dates))])
    
    merged_data = pd.concat(n_dfs, axis=1)
    filtered_data = merged_data

    if start_min_date:
        filtered_data = merged_data[(
            merged_data.index >= max(mins_dates))]
    if end_max_date:
        filtered_data = merged_data[(
            merged_data.index <= min(maxs_dates))]
    
    if interpolate:
        interpolated_data = filtered_data.interpolate(method='time')
        return interpolated_data
    else:
        return filtered_data