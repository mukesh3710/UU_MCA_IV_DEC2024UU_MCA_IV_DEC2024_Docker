# visualizations/generate_correlation_matrix.py

import matplotlib.pyplot as plt
import seaborn as sns

def generate_correlation_matrix(df, output_path):
    """
    Generates a correlation matrix plot and saves it as a PNG.

    Args:
        df (DataFrame): The DataFrame to analyze.
        output_path (str): The path where the plot should be saved.
    """
    plt.figure(figsize=(14, 14))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    insight_text = (
        "Displays the correlation matrix for a given DataFrame that helps to identify relationships that might impact loan decisions.")
    plt.figtext(0.5, -0.1, insight_text, wrap=True, horizontalalignment='center', fontsize=10)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
