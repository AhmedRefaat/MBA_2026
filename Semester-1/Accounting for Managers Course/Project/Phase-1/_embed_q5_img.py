"""Embed Q5-Receivable.png at the top of Q5 in the report HTML."""
import os, base64

BASE = os.path.dirname(__file__)
HTML_PATH = os.path.join(BASE, "Project_Phase-1_Ahmed Refaat _ ICON company.html")
IMG_PATH = os.path.join(BASE, "Report_Images", "Q5-Receivable.png")

# Read and encode the image
with open(IMG_PATH, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

# Build the image block
img_block = (
    '<div class="photo-col" style="max-width:750px; margin:0 auto 24px;">\n'
    '            <div class="photo-col-label">Note 9 &mdash; Trade and Notes Receivables (from Financial Statements)</div>\n'
    f'            <img src="data:image/png;base64,{b64}" alt="Note 9 - Trade and Notes Receivables">\n'
    '        </div>'
)

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Insert right after the Q5 answer-section opening div
marker = '<div class="answer-section" id="answer-q5">'
idx = html.find(marker)
if idx == -1:
    print("ERROR: Could not find Q5 answer-section marker.")
else:
    insert_pos = idx + len(marker)
    html = html[:insert_pos] + '\n\n        ' + img_block + '\n' + html[insert_pos:]
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("Done — Note 9 image embedded at top of Q5.")
