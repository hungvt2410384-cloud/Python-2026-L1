import os
import matplotlib.pyplot as plt
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "scores.csv")

df = pd.read_csv(csv_path)

plt.figure(figsize=(8, 6))
plt.scatter(df.index, df["math"], label="Math", alpha=0.7)
plt.scatter(df.index, df["python"], label="Python", alpha=0.7)
plt.scatter(df.index, df["db"], label="DB", alpha=0.7)
plt.title("Student Scores Scatter Plot")
plt.xlabel("Student Index")
plt.ylabel("Scores")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(script_dir, "scattered.png"))
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
axes[0].hist(df["math"], bins=10, color="skyblue", edgecolor="black")
axes[0].set_title("Math Scores")
axes[0].set_xlabel("Marks")
axes[0].set_ylabel("Frequency")

axes[1].hist(df["python"], bins=10, color="lightgreen", edgecolor="black")
axes[1].set_title("Python Scores")
axes[1].set_xlabel("Marks")

axes[2].hist(df["db"], bins=10, color="salmon", edgecolor="black")
axes[2].set_title("DB Scores")
axes[2].set_xlabel("Marks")

plt.tight_layout()
plt.savefig(os.path.join(script_dir, "histo.png"))
plt.close()

plt.figure(figsize=(8, 6))
df[["math", "python", "db"]].boxplot()
plt.title("Box Plot of Course Scores")
plt.ylabel("Scores")
plt.tight_layout()
plt.savefig(os.path.join(script_dir, "box.png"))
plt.close()
plt.show()