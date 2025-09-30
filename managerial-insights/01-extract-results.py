#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os

input_folder = "raw-data"
output_folder = "processed-data"

if not os.path.exists(output_folder):
      os.makedirs(output_folder)

organization_costs = ["travel_time", "total_waiting_time", "max_idle_time"]
patient_costs = ["preferences", "unscheduled",  "total_tardiness", "highest_tardiness",]
caregiver_costs = ["total_extra_time", "missed_lunch_break", "workload_balance",]
total_costs = ["travel_time", "total_tardiness", "highest_tardiness", "total_waiting_time", "total_extra_time", "max_idle_time", "workload_balance", "preferences", "unscheduled", "missed_lunch_break"]
interesting_columns = ["instance", "total", "organization", "patient", "caregiver"]

def calc_total_cost(row):
    tot = 0
    for col in total_costs:
        tot += row[col]
    return tot

def calc_organization_cost(row):
    tot = 0
    for col in organization_costs:
        tot += row[col]
    return tot

def calc_patient_cost(row):
    tot = 0
    for col in patient_costs:
        tot += row[col]
    return tot

def calc_caregiver_cost(row):
    tot = 0
    for col in caregiver_costs:
        tot += row[col]
    return tot

for focus in ["organization", "patients", "caregivers", "SA"]:
    sep = ";" if focus in ["SA"] else "," 
    df = pd.read_csv(f"{input_folder}/{focus}_log.csv", sep=sep)
    df["total"] = df.apply(lambda row: calc_total_cost(row), axis=1)
    df["organization"] = df.apply(lambda row: calc_organization_cost(row), axis=1)
    df["patient"] = df.apply(lambda row: calc_patient_cost(row), axis=1)
    df["caregiver"] = df.apply(lambda row: calc_caregiver_cost(row), axis=1)
    df[interesting_columns].groupby("instance").mean().reset_index().to_csv(f"{output_folder}/avg_{focus}_stake.csv")

efficiency_costs = ["travel_time", "total_extra_time", "total_waiting_time", "max_idle_time", "unscheduled"]
fairness_costs = ["total_tardiness", "highest_tardiness", "max_idle_time", "workload_balance"]
well_being_costs = [ "total_extra_time", "total_tardiness", "highest_tardiness","unscheduled","preferences", "missed_lunch_break"]

total_costs = ["travel_time", "total_tardiness", "highest_tardiness", "total_waiting_time", "total_extra_time", "max_idle_time", "workload_balance", "preferences", "unscheduled", "missed_lunch_break"]
interesting_columns = ["instance", "total", "efficiency", "fairness", "wellbeing"]

def calc_total_cost(row):
    tot = 0
    for col in total_costs:
        tot += row[col]
    return tot

def calc_efficiency_cost(row):
    tot = 0
    for col in efficiency_costs:
        tot += row[col]
    return tot

def calc_fairness_cost(row):
    tot = 0
    for col in fairness_costs:
        tot += row[col]
    return tot

def calc_well_being_cost(row):
    tot = 0
    for col in well_being_costs:
        tot += row[col]
    return tot


for focus in ["efficiency", "fairness", "wellbeing", "SA"]:
    sep = ";" if focus in ["SA"] else "," 
    df = pd.read_csv(f"{input_folder}/{focus}_log.csv", sep=sep)
    df["total"] = df.apply(lambda row: calc_total_cost(row), axis=1)
    df["efficiency"] = df.apply(lambda row: calc_efficiency_cost(row), axis=1)
    df["fairness"] = df.apply(lambda row: calc_fairness_cost(row), axis=1)
    df["wellbeing"] = df.apply(lambda row: calc_well_being_cost(row), axis=1)
    df[interesting_columns].groupby("instance").mean().reset_index().to_csv(f"{output_folder}/avg_{focus}_oper.csv")

