# 🩺 Healthcare Data Analysis Dashboard

This project is an interactive dashboard built with Streamlit for analyzing and visualizing a comprehensive healthcare dataset. The primary goal is to uncover patterns and relationships between patient demographics, medical conditions, and treatment costs.

This dashboard was developed as a final project for a data analysis course.

---

## ✨ Features

* **📈 Comprehensive Statistical Analysis:** Displays patient distributions by medical condition, gender, and age ranges.
* **📊 Interactive Visualizations:** Includes dynamic bar charts, histograms, box plots, and pie charts for a deeper understanding of the data.
* **🔍 Dynamic Filtering:** Allows users to filter the data by medical condition, gender, and age, with all charts updating in real-time.
* **⏳ Time-Series Analysis:** Explores trends in patient admissions for various medical conditions over the years.
* **💰 Cost Analysis:** Compares and examines billing amounts across different medical conditions and admission types.

---

## 📊 Dataset

The analysis is based on the `healthcare_dataset.csv` file, which contains records for 10,000 patients. Key columns include:

* **Age, Gender, Blood Type:** Patient demographic information.
* **Medical Condition:** The primary diagnosis (e.g., Asthma, Cancer, Diabetes).
* **Date of Admission, Discharge Date:** Admission and discharge dates.
* **Billing Amount:** The total amount billed to the patient.
* **Admission Type:** The reason for admission (e.g., Emergency, Elective, Urgent).
* **Doctor, Hospital, Insurance Provider:** Information on the healthcare providers.

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3.12
* **Libraries:**
    * **Streamlit:** For building the interactive web dashboard.
    * **Pandas:** For data cleaning, manipulation, and analysis.
    * **Seaborn & Matplotlib:** For creating a wide range of data visualizations.

---

## 🚀 Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Kasraabdi/analysis_of_healthcare_dataset.git](https://github.com/Kasraabdi/analysis_of_healthcare_dataset.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd analysis_of_healthcare_dataset
    ```

3.  **Install the required libraries:**
    ```bash
    pip install streamlit pandas seaborn matplotlib
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    After running this command, the application will open in your web browser.

---

### Author
* **Kasra Abdi**