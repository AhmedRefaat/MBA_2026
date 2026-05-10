"""Embed Profit_Losses_report.png at the top of Q3 in the report HTML."""
import os, base64

BASE = os.path.dirname(__file__)
HTML_PATH = os.path.join(BASE, "Project_Phase-1_Ahmed Refaat _ ICON company.html")
IMG_PATH = os.path.join(BASE, "Report_Images", "Profit_Losses_report.png")

# Read and encode the image
with open(IMG_PATH, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

# Build the image block
img_block = (
    '<div class="photo-col" style="max-width:750px; margin:0 auto 24px;">\n'
    '                <div class="photo-col-label">Consolidated Statement of Profit or Loss &mdash; 9 months ended 30 Sep 2025</div>\n'
    f'                <img src="data:image/png;base64,{b64}" alt="Consolidated Profit or Loss">\n'
    '            </div>'
)

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Insert right after the Q3 answer-section opening div
old = '<div class="answer-section" id="answer-q3">\n\n        <!-- ── Part A'
new = '<div class="answer-section" id="answer-q3">\n\n            ' + img_block + '\n\n        <!-- ── Part A'

html = html.replace(old, new, 1)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Done — Profit/Loss image embedded at top of Q3.")
