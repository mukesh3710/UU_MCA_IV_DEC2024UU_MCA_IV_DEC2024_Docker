# visualizations/generate_income_distribution.py

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generate_income_distribution(df, output_path):
    """
    Generates a histogram showing the distribution of applicant income for approved and denied loans.

    Args:
        df (DataFrame): The DataFrame to analyze.
        output_path (str): The path where the plot should be saved.
    """
    plt.figure(figsize=(10, 6))
    # Split the data based on loan status
    denied = df[df['Loan_Status'] == 0]['Income']
    approved = df[df['Loan_Status'] == 1]['Income']

    # Determine range and bins for 10 distributions
    income_min = df['Income'].min()
    income_max = df['Income'].max()
    bins = np.linspace(income_min, income_max, 11)

    # Plot histograms for denied and approved loans
    plt.hist(denied, bins=bins, color='red', edgecolor='black', alpha=0.6, label='Denied (0)')
    plt.hist(approved, bins=bins, color='blue', edgecolor='black', alpha=0.6, label='Approved (1)')

    plt.title('Visualization of Applicant Income Distribution, Loan Denial and Approval')
    plt.xlabel('Applicant Income')
    plt.ylabel('Number of Loan Applicants')

    # Add legend
    plt.legend()

    # Add insight text at the bottom of the plot
    insight_text = "This plot visualizes the distribution of loan applicants within each income bracket, distinguishing between approved and denied loans and getting approvals."
    plt.figtext(0.5, -0.1, insight_text, wrap=True, horizontalalignment='center', fontsize=10)

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
