"""Rebuild Q2 in the report HTML with embedded base64 images in a 3-column layout."""
import base64, os

HTML_PATH = os.path.join(os.path.dirname(__file__),
    "Project_Phase-1_Ahmed Refaat _ ICON company.html")
IMG_DIR = os.path.join(os.path.dirname(__file__), "Report_Images")

def b64(name):
    with open(os.path.join(IMG_DIR, name), "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

# Load images
imgs = {
    "stmt":        b64("Classification4Statement_Current_NonCurrent.png"),
    "nca":         b64("Classification4Statement_AssetsNonCurrent.png"),
    "ca":          b64("Classification4Statement_AssetsCurrent.png"),
    "total_a":     b64("Classification4Statement_TotalAssets.png"),
    "equity":      b64("Classification4Statement_TotalEquity.png"),
    "ncl":         b64("Classification4Statement_LiabilitiesNonCurrent.png"),
    "cl":          b64("Classification4Statement_LiabilitiesCurrent.png"),
    "total_l":     b64("Classification4Statement_TotalLiabilities.png"),
}

NEW_CSS = """
        /* ── Q2 three-column photo layout ── */
        .photo-breakdown { margin-top: 24px; }
        .photo-breakdown h3 {
            font-size: 1.1rem; color: #1a3a5c; margin: 24px 0 12px;
            border-bottom: 2px solid #a8d4f5; padding-bottom: 6px;
        }
        .photo-breakdown h3:first-child { margin-top: 0; }
        .photo-row {
            display: flex; gap: 16px; align-items: flex-start;
            margin-bottom: 20px; flex-wrap: wrap;
        }
        .photo-col {
            flex: 1; min-width: 200px;
            border: 3px solid #a8d4f5; border-radius: 10px;
            overflow: hidden; background: #fff;
            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        }
        .photo-col.stmt-col { flex: 0 0 320px; }
        .photo-col img { width: 100%; display: block; }
        .photo-col-label {
            background: #1a3a5c; color: #fff; text-align: center;
            padding: 6px 10px; font-size: 0.82rem; font-weight: 600;
        }
        .arrow-col {
            flex: 0 0 40px; display: flex; align-items: center;
            justify-content: center; font-size: 1.8rem; color: #7ab8db;
            min-width: 40px;
        }
"""

NEW_Q2 = f"""<!-- Q2 Answer -->
    <div class="answer-section" id="answer-q2">
        <div class="analysis-section">
            <h3>Classification of the Statement of Financial Position</h3>
            <p>
                ICON (S.A.E.) uses a <strong>classified (grouped) balance sheet</strong> format,
                which separates assets into <strong>non-current</strong> and <strong>current</strong>,
                and liabilities into <strong>non-current</strong> and <strong>current</strong>,
                with <strong>equity</strong> presented between assets and liabilities.
                This follows <strong>Egyptian Accounting Standard (EAS)</strong>.
            </p>
        </div>

        <div class="photo-breakdown">

            <!-- ═══ ASSETS ═══ -->
            <h3>&#128200; Assets Breakdown</h3>
            <div class="photo-row">
                <div class="photo-col stmt-col">
                    <div class="photo-col-label">Full Statement</div>
                    <img src="{imgs['stmt']}" alt="Full Statement">
                </div>
                <div class="arrow-col">&#10132;</div>
                <div class="photo-col">
                    <div class="photo-col-label">Non-current Assets</div>
                    <img src="{imgs['nca']}" alt="Non-current Assets">
                    <div style="border-top:2px dashed #a8d4f5;"></div>
                    <div class="photo-col-label" style="background:#2a6496;">Current Assets</div>
                    <img src="{imgs['ca']}" alt="Current Assets">
                </div>
                <div class="arrow-col">&#10132;</div>
                <div class="photo-col">
                    <div class="photo-col-label" style="background:#174068;">Total Assets</div>
                    <img src="{imgs['total_a']}" alt="Total Assets">
                </div>
            </div>

            <!-- ═══ EQUITY ═══ -->
            <h3>&#128176; Equity</h3>
            <div class="photo-row">
                <div class="photo-col">
                    <div class="photo-col-label" style="background:#2a6496;">Total Equity</div>
                    <img src="{imgs['equity']}" alt="Total Equity">
                </div>
            </div>

            <!-- ═══ LIABILITIES ═══ -->
            <h3>&#128181; Liabilities Breakdown</h3>
            <div class="photo-row">
                <div class="photo-col">
                    <div class="photo-col-label">Non-current Liabilities</div>
                    <img src="{imgs['ncl']}" alt="Non-current Liabilities">
                    <div style="border-top:2px dashed #a8d4f5;"></div>
                    <div class="photo-col-label" style="background:#2a6496;">Current Liabilities</div>
                    <img src="{imgs['cl']}" alt="Current Liabilities">
                </div>
                <div class="arrow-col">&#10132;</div>
                <div class="photo-col">
                    <div class="photo-col-label" style="background:#174068;">Total Liabilities</div>
                    <img src="{imgs['total_l']}" alt="Total Liabilities">
                </div>
            </div>

        </div>

        <div class="comment-box">
            <strong>Key observations:</strong><br>
            &#8226; Assets are presented from <em>least liquid to most liquid</em>
            (fixed assets &rarr; cash), standard under Egyptian Accounting Standards.<br>
            &#8226; Equity is presented <em>before</em> liabilities, reflecting Assets = Equity + Liabilities.<br>
            &#8226; Liabilities follow the same permanence order: non-current before current.<br>
            &#8226; The balance sheet balances: Total Assets = Total Equity &amp; Liabilities. &#10003;
        </div>
    </div>"""

# ── Apply changes ──
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Insert new CSS before the @keyframes rule
html = html.replace(
    "        @keyframes fadeIn {",
    NEW_CSS + "\n        @keyframes fadeIn {"
)

# 2. Replace Q2 section
q2_start = html.find("<!-- Q2 Answer -->")
# Find the closing </div> of Q2 answer-section, then the parent </div> (container)
q2_end_marker = "    </div>\n\n</div>\n\n<script>"
q2_end = html.find(q2_end_marker, q2_start)
old_q2 = html[q2_start:q2_end]
html = html.replace(old_q2, NEW_Q2 + "\n\n")

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Done — Q2 rebuilt with embedded images.")
