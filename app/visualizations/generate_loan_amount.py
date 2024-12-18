# visualizations/generate_loan_amount.py

import matplotlib.pyplot as plt
import seaborn as sns

def generate_loan_amount(df, output_path):
    """
    Generates a boxplot to visualize the variation in loan amounts based on loan approval status.

    Args:
        df (DataFrame): The DataFrame to analyze.
        output_path (str): The path where the plot should be saved.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Loan_Status', y='LoanAmount', data=df)
    plt.title('Loan Amount Variation by Approval Status')

    # Update x-axis labels
    x_labels = ['Denied (0)', 'Approved (1)']
    plt.xticks(ticks=[0, 1], labels=x_labels)

    plt.xlabel('Loan Status')
    plt.ylabel('Loan Amount')

    # Add insight text at the bottom of the plot
    insight_text = "This illustrates the distribution of loan amounts based on loan approval status."
    plt.figtext(0.5, -0.1, insight_text, wrap=True, horizontalalignment='center', fontsize=10)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
