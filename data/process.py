if __name__ == '__main__':
    import pandas as pd

    inflation              = pd.read_csv('./data/raw/PCETRIM12M159SFRBDAL.csv')
    yr30_morgage_rate      = pd.read_csv('./data/raw/MORTGAGE30US.csv')
    consumer_basket        = pd.read_csv('./data/raw/CPIAUCSL.csv')
    disp_income            = pd.read_csv('./data/raw/DSPIC96.csv')
    real_gross_dom_product = pd.read_csv('./data/raw/GDPC1.csv')
    person_savings         = pd.read_csv('./data/raw/PMSAVE.csv')
    econ_activity          = pd.read_csv('./data/raw/USPHCI.csv')
    unemployment_rate      = pd.read_csv('./data/raw/UNRATE.csv')
    labor_productivity     = pd.read_csv('./data/raw/PRS84006091.csv')
    producer_price_index   = pd.read_csv('./data/raw/PCUOMFGOMFG.csv')

    # part 1
    debt_vs_monthlyIncome = pd.read_csv('./data/raw/TDSP.csv')
    num_morgages          = pd.read_csv('./data/raw/new_morgages.csv')
    population            = pd.read_csv('./data/raw/POPTHM.csv')

    dfs = [consumer_basket, yr30_morgage_rate, inflation, disp_income, real_gross_dom_product, person_savings,
           econ_activity, unemployment_rate, labor_productivity, producer_price_index, debt_vs_monthlyIncome, num_morgages
           , population, ]

    for df in dfs:
        df['DATE'] = pd.to_datetime(df['DATE'])
        df.set_index('DATE', inplace=True)

    merged_data = pd.concat(dfs, axis=1)

    filtered_data = merged_data[(
        merged_data.index >= '1998-01-01') & (merged_data.index <= '2023-01-01')]

    interpolated_data = filtered_data.interpolate(method='time')

    import sys
    path_to_save = sys.argv[1]
    interpolated_data.to_csv(path_to_save)
