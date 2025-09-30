#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", context="paper",font_scale=1.7)

# operational goals, prepare data 

df_operational = pd.read_csv("processed-data/MA-operational.csv",sep=",",index_col=0)
components_operational = ["total", "efficiency",  "fairness", "wellbeing"]
hues_operational = ["efficiency",  "fairness","wellbeing",]
data = []
for component in components_operational:
    baseline_col = f"SA_{component}"
    baseline_mean = df_operational[baseline_col].mean()

    for hue in hues_operational:
        col = f"{hue}_{component}"
        value_mean = df_operational[col].mean()

        data.append({
            "hue": hue if hue not in ["wellbeing"] else "well-being",
            "component": component if component not in ["wellbeing"] else "well-being",
            "avg": (value_mean - baseline_mean) / baseline_mean
        })
avg_df_operatioanl = pd.DataFrame(data)
avg_df_operatioanl["avg_perc"] = avg_df_operatioanl["avg"] * 100
avg_df_operatioanl["hue"] = avg_df_operatioanl["hue"].str.capitalize()
avg_df_operatioanl["component"] = avg_df_operatioanl["component"].str.capitalize()


# stakeholders, prepare data 

df_stake = pd.read_csv("processed-data/MA-stakeholders.csv")
components_stake = ["total", "caregiver", "patient", "organization"]
hues_stake = ["caregiver", "patient", "organization"]

data = []

for component in components_stake:
    baseline_col = f"SA_{component}"
    baseline_mean = df_stake[baseline_col].mean()

    for hue in hues_stake:
        col = f"{hue}_{component}"
        value_mean = df_stake[col].mean()

        data.append({
            "hue": hue,
            "component": component,
            "avg": (value_mean - baseline_mean) / baseline_mean
        })
avg_df_stake = pd.DataFrame(data)
avg_df_stake["avg_perc"] = avg_df_stake["avg"] * 100
avg_df_stake["hue"] = avg_df_stake["hue"].str.capitalize()
avg_df_stake["component"] = avg_df_stake["component"].str.capitalize()

# bar plot

fig, (ax_stake, ax_oper) = plt.subplots(
    1, 2,
    figsize=(14, 5),      
)

palette_stake       = sns.color_palette("Set2")[0:3] 
palette_operational = sns.color_palette("Set2")[4:7] 

order_stake        = ["Total", "Patient", "Caregiver", "Organization"]
order_operational  = ["Total", "Efficiency", "Fairness", "Well-being"]

sns.barplot(
    data=avg_df_stake,
    x="component", y="avg_perc", hue="hue",
    order=order_stake,
    palette=palette_stake,
    width=0.6, edgecolor="0.3",
    ax=ax_stake
)

ax_stake.set_xlabel("Cost component")
ax_stake.set_ylabel("Average gap (%)")
ax_stake.set_title("a) Stakeholders", loc="left", fontweight="semibold")
ax_stake.legend(title="Opt. focus", frameon=True)

sns.barplot(
    data=avg_df_operatioanl,               
    x="component", y="avg_perc", hue="hue",
    order=order_operational,
    palette=palette_operational,
    width=0.6, edgecolor="0.3",
    ax=ax_oper
)

ax_oper.set_xlabel("Cost component")
ax_oper.set_ylabel("")                     
ax_oper.set_title("b) Operational goals", loc="left", fontweight="semibold")   
ax_oper.legend(title="Opt. focus", frameon=True,)          

def annotate_bars(ax, fmt="%.0f", padding=2, fontsize=12):
    """Attach a label above each bar showing its height."""
    for container in ax.containers:              
        ax.bar_label(container,
                     labels=[fmt % v.get_height() for v in container],
                     label_type="edge",          # place slightly above the bar
                     padding=padding,
                     fontsize=fontsize)

annotate_bars(ax_stake)
annotate_bars(ax_oper)

sns.despine(trim=True)
fig.tight_layout()
fig.subplots_adjust(wspace=0.15)      
plt.savefig("gap_components.pdf", dpi=300, bbox_inches="tight")

# radar plot

components_stake = ["total", "caregiver", "patient", "organization"]
hues_stake = ["SA", "caregiver", "patient", "organization"]

component_columns_stake = {
    "total": [f"{hue}_total" for hue in hues_stake],
    "caregiver": [f"{hue}_caregiver" for hue in hues_stake],
    "patient": [f"{hue}_patient" for hue in hues_stake],
    "organization": [f"{hue}_organization" for hue in hues_stake],
}

# massimo per colonna
for component, cols in component_columns_stake.items():
    max_col = f"max_{component}"
    df_stake[max_col] = df_stake[cols].max(axis=1)

# normalizza
for component, cols in component_columns_stake.items():
    max_col = f"max_{component}"
    for col in cols:
        norm_col = f"norm_{col}"
        df_stake[norm_col] = df_stake[col] / df_stake[max_col]



component_operational = ["total", "efficiency",  "fairness","wellbeing"]
hues_operational = ["SA", "efficiency",  "fairness","wellbeing"]

component_columns_operational = {
    "total": [f"{hue}_total" for hue in hues_operational],
    "efficiency": [f"{hue}_efficiency" for hue in hues_operational],
    "fairness": [f"{hue}_fairness" for hue in hues_operational],
    "wellbeing": [f"{hue}_wellbeing" for hue in hues_operational],
}

# max per column
for component, cols in component_columns_operational.items():
    max_col = f"max_{component}"
    df_operational[max_col] = df_operational[cols].max(axis=1)

# normalization 
for component, cols in component_columns_operational.items():
    max_col = f"max_{component}"
    for col in cols:
        norm_col = f"norm_{col}"
        df_operational[norm_col] = df_operational[col] / df_operational[max_col]

# generate for the following instance

INSTANCE_ID = "i-083"

color_palette_organiz = {
    "SA": sns.color_palette("Set2")[3],
    "efficiency": sns.color_palette("Set2")[4],
    "fairness": sns.color_palette("Set2")[5],
    "well-being": sns.color_palette("Set2")[6],
}
color_palette_stake = {
    "SA": sns.color_palette("Set2")[3],
    "patient": sns.color_palette("Set2")[1],
    "caregiver": sns.color_palette("Set2")[0],
    "organization": sns.color_palette("Set2")[2],
}

focuses_organiz = ["SA", "efficiency", "fairness", "wellbeing"]
components_organiz = ["efficiency", "fairness", "wellbeing"]

focuses_stake = ["SA", "patient", "caregiver", "organization"]
components_stake = ["caregiver", "patient", "organization"]

def make_radar(ax, row, focuses, components, palette, title):
    data = {
    ("well-being" if obj == "wellbeing" else obj): [
        row[f"norm_{obj}_{comp}"] for comp in components
    ]
    for obj in focuses}
    labels = [lbl.capitalize() if lbl !="wellbeing" else "Well-being" for lbl in components] 
    for n,i in enumerate(labels):
        if i == "Sa":
            labels[n] = "SA"
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    for obj in focuses:
        obj = "well-being" if obj == "wellbeing" else obj
        vals = data[obj] + [data[obj][0]]
        ax.plot(angles, vals, label=obj.capitalize(), color=palette[obj])
        ax.fill(angles, vals, alpha=0.1, color=palette[obj])

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.set_title(title, loc="left", fontweight="semibold")
    ax.grid(True)

row_operat = df_operational.loc[df_operational["instance"] ==  INSTANCE_ID].iloc[0]
row_stake = df_stake.loc[df_stake["instance"] == INSTANCE_ID].iloc[0]

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), subplot_kw=dict(polar=True))

make_radar(
    ax=axes[0],
    row=row_stake,
    focuses=focuses_stake,
    components=components_stake,
    palette=color_palette_stake,
    title="a) Stakeholders",
)

make_radar(
    ax=axes[1],
    row=row_operat,
    focuses=focuses_organiz,
    components=components_organiz,
    palette=color_palette_organiz,
    title="b) Operational Goals",
)

handles_1, labels_1 = axes[0].get_legend_handles_labels()
handles_2, labels_2 = axes[1].get_legend_handles_labels()
handles = handles_1 + handles_2


for n, i in enumerate(labels_2):
    if i == "Sa":
        labels_2[n] = "Total"
for n, i in enumerate(labels_1):
    if i == "Sa":
        labels_1[n] = "Total"
labels = labels_1 + labels_2

unique = {"Total" if lbl == "Total" else lbl.lower(): (h, lbl) for h, lbl in zip(handles, labels)}
handles, labels = zip(*unique.values())

fig.legend(
    handles,
    labels,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.05),
    ncol=4,
    title="Version of SA",
)

plt.tight_layout()
plt.subplots_adjust(bottom=0.18)  # spazio per la legenda
plt.savefig("radar.pdf", dpi=300, bbox_inches="tight")




