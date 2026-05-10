"""Rebuild Q3 (Profit or Loss classification) in the report HTML."""
import base64
import os
import re


BASE_DIR = os.path.dirname(__file__)
HTML_PATH = os.path.join(BASE_DIR, "Project_Phase-1_Ahmed Refaat _ ICON company.html")
IMAGE_PATH = os.path.join(BASE_DIR, "Report_Images", "Profit_Losses_report.png")


def format_egp(value: int) -> str:
    text = f"{abs(value):,}"
    return f"({text})" if value < 0 else text


def badge_html(current: int, previous: int, favorable_when: str) -> str:
    current_size = abs(current)
    previous_size = abs(previous)
    if current_size >= previous_size:
        direction = "up"
        arrow = "&#9650;"
    else:
        direction = "down"
        arrow = "&#9660;"

    change = 0.0 if previous_size == 0 else abs((current_size - previous_size) / previous_size * 100)
    css_class = "up" if direction == favorable_when else "down"
    sign = "+" if direction == "up" else "-"
    return f'<span class="chart-change {css_class}">{arrow} {sign}{change:.1f}%</span>'


def comparison_row(label: str, current: int, previous: int, favorable_when: str, row_class: str = "") -> str:
    class_attr = f' class="{row_class}"' if row_class else ""
    return (
        f"<tr{class_attr}>"
        f"<td>{label}</td>"
        f"<td class=\"num\">{format_egp(current)}</td>"
        f"<td class=\"num\">{format_egp(previous)}</td>"
        f"<td class=\"num\">{badge_html(current, previous, favorable_when)}</td>"
        f"</tr>"
    )


def chart_item(label: str, current: int, previous: int, favorable_when: str, max_value: int, total: bool = False) -> str:
    row_class = " chart-total" if total else ""
    current_width = 0 if max_value == 0 else abs(current) / max_value * 100
    previous_width = 0 if max_value == 0 else abs(previous) / max_value * 100
    return f"""
            <div class="chart-item{row_class}">
                <div class="chart-label">{label}</div>
                <div class="chart-bars">
                    <div class="bar-row">
                        <div class="bar-year">2025</div>
                        <div class="bar-track"><div class="bar bar-2025" style="width:{current_width:.1f}%;"></div></div>
                        <div class="bar-val">{format_egp(current)}</div>
                    </div>
                    <div class="bar-row">
                        <div class="bar-year">2024</div>
                        <div class="bar-track"><div class="bar bar-2024" style="width:{previous_width:.1f}%;"></div></div>
                        <div class="bar-val">{format_egp(previous)}</div>
                    </div>
                </div>
                {badge_html(current, previous, favorable_when)}
            </div>"""


with open(HTML_PATH, "r", encoding="utf-8") as file_handle:
    html = file_handle.read()

if 'value="q3"' not in html:
    html = html.replace(
        '<option value="q2">Q2: How did the company classify the Statement of Financial Position?</option>',
        '<option value="q2">Q2: How did the company classify the Statement of Financial Position?</option>\n'
        '            <option value="q3">Q3: How did the company classify the Statement of Profit or Loss?</option>',
    )

with open(IMAGE_PATH, "rb") as file_handle:
    profit_loss_image = base64.b64encode(file_handle.read()).decode("ascii")

revenue_rows = [
    ("Revenue from contracts with customers", 5_337_752_819, 4_551_152_418, "up"),
    ("Cost of revenue", -3_382_179_943, -2_850_783_885, "down"),
    ("Gross profit", 1_955_572_876, 1_700_368_533, "up"),
]

operating_rows = [
    ("Revenue from contracts with customers", 5_337_752_819, 4_551_152_418, "up"),
    ("Cost of revenue", -3_382_179_943, -2_850_783_885, "down"),
    ("Gross profit", 1_955_572_876, 1_700_368_533, "up"),
    ("General and administrative expenses", -431_081_223, -294_958_718, "down"),
    ("Selling and marketing expenses", -209_574_721, -113_383_806, "down"),
    ("Other operating income", 64_524_708, 53_928_915, "up"),
    ("Other operating expenses", -48_071_611, -31_006_212, "down"),
    ("Net impairment losses on financial assets", -181_255_926, -625_489_357, "down"),
    ("Operating profit", 1_150_114_103, 689_459_355, "up"),
]

non_operating_rows = [
    ("Finance costs", -430_403_477, -279_721_905, "down"),
    ("Financing income", 14_086_727, 799_840_952, "up"),
    ("Share of associates' profits", 33_031_645, 63_913_002, "up"),
    ("Profit before tax", 766_828_998, 1_273_491_404, "up"),
    ("Income tax", -240_879_399, -458_976_136, "down"),
    ("Profit for the period", 525_949_599, 814_515_268, "up"),
]

chart_max_value = max(max(abs(current), abs(previous)) for _, current, previous, _ in revenue_rows)
trend_chart_html = "".join(
    chart_item(label, current, previous, favorable_when, chart_max_value, total=(label == "Gross profit"))
    for label, current, previous, favorable_when in revenue_rows
)

operating_table_html = "".join(
    comparison_row(label, current, previous, favorable_when, row_class="grand-total" if label == "Operating profit" else "")
    for label, current, previous, favorable_when in operating_rows
)
non_operating_table_html = "".join(
    comparison_row(label, current, previous, favorable_when, row_class="grand-total" if label == "Profit for the period" else "")
    for label, current, previous, favorable_when in non_operating_rows
)

Q3_HTML = f"""
    <!-- Q3 Answer -->
    <div class="answer-section" id="answer-q3">

        <div class="photo-col" style="max-width:750px; margin:0 auto 24px;">
            <div class="photo-col-label">Consolidated Statement of Profit or Loss &mdash; 9 months ended 30 Sep 2025</div>
            <img src="data:image/png;base64,{profit_loss_image}" alt="Consolidated Profit or Loss">
        </div>

        <div class="analysis-section">
            <h3>Presentation Format Under Egyptian Accounting Standards</h3>
            <p>
                The company presents the statement of profit or loss using the <strong>standard Egyptian Accounting Standards format</strong>,
                and it follows a <strong>multi-step income statement</strong> presentation.
                The statement moves step by step from revenue to gross profit, then to operating profit,
                then to profit before tax, and finally to profit for the period.
            </p>
            <p>
                In other words, the report does not jump directly to one net result.
                It shows each performance layer separately so the reader can distinguish
                the core business result from financing and investment-related results.
            </p>
        </div>

        <div class="analysis-section">
            <h3>Can We Differentiate Between Operating and Non-Operating Sections?</h3>
            <p>
                Yes. The statement can be separated clearly.
                The first visible block starts with <strong>revenue</strong>, <strong>cost of revenue</strong>,
                and <strong>gross profit</strong>, then continues through the other operating items until <strong>operating profit</strong>.
                After operating profit, the statement moves to the <strong>non-operating section</strong>,
                which includes <strong>finance costs</strong>, <strong>financing income</strong>, and
                <strong>the Group's share in associates' profits</strong>, followed by tax and the final profit figure.
            </p>
        </div>

        <div class="trend-card">
            <div class="trend-card-header">Revenue, Cost of Revenue, and Gross Profit | 9M 2024 vs 9M 2025</div>
            {trend_chart_html}
            <div class="trend-desc">
                Revenue increased by <strong>EGP 786.6M (+17.3%)</strong> in 2025.
                Cost of revenue also increased by <strong>EGP 531.4M (+18.6%)</strong>,
                but gross profit still improved by <strong>EGP 255.2M (+15.0%)</strong>.
                This means the company generated more business volume in 2025, although it also carried higher direct project costs.
            </div>
        </div>

        <div class="analysis-section">
            <p>
                The blue panel below shows the <strong>operating section</strong>, and the yellow panel shows the <strong>non-operating section</strong>.
                The last column compares 2025 with 2024. Green means the movement is favorable, while red means it is unfavorable.
            </p>

            <div style="display:flex; gap:20px; flex-wrap:wrap; margin-top:16px; align-items:flex-start;">

                <div style="flex:1; min-width:360px; border:3px solid #2a6496; border-radius:12px; overflow:hidden; background:#fff;">
                    <div style="background:#2a6496; color:#fff; padding:10px 16px; font-weight:700; font-size:0.95rem;">
                        &#9881; OPERATING SECTION | 2025 vs 2024
                    </div>
                    <table class="data-table" style="margin:0; box-shadow:none;">
                        <tr class="section-header">
                            <td>Item</td>
                            <td class="num">2025</td>
                            <td class="num">2024</td>
                            <td class="num">Change</td>
                        </tr>
                        {operating_table_html}
                    </table>
                </div>

                <div style="flex:1; min-width:360px; border:3px solid #e8a735; border-radius:12px; overflow:hidden; background:#fff;">
                    <div style="background:#e8a735; color:#fff; padding:10px 16px; font-weight:700; font-size:0.95rem;">
                        &#128181; NON-OPERATING SECTION | 2025 vs 2024
                    </div>
                    <table class="data-table" style="margin:0; box-shadow:none;">
                        <tr class="section-header">
                            <td>Item</td>
                            <td class="num">2025</td>
                            <td class="num">2024</td>
                            <td class="num">Change</td>
                        </tr>
                        {non_operating_table_html}
                    </table>
                </div>

            </div>
        </div>

        <div class="analysis-section">
            <h3>What Items Are Classified as Operating Items?</h3>
            <p>The main items classified as operating items in this statement are:</p>
            <ol class="order-list">
                <li><span class="order-badge">1</span><span class="label"><strong>Revenue from contracts with customers</strong></span><span class="value">5,337,752,819</span></li>
                <li><span class="order-badge">2</span><span class="label"><strong>Cost of revenue</strong></span><span class="value">(3,382,179,943)</span></li>
                <li><span class="order-badge">3</span><span class="label"><strong>Gross profit</strong></span><span class="value">1,955,572,876</span></li>
                <li><span class="order-badge">4</span><span class="label"><strong>General and administrative expenses</strong></span><span class="value">(431,081,223)</span></li>
                <li><span class="order-badge">5</span><span class="label"><strong>Selling and marketing expenses</strong></span><span class="value">(209,574,721)</span></li>
                <li><span class="order-badge">6</span><span class="label"><strong>Other operating income</strong></span><span class="value">64,524,708</span></li>
                <li><span class="order-badge">7</span><span class="label"><strong>Other operating expenses</strong></span><span class="value">(48,071,611)</span></li>
                <li><span class="order-badge">8</span><span class="label"><strong>Net impairment losses on financial assets</strong></span><span class="value">(181,255,926)</span></li>
                <li><span class="order-badge">9</span><span class="label"><strong>Operating profit</strong></span><span class="value">1,150,114,103</span></li>
            </ol>
        </div>

        <div class="analysis-section">
            <h3>Other Income / Expense Items Reported on the Statement</h3>
            <div style="display:flex; gap:20px; flex-wrap:wrap; margin-top:12px;">
                <div style="flex:1; min-width:280px;">
                    <div style="background:#e6f7ec; border:2px solid #1a7a3a; border-radius:10px; padding:16px;">
                        <div style="font-weight:700; color:#1a7a3a; font-size:1rem; margin-bottom:10px;">
                            &#9989; Other Operating Income (Note 5/B)
                        </div>
                        <p style="font-size:0.9rem; line-height:1.6; color:#333; margin:0;">
                            Reported as a separate operating income line.<br>
                            2025: <strong>EGP 64,524,708</strong><br>
                            2024: <strong>EGP 53,928,915</strong>
                        </p>
                    </div>
                </div>
                <div style="flex:1; min-width:280px;">
                    <div style="background:#fde8e8; border:2px solid #b91c1c; border-radius:10px; padding:16px;">
                        <div style="font-weight:700; color:#b91c1c; font-size:1rem; margin-bottom:10px;">
                            &#10060; Other Operating Expenses (Note 5/C)
                        </div>
                        <p style="font-size:0.9rem; line-height:1.6; color:#333; margin:0;">
                            Reported as a separate operating expense line.<br>
                            2025: <strong>EGP (48,071,611)</strong><br>
                            2024: <strong>EGP (31,006,212)</strong>
                        </p>
                    </div>
                </div>
            </div>
            <p style="margin-top:14px;">
                In addition, after operating profit the statement separately reports <strong>financing income</strong>,
                <strong>finance costs</strong>, and <strong>the Group's share in the net profits of associates</strong>.
                The detailed sub-components of Note 5/B and Note 5/C are disclosed in the notes, not on this face page.
            </p>
        </div>

        <div class="comment-box">
            <strong>Summary:</strong><br>
            &#8226; The company uses the standard <em>multi-step</em> statement of profit or loss format under Egyptian Accounting Standards.<br>
            &#8226; Revenue, cost of revenue, and gross profit form the opening operating block, and the operating section continues down to operating profit.<br>
            &#8226; Operating profit improved strongly in 2025, but lower financing income and higher finance costs reduced the final profit for the period.<br>
            &#8226; The key operating "other" lines reported on the face of the statement are <strong>Other operating income</strong> (Note 5/B) and <strong>Other operating expenses</strong> (Note 5/C).
        </div>
    </div>
"""

pattern = re.compile(r"    <!-- Q3 Answer -->.*?(?=\n    </div>\n\n</div>\n\n<script>)", re.S)
if pattern.search(html):
    html = pattern.sub(Q3_HTML.rstrip() + "\n", html, count=1)
else:
    html = html.replace(
        '    </div>\n\n</div>\n\n<script>',
        Q3_HTML + '\n    </div>\n\n</div>\n\n<script>',
    )

with open(HTML_PATH, "w", encoding="utf-8") as file_handle:
    file_handle.write(html)

print("Done - Q3 rebuilt.")
