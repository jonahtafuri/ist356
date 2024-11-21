# ## Challenge 6-1-1

# Using the `data/mobile_user_behavior_dataset.csv` file, create a streamlit to show:

# 1. the data in a dataframe 
# 2. select a category: gender or operating system
# 3. select a measure: Data useage, battery drain, screen on time, or app useage time
# 4. show a bar plot of the average of 3. by 2.

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")

st.write(mobile.columns)
category = st.selectbox("Pick a category:", ["Operating System", "Gender"])
measure = st.selectbox("Pick a measure:", ["App Usage Time (min/day)", 
                                           "Screen On Time (hours/day)", 
                                           "Battery Drain (mAh/day)",
                                           "Data Usage (MB/day)"])

plot, series = plt.subplots()
sns.barplot(data=mobile,
            x = category,
            y = measure,
            estimator = "mean",
            errorbar = None,
            order = mobile.groupby(category)[measure].mean().sort_values(ascending=False).index,
            ax = series).set_title("Average Data Useage by Gender")

st.pyplot(plot)
                                   
