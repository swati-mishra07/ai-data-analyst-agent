import logging

from src.data_loader import load_data
from src.eda_engine import basic_eda
from src.visualization import plot_histograms
from src.agent import generate_insights


# configure logging
logging.basicConfig(level=logging.INFO)


def main():

    file_path = "data/adult.csv"

    logging.info("Loading dataset...")
    df = load_data(file_path)

    if df is None:
        logging.error("Failed to load dataset.")
        return

    logging.info("Running EDA...")
    summary = basic_eda(df)

    print("\n=== EDA Summary ===\n")
    print(summary)

    logging.info("Generating AI insights...")
    insights = generate_insights(summary)

    print("\n=== AI Insights ===\n")
    print(insights)

    logging.info("Generating visualizations...")
    plot_histograms(df)


if __name__ == "__main__":
    main()
