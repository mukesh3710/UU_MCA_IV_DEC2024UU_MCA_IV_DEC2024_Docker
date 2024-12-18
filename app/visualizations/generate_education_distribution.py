# visualizations/generate_education_distribution.py

import matplotlib.pyplot as plt
import seaborn as sns

def generate_education_distribution(df, output_path):
    """
    Generates a countplot showing loan approval distribution based on education level.

    Args:
        df (DataFrame): The DataFrame to analyze.
        output_path (str): The path where the plot should be saved.
    """
    df['Education'] = df['Education'].replace({0: 'Graduate', 1: 'Not Graduate'})
    plt.figure(figsize=(8, 10))

    # Filter data based on Loan_Status
    approved_loans = df[df['Loan_Status'] == 1]
    denied_loans = df[df['Loan_Status'] == 0]

    # Plot approved loans in blue
    sns.countplot(x='Education', data=approved_loans, color='blue', label='Approved')

    # Plot denied loans in red
    sns.countplot(x='Education', data=denied_loans, color='red', label='Denied')

    plt.title('Approval count based on Education')
    plt.xlabel('Education')
    plt.ylabel('Count')
    plt.legend()

    # Calculate counts for each education level and approval/denial
    graduate_approved = approved_loans['Education'].value_counts().get('Graduate', 0)
    graduate_denied = denied_loans['Education'].value_counts().get('Graduate', 0)
    not_graduate_approved = approved_loans['Education'].value_counts().get('Not Graduate', 0)
    not_graduate_denied = denied_loans['Education'].value_counts().get('Not Graduate', 0)

    insight_text = (f" This plot shows the Approval of loan based on education levels among the applicants. \n"
                    f"Graduate:\n"
                    f"- Approved: {graduate_approved}\n"
                    f"- Denied: {graduate_denied}\n"
                    f"Not Graduate:\n"
                    f"- Approved: {not_graduate_approved}\n"
                    f"- Denied: {not_graduate_denied}")

    plt.figtext(0.5, -0.1, insight_text, wrap=True, horizontalalignment='center', fontsize=10)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
