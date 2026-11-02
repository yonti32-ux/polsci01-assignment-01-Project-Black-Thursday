# Educational policy model — methodology v1.0

**NOT a 1983 data reconstruction, causal estimate, prediction, or validated counterfactual.** A transparent twelve-period deterministic illustration of limited bank support and finite public intervention.

## Inputs
`confidence` (0–100), `sell_pressure` (0–100), `bank_capacity` (0–100), `intervention` (`none`, `delayed`, `early`). All are hypothetical. Every request executes actual Python source at `python/simulation.py`.

## State and computation
Starting index `I_0 = 100`. Each of 12 illustrative periods uses unrounded state variables:

- `D_t = clamp(4 + .18*sell_pressure + .12*(100-confidence) + .10*(100-I_(t-1)),0,100)`
- `B_0=3.2*bank_capacity`; `b_t=min(D_t,12,B_(t-1))`, then `B_t=B_(t-1)-b_t`.
- Public budget `G_0=75`; `g_t=min(max(D_t-b_t,0),8,G_(t-1))` if eligible; else `g_t=0`. `early` eligible t≥1, `delayed` t≥6, `none` never. `G_t=G_(t-1)-g_t`.
- `U_t=max(0,D_t-b_t-g_t)`; `I_t=clamp(I_(t-1)-.28*U_t,0,100)`.
- Output rounded to 3 decimals, internally not rounded. Stability, capacity and public support are nonnegative and bounded.

The units, 12-period horizon, thresholds and coefficients are **invented educational choices**, not calibrated econometric findings. The model deliberately does not represent economic feedback, fiscal valuation, investor psychology, inflation, debt servicing, individual banks, shareholding structure or real rescue costs. There are no historical dollar values in the simulation.

## How to test

`python -m unittest discover -s python/tests -v`

API: POST JSON to `/api/simulate` served by `python python/app.py`. Same inputs produce the same result. The frontend refuses to treat the response as historical unless `historical:false` is present. There is no fake in-browser substitute when the service is not reachable.
