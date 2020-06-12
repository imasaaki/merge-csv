import os
import glob
import csv
import pandas as pd
import datetime

csv_path = "csv/"
file_list = glob.glob('{}*.csv'.format(csv_path))

out_list = []
for file in file_list:
    df = pd.read_csv(file)
    print(df.info())
    out_list.append(df)
out_df = pd.concat(out_list, sort=False).sort_values(['url'], ascending=[1])
print('***merged***')
print(out_df.info())
out_df = out_df.drop_duplicates(['url'], keep='first')
print('***only unique item***')
print(out_df.info())

out_df.to_csv('output' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.csv', encoding='utf_8', index=False)