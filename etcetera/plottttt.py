# import numpy as np
# import matplotlib.pyplot as plt

# # High-quality square canvas
# fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
# ax.set_facecolor('black')

# # Generate colorful spiral waves
# for i in range(80):
#     t = np.linspace(0, 12 * np.pi, 2500)

#     r = np.sin(3 * t + i / 8) * (0.15 * i)

#     x = r * np.cos(t)
#     y = r * np.sin(t)

#     ax.plot(
#         x,
#         y,
#         linewidth=1,
#         alpha=0.7
#     )

# # Remove axes
# ax.axis('off')

# # Keep aspect ratio perfect
# ax.set_aspect('equal')

# # Save image
# plt.savefig(
#     'whatsapp_dp.png',
#     dpi=500,
#     bbox_inches='tight',
#     pad_inches=0,
#     facecolor='black'
# )

# plt.show()
""""
import numpy as np
import matplotlib.pyplot as plt

# High-quality square canvas
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_facecolor('black')

# Generate colorful spiral waves
for i in range(80):
    t = np.linspace(0, 12 * np.pi, 2500)

    r = np.sin(3 * t + i / 8) * (0.15 * i)

    x = r * np.cos(t)
    y = r * np.sin(t)

    ax.plot(
        x,
        y,
        linewidth=1,
        alpha=0.7
    )

# Remove axes
ax.axis('off')

# Keep aspect ratio perfect
ax.set_aspect('equal')

# Save image
plt.savefig(
    'whatsapp_dp.png',
    dpi=500,
    bbox_inches='tight',
    pad_inches=0,
    facecolor='black'
)

plt.show()
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dark aesthetic
plt.style.use("dark_background")

# Random seed
np.random.seed(7)

# Generate galaxy-like spiral arms
n = 6000
theta = np.random.uniform(0, 6 * np.pi, n)

r = theta + np.random.normal(0, 1.5, n)

x = r * np.cos(theta)
y = r * np.sin(theta)

# Add secondary swirl
x2 = -r * np.cos(theta + np.pi / 4)
y2 = -r * np.sin(theta + np.pi / 4)

# Combine
X = np.concatenate([x, x2])
Y = np.concatenate([y, y2])

df = pd.DataFrame({
    "x": X,
    "y": Y
})

# Create figure
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')

# Seaborn scatter glow effect
sns.scatterplot(
    data=df,
    x="x",
    y="y",
    hue=np.sqrt(X**2 + Y**2),
    palette="rocket",
    s=6,
    linewidth=0,
    alpha=0.7,
    legend=False,
    ax=ax
)

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Equal scaling
ax.set_aspect('equal')

# Save
plt.savefig(
    "galaxy_dp.png",
    dpi=500,
    bbox_inches='tight',
    pad_inches=0,
    facecolor='black'
)

plt.show()