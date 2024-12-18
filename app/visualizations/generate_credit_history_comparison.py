# visualizations/generate_credit_history_comparison.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def generate_credit_history_comparison(df, output_path):
    """
    Generates a horizontal bar plot comparing loan approval and denial rates based on credit history.
    The credit history is grouped into 10 intervals, and a bar plot is created for each.

    Args:
        df (DataFrame): The DataFrame to analyze.
        output_path (str): The path where the plot should be saved.
    """
    # Ensure Credit_History is numeric
    df['Credit_History'] = pd.to_numeric(df['Credit_History'], errors='coerce')

    # Bin the Credit_History into 10 groups
    bins = np.linspace(df['Credit_History'].min(), df['Credit_History'].max(), 11)
    labels = [f'{int(bins[i])}-{int(bins[i + 1])}' for i in range(len(bins) - 1)]
    df['Credit_History_Binned'] = pd.cut(df['Credit_History'], bins=bins, labels=labels, include_lowest=True)

    # Calculate counts for each bin, Loan_Status = 1 (approved), Loan_Status = 0 (denied)
    grouped = df.groupby('Credit_History_Binned')['Loan_Status'].agg(['sum', 'count'])
    grouped.columns = ['Approved', 'Total']

    # Denied loans are Total - Approved
    grouped['Denied'] = grouped['Total'] - grouped['Approved']

    # Set up the plot
    plt.figure(figsize=(10, 6))

    # Plot total applicants in blue, approved in green, and denied in red
    grouped['Total'].plot(kind='barh', color='blue', alpha=0.6, label='Total Applicants', figsize=(10, 8))
    grouped['Approved'].plot(kind='barh', color='green', alpha=0.6, label='Approved Loans', figsize=(10, 8))
    grouped['Denied'].plot(kind='barh', color='red', alpha=0.6, label='Denied Loans', figsize=(10, 8))

    # Add labels and title
    plt.title('Comparison of Loan Approval and Denial Based on Credit History')
    plt.xlabel('Number of Applicants')
    plt.ylabel('Credit History')
    plt.legend()

    # Add insight text to explain the plot
    insight_text = (
        "This plot shows the distribution of loan approvals, denials, and total applicants "
        "grouped by Credit History. Each group represents a range of credit history values, "
        "with green indicating approval, red indicating denial, and blue indicating the total "
        "number of applicants within that group."
    )
    plt.figtext(0.5, -0.2, insight_text, wrap=True, horizontalalignment='center', fontsize=10)

    # Save the plot to the specified output path
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
