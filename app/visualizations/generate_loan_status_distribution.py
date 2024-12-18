# visualizations/generate_loan_status_distribution.py

import matplotlib.pyplot as plt
import seaborn as sns

def generate_loan_status_distribution(df, output_path):
    """
    Generates a pie chart showing the distribution of loan approval and denial rates.

    Args:
        df (DataFrame): The DataFrame to analyze.
        output_path (str): The path where the plot should be saved.
    """
    loan_status_counts = df['Loan_Status'].value_counts()
    loan_status_percentages = loan_status_counts / loan_status_counts.sum() * 100

    # Rename the index to make it more descriptive
    loan_status_percentages.index = ['Approval' if x == 1 else 'Denial' for x in loan_status_percentages.index]

    approved_percent = loan_status_percentages.get('Approval', 0)
    denied_percent = loan_status_percentages.get('Denial', 0)

    # Plotting the pie chart
    plt.figure(figsize=(8, 6))
    ax = loan_status_percentages.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['green', 'red'],
                                      legend=False)
    ax.set_ylabel('')  # Remove the y-label to make it cleaner
    plt.title('Distribution of Loan Status')

    # Adding insight text outside the chart
    insight_text = (f"This plot provides an overview of the distribution of loan status in the dataset. "
                    f"The approval rate is : {approved_percent:.2f}% of the applications are approved, while "
                    f"{denied_percent:.2f}% faced denial.")

    # Add text at the bottom of the figure
    plt.figtext(0.5, -0.1, insight_text, wrap=True, horizontalalignment='center', fontsize=10)

    # Save the figure
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
