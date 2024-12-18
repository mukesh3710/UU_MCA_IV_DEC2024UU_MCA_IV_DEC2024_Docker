# visualizations/generate_term_vs_loan_status_bar_chart.py

import matplotlib.pyplot as plt
import seaborn as sns

def generate_term_vs_loan_status_bar_chart(df, output_path):
    """
    Generates a grouped bar chart comparing loan approval and denial rates based on the loan term.
    The chart will show the distribution of approvals and denials for each loan term.

    Args:
        df (DataFrame): The DataFrame to analyze.
        output_path (str): The path where the plot should be saved.
    """
    # Ensure 'Term' and 'Loan_Status' are numeric (if necessary)
    df['Term'] = df['Term'].astype(str)  # Convert Term to string for better labeling
    df['Loan_Status'] = df['Loan_Status'].astype(int)

    # Group by 'Term' and 'Loan_Status' to count approvals and denials
    term_loan_status_counts = df.groupby(['Term', 'Loan_Status']).size().unstack(fill_value=0)
    term_loan_status_counts.columns = ['Denied', 'Approved']  # Rename columns for clarity

    # Create a grouped bar chart
    term_loan_status_counts.plot(kind='bar', stacked=False, figsize=(10, 6),
                                  color=['red', 'green'], width=0.8)

    # Add labels and title
    plt.title('Loan Approval and Denial Distribution by Loan Term')
    plt.xlabel('Loan Term (Years)')
    plt.ylabel('Number of Applicants')
    plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
    plt.legend(title='Loan Status', labels=['Denied', 'Approved'], loc='upper right')

    # Add insight text to explain the plot
    insight_text = (
        "This grouped bar chart shows the distribution of loan approvals (green) and denials (red) "
        "based on the loan term (e.g., 15 or 30 years). Each bar represents the number of approved or denied loans "
        "for each loan term. The chart helps identify how loan term affects the loan approval/denial rate."
    )
    plt.figtext(0.5, -0.15, insight_text, wrap=True, horizontalalignment='center', fontsize=10)

    # Save the plot to the specified output path
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
