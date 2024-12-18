# visualizations/generate_marital_status_distribution.py

import matplotlib.pyplot as plt
import seaborn as sns

def generate_marital_status_distribution(df, output_path):
    """
    Generates a countplot showing the relationship between marital status and loan decisions.

    Args:
        df (DataFrame): The DataFrame to analyze.
        output_path (str): The path where the plot should be saved.
    """
    plt.figure(figsize=(8, 10))

    # Filter data based on Loan_Status
    approved_loans = df[df['Loan_Status'] == 1]
    denied_loans = df[df['Loan_Status'] == 0]

    # Plot approved loans in blue
    sns.countplot(x='Married', data=approved_loans, color='blue', label='Approved')

    # Plot denied loans in red
    sns.countplot(x='Married', data=denied_loans, color='red', label='Denied')

    plt.title('Analyzing the Relationship Between Marital Status and Loan Decisions')
    x_labels = ['Un-married', 'Married']
    plt.xticks([0, 1], x_labels)
    plt.xlabel('Marital Status')
    plt.ylabel('Count')
    plt.legend()

    # Calculate counts for each marital status and approval/denial
    married_approved = approved_loans['Married'].value_counts().get(1, 0)
    married_denied = denied_loans['Married'].value_counts().get(1, 0)
    unmarried_approved = approved_loans['Married'].value_counts().get(0, 0)
    unmarried_denied = denied_loans['Married'].value_counts().get(0, 0)

    insight_text = (
        f"This plot analyzes the relationship between applicant marital status and loan approval/denial rates. \n"
        f"Married applicants:\n"
        f"- Approved: {married_approved}\n"
        f"- Denied: {married_denied}\n"
        f"Un-married applicants:\n"
        f"- Approved: {unmarried_approved}\n"
        f"- Denied: {unmarried_denied}")

    plt.figtext(0.5, -0.1, insight_text, wrap=True, horizontalalignment='center', fontsize=10)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()

