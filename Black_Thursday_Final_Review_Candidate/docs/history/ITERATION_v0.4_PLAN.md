# Project Black Thursday — Candidate Iteration v0.4

**Prepared:** 2 Nov 2026 · **Team:** Yonatan + Liron · **Group:** `polsci01`  
**Status:** Tested candidate assets and local integration checks; **not merged or pushed to GitHub**.

## Goals and technical decisions

1. **Prioritize Liron's video feedback.** Preserve recognizable 3D visual concept but replace unclear captions with seven sequential, source-supported chapters. Clearly distinguish bank-share returns from other listed shares and the trading halt from the physical or corporate collapse of the exchange.
2. **Reduce presentation startup friction.** Provide `START_BLACK_THURSDAY.bat` (Windows double-click) and `launch_presentation.py`, with no required pip install because the existing `python/app.py` already has a standard-library server fallback. This preserves **real Python execution** and the mandatory interactive simulator.
3. **Allow static viewing.** Relative asset links now allow direct file opening of `Project-Black-Thursday-deliverable/presentation/index.html` from an extracted folder. All slides and the embedded film are intended to work in static viewing mode; **slide 13's Python-backed calculation correctly requires the one-click launcher**. Some browser security policies may limit local file behavior and must be tested on the presenter laptop.
4. **Consolidate without destructive changes.** Keep original 3D video `crisis-animation.mp4` and original CPU/WebGL code. New edited film is `crisis-animation-v2.mp4`; slide 9 points at the v2. Don't rewrite code Liron may have changed since the team's ZIP snapshot. Preserve original `PRD 0.1.md` while adding canonical `PRD.md` with a documented implementation addendum.
5. **Historical evidence.** We use the *actual* 1984 Comptroller's report, Table 1.3, for the January–September 1983 real-return comparison: **all commercial-bank shares +8.6%** versus **nonbank shares −57.5%**. The categories are different from a named official bank-stock index and the TASE's daily index. The TASE did **not** become bankrupt; trading was suspended following a market and banking crisis. Reopening day/duration claims should be confirmed before final release due to counting disagreements among sources.

## v2 video — seven scenes, 72 seconds

| Seconds | Chapter | Specific audience lesson | Evidence |
|---|---|---|---|
| 00–09 | The market | Bank shares traded on TASE, were considered relatively stable | 1984 Comptroller pp. 7–9 |
| 09–20 | The practice | Banks and affiliates purchased shares to support prices | 1984 Comptroller pp. 7–8, 22–24 |
| 20–31 | Actual data | Jan–Sep 1983 real returns **+8.6% vs −57.5%**, not daily indices | 1984 Comptroller p. 19, Table 1.3 |
| 31–43 | Pressure | Growing public selling and declining ability to absorb offers; support inventory about US$1.06bn on 6 Oct | 1984 Comptroller pp. 7, 10 |
| 43–53 | 6 Oct halt | Exchange **suspended trading**; no physical collapse or bankruptcy of exchange is claimed | 1984 Comptroller pp. 7, 10 |
| 53–65 | Rescue | Future redemption obligations for eligible shares, not instant cash for all holders | 1984 Comptroller pp. 7, 11 |
| 65–72 | Accountability | Prior 1981 warnings and public-oversight question | 1984 Comptroller pp. 11–13 |

**Palette set by Liron:** `#1c242c`, `#c19d43`, `#d3cebe`, `#1f3c58`, `#8ab9ee`, `#7a8694`, `#e7eef4`, `#f5cb39`, `#ed1c16`.

**Technique/provenance:** This is an **edited version of the original genuine 3D rendered video**, not a completely new Three.js render. The underlying camera animation and 3D geometry are the prototype's original software-rendered footage. New film cards, a clearer chronological structure and the verified data comparison were composited over it using Pillow and FFmpeg. To re-edit, run `python animation/render_movie_v2.py` from the application folder after installing the export-only Pillow library and FFmpeg. Neither library is needed to play the video or run the presentation. Original film retained for rollback. Generated `animation/generated-v2-overlays/` is a temporary rebuild directory and need not be committed.

**Important future upgrade:** Liron may still prefer a fully **new** 3D film with more sophisticated index movement and new scene geometry. Consider replacing the v2's inherited v1 source scenes in a separate Phase 6C, only after agreeing that the evidence-based infographic and narration meet historical standards. Do not assert we've produced a wholly new Three.js video.

## Integration checklist (candidate patch only)

- [x] New 72-second v2 MP4 exported from the original 3D film with source-backed graphics.
- [x] FFprobe confirms output duration 72 seconds and a valid MP4.
- [x] Real v2 poster and historical comparison screenshot generated from MP4.
- [x] Slide 9's MP4 + poster references changed; seven-stage subtitle corrected.
- [x] Local-file-compatible relative paths changed in HTML, film and scripts.
- [x] Offline static mode gives an explicit explanation on slide 13 instead of a misleading result.
- [x] Windows double-click and cross-platform Python launch scripts created.
- [x] Canonical source `S10` added for the 1984 Comptroller report, without renumbering pre-existing app `S01`–`S09` IDs.
- [ ] Live Windows double-click smoke test on Yonatan's laptop and verify slide 13 returns Python data.
- [ ] Live browser test of file:// mode for slides, video playback, navigation and readable RTL.
- [ ] Academic signoff from Yonatan and Liron on final captions, claim labels, exact sources.
- [ ] Check final GitHub branch differs from uploaded ZIP snapshot before applying any patch.
- [ ] Merge only reviewed changes; update live GitHub README and screenshots; do not pretend the push has been done.

## Recommended next work

**P0:** Create a Git branch for doc/source consolidation; run all local Python tests; verify 14-slide tour and all links; resolve exact trading-suspension duration with primary TASE record.  
**P1:** Discuss v2 movie with Liron; if she wants new geometry, implement storyboard-driven three-dimensional graph/index panels next; improve Hebrew captions and add audio only if helpful and accessible.  
**P1:** Make actual sourced 1981 warning and Jan–Sep 1983 comparison more visible on slides 7 and 12, with citations embedded in the app's canonical `S10` registry.  
**P2:** Reconcile Phase-3 source IDs and the delivered slide source IDs using an explicit crosswalk. Polish styles, accessibility, performance and final documentation.  
**P0 before submission:** Full red-team QA, repository access for `rmisegal@gmail.com`, individual Moodle PDF submissions (`polsci01-ex01.pdf` if exercise suffix confirmed) and justified self-grade.

## Suggested commits (after you verify locally)

```
feat: improve slide 9 documentary captions and sourced market comparison
feat: support local preview and one-click Python launch
research: add primary 1984 Comptroller report reference
 docs: synchronize PRD README and video iteration notes
```

Never make up commits; commit only the actual accepted changes in the appropriate branch.
