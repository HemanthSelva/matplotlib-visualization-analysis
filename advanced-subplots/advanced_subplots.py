import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
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
# SUBPLOT 1: 2x3 Grid — Sales Dashboard
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('📊 Sales Dashboard — 2×3 Subplot Grid', fontsize=18, fontweight='bold', y=1.01)
fig.patch.set_facecolor('white')

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
x = np.arange(12)

# [0,0] Line
sales = [120,145,162,158,175,190,185,210,225,215,240,260]
axes[0,0].plot(x, sales, marker='o', color='#2563eb', linewidth=2.5, markersize=5)
axes[0,0].fill_between(x, sales, alpha=0.1, color='#2563eb')
axes[0,0].set_xticks(x); axes[0,0].set_xticklabels(months, rotation=45, fontsize=7)
axes[0,0].set_title('Monthly Sales Trend', fontweight='bold')
axes[0,0].set_ylabel('Units')

# [0,1] Bar
categories = ['Electronics','Clothing','Food','Books','Sports']
revenue = [68000, 45000, 58000, 23000, 30000]
colors_bar = ['#6366f1','#f43f5e','#10b981','#f59e0b','#3b82f6']
axes[0,1].bar(categories, revenue, color=colors_bar, alpha=0.85, edgecolor='white')
axes[0,1].set_title('Q4 Revenue by Category', fontweight='bold')
axes[0,1].set_ylabel('Revenue (₹)')
axes[0,1].yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f'₹{v/1000:.0f}K'))
axes[0,1].tick_params(axis='x', rotation=20, labelsize=8)

# [0,2] Pie
sizes = [32,25,15,12,10,6]
labels = ['Mobile','Web','Desktop','AI/ML','IoT','Cloud']
axes[0,2].pie(sizes, labels=labels, autopct='%1.1f%%',
              colors=['#6366f1','#3b82f6','#10b981','#f59e0b','#f43f5e','#8b5cf6'],
              startangle=140, wedgeprops={'edgecolor':'white','linewidth':1.5},
              textprops={'fontsize':8})
axes[0,2].set_title('Revenue Share by Product', fontweight='bold')

# [1,0] Scatter
exp = np.random.uniform(1, 15, 80)
sal = 30000 + exp * 5000 + np.random.normal(0, 8000, 80)
axes[1,0].scatter(exp, sal, c='#7c3aed', alpha=0.6, s=50, edgecolors='white', linewidth=0.5)
z = np.polyfit(exp, sal, 1)
xline = np.linspace(1,15,100)
axes[1,0].plot(xline, np.poly1d(z)(xline), '--', color='#dc2626', linewidth=2)
axes[1,0].set_title('Experience vs Salary', fontweight='bold')
axes[1,0].set_xlabel('Years'); axes[1,0].set_ylabel('Salary (₹)')
axes[1,0].yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f'₹{v/1000:.0f}K'))

# [1,1] Histogram
scores = np.random.normal(72, 12, 500)
axes[1,1].hist(scores, bins=25, color='#10b981', alpha=0.82, edgecolor='white')
axes[1,1].axvline(np.mean(scores), color='#dc2626', linestyle='--', linewidth=2, label=f'Mean: {np.mean(scores):.1f}')
axes[1,1].axvline(np.median(scores), color='#1f2937', linestyle=':', linewidth=2, label=f'Median: {np.median(scores):.1f}')
axes[1,1].set_title('Score Distribution', fontweight='bold')
axes[1,1].set_xlabel('Score'); axes[1,1].legend(fontsize=8)

# [1,2] Heatmap
corr_data = pd.DataFrame(np.random.randn(5,5), columns=['Sales','Mktg','Staff','Rating','Profit'])
corr_data['Sales'] += corr_data['Mktg'] * 0.8
sns.heatmap(corr_data.corr(), ax=axes[1,2], annot=True, fmt='.2f',
            cmap='RdYlGn', center=0, linewidths=0.5,
            annot_kws={'size':8}, cbar_kws={'shrink':0.8})
axes[1,2].set_title('Correlation Heatmap', fontweight='bold')
axes[1,2].tick_params(labelsize=8)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/subplot1_dashboard.png', dpi=150, bbox_inches='tight')
plt.close()
print("Subplot 1 done")

# ═══════════════════════════════════════════════════════════════
# SUBPLOT 2: GridSpec Layout — Unequal sized subplots
# ═══════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(16, 10))
fig.patch.set_facecolor('white')
fig.suptitle('📐 GridSpec Layout — Unequal Subplot Sizes', fontsize=17, fontweight='bold', y=1.01)

gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35)

# Wide top plot
ax1 = fig.add_subplot(gs[0, :])
years = np.arange(2018, 2025)
profit = [22, 28, 19, 35, 42, 38, 51]
ax1.plot(years, profit, marker='s', color='#2563eb', linewidth=2.5, markersize=8)
ax1.fill_between(years, profit, alpha=0.12, color='#2563eb')
for y, p in zip(years, profit):
    ax1.annotate(f'{p}%', (y, p), textcoords='offset points', xytext=(0,8), fontsize=8, ha='center', color='#2563eb')
ax1.set_title('Annual Profit Margin % (2018–2024)', fontweight='bold')
ax1.set_ylabel('Profit %')

# Middle left (2 cols)
ax2 = fig.add_subplot(gs[1, :2])
dept = ['Engineering','Sales','Marketing','HR','Finance']
headcount = [45, 32, 28, 15, 20]
colors2 = ['#6366f1','#f43f5e','#10b981','#f59e0b','#3b82f6']
bars = ax2.barh(dept, headcount, color=colors2, alpha=0.85, edgecolor='white')
for bar, val in zip(bars, headcount):
    ax2.text(val+0.5, bar.get_y()+bar.get_height()/2, str(val), va='center', fontsize=9)
ax2.set_title('Department Headcount', fontweight='bold')
ax2.set_xlabel('Employees')

# Middle right (1 col)
ax3 = fig.add_subplot(gs[1, 2])
months_q = ['Q1','Q2','Q3','Q4']
growth = [12, 18, 15, 24]
ax3.bar(months_q, growth, color=['#10b981','#3b82f6','#f59e0b','#6366f1'], alpha=0.85, edgecolor='white')
ax3.set_title('Quarterly\nGrowth %', fontweight='bold')
ax3.set_ylabel('Growth %')

# Bottom 3 small plots
regions = ['North','South','West','East','Central']
colors_r = ['#2563eb','#16a34a','#d97706','#dc2626','#7c3aed']

ax4 = fig.add_subplot(gs[2, 0])
vals4 = [38, 27, 20, 15, 10]
ax4.pie(vals4, labels=regions, colors=colors_r,
        autopct='%1.0f%%', startangle=90,
        wedgeprops={'edgecolor':'white'}, textprops={'fontsize':7})
ax4.set_title('Region Split', fontweight='bold', fontsize=9)

ax5 = fig.add_subplot(gs[2, 1])
data5 = np.random.normal(65, 10, 300)
ax5.hist(data5, bins=20, color='#f43f5e', alpha=0.8, edgecolor='white')
ax5.axvline(np.mean(data5), color='black', linestyle='--', linewidth=1.5)
ax5.set_title('Age Distribution', fontweight='bold', fontsize=9)
ax5.set_xlabel('Age', fontsize=8)

ax6 = fig.add_subplot(gs[2, 2])
x6 = np.random.uniform(0, 10, 60)
y6 = 2*x6 + np.random.normal(0, 3, 60)
ax6.scatter(x6, y6, color='#10b981', alpha=0.6, s=40, edgecolors='white')
ax6.set_title('Sales vs Leads', fontweight='bold', fontsize=9)
ax6.set_xlabel('Leads', fontsize=8); ax6.set_ylabel('Sales', fontsize=8)

plt.savefig('/mnt/user-data/outputs/subplot2_gridspec.png', dpi=150, bbox_inches='tight')
plt.close()
print("Subplot 2 done")

# ═══════════════════════════════════════════════════════════════
# SUBPLOT 3: Shared Axes — Stock Price Analysis
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(4, 1, figsize=(14, 14), sharex=True)
fig.patch.set_facecolor('white')
fig.suptitle('📈 Stock Price Analysis — Shared X-Axis Subplots', fontsize=16, fontweight='bold')

days = np.arange(1, 91)
price  = 100 + np.cumsum(np.random.randn(90) * 2)
volume = np.random.randint(100000, 500000, 90)
ma7    = pd.Series(price).rolling(7).mean()
ma21   = pd.Series(price).rolling(21).mean()
rsi    = 50 + np.cumsum(np.random.randn(90) * 1.5)
rsi    = np.clip(rsi, 20, 80)

# Price + MA
axes[0].plot(days, price, color='#1f2937', linewidth=1.5, label='Price', alpha=0.9)
axes[0].plot(days, ma7,   color='#2563eb', linewidth=1.8, label='MA7',  linestyle='--')
axes[0].plot(days, ma21,  color='#dc2626', linewidth=1.8, label='MA21', linestyle='-.')
axes[0].fill_between(days, price, alpha=0.05, color='#2563eb')
axes[0].set_title('Price with Moving Averages', fontweight='bold', fontsize=11)
axes[0].set_ylabel('Price (₹)')
axes[0].legend(fontsize=9)

# Volume
colors_vol = ['#16a34a' if price[i] >= price[i-1] else '#dc2626' for i in range(1, 90)]
colors_vol = ['#16a34a'] + colors_vol
axes[1].bar(days, volume, color=colors_vol, alpha=0.75, width=0.8)
axes[1].set_title('Trading Volume (Green=Up, Red=Down)', fontweight='bold', fontsize=11)
axes[1].set_ylabel('Volume')
axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f'{v/1000:.0f}K'))

# RSI
axes[2].plot(days, rsi, color='#7c3aed', linewidth=2)
axes[2].axhline(70, color='#dc2626', linestyle='--', linewidth=1.5, alpha=0.8, label='Overbought (70)')
axes[2].axhline(30, color='#16a34a', linestyle='--', linewidth=1.5, alpha=0.8, label='Oversold (30)')
axes[2].fill_between(days, rsi, 70, where=(rsi>=70), alpha=0.15, color='#dc2626')
axes[2].fill_between(days, rsi, 30, where=(rsi<=30), alpha=0.15, color='#16a34a')
axes[2].set_title('RSI Indicator', fontweight='bold', fontsize=11)
axes[2].set_ylabel('RSI')
axes[2].legend(fontsize=9)
axes[2].set_ylim(0, 100)

# Daily Returns
returns = np.diff(price) / price[:-1] * 100
returns = np.append(returns, 0)
colors_ret = ['#16a34a' if r >= 0 else '#dc2626' for r in returns]
axes[3].bar(days, returns, color=colors_ret, alpha=0.8, width=0.8)
axes[3].axhline(0, color='#1f2937', linewidth=1)
axes[3].set_title('Daily Returns %', fontweight='bold', fontsize=11)
axes[3].set_ylabel('Return %')
axes[3].set_xlabel('Trading Days')

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/subplot3_shared_axes.png', dpi=150, bbox_inches='tight')
plt.close()
print("Subplot 3 done")

# ═══════════════════════════════════════════════════════════════
# SUBPLOT 4: 3x3 Distribution Analysis
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(3, 3, figsize=(16, 14))
fig.patch.set_facecolor('white')
fig.suptitle('📉 Distribution & Statistical Analysis — 3×3 Subplots', fontsize=16, fontweight='bold', y=1.01)

plot_configs = [
    ('Normal Dist\n(μ=70, σ=10)',   np.random.normal(70,10,500),     '#3b82f6', 'hist'),
    ('Right Skewed',                 np.random.exponential(8,500)+18, '#f43f5e', 'hist'),
    ('Left Skewed',                  100 - np.random.exponential(8,500), '#10b981', 'hist'),
    ('Bimodal',                      np.concatenate([np.random.normal(40,8,250), np.random.normal(75,8,250)]), '#f59e0b', 'hist'),
    ('Uniform Dist',                 np.random.uniform(20,100,500),   '#8b5cf6', 'hist'),
    ('Box Plot — Depts',             None,                             None,      'box'),
    ('Violin Plot',                  None,                             None,      'violin'),
    ('KDE Plot',                     None,                             None,      'kde'),
    ('CDF Plot',                     None,                             None,      'cdf'),
]

dept_data = [np.random.normal(m, s, 80) for m, s in
             [(65,10),(72,8),(68,12),(75,9),(70,11)]]
dept_names = ['Eng','Sales','Mktg','HR','Fin']

for idx, (title, data, color, ptype) in enumerate(plot_configs):
    ax = axes[idx//3][idx%3]
    if ptype == 'hist':
        ax.hist(data, bins=25, color=color, alpha=0.82, edgecolor='white')
        ax.axvline(np.mean(data), color='#1f2937', linestyle='--', linewidth=1.8, label=f'μ={np.mean(data):.1f}')
        ax.legend(fontsize=8)
    elif ptype == 'box':
        bp = ax.boxplot(dept_data, labels=dept_names, patch_artist=True, notch=True)
        bcolors = ['#6366f1','#f43f5e','#10b981','#f59e0b','#3b82f6']
        for patch, c in zip(bp['boxes'], bcolors):
            patch.set_facecolor(c); patch.set_alpha(0.75)
    elif ptype == 'violin':
        vp = ax.violinplot(dept_data, positions=range(1,6), showmeans=True, showmedians=True)
        for i, body in enumerate(vp['bodies']):
            body.set_facecolor(['#6366f1','#f43f5e','#10b981','#f59e0b','#3b82f6'][i])
            body.set_alpha(0.7)
        ax.set_xticks(range(1,6)); ax.set_xticklabels(dept_names, fontsize=8)
    elif ptype == 'kde':
        for d, c, n in zip(dept_data, ['#6366f1','#f43f5e','#10b981','#f59e0b','#3b82f6'], dept_names):
            kde_x = np.linspace(min(d)-10, max(d)+10, 200)
            from scipy.stats import gaussian_kde
            kde = gaussian_kde(d)
            ax.plot(kde_x, kde(kde_x), color=c, linewidth=2, label=n)
        ax.legend(fontsize=7)
    elif ptype == 'cdf':
        for d, c, n in zip(dept_data, ['#6366f1','#f43f5e','#10b981','#f59e0b','#3b82f6'], dept_names):
            sorted_d = np.sort(d)
            cdf = np.arange(1, len(sorted_d)+1) / len(sorted_d)
            ax.plot(sorted_d, cdf, color=c, linewidth=2, label=n)
        ax.legend(fontsize=7)
        ax.set_ylabel('Cumulative Probability')
    ax.set_title(title, fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/subplot4_distributions.png', dpi=150, bbox_inches='tight')
plt.close()
print("Subplot 4 done")

# ═══════════════════════════════════════════════════════════════
# SUBPLOT 5: Twin Axes & Secondary Y-Axis
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.patch.set_facecolor('white')
fig.suptitle('🔀 Twin & Secondary Axes Subplots', fontsize=16, fontweight='bold')

months_s = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
x = np.arange(12)

# [0,0] Revenue + Growth Rate twin axes
revenue2 = [42,48,55,51,62,70,68,75,82,78,90,105]
growth2  = [0,14,15,-7,22,13,-3,10,9,-5,15,17]
ax00 = axes[0,0]
ax00b = ax00.twinx()
bars00 = ax00.bar(x, revenue2, color='#3b82f6', alpha=0.7, label='Revenue (₹K)', width=0.6)
line00, = ax00b.plot(x, growth2, color='#dc2626', marker='o', linewidth=2.5, markersize=6, label='Growth %')
ax00.set_xticks(x); ax00.set_xticklabels(months_s, rotation=45, fontsize=7)
ax00.set_ylabel('Revenue (₹K)', color='#3b82f6', fontsize=10)
ax00b.set_ylabel('Growth %', color='#dc2626', fontsize=10)
ax00.set_title('Revenue vs Growth Rate', fontweight='bold')
lines = [bars00, line00]
ax00.legend([bars00, line00], ['Revenue', 'Growth %'], fontsize=8, loc='upper left')

# [0,1] Temperature + Humidity
temp = [18,20,24,28,33,36,35,34,30,26,22,18]
humidity = [65,60,55,50,45,42,48,52,58,63,68,70]
ax01 = axes[0,1]
ax01b = ax01.twinx()
ax01.plot(x, temp, color='#f43f5e', marker='o', linewidth=2.5, markersize=6, label='Temp °C')
ax01.fill_between(x, temp, alpha=0.1, color='#f43f5e')
ax01b.plot(x, humidity, color='#3b82f6', marker='s', linewidth=2.5, markersize=6, linestyle='--', label='Humidity %')
ax01.set_xticks(x); ax01.set_xticklabels(months_s, rotation=45, fontsize=7)
ax01.set_ylabel('Temperature (°C)', color='#f43f5e', fontsize=10)
ax01b.set_ylabel('Humidity (%)', color='#3b82f6', fontsize=10)
ax01.set_title('Temperature vs Humidity', fontweight='bold')
ax01.legend(loc='upper left', fontsize=8)
ax01b.legend(loc='upper right', fontsize=8)

# [1,0] Marketing spend vs Conversions
spend   = [5,8,12,10,15,18,16,20,22,19,25,30]
conv    = [120,185,260,230,330,400,360,450,490,430,560,680]
ax10 = axes[1,0]
ax10b = ax10.twinx()
ax10.bar(x, spend, color='#10b981', alpha=0.7, width=0.6, label='Ad Spend (₹K)')
ax10b.plot(x, conv, color='#7c3aed', marker='^', linewidth=2.5, markersize=7, label='Conversions')
ax10.set_xticks(x); ax10.set_xticklabels(months_s, rotation=45, fontsize=7)
ax10.set_ylabel('Ad Spend (₹K)', color='#10b981', fontsize=10)
ax10b.set_ylabel('Conversions', color='#7c3aed', fontsize=10)
ax10.set_title('Ad Spend vs Conversions', fontweight='bold')
ax10.legend(loc='upper left', fontsize=8)
ax10b.legend(loc='lower right', fontsize=8)

# [1,1] Users vs Server Load
users = [1200,1500,1800,1600,2100,2400,2200,2600,2800,2500,3000,3500]
load  = [35,42,55,48,62,72,68,75,82,70,88,95]
ax11 = axes[1,1]
ax11b = ax11.twinx()
ax11.fill_between(x, users, alpha=0.15, color='#f59e0b')
ax11.plot(x, users, color='#f59e0b', linewidth=2.5, marker='o', markersize=5, label='Active Users')
ax11b.plot(x, load, color='#dc2626', linewidth=2.5, marker='s', markersize=5, linestyle='--', label='Server Load %')
ax11b.axhline(80, color='#dc2626', linestyle=':', alpha=0.5, linewidth=1.5)
ax11.set_xticks(x); ax11.set_xticklabels(months_s, rotation=45, fontsize=7)
ax11.set_ylabel('Active Users', color='#f59e0b', fontsize=10)
ax11b.set_ylabel('Server Load %', color='#dc2626', fontsize=10)
ax11.set_title('Users vs Server Load', fontweight='bold')
ax11.legend(loc='upper left', fontsize=8)
ax11b.legend(loc='lower right', fontsize=8)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/subplot5_twin_axes.png', dpi=150, bbox_inches='tight')
plt.close()
print("Subplot 5 done")

print("\n✅ ALL 5 ADVANCED SUBPLOTS GENERATED!")
