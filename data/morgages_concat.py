import os
import pandas as pd

dfs = []

for f in os.listdir('./data/new_morgages/'):
    df = pd.read_csv(f'./data/new_morgages/{f}')
    df = df.drop(columns=['SOURCE', 'GEONAME', 'SERIESID', 'GEOLEVEL', 'GEOID', 'SUPPRESSED'])
    df = df[df['MARKET'] == 'All Mortgages']

    year, month = df['YEAR'].astype(str), df['MONTH'].astype(str).str.zfill(2)
    value = df['VALUE1']

    df = pd.DataFrame({
        'DATE': pd.to_datetime(year + '-' + month),
        'NUMMORGAGES': value
    })
    dfs.append(df)

# Concatenate all the dataframes
combined_df = pd.concat(dfs, ignore_index=True)

# Sort the DataFrame by the 'DATE' column
combined_df = combined_df.sort_values(by='DATE')

# Group by 'DATE' and calculate the sum of 'NUMMORGAGES' for each month
monthly_sum = combined_df.groupby('DATE')['NUMMORGAGES'].sum().reset_index()

# Now, monthly_sum is a DataFrame with the sum of 'NUMMORGAGES' for each month
print(monthly_sum.head())