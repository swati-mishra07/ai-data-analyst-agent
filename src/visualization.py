import matplotlib.pyplot as plt


def plot_histograms(df):

    try:
        df.hist(figsize=(12, 10))
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Visualization error: {e}")
