"""Add comparison mini-charts (2024 vs 2025) to Q2 in the report HTML."""
import os

HTML_PATH = os.path.join(os.path.dirname(__file__),
    "Project_Phase-1_Ahmed Refaat _ ICON company.html")

# ── Data from consolidated statement: 31 Dec 2024 vs 30 Sep 2025 ──
charts_data = {
    "assets": [
        ("Non-current Assets", 1_760_561_739, 1_928_784_709),
        ("Current Assets",     5_199_422_281, 5_264_516_290),
        ("Total Assets",       6_959_984_020, 7_193_300_999),
    ],
    "equity": [
        ("Equity (Parent)",        2_427_335_160, 2_469_275_417),
        ("Non-controlling Int.",     520_532_300,   608_005_323),
        ("Total Equity",           2_947_867_460, 3_077_280_740),
    ],
    "liabilities": [
        ("Non-current Liabilities",  255_462_406,   219_638_197),
        ("Current Liabilities",    3_756_654_154, 3_896_382_062),
        ("Total Liabilities",      4_012_116_560, 4_116_020_259),
    ],
}

descriptions = {
    "assets": "Total assets grew by <strong>EGP 233.3M (+3.4%)</strong> from Dec 2024 to Sep 2025. "
              "Non-current assets rose significantly (+9.6%) driven by new construction projects and investment in associates, "
              "while current assets had a modest increase (+1.3%).",
    "equity": "Total equity increased by <strong>EGP 129.4M (+4.4%)</strong>. "
              "Retained earnings grew as the company remained profitable. "
              "Non-controlling interests also rose by 16.8%, reflecting subsidiary growth.",
    "liabilities": "Total liabilities increased slightly by <strong>EGP 103.9M (+2.6%)</strong>. "
                    "Non-current liabilities <em>decreased</em> by 14.0% (lower deferred tax), "
                    "but current liabilities rose by 3.7% mainly due to higher credit facilities and trade payables.",
}

def fmt(n):
    """Format number with commas."""
    return f"{n:,.0f}"

def pct_change(old, new):
    return ((new - old) / old) * 100

def build_chart_html(category, items):
    """Build a single chart card with horizontal bars."""
    # Find max value for scaling
    max_val = max(max(v2024, v2025) for _, v2024, v2025 in items)

    rows = ""
    for label, v2024, v2025 in items:
        pct = pct_change(v2024, v2025)
        arrow = "&#9650;" if pct >= 0 else "&#9660;"
        color_cls = "up" if pct >= 0 else "down"
        bar_w_2024 = (v2024 / max_val) * 100
        bar_w_2025 = (v2025 / max_val) * 100
        is_total = label.startswith("Total")
        bold = "font-weight:700;" if is_total else ""

        rows += f"""
            <div class="chart-item{' chart-total' if is_total else ''}">
                <div class="chart-label" style="{bold}">{label}</div>
                <div class="chart-bars">
                    <div class="bar-row">
                        <span class="bar-year">2024</span>
                        <div class="bar-track">
                            <div class="bar bar-2024" style="width:{bar_w_2024:.1f}%"></div>
                        </div>
                        <span class="bar-val">{fmt(v2024)}</span>
                    </div>
                    <div class="bar-row">
                        <span class="bar-year">2025</span>
                        <div class="bar-track">
                            <div class="bar bar-2025" style="width:{bar_w_2025:.1f}%"></div>
                        </div>
                        <span class="bar-val">{fmt(v2025)}</span>
                    </div>
                </div>
                <div class="chart-change {color_cls}">
                    <span class="arrow">{arrow}</span> {pct:+.1f}%
                </div>
            </div>"""

    desc = descriptions[category]
    return f"""
        <div class="trend-card">
            <div class="trend-card-header">31 Dec 2024 vs 30 Sep 2025</div>
            {rows}
            <div class="trend-desc">{desc}</div>
        </div>"""


# ── New CSS ──
NEW_CSS = """
        /* ── Trend charts ── */
        .trend-card {
            background: #fff; border: 2px solid #d4e9f7; border-radius: 10px;
            padding: 20px; margin: 16px 0 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        .trend-card-header {
            font-size: 0.82rem; font-weight: 600; color: #fff;
            background: #2a6496; display: inline-block;
            padding: 4px 14px; border-radius: 20px; margin-bottom: 16px;
        }
        .chart-item {
            display: flex; align-items: center; gap: 12px;
            padding: 8px 0; border-bottom: 1px solid #f0f4f8;
        }
        .chart-item:last-of-type { border-bottom: none; }
        .chart-total { background: #f5faff; margin: 4px -12px; padding: 10px 12px; border-radius: 6px; }
        .chart-label { flex: 0 0 180px; font-size: 0.88rem; color: #333; }
        .chart-bars { flex: 1; }
        .bar-row { display: flex; align-items: center; gap: 8px; margin: 2px 0; }
        .bar-year { flex: 0 0 34px; font-size: 0.72rem; color: #888; text-align: right; }
        .bar-track { flex: 1; height: 16px; background: #f0f4f8; border-radius: 8px; overflow: hidden; }
        .bar { height: 100%; border-radius: 8px; transition: width 0.6s ease; }
        .bar-2024 { background: linear-gradient(90deg, #a8d4f5, #7ab8db); }
        .bar-2025 { background: linear-gradient(90deg, #2a6496, #1a3a5c); }
        .bar-val { flex: 0 0 130px; font-size: 0.75rem; color: #555; font-family: 'Consolas', monospace; text-align: right; }
        .chart-change {
            flex: 0 0 75px; text-align: center; font-size: 0.85rem;
            font-weight: 700; border-radius: 6px; padding: 4px 8px;
        }
        .chart-change.up { color: #1a7a3a; background: #e6f7ec; }
        .chart-change.down { color: #b91c1c; background: #fde8e8; }
        .chart-change .arrow { font-size: 0.7rem; }
        .trend-desc {
            margin-top: 14px; padding: 12px 16px;
            background: #f9fbfd; border-left: 4px solid #a8d4f5;
            border-radius: 4px; font-size: 0.9rem; line-height: 1.65; color: #444;
        }
"""

# ── Build chart HTML for each section ──
assets_chart = build_chart_html("assets", charts_data["assets"])
equity_chart = build_chart_html("equity", charts_data["equity"])
liabilities_chart = build_chart_html("liabilities", charts_data["liabilities"])

# ── Load and modify HTML ──
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Insert CSS (before the trend-card styles if not present, or before @keyframes)
if ".trend-card" not in html:
    html = html.replace(
        "        @keyframes fadeIn {",
        NEW_CSS + "\n        @keyframes fadeIn {"
    )

# 2. Insert charts after each photo-row section in Q2
# After Assets photo-row (before Equity heading)
html = html.replace(
    '            <!-- ═══ EQUITY ═══ -->',
    assets_chart + '\n\n            <!-- ═══ EQUITY ═══ -->'
)

# After Equity photo-row (before Liabilities heading)
html = html.replace(
    '            <!-- ═══ LIABILITIES ═══ -->',
    equity_chart + '\n\n            <!-- ═══ LIABILITIES ═══ -->'
)

# After Liabilities photo-row (before </div> of photo-breakdown)
html = html.replace(
    '        </div>\n\n        <div class="comment-box">\n            <strong>Key observations:</strong>',
    liabilities_chart + '\n\n        </div>\n\n        <div class="comment-box">\n            <strong>Key observations:</strong>'
)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Done — trend charts added to Q2.")
