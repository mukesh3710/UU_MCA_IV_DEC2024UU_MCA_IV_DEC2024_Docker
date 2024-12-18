# visualizations/generate_gender_vs_loan_status_bar_chart.py

import matplotlib.pyplot as plt
import seaborn as sns

def generate_gender_vs_loan_status_bar_chart(df, output_path):
    """
    Generates a vertical grouped bar chart comparing loan approval and denial rates based on gender.
    The chart will show the distribution of approvals and denials for each gender.

    Args:
        df (DataFrame): The DataFrame to analyze.
        output_path (str): The path where the plot should be saved.
    """
    # Ensure 'Loan_Status' is numeric (if necessary)
    df['Loan_Status'] = df['Loan_Status'].astype(int)

    # Map numeric 'Gender' values to actual labels ('Male' and 'Female')
    gender_mapping = {0: 'Female', 1: 'Male'}
    df['Gender'] = df['Gender'].map(gender_mapping)

    # Group by 'Gender' and 'Loan_Status' to count approvals and denials
    gender_loan_status_counts = df.groupby(['Gender', 'Loan_Status']).size().unstack(fill_value=0)
    gender_loan_status_counts.columns = ['Denied', 'Approved']  # Rename columns for clarity

    # Reset index to have 'Gender' as a column for plotting
    gender_loan_status_counts = gender_loan_status_counts.reset_index()

    # Create the vertical grouped bar chart
    plt.figure(figsize=(8, 6))

    # Plot the data with 'Gender' on x-axis and 'Loan_Status' on color
    ax = gender_loan_status_counts.plot(kind='bar', x='Gender', stacked=False, color=['red', 'green'],
                                        width=0.8, edgecolor='black', figsize=(8, 6))

    # Manually set x-ticks labels to 'Male' and 'Female'
    ax.set_xticklabels(gender_loan_status_counts['Gender'], rotation=0)

    # Add labels and title
    plt.title('Loan Approval and Denial Distribution by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Number of Applicants')
    plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
    plt.legend(title='Loan Status', labels=['Denied', 'Approved'], loc='upper right')

    # Add insight text to explain the plot
    insight_text = (
        "This vertical grouped bar chart shows the distribution of loan approvals (green) and denials (red) "
        "based on gender (Male, Female). Each bar represents the number of approved or denied loans for each gender. "
        "The chart helps identify patterns in loan approval/denial based on gender."
    )
    plt.figtext(0.5, -0.2, insight_text, wrap=True, horizontalalignment='center', fontsize=10)

    # Save the plot to the specified output path
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()