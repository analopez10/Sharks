def examination():
    missing_values = pd.isnull(df)
    missing_counts = missing_values.sum()
    columns_with_missing = missing_counts[missing_counts > 0].count()
    all_columns_missing = missing_counts.all()
    total_missing_values = missing_counts.sum()
    print("Missing Values in Each Column:\n", missing_counts)
    print("\nNumber of Columns with Missing Values:", columns_with_missing)
    print("All Columns Have Missing Values:", all_columns_missing)
    print("\nTotal Missing Values in the DataFrame:", total_missing_values)