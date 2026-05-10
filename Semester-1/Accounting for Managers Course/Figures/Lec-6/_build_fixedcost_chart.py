import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Units produced
units = np.arange(100, 2001, 50)

# Costs (using ice cream bar example)
fixed_cost = 400  # total fixed cost
var_cost_per_unit = 0.50
sell_price = 1.50  # assume selling price

fixed_per_unit = fixed_cost / units
var_per_unit = np.full_like(units, var_cost_per_unit, dtype=float)
total_cost_per_unit = fixed_per_unit + var_per_unit

# Break-even point: where sell price = total cost per unit
# 1.50 = 400/x + 0.50 => 1.00 = 400/x => x = 400
break_even = int(fixed_cost / (sell_price - var_cost_per_unit))

fig, ax = plt.subplots(figsize=(10, 6))

# Plot lines
ax.plot(units, total_cost_per_unit, 'r-', linewidth=2.5, label='Total Cost per Unit')
ax.plot(units, fixed_per_unit, 'b--', linewidth=2, label='Fixed Cost per Unit')
ax.axhline(y=var_cost_per_unit, color='orange', linestyle=':', linewidth=2, label=f'Variable Cost per Unit ($0.50)')
ax.axhline(y=sell_price, color='green', linestyle='-', linewidth=2.5, label=f'Selling Price (${sell_price:.2f})')

# Fill profit zone (where sell price > total cost)
profit_mask = total_cost_per_unit <= sell_price
ax.fill_between(units, total_cost_per_unit, sell_price, where=profit_mask,
                alpha=0.2, color='green', label='PROFIT Zone')

# Fill loss zone (where total cost > sell price)
loss_mask = total_cost_per_unit > sell_price
ax.fill_between(units, sell_price, total_cost_per_unit, where=loss_mask,
                alpha=0.2, color='red', label='LOSS Zone')

# Mark break-even point
ax.axvline(x=break_even, color='purple', linestyle='--', linewidth=1.5, alpha=0.7)
ax.plot(break_even, sell_price, 'ko', markersize=10, zorder=5)
ax.annotate(f'Break-Even\n{break_even} units', xy=(break_even, sell_price),
            xytext=(break_even + 150, sell_price + 0.5),
            fontsize=11, fontweight='bold', color='purple',
            arrowprops=dict(arrowstyle='->', color='purple', lw=2))

# Labels
ax.set_xlabel('Number of Units Produced', fontsize=12, fontweight='bold')
ax.set_ylabel('Cost / Price per Unit ($)', fontsize=12, fontweight='bold')
ax.set_title('Fixed Cost Advantage: More Volume = More Profit', fontsize=14, fontweight='bold')
ax.legend(loc='upper right', fontsize=10)
ax.set_xlim(100, 2000)
ax.set_ylim(0, 5)
ax.grid(True, alpha=0.3)

# Add annotation for the key insight
ax.annotate('Fixed Cost shrinks per unit\nas volume increases!',
            xy=(600, fixed_cost/600), xytext=(800, 3.0),
            fontsize=10, fontstyle='italic', color='blue',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

plt.tight_layout()
plt.savefig(r'c:\Personal\Personal Docs\2025-Doc\Daily\MBA\Semester-1\Accounting for Managers Course\Figures\Lec-6\Chart3_FixedCost_Profit.png', dpi=150, bbox_inches='tight')
print('Chart saved successfully!')
