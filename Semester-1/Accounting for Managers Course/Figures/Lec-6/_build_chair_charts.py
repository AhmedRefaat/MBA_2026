import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

matplotlib.rcParams['font.size'] = 13

months = ['January', 'February', 'March']
x = np.arange(len(months))
bar_width = 0.25

# ── Chart 1: Revenue vs Costs ──
fig1, ax1 = plt.subplots(figsize=(10, 6))

sales =       [175, 75, 0]
cogs =        [70,  30, 0]
period_cost = [50,  50, 50]

b1 = ax1.bar(x - bar_width, sales,       bar_width, label='Sales Revenue', color='#4A90D9', edgecolor='white', linewidth=1.2)
b2 = ax1.bar(x,             cogs,        bar_width, label='COGS (Product Cost)', color='#E8832A', edgecolor='white', linewidth=1.2)
b3 = ax1.bar(x + bar_width, period_cost, bar_width, label='Period Cost (SG&A)', color='#FFEB3B', edgecolor='#bbb', linewidth=1.2)

# Labels on bars
for bar_group, values, color in [(b1, sales, 'white'), (b2, cogs, 'white'), (b3, period_cost, 'black')]:
    for bar, val in zip(bar_group, values):
        if val > 0:
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2, 
                     f'{val}K', ha='center', va='center', fontweight='bold', fontsize=12, color=color)
        else:
            ax1.text(bar.get_x() + bar.get_width()/2, 5, 
                     '0', ha='center', va='bottom', fontweight='bold', fontsize=11, color='#666')

ax1.set_xlabel('Month', fontsize=14, fontweight='bold')
ax1.set_ylabel('Amount (K EGP)', fontsize=14, fontweight='bold')
ax1.set_title('Chart 1: Income Statement Breakdown per Month\n(What appears in the Income Statement?)', fontsize=15, fontweight='bold', pad=15)
ax1.set_xticks(x)
ax1.set_xticklabels(months, fontsize=13)
ax1.set_ylim(0, 210)
ax1.legend(loc='upper right', fontsize=12, framealpha=0.9)
ax1.grid(axis='y', alpha=0.3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Annotation for Period Cost
ax1.annotate('Period Cost is CONSTANT\nregardless of sales!', 
             xy=(2 + bar_width, 50), xytext=(2.1, 100),
             fontsize=11, fontweight='bold', color='#D4A000',
             arrowprops=dict(arrowstyle='->', color='#D4A000', lw=2),
             ha='center')

fig1.tight_layout()
script_dir = os.path.dirname(os.path.abspath(__file__))
fig1.savefig(os.path.join(script_dir, 'Chart1_Revenue_vs_Costs.png'), dpi=150, bbox_inches='tight', facecolor='white')
print("Chart 1 saved.")

# ── Chart 2: Profit Trend ──
fig2, ax2 = plt.subplots(figsize=(11, 6.5))

gross_profit =     [105, 45,   0]
operating_profit = [55,  -5,  -50]
period_line =      [50,  50,   50]

b_gp = ax2.bar(x, gross_profit, 0.5, label='Gross Profit', color='#5CB85C', edgecolor='white', linewidth=1.2, zorder=3)

# Labels on Gross Profit bars
gp_label_y = [80, 22, 3]
for bar, val, ly in zip(b_gp, gross_profit, gp_label_y):
    ax2.text(bar.get_x() + bar.get_width()/2, ly, 
             f'{val}K' if val > 0 else '0', ha='center', va='center', fontweight='bold', fontsize=14, 
             color='white' if val > 0 else '#666')

# Period Cost line (flat) — label only on Feb and Mar to avoid Jan overlap
ax2.plot(x, period_line, 'o--', color='#E8832A', linewidth=3, markersize=10, label='Period Cost (constant 50K)', zorder=4)
ax2.text(1, 56, '50K', ha='center', fontweight='bold', fontsize=12, color='#E8832A')
ax2.text(2, 56, '50K', ha='center', fontweight='bold', fontsize=12, color='#E8832A')

# Operating Profit line — position labels to avoid overlap
ax2.plot(x, operating_profit, 's-', color='#D9534F', linewidth=3, markersize=12, label='Operating Profit', zorder=5)
op_labels = [
    (0, 55, 63, '#36CB2F', '55K  PROFIT', 'left'),   # Jan: push label left+up
    (1, -5, -18, '#FF4444', '-5K  LOSS', 'center'),  # Feb: below
    (2, -50, -62, '#FF4444', '-50K  LOSS', 'center'), # Mar: below
]
for xi, val, ly, c, txt, ha in op_labels:
    ax2.text(xi - 0.15 if ha == 'left' else xi, ly, txt, ha=ha, fontweight='bold', fontsize=13, color=c,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=c, alpha=0.9))

# Shade loss zone
ax2.axhspan(-70, 0, alpha=0.08, color='red', zorder=1)
ax2.axhline(y=0, color='black', linewidth=1, linestyle='-', alpha=0.5, zorder=2)
ax2.text(2.42, -35, 'LOSS\nZONE', ha='center', fontsize=12, fontweight='bold', color='#FF4444', alpha=0.5)

# Rule annotation — bottom-left to avoid legend collision
ax2.annotate('Rule: Bar > Dashed line = PROFIT\n          Bar < Dashed line = LOSS', 
             xy=(0.02, 0.02), xycoords='axes fraction',
             fontsize=11, fontweight='bold', ha='left', va='bottom',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF9C4', edgecolor='#D4A000', alpha=0.95))

# Remove plt.show() emoji glyphs by using ASCII
# (already handled above with plain text)

ax2.set_xlabel('Month', fontsize=14, fontweight='bold')
ax2.set_ylabel('Amount (K EGP)', fontsize=14, fontweight='bold')
ax2.set_title('Chart 2: Gross Profit vs. Period Cost — When do we lose money?', fontsize=15, fontweight='bold', pad=15)
ax2.set_xticks(x)
ax2.set_xticklabels(months, fontsize=13)
ax2.set_ylim(-75, 140)
ax2.legend(loc='upper right', fontsize=11, framealpha=0.9)
ax2.grid(axis='y', alpha=0.3)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

fig2.tight_layout()
fig2.savefig(os.path.join(script_dir, 'Chart2_Profit_Trend.png'), dpi=150, bbox_inches='tight', facecolor='white')
print("Chart 2 saved.")

plt.show()
