import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# Set random seed
np.random.seed(42)

# Generate synthetic data for support response times
n_samples = 400
channels = ['Email', 'Chat', 'Phone', 'Social Media']

data = {
    'Channel': np.repeat(channels, n_samples // 4),
    'Response_Time': np.concatenate([
        np.random.normal(loc=30, scale=8, size=n_samples // 4),   # Email
        np.random.normal(loc=10, scale=3, size=n_samples // 4),   # Chat
        np.random.normal(loc=15, scale=4, size=n_samples // 4),   # Phone
        np.random.normal(loc=25, scale=6, size=n_samples // 4)    # Social Media
    ])
}
df = pd.DataFrame(data)

# Styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Make 512x512 figure
plt.figure(figsize=(8, 8), dpi=64)

# Violinplot
sns.violinplot(
    data=df,
    x="Channel",
    y="Response_Time",
    palette="Set2",
    inner="box"
)

# Labels
plt.title("Customer Support Response Time Distribution\nAcross Channels",
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Support Channel", fontsize=14, fontweight='semibold')
plt.ylabel("Response Time (minutes)", fontsize=14, fontweight='semibold')

sns.despine()
plt.tight_layout()

# Save raw
plt.savefig("chart.png", dpi=64)  # no bbox_inches

# 🔒 Ensure final PNG is exactly 512x512
img = Image.open("chart.png")
img = img.resize((512, 512), Image.Resampling.LANCZOS)
img.save("chart.png", "PNG")

print("Chart generated successfully with exact 512x512 pixels.")
