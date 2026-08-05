import os
import pandas as pd
import numpy as np
import random

# Load Dataset
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "customer_churn.csv")

data = pd.read_csv(csv_file)

print("===== CUSTOMER CHURN DATA =====")
print(data)

episodes = 100
gamma = 0.9

state_value = 0

print("\n===== MONTE CARLO POLICY EVALUATION =====")

for episode in range(episodes):

    sample = data.sample().iloc[0]

    churn = sample["Churn"]
    support = sample["SupportCalls"]

    # Reward Function
    if churn == 0:
        reward = 10 - support
    else:
        reward = -10 - support

    state_value = state_value + (reward - state_value) / (episode + 1)

print("\nEstimated State Value =", round(state_value,2))

# Policy Analysis
retain = data[data["Churn"] == 0]
churned = data[data["Churn"] == 1]

print("\n===== ANALYSIS =====")
print("Average Subscription (Retained):",
      round(retain["SubscriptionMonths"].mean(),2),"months")

print("Average Subscription (Churned):",
      round(churned["SubscriptionMonths"].mean(),2),"months")

print("Average Monthly Charge:",
      round(data["MonthlyCharges"].mean(),2))

if state_value > 0:
    print("\nPolicy Performance : GOOD")
else:
    print("\nPolicy Performance : NEEDS IMPROVEMENT")

print("\nExperiment Completed Successfully")
