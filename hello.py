
import streamlit as st
import pandas as pd
import numpy as np
import time

'데이터 분석 진행 중...'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'진행프로세스 {i+1}%')
  bar.progress(i + 1)
  time.sleep(0.05)

'분석 완료!'




df = pd.DataFrame({
    'fruit name':['수박', '사과', '딸기'],
    'fruit size':[10, 5, 2]
})
option = st.selectbox(
    '당신이 좋아하는 과일은?',
     df['fruit name'])

'You selected: ', option


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['피자', '치킨', '파스타'])

st.line_chart(chart_data)

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.50, 127.00],
    columns=['lat', 'lon'])

st.map(map_data)


st.title('퇴근 후 딴짓')
st.write('# 퇴근 후 딴짓')
st.write("hello world")

df = pd.DataFrame({
    'fruit name':['수박', '사과', '딸기'],
    'fruit size':[10, 5, 2]
})

df


df = pd.DataFrame({
    '과일 이름':['수박', '사과', '딸기'],
    '과일 크기':[10, 5, 2]
})

df

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


# st.write("Here's our first attempt at using data to create a table:")

# # Draw a line chart
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
# st.line_chart(chart_data)

# # Plot a map
# map_data = pd.DataFrame(
#     np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)


# # Use checkboxes to show/hide data
# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data

# # Use a selectbox for options
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })
# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option


# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'