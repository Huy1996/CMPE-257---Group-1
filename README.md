# Heart Disease Prediction - Data Processing and EDA

## Overview
This project focuses on predicting heart disease using machine learning techniques. The dataset is initially stored in SAS XPT format and needs preprocessing before model training. The workflow includes:

1. **Data Conversion:** Converting the XPT file into a CSV format.
2. **Feature Extraction:** Extracting metadata (features, encoded values, and their original values).
3. **Exploratory Data Analysis (EDA):** Cleaning the dataset, performing statistical analysis, and generating insights.
4. **Model Development:** The cleaned dataset will be used for training and evaluating machine learning models.

## Project Structure
```
Project
│── Original Data/                                                          # Contains original dataset (not published on GitHub) 
│   ├── LLCP2023.XPT                                                        # Original heart disease dataset in XPT format 
│   ├── USCODE23_LLCP_091024.HTML                                           # Encoded feature and value mappings 
│── .gitignore                                                              # Excludes sensitive/original data from GitHub 
│── convert_csv.py                                                          # Converts XPT file to CSV 
│── extract_label.py                                                        # Extracts SAS variable metadata from the HTML file 
│── data.csv                                                                # Converted CSV dataset 
│── EDA.ipynb                                                               # Jupyter notebook for EDA and data preprocessing 
│── LLCP2023.csv                                                            # Coverted data from XPT format to CSV dataset
```

## File Descriptions

### **Original Data/** (Not Published on GitHub) https://drive.google.com/file/d/13Bj0if92el3IzpwI5s6bjrJvdg-akHoL/view?usp=drive_link
- **`LLCP2023.XPT`**: The original heart disease dataset in SAS Transport (XPT) format.  
- **`USCODE23_LLCP_091024.HTML`**: Contains encoded feature names and values from the dataset.

### **Scripts**
- **`convert_csv.py`**: Reads the XPT file and converts it into a CSV format.  
- **`extract_label.py`**: Implements `parse_sas_html`, which scans the HTML file and extracts SAS variables, feature names, encoded values, and their original values.

### **Exploratory Data Analysis (EDA)**
- **`EDA.ipynb`**: Jupyter notebook containing the EDA process. It includes data cleaning, statistical analysis, feature selection, and visualization. The final cleaned dataset is saved as a CSV file for machine learning.  
- **`eda_report.html`**: An automatically generated HTML report summarizing the findings from EDA.


## Steps to Run the Project

### **1. Convert the XPT dataset to CSV**
Run the following command to convert the original XPT file into a CSV format:
```sh
python convert_csv.py
```

### **2. Perform Exploratory Data Analysis (EDA)**
To analyze and preprocess the dataset, follow these steps:

1. Open Jupyter Notebook:
   ```sh
   jupyter notebook
   ```

2. Open the **`EDA.ipynb`** file inside Jupyter Notebook.

3. Run all the cells in the notebook to:
    - Load and inspect the dataset.
    - Handle missing values and outliers.
    - Perform statistical analysis and data visualization.
    - Generate feature distributions and correlation matrices.
    - Save the cleaned dataset as LLCP2023.csv for model training.


## Requirements

Ensure you have the necessary Python libraries installed before running the scripts.  
Install dependencies using:
```sh
pip install pandas numpy matplotlib seaborn scikit-learn jupyter bs4 pyreadstat
```
Or
```sh
pip install -r requirements.txt
```
