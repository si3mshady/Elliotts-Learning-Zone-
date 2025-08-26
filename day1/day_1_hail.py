import pandas as pd

url = "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d2023_c20240425.csv.gz"
df = pd.read_csv(url, compression="gzip", low_memory=False)

# Filter for hail events
hail_df = df[df['EVENT_TYPE'] == 'Hail'][['BEGIN_DATE_TIME', 'STATE', 'MAGNITUDE']]
print(hail_df.head())
