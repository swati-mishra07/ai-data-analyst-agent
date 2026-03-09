def basic_eda(df):

    try:
        summary = {
            "shape": df.shape,
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "describe": df.describe().to_dict(),
        }

        return summary

    except Exception as e:
        print(f"EDA Error: {e}")
