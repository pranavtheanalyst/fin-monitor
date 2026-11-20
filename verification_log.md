# AI Summary Verification Log
Method: every number in each AI summary recomputed from fin data (final.csv). Source: stockanalysis.com, USD millions.

| Ticker | Claim checked | Actual | Correct? |
|---|---|---|---|
| AAPL | YoY 2023 / 2024 / 2025 = -2.8 / 2.02 / 6.43% | -2.80 / 2.02 / 6.43 | Yes |
| AAPL | Op margin 30.29% to 31.97% | 30.29 / 31.97 | Yes |
| AAPL | Net margin 23.97% (2024), 26.92% (2025) | 23.97 / 26.92 | Yes |
| AAPL | D/E 2.61 to 1.52; 1.99 to 2.09 in 2024 | 2.61 / 1.52 / 1.99 / 2.09 | Yes |
| MSFT | YoY 6.88 / 15.67 / 14.93% | Same | Yes |
| MSFT | Op margin 42.06 / 41.77 / 44.64 / 45.62% | Same | Yes |
| MSFT | Net margin 36.69 / 34.15 / 35.96 / 36.15% | Same | Yes |
| MSFT | D/E 0.47 to 0.33; equity 343,479; debt 112,184 | Same | Yes |
| GOOGL | YoY 8.68 / 13.87 / 15.09% | Same | Yes |
| GOOGL | Net margin 21.2 to 32.81%; op margin 26.46 to 32.03% | Same | Yes |
| GOOGL | D/E 0.12, 0.09 (2024), 0.16 (2025); debt 66,996 | Same | Yes |
| AMZN | YoY 11.83 / 10.99 / 12.38% | Same | Yes |
| AMZN | Net margin -0.53 to 10.83%; op margin 2.6 to 11.16% | Same | Yes |
| AMZN | D/E 1.16 to 0.43, falling every year | 1.16 / 0.80 / 0.54 / 0.43 | Yes |
| META | YoY 15.69 / 21.94 / 22.17% | Same | Yes |
| META | Net margin 19.9 / 37.91 / 30.08%; op margin 28.78 / 42.18 / 41.44% | Same | Yes |
| META | D/E 0.21 / 0.24 / 0.27 / 0.39; debt 26,591 to 85,081 | Same | Yes |

## Findings
- Numeric errors: 0 of 17 claim groups.
- Interpretive wording (not numbers): AMZN "leverage risk is declining" ignores that absolute debt rose in 2025 (155,401 to 178,547); the ratio fell only because equity grew faster. META "accelerating" rests on a small last step (21.94 to 22.17%).
- No outside facts found in any summary.
- Prompt rules that worked: use only given data, blank = not available, one company per chat.

AI layer is manual. API automation is v2.
