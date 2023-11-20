import wf_dataprocessing
import wf_visualization

__author__ = "James Thayer"
__date__ = "10/18/2023"
__assignment__ = "SER594: MS3"

if __name__ == "__main__":
    input_filename = 'data_original/mmi_kids_gva_v2021.2.csv'
    output_filename = 'processed_data.csv'

    # Data processing methods
    records = wf_dataprocessing.load_csv(input_filename)
    records = wf_dataprocessing.floor_age_values(records)
    records = wf_dataprocessing.truncate_mmi_score(records)

    # Save the processed data to a new CSV file in the 'data_processed/' directory
    wf_dataprocessing.save_processed_data_to_csv(records)

    # Write qualitative and quantitative data to summary.txt in 'data_processed/' directory
    wf_visualization.write_to_summary('data_processed/summary.txt')
    wf_visualization.pairwise_correlations(records)

    # Create graphs
    wf_visualization.mediah_vs_grades(records)
    wf_visualization.mmi_score_vs_grades(records)
    wf_visualization.mediah_vs_age(records)
    wf_visualization.mediah_vs_mmi_score(records)
    wf_visualization.school_year_histogram(records)