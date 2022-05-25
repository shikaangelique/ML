import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt


trends = TrendReq()
trends.build_payload(kw_list=["Online dating"])
data = trends.interest_by_region()
data = data.sort_values(by="Online dating", ascending=False)
data = data.head(10)
# print(data)

data.reset_index().plot(x="geoName", y="Online dating",
                        figsize=(20,15), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()

other_data = trends.interest_over_time()
fig, ax = plt.subplots(figsize=(20, 15))
other_data['Online dating'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Online dating', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()