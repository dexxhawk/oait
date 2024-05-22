import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:1234@127.0.0.1:5432/videohosting")
query = """
SELECT m.resolution, v.rating
FROM video v
JOIN metadata m ON v.metadata_id = m.metadata_id
ORDER BY m.resolution;
"""
df = pd.read_sql(query, engine)
plt.figure(figsize=(10, 6))
df.groupby("resolution")["rating"].mean().plot(kind="bar", color="orange")

plt.title("Distribution of video rating depending on the video resolution")
plt.xlabel("Resolution")
plt.ylabel("Average popularity")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("stat_rating.png")
