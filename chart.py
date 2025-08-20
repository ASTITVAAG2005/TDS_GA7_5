import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for support response times (in minutes)
n_samples = 400
channels = ['Email', 'Chat', 'Phone', 'Social Media']

data = {
    'Channel': np.random.choice(channels, n_samples),
    'Response_Time': np.concatenate([
        np.random.normal(loc=30, scale=8, size=n_samples // 4),   # Email: slower
        np.random.normal(loc=10, scale=3, size=n_samples // 4),   # Chat: fast
        np.random.normal(loc=15, scale=4, size=n_samples // 4),   # Phone: medium
        np.random.normal(loc=25, scale=6, size=n_samples // 4)    # Social Media: variable
    ])
}

df = pd.DataFrame(data)

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create figure with exact 512x512 pixels (8 inches * 64 dpi = 512)
plt.figure(figsize=(8, 8), dpi=64)

# Create violinplot
sns.violinplot(
    data=df,
    x="Channel",
    y="Response_Time",
    palette="Set2",
    inner="box"
)

# Titles and labels
plt.title("Customer Support Response Time Distribution\nAcross Channels", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Support Channel", fontsize=14, fontweight='semibold')
plt.ylabel("Response Time (minutes)", fontsize=14, fontweight='semibold')

# Clean style
sns.despine()
plt.tight_layout()

# Save as required
plt.savefig("chart.png", dpi=64, bbox_inches='tight')

print("Chart generated successfully with Seaborn violinplot!")
