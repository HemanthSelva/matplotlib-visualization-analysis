import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': '#f8f9fa',
    'axes.grid': True,
    'grid.alpha': 0.4,
    'grid.color': '#cccccc',
})

np.random.seed(42)

# ═══════════════════════════════════════════════════════════════
# PLOT 1: LINE PLOT — Monthly Sales Trend
# Importance: Best for visualizing trends over time.
# Tracks 5 products over 12 months to reveal growth patterns
# and seasonal spikes.
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('white')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
products = {
    'Product A': [120, 145, 162, 158, 175, 190, 185, 210, 225, 215, 240, 260],
    'Product B': [95,  110, 105, 130, 125, 140, 155, 148, 165, 172, 180, 195],
    'Product C': [60,  72,  85,  80,  92,  88,  100, 115, 108, 125, 132, 145],
    'Product D': [40,  55,  50,  65,  70,  85,  78,  90,  95,  105, 98,  115],
    'Product E': [20,  30,  35,  28,  42,  48,  55,  52,  60,  68,  72,  80],
}
colors = ['#2563eb', '#dc2626', '#16a34a', '#d97706', '#7c3aed']
x = np.arange(len(months))

for (name, values), color in zip(products.items(), colors):
    ax.plot(x, values, marker='o', linewidth=2.5, markersize=5,
            color=color, label=name, alpha=0.9)
    ax.fill_between(x, values, alpha=0.06, color=color)

ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=11)
ax.set_xlabel('Month (2024)', fontsize=12, labelpad=10)
ax.set_ylabel('Sales Units', fontsize=12, labelpad=10)
ax.set_title('📈  Monthly Sales Trend — 5 Products (2024)',
             fontsize=15, fontweight='bold', pad=18)
ax.legend(loc='upper left', framealpha=0.9, fontsize=10)
ax.set_ylim(0, 290)

ax.annotate('Peak: 260', xy=(11, 260), xytext=(9.2, 270),
            fontsize=9, color='#2563eb',
            arrowprops=dict(arrowstyle='->', color='#2563eb', lw=1.5))

plt.tight_layout()
plt.savefig('plot1_line.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Plot 1 - Line Plot saved")


# ═══════════════════════════════════════════════════════════════
# PLOT 2: BAR PLOT — Quarterly Revenue by Category
# Importance: Best for comparing discrete values across groups.
# Grouped bars let you compare Q1–Q4 for each product category.
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor('white')

categories = ['Electronics', 'Clothing', 'Food & Bev', 'Books', 'Sports', 'Toys']
q_data = {
    'Q1': [42000, 28000, 35000, 18000, 22000, 15000],
    'Q2': [48000, 32000, 31000, 20000, 27000, 18000],
    'Q3': [55000, 38000, 42000, 17000, 35000, 22000],
    'Q4': [68000, 45000, 58000, 23000, 30000, 28000],
}
q_colors = ['#3b82f6', '#22c55e', '#f59e0b', '#ef4444']
width = 0.18
x = np.arange(len(categories))

for i, (q, vals) in enumerate(q_data.items()):
    ax.bar(x + i * width, vals, width, label=q,
           color=q_colors[i], alpha=0.88, edgecolor='white', linewidth=0.8)

ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylabel('Revenue (₹)', fontsize=12)
ax.set_title('📊  Quarterly Revenue by Product Category',
             fontsize=15, fontweight='bold', pad=18)
ax.legend(title='Quarter', fontsize=10)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'₹{v/1000:.0f}K'))

plt.tight_layout()
plt.savefig('plot2_bar.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Plot 2 - Bar Plot saved")


# ═══════════════════════════════════════════════════════════════
# PLOT 3: SCATTER PLOT — Experience vs Salary (Bubble Size = Performance)
# Importance: Reveals correlations and outliers between two
# continuous variables. 3rd dimension added via bubble size.
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor('white')

departments = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance', 'Operations']
dept_colors = ['#6366f1', '#f43f5e', '#10b981', '#f59e0b', '#3b82f6', '#8b5cf6']

for dept, color in zip(departments, dept_colors):
    n = np.random.randint(18, 30)
    exp  = np.random.uniform(1, 15, n)
    sal  = 30000 + exp * 5000 + np.random.normal(0, 8000, n)
    perf = np.clip(50 + exp * 3 + np.random.normal(0, 10, n), 30, 100)
    ax.scatter(exp, sal, s=perf * 3, c=color, alpha=0.72,
               edgecolors='white', linewidth=0.7, label=dept)

# Trend line
all_exp = np.random.uniform(1, 15, 120)
all_sal = 30000 + all_exp * 5000 + np.random.normal(0, 8000, 120)
z = np.polyfit(all_exp, all_sal, 1)
p = np.poly1d(z)
xline = np.linspace(1, 15, 100)
ax.plot(xline, p(xline), '--', color='#374151', linewidth=1.8, alpha=0.6, label='Trend')

ax.set_xlabel('Years of Experience', fontsize=12, labelpad=10)
ax.set_ylabel('Annual Salary (₹)', fontsize=12, labelpad=10)
ax.set_title('🔵  Experience vs Salary  (bubble size = performance score)',
             fontsize=13, fontweight='bold', pad=18)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'₹{v/1000:.0f}K'))
ax.legend(fontsize=9, loc='upper left', framealpha=0.9)

plt.tight_layout()
plt.savefig('plot3_scatter.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Plot 3 - Scatter Plot saved")


# ═══════════════════════════════════════════════════════════════
# PLOT 4: PIE + DONUT CHART — Market Breakdown
# Importance: Best for part-of-whole comparisons.
# Pie = product revenue share, Donut = regional customer split.
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.patch.set_facecolor('white')

# --- Pie Chart ---
labels = ['Mobile\nApps', 'Web\nPlatform', 'Desktop\nSoftware',
          'IoT\nDevices', 'AI / ML\nServices', 'Cloud\nServices']
sizes  = [32, 25, 15, 10, 12, 6]
explode = [0.06, 0, 0, 0, 0.06, 0]
colors_pie = ['#6366f1', '#3b82f6', '#10b981', '#f59e0b', '#f43f5e', '#8b5cf6']

wedges, texts, autotexts = axes[0].pie(
    sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    colors=colors_pie, startangle=140, pctdistance=0.78,
    textprops={'fontsize': 9}, wedgeprops={'edgecolor': 'white', 'linewidth': 2})
for at in autotexts:
    at.set_fontweight('bold')
axes[0].set_title('Revenue Share by Product Line', fontsize=13, fontweight='bold', pad=14)

# --- Donut Chart ---
sizes2  = [38, 27, 20, 15]
labels2 = ['North India', 'South India', 'West India', 'East India']
colors2 = ['#2563eb', '#16a34a', '#d97706', '#dc2626']

wedges2, texts2, auto2 = axes[1].pie(
    sizes2, labels=labels2, autopct='%1.1f%%', colors=colors2,
    startangle=90, pctdistance=0.82,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'width': 0.5},
    textprops={'fontsize': 10})
for at in auto2:
    at.set_fontweight('bold')
axes[1].text(0, 0, 'Region\nSplit', ha='center', va='center',
             fontsize=11, fontweight='bold', color='#374151')
axes[1].set_title('Regional Customer Distribution (Donut)', fontsize=13, fontweight='bold', pad=14)

plt.suptitle('🥧  Pie & Donut Charts — Market Breakdown',
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('plot4_pie_donut.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Plot 4 - Pie + Donut Chart saved")


# ═══════════════════════════════════════════════════════════════
# PLOT 5: HISTOGRAM — Distribution Shapes (Normal, Skewed, Bimodal)
# Importance: Reveals how data is distributed.
# Mean vs Median lines expose symmetry or skewness.
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.patch.set_facecolor('white')

datasets = {
    'Student Scores\n(Normal)':      (np.random.normal(72, 12, 500),              '#3b82f6'),
    'Customer Age\n(Skewed)':         (np.random.exponential(10, 500) + 18,        '#10b981'),
    'Daily Transactions\n(Bimodal)':  (np.concatenate([
                                           np.random.normal(200, 30, 300),
                                           np.random.normal(500, 40, 200)]),       '#f43f5e'),
}

for ax, (title, (data, color)) in zip(axes, datasets.items()):
    ax.hist(data, bins=30, color=color, alpha=0.82,
            edgecolor='white', linewidth=0.6)
    ax.axvline(np.mean(data),   color='#1f2937', linestyle='--',
               linewidth=2, label=f'Mean:   {np.mean(data):.1f}')
    ax.axvline(np.median(data), color='#6b7280', linestyle=':',
               linewidth=2, label=f'Median: {np.median(data):.1f}')
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    ax.set_xlabel('Value', fontsize=10)
    ax.set_ylabel('Frequency', fontsize=10)
    ax.legend(fontsize=8)

plt.suptitle('📉  Histogram Analysis — Distribution Shapes',
             fontsize=14, fontweight='bold', y=1.03)
plt.tight_layout()
plt.savefig('plot5_histogram.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Plot 5 - Histogram saved")


# ═══════════════════════════════════════════════════════════════
# PLOT 6: HEATMAP — Correlation Matrix + Hourly Traffic
# Importance: Pattern detection across two dimensions.
# Left = KPI correlations, Right = peak traffic by hour & day.
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.patch.set_facecolor('white')

# --- Correlation Heatmap ---
df = pd.DataFrame({
    'Sales':        np.random.normal(50000, 10000, 100),
    'Marketing $':  np.random.normal(8000,  2000,  100),
    'Staff Count':  np.random.randint(10, 50, 100),
    'Satisfaction': np.random.uniform(3, 5, 100),
    'Returns %':    np.random.uniform(1, 15, 100),
    'Profit %':     np.random.uniform(5, 35, 100),
})
df['Sales']    += df['Marketing $'] * 3
df['Profit %'] -= df['Returns %'] * 0.5
corr = df.corr()

sns.heatmap(corr, ax=axes[0], annot=True, fmt='.2f', cmap='RdYlGn',
            center=0, linewidths=0.5, linecolor='white',
            annot_kws={'size': 10, 'weight': 'bold'},
            square=True, cbar_kws={'shrink': 0.8})
axes[0].set_title('Correlation Matrix — Business KPIs',
                  fontsize=12, fontweight='bold', pad=14)

# --- Hourly Traffic Heatmap ---
hours   = [f'{h:02d}:00' for h in range(24)]
days    = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
traffic = np.random.randint(10, 100, (7, 24))
traffic[:5, 9:18]  += np.random.randint(40, 80, (5, 9))
traffic[5:, 11:20] += np.random.randint(20, 50, (2, 9))
traffic[5:, 20:23] += np.random.randint(10, 30, (2, 3))

sns.heatmap(traffic, ax=axes[1], xticklabels=hours, yticklabels=days,
            cmap='YlOrRd', linewidths=0.3, linecolor='white',
            cbar_kws={'label': 'Visitors', 'shrink': 0.8})
axes[1].set_xticklabels(hours, rotation=45, ha='right', fontsize=7)
axes[1].set_title('Website Traffic — Hour × Day Heatmap',
                  fontsize=12, fontweight='bold', pad=14)

plt.suptitle('🔥  Heatmap Analysis', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('plot6_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Plot 6 - Heatmap saved")

print("\n🎉 ALL 6 PLOTS COMPLETED SUCCESSFULLY!")
