import os
import io
import matplotlib
from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from PyPDF2 import PdfWriter
from PIL import Image
matplotlib.use('Agg')  # Use non-GUI backend


# Import visualization modules
import visualizations.generate_correlation_matrix as correlation_matrix
import visualizations.generate_education_distribution as education_distribution
import visualizations.generate_loan_status_distribution as loan_status_distribution
import visualizations.generate_loan_amount as loan_amount
import visualizations.generate_income_distribution as income_distribution
import visualizations.generate_marital_status_distribution as marital_status_distribution
import visualizations.generate_credit_history_comparison as credit_history_comparison
import visualizations.generate_term_vs_loan_status_bar_chart as term_vs_loan_status_bar_chart
import visualizations.generate_property_area_vs_loan_status_bar_chart as property_area_vs_loan_status_bar_chart
import visualizations.generate_gender_vs_loan_status_bar_chart as gender_vs_loan_status_bar_chart

import visualizations.convert_png_to_pdf as convert_to_pdf


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download_template')
def download_template():
    return send_file('static/template.csv', as_attachment=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Process the uploaded file
        processed_file_path = process_csv(filepath)
        if processed_file_path:
            # Perform further processing on the processed file
            pdf_file_path = further_processing_and_generate_pdf(processed_file_path)
            if pdf_file_path:
                return send_file(pdf_file_path, as_attachment=True)
            else:
                return "Error generating visualizations or PDF", 500
        else:
            return "Error processing file", 500  # Handle errors from process_csv
    return "An unexpected error occurred.", 500


def process_csv(filepath):
    """
    Reads the CSV file, selects relevant columns, handles missing values,
    and saves a processed version to the 'uploads' folder.

    Args:
        filepath (str): Path to the input CSV file.

    Returns:
        str: Path to the processed CSV file (if successful), None otherwise.
    """
    try:
        df = pd.read_csv(filepath)

        # Define the desired columns
        selected_columns = ['Gender', 'Married', 'Education', 'Income',
                            'LoanAmount', 'Term', 'Credit_History',
                            'Property_Area', 'Loan_Status']

        # Check if at least 2 selected columns exist
        existing_columns = list(set(selected_columns).intersection(set(df.columns)))
        if len(existing_columns) < 2 or 'Loan_Status' not in existing_columns:
            return None  # Return None if less than 2 selected columns or 'Loan_Status' is missing

        df_selected = df[existing_columns]

        # Check for missing values
        print(df_selected.isna().sum())

        # Handle missing values (e.g., drop rows with missing values)
        df_selected = df_selected.dropna()

        # Save the processed DataFrame to the 'uploads' folder
        processed_filepath = os.path.join(os.path.dirname(filepath), 'processed_' + os.path.basename(filepath))
        df_selected.to_csv(processed_filepath, index=False)

        return processed_filepath

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"An error occurred while processing the CSV file: {e}")
        return None


def further_processing_and_generate_pdf(processed_filepath):
    """
    Performs further processing on the cleaned CSV, generates visualizations,
    and converts them to a PDF.

    Args:
        processed_filepath (str): Path to the processed CSV file.

    Returns:
        str: Path to the output PDF file (if successful), None otherwise.
    """
    try:
        df = pd.read_csv(processed_filepath)

        # Encode categorical variables
        label_encoder = preprocessing.LabelEncoder()
        for column in ['Gender', 'Married', 'Self_Employed', 'Property_Area', 'Education', 'Loan_Status']:
            if column in df.columns:
                df[column] = label_encoder.fit_transform(df[column])

        # Choose the visualization type based on request
        visualizations = []

        # Always generate the correlation matrix visualization
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'correlation_matrix.png')
        correlation_matrix.generate_correlation_matrix(df, filepath)
        visualizations.append(filepath)

        # Always generate the loan_status_distribution
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'loan_status_distribution.png.png')
        loan_status_distribution.generate_loan_status_distribution(df, filepath)
        visualizations.append(filepath)

        # Conditionally generate the education distribution visualization if 'Education' column is present
        if 'Education' in df.columns:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'education_distribution.png')
            education_distribution.generate_education_distribution(df, filepath)
            visualizations.append(filepath)

        # Conditionally generate the loan amount visualization if 'LoanAmount' column is present
        if 'LoanAmount' in df.columns:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'loan_amount.png')
            loan_amount.generate_loan_amount(df, filepath)
            visualizations.append(filepath)

        # Conditionally generate the Income visualization if 'Income' column is present
        if 'Income' in df.columns:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'income_distribution.png')
            income_distribution.generate_income_distribution(df, filepath)
            visualizations.append(filepath)

        # Conditionally generate the marital_status visualization if 'Married' column is present
        if 'Married' in df.columns:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'marital_status_distribution.png')
            marital_status_distribution.generate_marital_status_distribution(df, filepath)
            visualizations.append(filepath)

        # Conditionally generate the credit_history_comparison visualization if 'Credit_History' column is present
        if 'Credit_History' in df.columns:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'marital_status_distribution.png')
            credit_history_comparison.generate_credit_history_comparison(df, filepath)
            visualizations.append(filepath)

        # Conditionally generate the term_vs_loan_status visualization if 'Term' column is present
        if 'Term' in df.columns:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'term_vs_loan_status_bar_chart.png')
            term_vs_loan_status_bar_chart.generate_term_vs_loan_status_bar_chart(df, filepath)
            visualizations.append(filepath)

        # Conditionally generate the Property_Area visualization if 'Property_Area' column is present
        if 'Property_Area' in df.columns:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'property_area_vs_loan_status_bar_chart.png')
            property_area_vs_loan_status_bar_chart.generate_property_area_vs_loan_status_bar_chart(df, filepath)
            visualizations.append(filepath)

        # Conditionally generate the Gender visualization if 'Gender' column is present
        if 'Gender' in df.columns:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'generate_gender_vs_loan_status_bar_chart.png')
            gender_vs_loan_status_bar_chart.generate_gender_vs_loan_status_bar_chart(df, filepath)
            visualizations.append(filepath)


        # Convert PNGs to a single PDF
        output_pdf = os.path.join(app.config['UPLOAD_FOLDER'], 'output.pdf')
        convert_to_pdf.convert_png_to_pdf(visualizations, output_pdf)

        return output_pdf

    except Exception as e:
        print(f"An error occurred during further processing: {e}")
        return None


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host="0.0.0.0", port=9000)
