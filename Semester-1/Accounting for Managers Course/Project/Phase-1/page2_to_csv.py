import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "Page-2_Balance_Sheet.csv")

rows = [
    ["INDUSTRIAL ENGINEERING AND ARCHITECTURE COMPANY FOR CONSTRUCTION AND DEVELOPMENT 'ICON' (S.A.E.)"],
    ["Separate statement of financial position - As of 31 December 2024"],
    ["(All amounts are shown in Egyptian pounds)"],
    [],
    ["Item", "Note", "2024", "2023"],
    # Non-current assets
    ["Non-current assets", "", "", ""],
    ["Fixed assets", "5", "13142242", "8706135"],
    ["Projects under construction", "6", "597205", ""],
    ["Investment properties", "7", "59597803", "62867681"],
    ["Investments in subsidiaries", "8", "780777362", "780783340"],
    ["Total non-current assets", "", "854114612", "852357156"],
    [],
    # Current assets
    ["Current assets", "", "", ""],
    ["Inventory", "9", "280271", "449944"],
    ["Trade and notes receivable", "10", "5073304", "19836427"],
    ["Due from related parties", "11-1", "107638507", "75948107"],
    ["Debtors and other debit balances", "12", "32261378", "26639456"],
    ["Cash and cash equivalents", "13", "6264748", "14301101"],
    ["Total current assets", "", "151518208", "137175035"],
    ["Total assets", "", "1005632820", "989532191"],
    [],
    # Equity
    ["Equity", "", "", ""],
    ["Issued and paid-up capital", "14", "582000000", "582000000"],
    ["Legal reserve", "15", "37445572", "26968230"],
    ["Retained earnings", "", "279586857", "268017554"],
    ["Total equity", "", "899032429", "876985784"],
    [],
    # Non-current liabilities
    ["Liabilities", "", "", ""],
    ["Non-current liabilities", "", "", ""],
    ["Deferred income tax liabilities", "16", "11753199", "438490"],
    ["Bank loans - non-current portion", "17-b", "2787977", "6842801"],
    ["Total non-current liabilities", "", "14541176", "7281291"],
    [],
    # Current liabilities
    ["Current liabilities", "", "", ""],
    ["Provisions", "18", "18543670", "22874672"],
    ["Banks - credit balances", "17-a", "1607", "413"],
    ["Bank loans - current portion", "17-a", "4054826", "4392344"],
    ["Trade and notes payable", "19", "3612115", "32663507"],
    ["Due to related parties", "11-2", "43999933", "1514959"],
    ["Creditors and other credit balances", "20", "16285515", "17737212"],
    ["Current income tax liabilities", "21", "5561549", "26082009"],
    ["Total current liabilities", "", "92059215", "105265116"],
    ["Total liabilities", "", "106600391", "112546407"],
    ["Total equity and liabilities", "", "1005632820", "989532191"],
]

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"CSV saved to: {output_path}")
