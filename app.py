import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------ Page Setup ------------------
st.set_page_config(page_title="Healthcare Analysis Dashboard", layout="wide")
st.title('🩺 Healthcare Data Analysis Dashboard')
st.write('Project by: Kasra Abdi')

# ------------------ Data Loading and Preparation ------------------
@st.cache_data
def load_data():
    df = pd.read_csv('healthcare_dataset.csv')
    df = df.drop(columns=['Name'])
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
    df['Admission Year'] = df['Date of Admission'].dt.year
    return df

df = load_data()

# ------------------ Sidebar Filters ------------------
st.sidebar.header('Please Filter Here:')

diseases = df['Medical Condition'].unique()
selected_diseases = st.sidebar.multiselect(
    'Select Medical Condition:',
    options=diseases,
    default=diseases
)

gender_options = ['All'] + list(df['Gender'].unique())
selected_gender = st.sidebar.radio(
    'Select Gender:',
    options=gender_options,
    index=0
)

min_age = int(df['Age'].min())
max_age = int(df['Age'].max())
selected_age = st.sidebar.slider(
    'Select Age Range:',
    min_value=min_age,
    max_value=max_age,
    value=(min_age, max_age)
)

# ------------------ Filtering Logic ------------------
df_selection = df[df['Medical Condition'].isin(selected_diseases)]

if selected_gender != 'All':
    df_selection = df_selection[df_selection['Gender'] == selected_gender]

df_selection = df_selection[
    (df_selection['Age'] >= selected_age[0]) & (df_selection['Age'] <= selected_age[1])
]

if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()


# ------------------ Main Page ------------------
st.header('Filtered Data Overview')
st.dataframe(df_selection)


# ------------------ Charts (All Included) ------------------
st.header('Visualizations')

st.subheader('1. Distribution of Medical Conditions')
fig, ax = plt.subplots()
sns.countplot(data=df_selection, y='Medical Condition', ax=ax)
st.pyplot(fig)

st.subheader('2. Gender Distribution')
fig, ax = plt.subplots()
sns.countplot(data=df_selection, x='Gender', ax=ax)
st.pyplot(fig)

st.subheader('3. Age Distribution')
fig, ax = plt.subplots()
sns.histplot(data=df_selection, x='Age', bins=20, kde=True, ax=ax)
st.pyplot(fig)

st.subheader('4. Medical Condition by Gender')
fig, ax = plt.subplots()
sns.countplot(data=df_selection, y='Medical Condition', hue='Gender', ax=ax)
st.pyplot(fig)

st.subheader('5. Medical Condition by Blood Type')
fig, ax = plt.subplots()
sns.countplot(data=df_selection, y='Medical Condition', hue='Blood Type', ax=ax)
st.pyplot(fig)

st.subheader('6. Admission Type Distribution (Pie Chart)')
admission_counts = df_selection['Admission Type'].value_counts()
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(admission_counts, labels=admission_counts.index, autopct='%1.1f%%', startangle=140)
ax.axis('equal')
st.pyplot(fig)

st.subheader('7. Billing Amount by Medical Condition')
fig, ax = plt.subplots()
sns.boxplot(data=df_selection, x='Billing Amount', y='Medical Condition', ax=ax)
st.pyplot(fig)

st.subheader('8. Billing Amount by Admission Type')
fig, ax = plt.subplots()
sns.boxplot(data=df_selection, x='Admission Type', y='Billing Amount', ax=ax)
st.pyplot(fig)

st.subheader('9. Age vs. Billing Amount')
fig, ax = plt.subplots()
sns.scatterplot(data=df_selection, x='Age', y='Billing Amount', ax=ax)
ax.grid(True)
st.pyplot(fig)

st.subheader('10. Trend of Medical Conditions Over Years')
yearly_counts = df_selection.groupby(['Admission Year', 'Medical Condition']).size().reset_index(name='Number of Patients')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=yearly_counts, x='Admission Year', y='Number of Patients', hue='Medical Condition', marker='o', ax=ax)
ax.grid(True)
st.pyplot(fig)