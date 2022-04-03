import pandas as pd
import numpy as np
import seaborn as sns; sns.set_theme()
import statsmodels
import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages

pdf = PdfPages("Airline Plots.pdf")

## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

custom_params = {"axes.spines.right": False, "axes.spines.top": False}

## Task 1
ax = sns.displot(flight.coach_price)
ax = sns.set_theme(rc=custom_params)
plt.xlabel("Price in Dollars")
plt.title("Distribution of coach prices")
#plt.show()
plt.savefig(pdf, format = "pdf")
plt.clf()

## Task 2

eight = flight.coach_price[flight.hours == 8]
ax1 = sns.displot(eight)
ax1 = sns.set_theme(rc=custom_params)
plt.title("Distribution")
# plt.show()
plt.savefig(pdf, format = "pdf")
plt.clf()

## Task 3
late_flights = flight[(flight.delay >= 1) & (flight.delay < 30)]
not_late = flight[flight.delay == 0]

ax2 = plt.subplots(figsize=(12,7))
ax2 = sns.violinplot(x="day_of_week", y="delay", hue = "redeye", data=late_flights)
ax2 = sns.set_theme(rc=custom_params)
plt.title("Delayed Flights")
plt.ylabel("Minutes Delayed")
plt.xlabel("Day")
# plt.show()
plt.savefig(pdf, format = "pdf")

ax3 = plt.subplots(figsize=(12,7))
sns.violinplot(x="day_of_week", y="hours", data=not_late)
ax3 = sns.set_theme(rc=custom_params)
plt.title("On time flights")
# plt.show()
plt.savefig(pdf, format = "pdf")
plt.clf()

## Task 4

perc = 0.05
sample_group = flight.sample(n = int(flight.shape[0]*perc))
ax5=sns.relplot(data=sample_group, x="coach_price", y="firstclass_price", hue="redeye", col="inflight_wifi", row="inflight_entertainment")
ax5.set(xlabel= "Coach Price", ylabel='First Class Price')
# plt.show()
plt.savefig(pdf, format = "pdf")
plt.clf()

## Task 5
#f, ax5 = plt.subplots(figsize=(12,7))
sns.relplot(data=sample_group, x= "miles", y='passengers', s=2)
sns.set_theme(rc=custom_params)
# plt.show()
plt.savefig(pdf, format = "pdf")
plt.clf()

ax = plt.subplots(figsize=(12,7))
ax = sns.violinplot(x="day_of_week", y="coach_price", hue = "redeye", data=flight)
ax = sns.set_theme(rc=custom_params)
plt.title("Coach Price by Day")
plt.ylabel("Price in Dollars")
plt.xlabel("Day")
# plt.show()
plt.savefig(pdf, format = "pdf")
plt.clf()

ax = plt.subplots(figsize=(12,7))
ax = sns.violinplot(x="day_of_week", y="firstclass_price", hue = "redeye", data=flight)
ax = sns.set_theme(rc=custom_params)
plt.title("Coach Price by Day")
plt.ylabel("Price in Dollars")
plt.xlabel("Day")
# plt.show()
plt.savefig(pdf, format = "pdf")
pdf.close()