import csv
import statistics
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

__author__ = "James Thayer"
__date__ = "10/18/2023"
__assignment__ = "SER594: MS3"

# Load data from the CSV file
filename = 'data_processed/processed_data.csv'

with open(filename, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    records = [record for record in reader]

# Min, Max, Median
def quantitative_analysis(data, column_name):
    values = [entry[column_name] for entry in data if entry[column_name] != 'NA']
    values = [float(value) for value in values]
    column_min = min(values)
    column_max = max(values)
    column_median = statistics.median(values)
    return column_min, column_max, column_median

# Categories
def qualitative_analysis(data, column_name):
    categories = [entry[column_name] for entry in data if entry[column_name] != 'NA']
    category_counts = Counter(categories)
    num_categories = len(category_counts)
    most_frequent_category, most_frequent_count = category_counts.most_common(1)[0]
    least_frequent_category, least_frequent_count = category_counts.most_common()[-1]
    return num_categories, most_frequent_category, most_frequent_count, least_frequent_category, least_frequent_count

# Write to summary.txt
def write_to_summary(summary_filedir):
    with open(summary_filedir, 'w') as summary_file:
        sys.stdout = summary_file

        media_h_min, media_h_max, media_h_median = quantitative_analysis(records, 'media_h')
        grades_min, grades_max, grades_median = quantitative_analysis(records, 'grades')
        mmi_score_min, mmi_score_max, mmi_score_median = quantitative_analysis(records, 'mmi_score')
        age_min, age_max, age_median = quantitative_analysis(records, 'age')

        num_gender_categories, most_frequent_gender, most_frequent_count, least_frequent_gender, least_frequent_count = qualitative_analysis(records, 'school_year')

        summary_file.write(f"{'':<15}{'Min':<10}{'Max':<10}{'Median':<10}\n")
        summary_file.write(f"{'media hours':<15}{media_h_min:<10}{media_h_max:<10}{media_h_median:<10}\n")
        summary_file.write(f"{'grades':<15}{grades_min:<10}{grades_max:<10}{grades_median:<10}\n")
        summary_file.write(f"{'mmi score':<15}{mmi_score_min:<10}{mmi_score_max:<10}{mmi_score_median:<10}\n")
        summary_file.write(f"{'age':<15}{age_min:<10}{age_max:<10}{age_median:<10}\n")

        summary_file.write(f"\n{'':<15}{'Num Categories':<20}{'Most Frequent':<20}{'Least Frequent':<20}\n")
        summary_file.write(f"{'school year':<15}{num_gender_categories:<20}{most_frequent_gender:<20}{least_frequent_gender:<20}\n")

    sys.stdout = sys.__stdout__

# Compute pairwise correlations
def pairwise_correlations(records):
    record = pd.DataFrame(records)

    quantitative_columns = ['media_h', 'grades', 'mmi_score', 'age']

    for column in quantitative_columns:
        record[column] = record[column].apply(lambda x: np.nan if x == 'NA' else float(x))

    correlation_matrix = record[quantitative_columns].corr()

    output_filename = 'data_processed/correlations.txt'
    with open(output_filename, 'w') as output_file:
        output_file.write(correlation_matrix.to_string())

# Scatter plot for media hours vs grades
def mediah_vs_grades(records):
    data = pd.DataFrame(records)
    data = data[data['media_h'] != 'NA']
    data = data[data['grades'] != 'NA']

    media_h_values = data['media_h'].astype(float)
    grades_values = data['grades'].astype(float)

    plt.figure()
    plt.scatter(media_h_values, grades_values)
    plt.xlabel('Media Hours')
    plt.ylabel('Grades')
    plt.title('Media Hours vs. Grades')
    plt.savefig("visuals/media_hours_vs_grades.png")

# Scatter plot for multiple media vs grades
def mmi_score_vs_grades(records):
    data = pd.DataFrame(records)
    data = data[data['mmi_score'] != 'NA']
    data = data[data['grades'] != 'NA']

    mmi_score_values = data['mmi_score'].astype(float)
    grades_values = data['grades'].astype(float)

    plt.figure()
    plt.scatter(mmi_score_values, grades_values)
    plt.xlabel('MMI Score')
    plt.ylabel('Grades')
    plt.title('MMI Score vs. Grades')
    plt.savefig("visuals/mmi_score_vs_grades.png")

# Scatter plot for media hours vs age
def mediah_vs_age(records):
    data = pd.DataFrame(records)
    data = data[data['media_h'] != 'NA']
    data = data[data['age'] != 'NA']

    media_h_values = data['media_h'].astype(float)
    age_values = data['age'].astype(float)

    plt.figure()
    plt.scatter(media_h_values, age_values)
    plt.xlabel('Media Hours')
    plt.ylabel('Age')
    plt.title('Media Hours vs. Age')
    plt.savefig("visuals/media_hours_vs_age.png")

# Scatter plot for media hours vs mmi score
def mediah_vs_mmi_score(records):
    data = pd.DataFrame(records)
    data = data[data['media_h'] != 'NA']
    data = data[data['mmi_score'] != 'NA']

    media_h_values = data['media_h'].astype(float)
    mmi_score_values = data['mmi_score'].astype(float)

    plt.figure()
    plt.scatter(media_h_values, mmi_score_values)
    plt.xlabel('Media Hours')
    plt.ylabel('MMI Score')
    plt.title('Media Hours vs. MMI Score')
    plt.savefig("visuals/media_hours_vs_mmi_score.png")

# Histogram for school_year
def school_year_histogram(records):
    data = pd.DataFrame(records)
    data = data[data['school_year'] != 'NA']

    number_of_bins = len(data['school_year'].unique())

    plt.figure()
    plt.hist(data['school_year'], bins=number_of_bins, edgecolor='k')
    plt.xlabel('School Year')
    plt.ylabel('Frequency')
    plt.title('School Year Histogram')
    plt.savefig("visuals/school_year_histogram.png")
