# Historical bibliography crosswalk — prevent citation collisions

**Canonical application bibliography:** `Project-Black-Thursday-deliverable/research/sources.md`, whose `Sxx` IDs are used directly in `presentation/slides-data.js`.

**Archived Phase 3 bibliography:** `black-thursday-phase3/research/sources.md`, an earlier independent research plan with different `Sxx` assignments. It should not be read as the application's citation mapping.

| Archived Phase 3 code | Meaning in archive | Current application code | Action |
|---|---|---|---|
| S01 / S01a | Yale Leonard 2021 and New Bagehot detail | S02 / S03 | Use app IDs in deck |
| S02 | 1993 State Comptroller | S01 | Use app ID in deck |
| S03 | Blass & Grossman 1996, BOI paper | S04 | Use app ID in deck |
| S04 | Ministry of Justice, Moshe Lador | S06 | Use app ID in deck |
| S05 | Bank of Israel inflation explainer | S05 | Same |
| S06 | Supreme Court record | S07 | Use app ID in deck |
| S07 | Institutional bank historical timeline | Not assigned | Cite fully in researcher notes, don't map automatically |
| S08 | Washington Post Aridor resignation | S08 | Same |
| S09 | 1983 Bank of Israel report | Not assigned | Needs precise pages if used |
| S10 | JTA reopening contemporary stories | Not assigned | Not a verified exact reopening day |
| S11 | Knesset/Bejski primary materials | Not assigned | Needs direct page review |
| S12 | Professional accounting appendices | Not assigned | Needs original agreement review |
| **New (Nov 2026)** | **1984 Comptroller primary audit** | **S10** | Preferred for first-hand 1981 warnings, 1983 return table and share inventory |

The archived IDs **must not** be mixed into on-slide citation badges. A future migration may instead adopt permanent semantic IDs (e.g. `COMPTROLLER_1984`, `COMPTROLLER_1993`, `YALE_2021`), but it must update **all** slide references and claim-register rows together.
