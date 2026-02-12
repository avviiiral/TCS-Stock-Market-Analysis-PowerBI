import pandas as pd

files = [
    "D:\Power BI\TCS stock market\Quote-Equity-TCS-EQ-11-02-2020-11-02-2021.csv",
    "D:\Power BI\TCS stock market\Quote-Equity-TCS-EQ-11-02-2021-11-02-2022.csv",
    "D:\Power BI\TCS stock market\Quote-Equity-TCS-EQ-11-02-2022-11-02-2023.csv",
    "D:\Power BI\TCS stock market\Quote-Equity-TCS-EQ-11-02-2023-11-02-2024.csv",
    "D:\Power BI\TCS stock market\Quote-Equity-TCS-EQ-11-02-2024-11-02-2025.csv",
    "D:\Power BI\TCS stock market\Quote-Equity-TCS-EQ-11-02-2025-11-02-2026.csv"
]

df_list = [pd.read_csv(file) for file in files]
combined_df = pd.concat(df_list, ignore_index=True)

if 'Date' in combined_df.columns:
    combined_df['Date'] = pd.to_datetime(combined_df['Date'], errors='coerce')
    combined_df = combined_df.sort_values("Date")

output_file = "D:\Power BI\TCS stock market\Combined_TCS_Stock_Data.csv"
combined_df.to_csv(output_file, index=False)

