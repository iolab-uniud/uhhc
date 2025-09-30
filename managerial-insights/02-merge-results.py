#!/usr/bin/env python
# coding: utf-8

import pandas as pd

efficiency = pd.read_csv("processed-data/avg_efficiency_oper.csv", index_col=0).add_prefix("efficiency_").rename(columns={"efficiency_instance":"instance"})
fairness = pd.read_csv("processed-data/avg_fairness_oper.csv", index_col=0).add_prefix("fairness_").rename(columns={"fairness_instance":"instance"})
wellbeing = pd.read_csv("processed-data/avg_wellbeing_oper.csv", index_col=0).add_prefix("wellbeing_").rename(columns={"wellbeing_instance":"instance"})
sa = pd.read_csv("processed-data/avg_SA_oper.csv", index_col=0).add_prefix("SA_").rename(columns={"SA_instance":"instance"})

pd.merge(pd.merge(
    pd.merge(
    efficiency,
    fairness,
    on=["instance"]
),
wellbeing,
on=["instance"]
),
sa,
on=["instance"]
).to_csv("processed-data/MA-operational.csv")

caregivers = pd.read_csv("processed-data/avg_caregivers_stake.csv", index_col=0).add_prefix("caregiver_").rename(columns={"caregiver_instance":"instance"})
patients = pd.read_csv("processed-data/avg_patients_stake.csv", index_col=0).add_prefix("patient_").rename(columns={"patient_instance":"instance"})
organization = pd.read_csv("processed-data/avg_organization_stake.csv", index_col=0).add_prefix("organization_").rename(columns={"organization_instance":"instance"})
sa_stake = pd.read_csv("processed-data/avg_SA_stake.csv", index_col=0).add_prefix("SA_").rename(columns={"SA_instance":"instance"})

pd.merge(pd.merge(
    pd.merge(
    caregivers,
    patients,
    on=["instance"]
),
organization,
on=["instance"]
),
sa_stake,
on=["instance"]
).to_csv("processed-data/MA-stakeholders.csv")

