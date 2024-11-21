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
st.dataframe(mobile)   

figure, series1 = plt.subplots()
sns.lineplot(data=mobile,
             x="Age",
             y="Number of Apps Installed",
             estimator="mean",
             errorbar=None,
                ax=series1
        )              

st.pyplot(figure)