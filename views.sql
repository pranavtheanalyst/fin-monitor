CREATE VIEW v_margins AS
SELECT ticker, year, revenue, net_income,
 ROUND(100.0*op_income/revenue,2) AS op_margin,
 ROUND(100.0*net_income/revenue,2) AS net_margin
FROM fin;

CREATE VIEW v_growth AS
SELECT ticker, year,
 ROUND(100.0*(revenue - LAG(revenue) OVER (PARTITION BY ticker ORDER BY year))
 / LAG(revenue) OVER (PARTITION BY ticker ORDER BY year),2) AS rev_yoy
FROM fin;

CREATE VIEW v_leverage AS
SELECT ticker, year, debt, equity,
 ROUND(1.0*debt/equity,2) AS debt_to_equity
FROM fin;

CREATE VIEW v_rolling AS
SELECT ticker, year,
 ROUND(AVG(net_margin) OVER (PARTITION BY ticker ORDER BY year
  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW),2) AS net_margin_3y_avg
FROM v_margins;

CREATE VIEW v_final AS
SELECT m.ticker, m.year, m.revenue, m.net_income,
 m.op_margin, m.net_margin, g.rev_yoy,
 l.debt, l.equity, l.debt_to_equity, r.net_margin_3y_avg
FROM v_margins m
JOIN v_growth g ON m.ticker=g.ticker AND m.year=g.year
JOIN v_leverage l ON m.ticker=l.ticker AND m.year=l.year
JOIN v_rolling r ON m.ticker=r.ticker AND m.year=r.year;