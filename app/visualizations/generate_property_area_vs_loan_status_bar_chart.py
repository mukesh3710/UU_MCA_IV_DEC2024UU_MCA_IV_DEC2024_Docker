# visualizations/generate_property_area_vs_loan_status_bar_chart.py

import matplotlib.pyplot as plt
import seaborn as sns

def generate_property_area_vs_loan_status_bar_chart(df, output_path):
    """
    Generates a horizontal grouped bar chart comparing loan approval and denial rates based on property area.
    The chart will show the distribution of approvals and denials for each property area.

    Args:
        df (DataFrame): The DataFrame to analyze.
        output_path (str): The path where the plot should be saved.
    """
    # Ensure 'Loan_Status' is numeric (if necessary)
    df['Loan_Status'] = df['Loan_Status'].astype(int)

    # Map numeric 'Property_Area' values to actual names (if needed)
    property_area_mapping = {0: 'Urban', 1: 'Semiurban', 2: 'Rural'}
    df['Property_Area'] = df['Property_Area'].map(property_area_mapping)

    # Group by 'Property_Area' and 'Loan_Status' to count approvals and denials
    property_loan_status_counts = df.groupby(['Property_Area', 'Loan_Status']).size().unstack(fill_value=0)
    property_loan_status_counts.columns = ['Denied', 'Approved']  # Rename columns for clarity

    # Reset index to have 'Property_Area' as a column for plotting
    property_loan_status_counts = property_loan_status_counts.reset_index()

    # Create the horizontal grouped bar chart
    plt.figure(figsize=(10, 6))
    ax = property_loan_status_counts.plot(kind='barh', stacked=False, color=['red', 'green'],
                                          width=0.8, edgecolor='black', figsize=(10, 6))

    # Update y-axis labels to show property area names (not numbers)
    ax.set_yticklabels(property_loan_status_counts['Property_Area'], rotation=0)

    # Add labels and title
    plt.title('Loan Approval and Denial Distribution by Property Area')
    plt.xlabel('Number of Applicants')
    plt.ylabel('Property Area')
    plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
    plt.legend(title='Loan Status', labels=['Denied', 'Approved'], loc='upper right')

    # Add insight text to explain the plot
    insight_text = (
        "This horizontal grouped bar chart shows the distribution of loan approvals (green) and denials (red) "
        "based on the property area (Urban, Semiurban, Rural). Each bar represents the number of approved or denied loans "
        "for each property area. The chart helps identify patterns in loan approval/denial across different areas."
    )
    plt.figtext(0.5, -0.2, insight_text, wrap=True, horizontalalignment='center', fontsize=10)

    # Save the plot to the specified output path
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
