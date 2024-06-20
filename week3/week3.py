import pandas as pd
import numpy as np
import zipfile

real_dataset_path = 'https://raw.githubusercontent.com/Kingtilon1/DATA604/main/LakeCounty_Health_2397514566901885190.csv'
real_df = pd.read_csv(real_dataset_path)

mock_dataset_url = 'https://raw.githubusercontent.com/Kingtilon1/DATA604/main/MOCK_DATA%20(3).csv'
mock_df = pd.read_csv(mock_dataset_url)

doubled_mock_df = pd.concat([mock_df, mock_df])

pivot_real = real_df.pivot_table(values='Obesity', index='NAME', aggfunc='mean')
pivot_mock = mock_df.pivot_table(values='Obesity', index='NAME', aggfunc='mean')
pivot_doubled_mock = doubled_mock_df.pivot_table(values='Obesity', index='NAME', aggfunc='mean')

pivot_mock = pivot_mock.reindex_like(pivot_real)
pivot_doubled_mock = pivot_doubled_mock.reindex_like(pivot_real)

real_profile_path = 'real_profile.xlsx'
mock_profile_path = 'mock_profile.xlsx'
doubled_mock_profile_path = 'doubled_mock_profile.xlsx'

pivot_real.to_excel(real_profile_path)
pivot_mock.to_excel(mock_profile_path)
pivot_doubled_mock.to_excel(doubled_mock_profile_path)

comparison_mock = pivot_real.compare(pivot_mock)
comparison_doubled_mock = pivot_real.compare(pivot_doubled_mock)

analysis_mock_path = 'analysis_mock.txt'
analysis_doubled_mock_path = 'analysis_doubled_mock.txt'

with open(analysis_mock_path, 'w') as f:
    f.write(str(comparison_mock))

with open(analysis_doubled_mock_path, 'w') as f:
    f.write(str(comparison_doubled_mock))

deliverables = [
    real_profile_path,
    mock_profile_path,
    doubled_mock_profile_path,
    analysis_mock_path,
    analysis_doubled_mock_path
]

zip_path = 'deliverables.zip'
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for file in deliverables:
        zipf.write(file)

print(f'Deliverables saved in {zip_path}')
