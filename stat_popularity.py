import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:1234@127.0.0.1:5432/videohosting")
query = """
SELECT v.creation_date, a.popularity
FROM video v
JOIN analytics a ON v.analytics_id = a.analytics_id
ORDER BY v.creation_date;
"""
df = pd.read_sql(query, engine)
df["creation_date"] = pd.to_datetime(df["creation_date"])
df["year_month"] = df["creation_date"].dt.to_period("Y")
plt.figure(figsize=(10, 6))
df.groupby("year_month")["popularity"].mean().plot(kind="bar", color="blue")

plt.title("Distribution of video popularity depending on the creation date")
plt.xlabel("Creation Date")
plt.ylabel("Average popularity")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("stat_popularity.png")
