# Generates data/summaries.csv with an LLM and auto-checks every number against data/final.csv.
# Setup: pip install google-genai pandas ; set env var GEMINI_API_KEY (never commit it).
import os, re, pandas as pd
from google import genai

MODEL = "gemini-4-hydrogen"   # copy from aistudio.google.com
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
df = pd.read_csv("data/final.csv")
df.columns = df.columns.str.strip().str.lower()

PROMPT = """You are a financial analyst. Use ONLY the data below. No outside facts, no guesses.
Blank = not available. Do not calculate it.
Units: revenue, net_income, debt, equity in USD millions. Margins and rev_yoy in %. Annual, FY2022-2025.
Write exactly 3 lines:
1. Growth: revenue trend and YoY %.
2. Profitability: net margin and op margin trend.
3. Risk: debt-to-equity trend.
Each line must quote at least 1 number from the data. Max 25 words per line.

DATA:
"""

def clean(v):
    s = str(v)
    return s[:-2] if s.endswith(".0") else s

allowed = {clean(v) for v in df.drop(columns="ticker").stack().dropna()}
rows = []
for t, g in df.groupby("ticker"):
    r = client.models.generate_content(model=MODEL, contents=PROMPT + g.sort_values("year").to_csv(index=False))
    text = r.text.strip()
    nums = set(re.findall(r"-?\d+\.?\d*", text.replace(",", "")))
    bad = sorted(n for n in nums if clean(float(n)) not in allowed)
    print(t, "OK" if not bad else f"CHECK these numbers: {bad}")
    rows.append((t, " | ".join(l for l in text.splitlines() if l.strip())))

pd.DataFrame(rows, columns=["ticker", "summary"]).to_csv("summaries.csv", index=False, encoding="utf-8-sig")
print("Saved data/summaries.csv")
