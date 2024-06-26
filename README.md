# Student Engagement Analysis

This project aims to analyze student engagement data to understand its relationship with various factors such as media usage, grades, age, and more. The code provided includes data processing, visualization, machine learning model training, and evaluation.

## Instructions:

1. **Clone Repository:**
   ```bash
   git clone https://github.com/jethayer/student-engagement.git

2. **Navigate to Project Directory:**
   ```bash
   cd student-engagement

4. **Setup Environment:**
   Ensure Python 3 is installed.
   Install required packages:
   ```bash
   pip install -r requirements.txt

6. **Run Code:**
   Execute the wf_core.py file:
   ```bash
   python wf_core.py

Important Files:  
The Visuals folder contains all charts and graphs generated by the program.  
  
wf_core.py: Main script to execute the entire workflow, including data processing, visualization, model training, and evaluation.  
wf_dataprocessing.py: Contains functions for loading, processing, and saving data.  
wf_ml_evaluation.py: Module for evaluating machine learning models using metrics like Mean Squared Error (MSE) and R-squared.  
wf_ml_prediction.py: Module for making predictions using trained machine learning models.  
wf_ml_training.py: Module for training machine learning models.  
wf_visualization.py: Module for generating various visualizations such as scatter plots and histograms.  

Notes:
Ensure the required data files are present in the specified directories (data_original/, data_processed/) as per the code.  
Output files such as visualizations and evaluation summaries will be saved in their respective directories (visuals/, evaluation/).  
