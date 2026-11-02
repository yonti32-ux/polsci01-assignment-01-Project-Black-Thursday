# MASTER IMPLEMENTATION PROMPT — PROJECT BLACK THURSDAY
## Professional interactive historical-documentary presentation | Version 1.0

**Intended recipient:** An AI coding assistant operating inside the actual project Git repository (Cursor Agent, Claude Code, Codex, Gemini CLI, or equivalent).  
**Instruction type:** Execute the work, create and test files, document outcomes. This is **not** a request for another plan or for mockup-only output.  
**Project:** *Black Thursday: The Political Economy of Israel's 1983 Bank-Share Crisis*  
**Hebrew title:** *יום חמישי השחור — הכלכלה הפוליטית של משבר מניות הבנקים בישראל, 1983*  
**Team:** Yonatan and Liron, University of Haifa, Political Science  
**Repository URL:** `https://github.com/yonti32-ux/polsci01-assignment-01-Project-Black-Thursday`  
**Project phase:** Phase 4/5 implementation, building on the previously developed PRD and Phase 3 historical storyboard.  
**Last editorial review:** 1 November 2026.

> **YOUR TASK:** Create an exceptionally polished, historically responsible, visually engaging, **fully navigable Hebrew RTL HTML presentation**, including a **genuine code-generated 3D animation video embedded inside the deck** and an **interactive computation genuinely executed by Python**. Work inside the existing repository and respect the documents and commits already there. Make the project convincingly professional for a live university demonstration **and** easy for a lecturer to clone, inspect, run, and grade.
>
> The product should feel like an **interactive financial-history documentary**, not a generic slideshow, corporate PowerPoint clone, static image gallery, imaginary stock-exchange video, or decorative dashboard without academic substance.

---

# 0. EXECUTION RULES — READ FIRST

1. **Inspect before editing.** At the start, confirm the Git working directory and branch, run `git status`, list files, open `PRD.md`, and look for existing `research/`, `content/`, `media/`, `prompts/`, and `docs/`. Do **not** assume the GitHub website is writable merely because this prompt contains a URL.
2. **Work on the existing project; never wipe it.** The initial PRD was already committed. Preserve its history, existing content, license and remote. Never run `git init`, `git reset --hard`, `git clean -fd`, or overwrite unrelated files. If there are uncommitted changes, protect and report them; do not discard another collaborator's work.
3. **Source-of-truth order:** (a) latest explicit team decisions and official assignment instructions; (b) existing project `PRD.md`; (c) Phase 3 historical timeline, storyboard and claim register if present; (d) the detailed editorial specification in this master prompt; (e) externally checked primary/scholarly sources. If two sources disagree, **flag the disagreement** instead of inventing a resolution.
4. **Do not stop at a proposal.** Make actual runnable files, execute tests, capture *real* evidence where tooling permits, and report what remains unverified. If a production deliverable cannot be produced in the available environment, create the best working intermediate and mark that requirement **INCOMPLETE**, never **DONE**.
5. **Work in meaningful stages:** (A) inspect + map requirements, (B) complete HTML shell, (C) real slide content + animations, (D) actual 3D movie and embedding, (E) working Python simulator, (F) QA + README + development trail. You may code autonomously; do not request needless approval between ordinary steps, but document meaningful decisions.
6. **Stay honest:** Do not fabricate economic datasets, stock prices, archival photographs, direct quotations, test results, local screenshots, Git commits, repository permissions, or final-submission confirmations. Do not claim a feature runs without testing it.
7. **Keep the team in control.** If an academic interpretation is not settled by published evidence, label it `ANALYSIS / TEAM REVIEW`. Students must approve the political-science conclusions. The coding agent may help draft and technically implement, but may not invent a historically authoritative conclusion.
8. **Do not automatically push.** Make descriptive local commits only if Git identity is configured and the team has asked the agent to commit; never push to the remote unless authorization and credentials are actually available and the team has approved that step. Never fabricate a collaborative Git history.
9. **No paid services.** Prefer source code and local tools; no account creation, paid AI rendering APIs, hidden credentials, or subscription-gated assets are needed.
10. **Final response required:** Summarize created files, precise launch commands, tests actually performed with pass/fail results, the embedded video's *real file path and format*, how Python is actually used, unresolved factual issues, and suggested next commit. Do not respond only with a list of ideas.

---

# 1. UNIVERSITY ASSIGNMENT — NON-NEGOTIABLE REQUIREMENTS

This section is based on **Lecture 1 and Lecture 2 course summaries** plus the lecturer's later written assignment notice provided by the team. The precise PDF/Moodle procedure belongs to the **final submission stage**, not to presentation rendering.

## 1.1 Graded project deliverables

- **HTML presentation:** A coherent, attractive, navigable presentation, **in Hebrew**, using correct `RTL` and `BiDi` handling, with real text and graphics—not a screenshot-only deck.
- **Embedded 3D animated video:** A video of a real three-dimensional scene, created through **Three.js or equivalent actual object-based 3D**, visibly incorporated into the HTML presentation. A link to an external video is **not sufficient**; the playable media should be part of the repository and deck.
- **Running Python contribution:** Python must **execute** and produce a visible change relevant to the presentation. A `.py` file sitting unused in the repository does not meet this requirement. Here it powers a scenario simulator through Flask.
- **Political-science relevance:** Political economy, institutional accountability, government interventions, financial regulation and public-risk allocation are central—not just a financial-history timeline.
- **Planning evidence:** A `PRD.md` exists and must remain in the root.
- **Engineering dialogue:** Keep a genuine `prompts/` history showing real user instructions, iterations, diagnoses and corrections. Keep meaningful Git commits/pushes across milestones; do not manufacture them retroactively.
- **Root `README.md`:** Explain the project, all components, how to run it, technical architecture, methodology, sources, real screenshots from slides, an actual 3D video frame and actual Python output.
- **QA / red-team:** Inspect functionality and historical accuracy. Where possible use a second LLM as a *critical reviewer*, then validate its criticisms rather than automatically accepting them. Keep a test report and documented remediation.

## 1.2 Context from lectures

- Lecture 2 demonstrates an HTML slide deck with **next / previous / home navigation**, a detailed **script for each slide**, animated objects, Hebrew RTL and BiDi, specific iterated edits, and a **Three.js 3D** animated film.
- The lecturer's course demonstration used 10 slides; **our team-approved design is 14 slides**, comfortably within the course's approximately 20-slide scope guidance.
- Lecture 1 emphasizes that **domain expertise, factual judgment and academic interpretation remain with students**, while the AI assists implementation. Both lectures emphasize project management, purposeful revisions, and testing as the determinant of quality.
- Class scope mentions approximately **4–8 hours of collaborative effort**. We favor a convincing, correct core product over a technically enormous, unstable project.

## 1.3 Requirements the presentation should remind students to complete later

The app must not collect personal IDs. Document a *release checklist*, but do not create a fake Moodle submission:

- Repository must be public, **or** the lecturer must be explicitly granted access through `rmisegal@gmail.com`. Team collaborators alone are insufficient if the repository is private.
- Use a unique **exactly eight-character group code, no spaces**. This is **not** necessarily the long repository name. **Group code remains TBD** until the team supplies it; don't invent an official identifier.
- Each student submits the university-provided Word reporting template *individually* as PDF, unchanged in layout, named `xxxxxxxx-exyy.pdf` (verify exact exercise number in Moodle).
- Provide evidence-backed self-assessment; don't manufacture a grade.
- Late penalties: 5 points per 24h per the more recent written instructions. Exceptions require official university authorization. Do not upload personal medical paperwork or student IDs to the public repo.

**Implementation distinction:** These last items belong in a `docs/release-checklist.md` or README subsection, **not** in the public slides as distracting admin content.

---

# 2. PRODUCT GOAL AND ACADEMIC POSITION

## 2.1 Central question

> **כיצד תרמו התמריצים והפעולות של בנקים, משקיעים, רגולטורים ומנהיגים פוליטיים למשבר מניות הבנקים ב־1983, ומה מלמדת ההתערבות הממשלתית על אחריות, פיקוח וחלוקת סיכונים בין המדינה לשוק?**

## 2.2 Intended learning outcomes

After the presentation, a university student should be able to:

1. Explain `ויסות מניות הבנקים` in simple language using a schematic supply/demand or purchase-flow visualization.
2. Explain why persistent bank buying could support prices for years but could not absorb unlimited selling pressure.
3. Identify the roles and incentives of **banks, investors, oversight bodies and government**; avoid attributing everything to one minister.
4. Describe the sequence surrounding **6 October 1983**, the stock-exchange shutdown, the subsequent bank-share arrangement, and later accountability processes.
5. Distinguish **gross government expenditure** on the arrangement from the state's **ultimate net loss**.
6. Use the Python scenario experiment and explain that its outputs are a hypothetical educational model, not actual 1983 market data or proved historical counterfactuals.
7. Formulate a political-science question about conflicts of interest, oversight, moral hazard, and state–market relations.

## 2.3 Tone

**Serious, intellectually confident, cinematic, restrained, clear, evidence-based.** We can be dramatic about the stakes without inventing dramatic events. Keep the story understandable to someone who has never studied banking, and substantive enough for political-science evaluation. Avoid polemics, accusatory single-villain narratives, excessive economic jargon and generic AI-flavored filler.

---

# 3. HISTORICAL ACCURACY POLICY — HARD GATES

## 3.1 Authoritative research references

Use source IDs exactly and maintain a `research/sources.md` bibliography. Use primary sources where possible and recent scholarly reconstructions for synthesis.

**S01 — State Comptroller of Israel (4 January 1993),** `ההיערכות למכירת מניות הבנקים שבהסדר`.  
https://library.mevaker.gov.il/sites/DigitalLibrary/Pages/Publications/641.aspx  
Direct evidence on long-term share manipulation, government arrangements, expenditure estimates and why fiscal expenditure is not automatically net loss.

**S02 — Natalie Leonard (2021), Yale Program on Financial Stability,** `Israeli Bank Shares Arrangement (Hesder Hamenayot Habankayot)`, *Journal of Financial Crises*, 3(3), pp. 210–227.  
https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss3/13/  
An accessible scholarly case on precrisis behavior, October timeline, government response and later redemption.

**S03 — Yale New Bagehot case,** `Israeli Bank Shares Arrangement`.  
https://newbagehot.yale.edu/docs/israeli-bank-shares-arrangement-hesder-hamenayot-habankayot  
Useful sections: *Abstract*, *At a Glance*, *Program Size*, *Governance*, *Fate of Existing Board and Management*.

**S04 — Asher A. Blass & Richard S. Grossman (1996),** `A Harmful Guarantee? The 1983 Israel Bank Shares Crisis Revisited`, Bank of Israel Discussion Paper 96.03.  
https://www.boi.org.il/media/rn3favup/dp9603e.pdf  
Academic research hosted by the Bank of Israel. **Authors' views do not necessarily represent official BOI positions.** Check sections and figure bases before reusing any quantitative chart.

**S05 — Bank of Israel Bankipedia,** `מספרים שהייתה פה היפר-אינפלציה`.  
https://www.boi.org.il/information/bankipedia/moneyandeconomy/hyperinflation/  
Macro context; **445% annual inflation was in 1984**, and stabilization policy was implemented in **1985**.

**S06 — Ministry of Justice retrospective legal writing,** `שורשים במשפט — פרשת ויסות מניות הבנקים`.  
https://www.gov.il/BlobFolder/reports/roots_1983/he/roots-1983.pdf  
For legal and institutional background; verify page and quotation if the exact text is used.

**S07 — Israeli Supreme Court record,** `ע״פ 2910/94 יפת נ' מדינת ישראל` (legal judgment; source linked through Israel Securities Authority).  
https://www.new.isa.gov.il/images/Fittings/isa/asset_library_pic/al_enforce_asset_library_/page_enforce_pdf_pages-63187a7a0aceb/2910-94.pdf  
Supports Bejski inquiry chronology, including **16 April 1986** report; don't conflate commission findings with later criminal judgments and appeals.

**S08 — Edward Walsh, The Washington Post, 14 October 1983,** `Israel's Finance Minister Quits in Row Over Plan Tying Economy to Dollar`.  
https://www.washingtonpost.com/archive/politics/1983/10/14/israels-finance-minister-quits-in-row-over-plan-tying-economy-to-dollar/95eb7e07-e2a0-4c03-a888-4f1c1fb3c40a/  
Contemporary record: **Yoram Aridor was Minister of Finance** and resigned on **13 October 1983** amid disagreement about a **separate dollarization proposal**.

**S09 — Lecture 1 summary and Lecture 2 summary**, team-provided PDF course sources; use only for assignment process, not as the original authority for historical events.

If `research/sources.md` and `claim-register.csv` exist already, **merge with them** without changing IDs silently. If our source IDs conflict with repository IDs, create a short crosswalk and use one consistent final scheme. Never silently erase researched caveats.

## 3.2 Historical facts that MAY be used when source tags accompany them

- Multiple major banks and related entities actively supported their own share prices in the 1970s–early 1980s. [S01–S04]
- The mechanism involved purchases, stock distribution and related financial channels, and created conflicts of interest. [S01–S04]
- Inflation, shekel depreciation and demand for foreign-currency assets formed important context, but inflation **alone** did not constitute the share-manipulation mechanism. [S02–S05]
- Rising selling pressure in 1983 exhausted the viability of bank-driven price support. [S02–S04]
- On **6 October 1983**, Tel Aviv Stock Exchange trading was shut down for **18 days**. [S02–S04]
- A government-backed bank-share arrangement was developed, involving future shareholder redemption obligations and substantial public-sector financial exposure. **Not all payments occurred in October 1983.** [S01–S03]
- Share ownership and direct operational control were not the same thing. Avoid suggesting the state directly managed every aspect of bank operations on the day of the arrangement. [S02–S03]
- The Bejski Commission submitted its report on **16 April 1986**; distinct subsequent legal proceedings had their own findings and appeals. [S07]
- The State Comptroller reported **approximately US$9.1 billion in government expenditure from October 1983 to late October 1991, including financing costs attributed through that date**. The **net direct loss** depends on proceeds from subsequent share sales; **never call $9.1bn final net taxpayer loss**. [S01]
- **1985** economic stabilization is a later and separate macroeconomic intervention. [S05]

## 3.3 Specific traps — prohibited claims and visuals

- DO NOT say “Finance Minister Yoram Aridor single-handedly caused the entire banking crisis,” and DO NOT call him “Minister of Economy.”
- DO NOT invent dates of personal meetings, private speeches, quotes, bank transactions, or exact daily stock-price trajectories.
- DO NOT make all banks look guilty by default. If specifying the involved banks, use historical naming and source validation; don't make the First International Bank a manipulating participant without evidence.
- DO NOT mislabel a fall in **bank shares** as all customer bank deposits becoming worthless or banks physically collapsing.
- DO NOT imply the 1983 rescue was the July 1985 stabilization plan.
- DO NOT display an unqualified `9.1 billion dollar cost` as though it were the state's final net financial loss. Distinguish spending, debt, acquired assets and eventual proceeds.
- DO NOT equate a government arrangement with immediate cash payout of the total eventual expenditure or direct operational nationalization overnight.
- DO NOT portray historical figures making speeches they never made; no fake archival news quotations or fabricated press screenshots.
- DO NOT make generic 3D buildings explode or fall apart as though Tel Aviv's physical banking infrastructure literally collapsed.
- DO NOT generate a line chart labeled “1983 bank-share prices” from mathematical toy data. **Any unsourced simulation must say `המחשה` on the axes and beside the chart.**
- **Date uncertainty:** Sources differ on how they describe the exact reopening day around **24/25 October 1983**. The safe main text is `לאחר 18 ימים` / `בסוף אוקטובר 1983`. If exact date is later shown, document its original primary exchange reference and explain any discrepancy.
- For archival photographs/newspaper images, verify rights and captions. **Don't put unauthorized archived images or course PDF illustrations directly into a public repository.** Prefer original diagrams and 3D scenes.

## 3.4 Visual/source labeling rules

Every historical slide includes a subtle, clickable source chip such as `[S01]`, `[S03]`, linking to a full-screen or side-panel source drawer. Source drawer lists title, institution, date, stable URL, cited section. Also maintain claim-level traceability in `research/claim-register.csv` where possible.

Use three explicit labels with consistent styling:

- **Historical fact:** `עובדה מתועדת`, followed by source keys.
- **Illustrative animation:** `המחשה סכמטית — לא שחזור של נתוני מסחר או תיעוד מצולם`.
- **Hypothetical simulation:** `סימולציה לימודית — לא נתונים היסטוריים, תחזית או הוכחה למה שהיה קורה`.

Where there is scholarly disagreement or a measurement definition issue, show `סוגיה לפרשנות / לבדיקה` rather than hiding it.

---

# 4. DELIVERABLES — WHAT MUST EXIST ON DISK

Use and adapt the repository's existing organization. Default target layout if these files do not yet exist:

```text
<existing-git-repo-root>/
├── PRD.md                                 # Preserve and cite the existing baseline
├── README.md                              # Actual setup + images + project explanation
├── requirements.txt                       # Pin tested Python dependency ranges
├── .gitignore
├── presentation/
│   ├── index.html                         # Main entry point
│   ├── styles.css                         # Coherent and responsive design system
│   ├── app.js                             # Slide navigation, interactions, source drawer
│   ├── slides-data.js                     # Hebrew slide data + source mappings
│   └── modules/
│       ├── navigation.js                  # Optional if modularization helps
│       ├── interactive-visuals.js
│       └── simulation-ui.js
├── animation/
│   ├── scene.html                         # Three.js actual 3D source viewer
│   ├── scene.js                           # Real geometry, lights, camera and motion
│   ├── capture.js                         # Browser recording/export utility, if supported
│   └── EXPORT.md                          # Exact reproducible capture instructions
├── media/
│   ├── video/
│   │   └── crisis-animation.webm           # **REAL PLAYABLE FILE**, MP4 preferred if possible
│   ├── screenshots/                        # REAL captures only, NOT AI mockups
│   ├── images/                             # Licensed/original only
│   └── ASSET-CREDITS.md
├── python/
│   ├── app.py                              # Flask static serving and JSON API
│   ├── simulation.py                       # Actual deterministic educational model
│   └── tests/
│       └── test_simulation.py
├── research/
│   ├── sources.md                          # Verified source bibliography
│   ├── historical-timeline.md
│   └── claim-register.csv
├── docs/
│   ├── development-log.md
│   ├── testing-report.md
│   ├── model-methodology.md
│   └── release-checklist.md
└── prompts/
    ├── ... existing real prompts preserved
    └── <this-master-prompt-file>.md          # Actual used input, added with real provenance
```

Important: **Do not create empty directory scaffolds and call the project finished.** Every included functional component must work. You may use a cleaner simpler structure if justified; README must match reality.

---

# 5. VISUAL ART DIRECTION — FANCY BUT PROFESSIONAL

## 5.1 Visual identity

**Creative concept:** A premium financial-history documentary meets a data journalism studio, inspired by the precision and suspense of an investigative film and the clarity of modern editorial infographics. No copying another brand's artwork or protected design.

**Keywords:** cinematic, academic, editorial, elegant, immersive, restrained, polished, readable from the back of a classroom, tactile, layered, premium, historical credibility.

Avoid: loud neon gamer UI, generic blue gradients, scattered unrelated icons, exaggerated red flashing errors, random emoji cards, AI-generated faces posing as historical individuals, stock trading dashboard clutter.

### Suggested design tokens

```css
:root {
  --ink: #081522;             /* deep midnight navy */
  --navy: #102739;
  --navy-raised: #18364a;
  --paper: #f5f0e6;           /* warm documentary cream */
  --muted: #bbc6cc;
  --gold: #d9ae68;            /* restrained archival brass */
  --aqua: #64bca8;            /* stability / support */
  --crisis: #d46b68;          /* warning / selling pressure */
  --border: rgba(241, 231, 209, .18);
  --radius-card: 18px;
  --radius-control: 10px;
}
```

Adjust for readability and sufficient contrast; don't make every slide a red-and-gold gradient. Each slide should have a recognizable composition while remaining part of the same design system.

## 5.2 Typography and composition

- Use a Hebrew-capable sans font such as **Heebo** / **Assistant** when legally and technically loadable; ensure robust local fallbacks like `Arial`, `sans-serif`. If self-hosting fonts, check licenses and do not commit restricted font files.
- Headline: ~42–72 px at 1920×1080; main copy: ~24–30 px. Source note: ~15–18 px where possible. Support responsive CSS `clamp()`.
- Default widescreen **16:9** stage with generous padding and deliberate negative space. Do not design for endlessly scrolling webpages.
- One central message per slide, usually **no more than 50–70 words** of visible main text (caption and citations excluded). Additional nuance goes into speaker notes/source drawer.
- Use a fixed presentation chrome: discreet progress line, slide counter `01 / 14`, project mark, source indicator and controls.
- Use varied editorial layouts: immersive cover, process diagram, split-screen, card grid, horizontal timeline, 3D stage, high-impact numerical figure, comparison matrix and interactive chart. Don't repeat the same four boxes on fourteen slides.
- Transitions: 250–650 ms, easing with coherent direction. Motion should reinforce causality; not just decoration.
- Object animation preferred over frame-by-frame generated artwork, in line with Lecture 2's object/pixel distinction.

## 5.3 Slides that deserve visual investment

- **Slide 01:** Big archival-style date `06.10.1983`, monolithic dark bank architecture, subtle animated stock-price trace (illustrative, not historical), refined typography and a large `התחילו` call to action.
- **Slide 04:** Interactive side-by-side schematic of normal demand vs bank share support, with moving purchase tokens.
- **Slide 06:** Memorable finite-capacity reserve visualization that makes the crisis mechanism instantly clear.
- **Slide 08:** Dramatic but factual 6 October timeline and stock-exchange shutdown motion.
- **Slide 09:** Actual playable documentary 3D film; designed frame and subtitles.
- **Slide 11:** Carefully qualified historical **9.1bn** number, typographic clarity, visual note explaining why expenditure ≠ final net loss.
- **Slide 13:** Serious interactive Python model with controls and an animated comparison chart.

## 5.4 Interaction quality

Every interactive object must provide an obvious affordance, accessible label, focus ring, pressed/open state when relevant, and a meaningful outcome. Do not sprinkle hover effects onto every text span just to appear interactive.

Use cohesive SVG diagrams or Canvas illustrations where appropriate. 3D is required for the film; the rest of the deck should use 3D only when it improves explanation, not just to spend GPU cycles.

---

# 6. PRESENTATION USER EXPERIENCE AND TECHNICAL FUNCTION

## 6.1 Entry and navigation

- Main route: `http://127.0.0.1:8000/` served by Python Flask; preserve a static deck entry `presentation/index.html` where possible.
- `lang="he" dir="rtl"` on root HTML. Fix BiDi with semantic `<bdi>`, `dir="ltr"`, `unicode-bidi: isolate` as needed for percentages, dollar values, file paths, English names, source IDs and dates.
- Four visible navigation functions: `הבא`, `הקודם`, `התחלה`, `תוכן עניינים`; slide counter.
- Keyboard: `ArrowLeft` = next in the visual Hebrew flow; `ArrowRight` = previous; `Home` = first; `End` = last; `Escape` closes dialogs/drawers. Show a keyboard help tooltip. Never hijack arrows while a range slider, text control or other active widget needs them.
- Touch swipe if feasible; don't let swipe advance while dragging a slider or chart.
- URL hash `#/slide/4` or comparable deep link should allow returning to a slide; browser Back should behave predictably if implemented.
- Presenter mode optional; a clear `?` keyboard help dialog is useful.
- Respect `prefers-reduced-motion`. A user should be able to pause all nonessential motion and the video.
- **Avoid accidental auto-advance**, especially during film or simulator interaction.

## 6.2 Speaker notes and source drawer

Each slide needs an off-screen/presenter-style or togglable notes section with **fact-checked speaker guidance**. Make notes accessible via a small button, not an overwhelming on-screen paragraph. Source chips open a panel containing bibliographic detail; external links use `rel="noopener noreferrer"`.

## 6.3 Full-screen and performance

- Provide a full-screen presentation button using Fullscreen API where supported, with a graceful fallback.
- Page should fit common 1366×768 and 1920×1080 screens; safe-area spacing and mobile scroll fallback. Avoid horizontal scroll at normal target resolutions.
- Eliminate horizontal shifts caused by mixed RTL/LTR dates.
- Target no errors in browser console, no dead navigation, no autoplay audio, and no external runtime API requirement.
- Prefer local packaged Three.js over a CDN where licensing and setup allow. If a dependency must remain remote during development, declare it and add a plan to vendor or build locally for the final offline run.

---

# 7. EXACT STORYBOARD AND RESEARCH CONTRACT — 14 SLIDES

**Implement these exact themes and academically cautious Hebrew messages, and improve wording only for clarity while maintaining meaning and citation status.** If the repository's current Phase 3 `content/storyboard.md` provides a newer approved script, prefer it and flag disagreements in `docs/development-log.md`. Each slide must contain **visual material and text**, with a considered transition and one documented interactive affordance when useful.

### SLIDE 01 — פתיחה | THE HOOK
**Headline:** `יום חמישי השחור`  
**Subtitle:** `הכלכלה הפוליטית של משבר מניות הבנקים בישראל, 1983`  
**On-screen question:** `כיצד הפכו מניות שנתפסו כיציבות לאיום על המערכת הפיננסית — ומי נשא באחריות?`  
**Graphic:** Original 3D-derived city silhouette / banking towers, restrained animated crack in a **symbolic** stock-trace, cinematic date `6.10.1983`.  
**Interaction:** `התחילו` and `הצגת שאלת המחקר`.  
**Evidence:** [S02–S04]. No fabricated exact share-price line.

### SLIDE 02 — הרקע | ISRAEL'S ECONOMIC ENVIRONMENT
**Headline:** `ישראל בתחילת שנות ה־80`  
**Main copy:** `אינפלציה גבוהה, פיחותי מטבע וצורך ביציבות פיננסית עיצבו את החלטות הציבור, הבנקים והממשלה. מניות הבנקים נתפסו בעיני משקיעים רבים כאפיק יציב יחסית.`  
**Supporting callout:** `שיא האינפלציה השנתי של 445% התרחש ב־1984 — לאחר משבר המניות של 1983.`  
**Graphic:** Three elegant labeled illustrated vectors: inflation, depreciating currency, bank-share confidence. If using historical numeric data, cite its exact reference and unit.  
**Interaction:** Short definitions of `אינפלציה`, `פיחות`, `ויסות`.  
**Evidence:** [S02–S05]. Avoid suggesting 445% describes October 1983.

### SLIDE 03 — THE ACTORS | INSTITUTIONAL MAP
**Headline:** `מי פעל בתוך המערכת?`  
**Main copy:** `הבנקים שתמכו בשערי מניותיהם, ציבור המשקיעים, רשויות הפיקוח והממשלה פעלו בתוך מערכת של תמריצים, סמכויות וסיכונים שונים.`  
**Graphic:** High-quality actor network of four categories: `בנקים`, `משקיעים`, `פיקוח ורגולציה`, `ממשלה`. Distinguish banking supervision from the entire government; don't falsely assign a legal authority to one actor without citation.  
**Interaction:** Clicking actor changes side card: `מטרה`, `כלים`, `שאלת אחריות`.  
**Evidence:** [S01–S04]. No all-banks-are-guilty claim.

### SLIDE 04 — CORE MECHANISM | WHAT IS ויסות?
**Headline:** `מהו ויסות מניות הבנקים?`  
**Main copy:** `בנקים וגופים הקשורים אליהם רכשו מניות כדי לתמוך בשעריהן. כך נוצרה יציבות מחיר שנבעה בחלקה מהתערבות בשוק, ולא רק מביקוש עצמאי של משקיעים.`  
**Graphic:** Two beautiful schematic market panes, clearly labeled `ללא תמיכה` vs `עם רכישות תומכות`; animated share tokens and arrows; labels `המחשה בלבד`.  
**Interaction:** Toggle between support conditions. For performance, Canvas/SVG is fine.  
**Evidence:** [S01–S04]. Never call synthetic curves recorded historical prices.

### SLIDE 05 — BANKING INCENTIVES | BEHIND THE SCENES
**Headline:** `המנגנון שמאחורי השער`  
**Main copy:** `רכישות תומכות, הפצת מניות, המלצות ללקוחות וגופים פיננסיים קשורים יצרו מערכת מורכבת — ובתוכה ניגודי עניינים.`  
**Graphic:** Isometric network around generic bank, broker, affiliated fund, investors and market; directional colored flows with clear arrow semantics.  
**Interaction:** Hover/tap arrows reveals definitions and an appropriate source.  
**Evidence:** [S02–S04]. Do not imply every specific institution used every practice.

### SLIDE 06 — FINITE RESOURCES | WHY SUPPORT FAILED
**Headline:** `ליציבות מלאכותית יש מחיר`  
**Main copy:** `כאשר יותר משקיעים ביקשו למכור, נדרשו רכישות גדולות יותר כדי להחזיק את השערים. יכולת התמיכה של הבנקים לא הייתה בלתי מוגבלת.`  
**Graphic:** Standout animated finite-support reservoir/capacity bar next to increasing selling tokens; transparent `יחידות להמחשה בלבד`.  
**Interaction:** Small explanatory scenario dial for increased selling; not the formal Python model.  
**Evidence:** [S02–S04]. Avoid unsupported historical dollar volumes.

### SLIDE 07 — WARNING SIGNS | EARLY 1983
**Headline:** `1983: האזהרות התגברו`  
**Main copy:** `בראשית 1983 נחלשו מניות שאינן בנקאיות. התמיכה במניות הבנקים נמשכה, אך משקיעים העדיפו בהדרגה נכסים במטבע חוץ ולחץ המכירות גבר.`  
**Graphic:** Anchored milestone timeline: `שנות ה־70` → `תחילת 1983` → `סתיו 1983` → `אוקטובר`. Avoid fake daily price graph.  
**Interaction:** Click dated milestones for brief sourced cards.  
**Evidence:** [S02–S04]. Quantitative additions require independent source check.

### SLIDE 08 — CRISIS | OCTOBER 6
**Headline:** `6 באוקטובר 1983: נקודת השבר`  
**Main copy:** `לאחר תקופה של היצעי מכירה כבדים במניות הבנקים, הופסק המסחר בבורסה לניירות ערך בתל אביב. ההפסקה נמשכה 18 ימים, ובמהלכה גובש הסדר להתמודדות עם המשבר.`  
**Graphic:** Documentary-style day marker, abstract TASE trading gates closing, verified date `06.10.1983` and `18 ימים`. Newspaper typography must be clearly an original design, **not** a counterfeit real newspaper page.  
**Interaction:** Short source-backed micro-timeline, `לצפייה בסרטון` navigates to 09.  
**Evidence:** [S02–S04]. Avoid precise reopening day until resolved.

### SLIDE 09 — DOCUMENTARY FILM | GENUINE 3D
**Headline:** `כיצד התפתח המשבר?`  
**Subheading:** `סרט תלת־ממד: מבט לתוך המנגנון`  
**Main copy:** `תמיכה בשערים → לחץ מכירות → מגבלת משאבים → עצירת מסחר → הסדר ממשלתי.`  
**Graphic:** **Real playable embedded 3D-animated video**. Implement `<video controls playsinline preload="metadata" ...>` with captions/subtitles where feasible. Full-width player, cinematic frame, custom optional replay button.  
**Mandatory disclaimer:** `המחשה סכמטית באנימציית תלת־ממד — אינה תיעוד מצולם או שחזור של נתוני מסחר.`  
**Evidence:** [S01–S04]. **An illustrative looping CSS GIF or video poster alone does NOT count.**

### SLIDE 10 — STATE INTERVENTION | RESCUE & OBLIGATIONS
**Headline:** `התערבות המדינה: הצלה, התחייבות ואחריות`  
**Main copy:** `הממשלה גיבשה הסדר שנועד לתת מענה למשבר ולבעלי מניות זכאים. ההסדר יצר התחייבויות פדיון עתידיות ומעורבות ציבורית משמעותית בבעלות על הבנקים, מבלי שמשמעות הדבר הייתה ניהול ממשלתי ישיר ומיידי של כל פעילותם.`  
**Graphic:** Three-stage balanced flow `משבר` → `התחייבות ציבורית` → `פדיונות ואחזקות לאורך שנים`. Don't show instant $9bn cash.  
**Optional small political context:** `שר האוצר יורם ארידור התפטר ב־13 באוקטובר 1983 על רקע המחלוקת סביב תוכנית הדולריזציה — אירוע נפרד אך סמוך למשבר.`  
**Interaction:** Switch between `למה להתערב?` / `מי נושא בסיכון?`.  
**Evidence:** [S01–S03, S08]. Political sidebar subordinate to the institutional story.

### SLIDE 11 — COSTS | ONE NUMBER, PROPER QUALIFICATION
**Headline:** `מה היה המחיר — ומי שילם?`  
**Main copy:** `לפי מבקר המדינה, ההוצאה המצטברת על הסדר מניות הבנקים מאוקטובר 1983 עד סוף אוקטובר 1991 הייתה שוות־ערך לכ־9.1 מיליארד דולר, כולל עלות מימון שיוחסה לתקופה זו.`  
**Crucial secondary copy:** `זו אינה בהכרח ההפסד הסופי נטו: יש להתחשב גם בתמורה ממכירת מניות הבנקים.`  
**Graphic:** Large editorial figure `$9.1B` **with an inseparable qualifying label** and a balanced flow diagram showing `הוצאות ומימון` versus `נכסים שנרכשו / תמורה עתידית`.  
**Interaction:** `הוצאה ≠ הפסד` explainer expands into a short accounting illustration with no fabricated resale totals.  
**Evidence:** [S01]. No interchangeable substitution of Yale's other program-size figures.

### SLIDE 12 — ACCOUNTABILITY | BEJSKI COMMISSION
**Headline:** `מי אחראי? ועדת בייסקי`  
**Main copy:** `ועדת החקירה בראשות השופט משה בייסקי הגישה את הדוח שלה ב־16 באפריל 1986. המשבר העלה שאלות קשות על ניגודי עניינים, פיקוח, החלטות מנהלים ומחויבות המדינה לציבור.`  
**Graphic:** Elegant accountability matrix: actors, powers, information, incentives, documented finding versus team question. Carefully distinguish inquiries, recommendations, prosecutions, court verdicts and appeals.  
**Interaction:** Toggle `ממצא מתועד` vs `שאלת ניתוח במדעי המדינה`.  
**Evidence:** [S01, S06, S07]. Don't invent criminal verdicts or commission quotations.

### SLIDE 13 — POLICY LAB | REAL PYTHON INTERACTION
**Headline:** `מעבדת מדיניות: ניסוי מחשבתי`  
**Main copy:** `כיצד מגיב מודל פיננסי פשוט ללחץ מכירות, אמון משקיעים, יכולת תמיכה והתערבות המדינה? שנו את ההנחות, הריצו תרחיש והשוו תוצאות.`  
**Disclaimer adjacent to chart at all times:** `סימולציה לימודית בלבד. הפרמטרים אינם מכוילים לנתוני 1983, והתוצאות אינן תחזית או שחזור היסטורי.`  
**Graphic:** Two-comparison chart, response cards, data markers, tiny model-methodology button. Chart axes `תקופות מדומות 1–12` and `מדד יציבות (ללא יחידות)` with no real calendar dates.  
**Interaction:** controls + `הרץ סימולציה` + `השווה` + `אפס`. Python must visibly compute values.  
**Evidence:** Source of **model algorithm**, not a purported factual historic series; label scenario mathematical assumptions as invented teaching assumptions.

### SLIDE 14 — CONCLUSION + SOURCES
**Headline:** `שלושה לקחים למדעי המדינה`  
**Three conclusion cards:**
1. `תמריצים וניגודי עניינים עלולים לעוות את השוק.`
2. `פיקוח, מידע ואמון הציבור הם חלק מהיציבות המוסדית.`
3. `התערבות ממשלתית עשויה לייצב מערכת במשבר — אך יוצרת שאלות של אחריות וחלוקת עלויות.`

**Closing question:** `מתי ראוי שהמדינה תציל מוסדות פיננסיים — ובאילו תנאים?`  
**Graphic:** Three pillars reflecting original actor network; source catalogue and product credits in a drawer or expandable panels.  
**Interaction:** `מקורות מלאים`, `מתודולוגיה`, `התחל מחדש`.  
**Status:** These are **team analytical conclusions informed by sources**, not direct quotations from any named inquiry.

**IMPORTANT:** Use a coherent source cross-reference on EVERY fact-dependent slide. The slide content above is a **reviewable editorial draft**, and academically sensitive interpretations require student approval.

---

# 8. THREE.JS VIDEO — FULL SPECIFICATION AND ACTUAL EXPORT

## 8.1 Primary requirement

Create an approximately **55–75 second** genuine 3D documentary animation. Source code is inspectable. Output is an actual browser-playable video file embedded in slide 09. Aim 16:9, **1280×720 minimum**, about 30 FPS. Prefer MP4/H.264 for broad compatibility, or a well-supported WebM plus an optional MP4 conversion path. Provide captions so narration is not required.

**Use real 3D:** Geometry, PerspectiveCamera, lights, depth, parallax, meaningful camera motion and animated 3D components. A flat 2D video disguised with perspective CSS does not count. Original schematic objects should not impersonate real 1983 artifacts.

## 8.2 Shot plan

| Time | Visual scene | Essential Hebrew narration/caption | Important rule |
|---|---|---|---|
| 00–09s | Low-poly 1980s-inspired financial district; investor tokens; bank towers | `במשך שנים תמכו בנקים בשערי מניותיהם.` | Generic buildings, no fabricated direct footage |
| 09–20s | Affiliated institution absorbs share tokens and maintains a symbolic value bar | `רכישות יצרו ביקוש שסייע להחזיק את השערים.` | Symbolic, not real buy orders |
| 20–31s | Loops between bank, broker, customers, fund; incentive arrows | `התמיכה הייתה חלק ממערכת מורכבת של תמריצים וניגודי עניינים.` | Don't imply every bank used every mechanism |
| 31–43s | Share selling intensifies while visibly limited capacity meter depletes | `כשהמכירות גברו, היכולת להמשיך ולתמוך נשחקה.` | Label meter `יחידות המחשה` |
| 43–53s | Calendar flips to `06.10.1983`; symbolic market trading shutters close | `המסחר בבורסה הופסק למשך 18 ימים.` | No exploding real buildings |
| 53–65s | Government intervention appears as **future-dated arrangement**, arrows to subsequent years | `המדינה התחייבה להסדר פדיון שיצר חובות ציבוריות לאורך זמן.` | Not an instant payout of billions |
| 65–72s | Fade to four actor groups and central institutional question | `מי פיקח? מי קיבל החלטות? ומי נשא בסיכון?` | Clearly interpretive question |

Maintain tasteful audio only if locally licensed and compatible; audience must understand the film **with sound off**. If music is absent, thoughtful sound-free design is preferable to unpleasant synthetic audio.

## 8.3 Camera, geometry and cinematic production notes

- Use `PerspectiveCamera`, at least a few recognizable 3D meshes (bank towers, extruded graph bars, coins/share tokens, market enclosure), directional/ambient lights and transparent overlays.
- Camera paths are smooth, predictable, and driven by `elapsedTime`/timeline, not frame-count accumulation; browser performance variations should not alter narrative duration.
- Scene colors align with presentation tokens; subtle fog/grain/vignette optional, but don't sacrifice performance or clarity.
- Hebrew titles should be implemented as DOM overlays or high-resolution textured labels, **not** blurry tiny WebGL text. Ensure correct RTL rendering.
- Place provenance/disclaimer briefly at beginning and end; retain perpetual disclaimer adjacent to video in slide 09.
- Add manual play/pause/scrub in the embedded HTML player. Disable sound autoplay. Ensure page changing stops/pause video predictably.

## 8.4 Produce a real file — choose a feasible route

Preferred workflow:

1. Implement and test actual Three.js scene `animation/scene.html` + `scene.js`, with a reproducible start/reset timeline.
2. Record it in Chrome using `HTMLCanvasElement.captureStream()` + `MediaRecorder` to a *real* local `.webm` where browser support allows; captions can be composited into the captured canvas or added to the actual video during export. Alternative: Playwright-driven frame captures + FFmpeg encoding. Use existing installed tools first.
3. If `ffmpeg` exists, transcode WebM to MP4/H.264 with a sensible bitrate/CRF; retain WebM fallback if helpful. Example (adapt to actual names): `ffmpeg -i animation.webm -c:v libx264 -pix_fmt yuv420p -crf 23 -movflags +faststart media/video/crisis-animation.mp4`.
4. Verify video end-to-end in the actual presentation page. Do not treat a non-working recording script as a video deliverable.
5. Record exact instructions in `animation/EXPORT.md`, including file duration, output file, codec, capture method, dependencies, and playback verification result.

**Fallback hierarchy:** Actual locally embedded WebM video is preferable to an absent MP4. A **live Three.js scene alone is not proof that the requested embedded 3D VIDEO was created**. If recording fails, document as incomplete and leave a conspicuous task item; do not mark acceptance passed.

---

# 9. PYTHON EDUCATIONAL SIMULATOR — FUNCTIONAL INTEGRATION

## 9.1 Requirement

Python is not cosmetic. It must **execute in a local backend** and return real computed results consumed on slide 13. The project must work without third-party APIs and without a database.

Proposed backend: **Python 3.11+ with Flask** serving static presentation assets and a small JSON API. Keep it beginner-friendly and well documented.

## 9.2 Inputs

All inputs are **illustrative model parameters**, not 1983 observations:

```json
{
  "confidence": 65,
  "sell_pressure": 50,
  "bank_capacity": 55,
  "intervention": "early"
}
```

- `confidence`: integer 0–100, label `אמון משקיעים`.
- `sell_pressure`: integer 0–100, label `לחץ מכירות`.
- `bank_capacity`: integer 0–100, label `יכולת תמיכה בנקאית`.
- `intervention`: `none`, `delayed`, `early`, labels `ללא`, `מאוחרת`, `מוקדמת`.

## 9.3 Outputs

For **12 simulated periods** return:

- Unitless **stability index** starting at 100 and bounded 0–100. Do NOT label it “historical bank share index.”
- Demand/selling pressure and unabsorbed selling pressure per period, purely hypothetical units.
- Cumulative bank support used, available remaining capacity and public intervention support used, always nonnegative.
- Model version, assumed parameters and a short explanatory Hebrew summary.
- `historical: false` to prevent UI misrepresentation.

Example conceptual JSON shape (fields may be refined but must be documented and consistently used):

```json
{
  "model_version": "1.0",
  "historical": false,
  "inputs": {"confidence": 65, "sell_pressure": 50, "bank_capacity": 55, "intervention": "early"},
  "periods": [
    {"period": 1, "stability_index": 99.1, "sell_demand": 17.2,
     "bank_support_used": 12.0, "public_support_used": 2.0, "unmet_demand": 3.2}
  ],
  "summary": {"last_stability_index": 89.4,
              "description_he": "בהנחות המודל בלבד, התערבות מוקדמת עשויה לצמצם לחץ שלא נספג."}
}
```

**These example numbers are placeholders for API shape, not required model outputs or historical facts. The code must compute actual response values.**

## 9.4 Algorithm specification

Implement a deterministic, easily explainable **toy model** with a stated finite bank support budget, a distinct finite public intervention budget and simplified demand. Do not use random noise unless a fixed seed is explicitly documented; deterministic output is preferable. One acceptable starting formula (all coefficients arbitrary teaching choices, not empirically estimated):

- Periods `t=1...12`, stability `I_0=100`.
- Base illustrative selling demand `D_t = clamp(4 + 0.18*sell_pressure + 0.12*(100-confidence) + 0.10*(100-I_(t-1)), 0, 100)`.
- Total finite bank support budget `B_0 = bank_capacity * 3.2` illustrative units. Per-period max bank absorption = 12 units; spend `b_t=min(D_t, 12, B_(t-1))`; update bank budget `B_t=B_(t-1)-b_t`.
- Total finite public intervention support budget `G_0=75` illustrative units, with per-period max 8. If `none`, zero every period; if `early`, government can act from period 1; if `delayed`, government can act starting period 6. After bank absorption, `g_t=min(max(D_t-b_t,0), 8, G_(t-1))` when eligible, else zero. Update `G_t=G_(t-1)-g_t`.
- Unmet `U_t=max(0,D_t-b_t-g_t)`; update stability `I_t=clamp(I_(t-1)-0.28*U_t,0,100)`.
- Round only on JSON serialization or chart display; **do not** round intermediate state variables.

Alternative formulas are permissible if simpler or clearly better, but must be documented in `docs/model-methodology.md` and tested for budget conservation, bounded values, deterministic output, and a sensible effect of varying selling pressure and support. Avoid hard-coding outputs or implying scholarly validation of arbitrary coefficients.

## 9.5 API contract

- `GET /api/health` → HTTP 200: `{"status":"ok","model_version":"1.0"}`.
- `POST /api/simulate` → validated JSON inputs and documented results, HTTP 200.
- Invalid input → HTTP 400 with safe explanatory JSON, not traceback/500.
- Support serving `/` and needed static media routes from one local Flask origin (avoid CORS surprises).
- Bind default host to `127.0.0.1`, not the public network. No authentication or secrets needed.
- Add unit tests including repeatability, boundary values 0/100, bad values, exhaustion of both budgets, and monotonic sanity checks (e.g., more exogenous selling should not inexplicably produce better stability under identical other assumptions).

## 9.6 Frontend simulation UX

- Sliders show labeled values at all times, have keyboard access and correct focus states.
- `הרץ` calls Python with `fetch`; visible loading indicator, result chart and explanation appear from **response JSON**, not static example arrays.
- `השווה` can store a previous case locally in the browser and overlay its series with distinct line styles, labels and legend. Alternative: a second explicit comparison request is fine.
- `אפס` resets parameters and clears comparison.
- If server is unavailable: show `שירות Python אינו פעיל. הפעילו את הפרויקט לפי הוראות README.` No fabricated fallback model output shown as actual Python execution.
- The chart's main axes should be legible in Hebrew with LTR isolation around numbers; tooltips show model parameters and unitless data.
- A `איך המודל עובד?` disclosure opens its documented simplifying assumptions. Show the educational disclaimer **at all times** next to the graph.

---

# 10. DATA, CITATIONS, COPYRIGHT, AND EDITORIAL QUALITY

1. Build `research/claim-register.csv` if absent and populate each material slide claim with unique ID, slide, Hebrew wording, source ID, section/page, verification status, and notes. **Do not label a claim verified just because an LLM said it.**
2. The slide footnotes/source drawer must be linked to a real bibliography, not generic `Wikipedia` or fake academic references.
3. Historical **prices, percentages, sums, dates and institutional names** need independently checkable sources. If an actual numeric chart cannot be supported, use an explicitly symbolic SVG or teaching model instead.
4. Provide a small glossary: `ויסות`, `מניה`, `פדיון`, `פיחות`, `הוצאה מצטברת`, `הפסד נטו`, `ניגוד עניינים`.
5. Do not reproduce long passages or archived newspaper images without checking permission. Use original graphics by default. Maintain `media/ASSET-CREDITS.md` with asset name, origin, license, author and whether permission was checked.
6. All slide illustrations should be **semantically honest**: red tokens signify selling pressure, gold = bank/state institutional flow, aqua = stability; add legends when a color encodes meaning.
7. Handle every historical-accuracy correction as a PRD/storyboard note and in the development log. If a source cannot confirm a claim, mark `needs verification` and soften/delete it.
8. The academic conclusions (especially slide 14) should be flagged as students' own analytical framework. Include a project credit `נכתב ונערך על ידי צוות הפרויקט בסיוע כלי AI; האחריות לאימות המקורות ולמסקנות היא של הסטודנטים.`

---

# 11. CODE QUALITY, ACCESSIBILITY AND RESILIENCE

## 11.1 Engineering guidelines

- Prefer small modules over a single 2,000-line HTML document, while ensuring the deck remains runnable. Keep CSS organized by design tokens, slide layouts, components, interactions and responsive rules.
- Avoid loading giant JS libraries for tiny charts. Use native SVG/Canvas for illustrations and charts. **Three.js** is justified for the 3D film.
- No build pipeline required for the core demo if plain browser modules suffice. If bundling is needed to serve local Three.js, explain exactly how to install/build/start.
- Create `requirements.txt` and install/run docs. Do not pin nonexistent dependency versions.
- Provide meaningful error messages, `aria-label`s, visible focus states, semantic headings, `<button type="button">`, and proper labels for range inputs.
- Avoid `innerHTML` injection with untrusted data; use text nodes/escaped templates as appropriate; Python endpoint validates JSON and enforces input ranges.
- No telemetry, remote keys or collection of student details; never commit `.env` or secrets.
- Reduce motion for users who request it, but leave the cinematic video available as an opt-in playback.
- Preserve contrast and readable typography on a classroom projector; chart information must not rely on color alone.

## 11.2 Failure modes and fallbacks

- If Three.js/WebGL fails in a live decorative section, present meaningful HTML/SVG fallback—not a blank slide.
- If the actual video file is missing, show a conspicuous error and mark the film requirement incomplete; **never make the player appear functional when only a poster exists**.
- If Python server fails, deck narrative and embedded video can still be read through a static server where configured, while the model explicitly reports offline.
- Unavailable source website should not crash a slide; bibliography can retain URLs and on-screen title.
- Avoid any requirement for an online map, realtime banking dataset, Google account or remote API during presentation.

---

# 12. IMPLEMENTATION WORKFLOW — ACTUAL AGENT ACTIONS

**Proceed in order. After every stage, inspect the output and update the development log.** If this environment supports browser automation, capture and inspect screenshots; otherwise provide precise manual verification instructions and never claim those visual tests passed.

## M0 — Inspect repository and reconcile planning artifacts

- Confirm repository remote via `git remote -v`, branch via `git branch --show-current`, status via `git status`.
- Read current `PRD.md`, existing README, research and storyboard. Note absent files. Establish team-approved phase and whether this prompt's 14-slide specification conflicts with any approved file.
- Log concise decisions in `docs/development-log.md`. Preserve existing PRD; propose version 1.1 changes rather than silently rewriting original agreements.
- Save a **real copy** of the exact prompt used at `prompts/` (if not already present); include a date, AI tool and stage, not fake prior exchanges.

## M1 — Functional HTML skeleton (first pass)

- Create a working RTL 14-slide shell with all slide headings, exact order, navigation buttons, progress indicator and source drawer.
- Verify all 14 slides are reachable and no previous/next logic jumps unexpectedly.
- Test Hebrew + English mixed dates/source IDs and at least 1366×768.
- Once working, make a meaningful commit (if authorized) and update README with accurate progress.

## M2 — Academic content and premium design (second pass)

- Implement each slide's content/graphic; connect source IDs, notes, glossary and interactive diagrams.
- Give each slide an intentional unique layout while preserving common visual language.
- Inspect hero, flow diagram, timeline, number slide and mobile fallback for clipping.
- Verify historical claims against sources; update source register. No fake numbers.

## M3 — Three.js actual 3D film (third pass)

- Implement actual scene/camera/geometry and test in browser.
- Record an actual local video file using a feasible method. Put the playable output in `media/video/`; embed in slide 09.
- Test pause/play/replay and caption visibility; include export instructions; record video file type and actual duration in documentation.
- Do **not** mark complete without an actual playable file.

## M4 — Python backend + interactive slide (fourth pass)

- Implement Flask app and the transparent deterministic model; add tests.
- Ensure browser controls trigger `POST /api/simulate`, update chart from JSON, and show errors honestly.
- Demonstrate with two distinct input sets; verify repeatable results and no invented historical timeseries.

## M5 — QA, documentation and source checks (fifth pass)

- Run relevant tests, browser console review and model sanity checks.
- Take **REAL screenshots** of opening slide, explanatory visual, player with actual movie frame, and actual Python-generated chart. Save under `media/screenshots/`.
- Build/polish root README with actual local commands, embedded *real* relative screenshot references, sources, method, screenshots, project directory structure and contributor acknowledgment.
- Add or update `docs/testing-report.md` with tests performed, status and known issues. Add `docs/release-checklist.md` with individual PDF/Moodle and GitHub access checks (not claims that those actions happened).
- Run an independent skeptical review, or create a copy-ready red-team review prompt and transparently note that review is pending if no second model is available.
- Mark incomplete items honestly; prioritize fixing all **must-have** defects over more decorative effects.

---

# 13. ROOT README — PROFESSIONAL GITHUB PRESENTATION

The GitHub page should function as a strong visual project showcase **and** a runnable technical guide. Build the README around the *actual implementation* and include:

1. **Header / hero:** Project English + Hebrew title, semester, course, team Yonatan & Liron, one-paragraph academic purpose.
2. **Main screenshots:** Real title slide; real 3D video **frame from the exported video**; real Python simulation result; optionally actor network screenshot. Use **relative markdown paths** so GitHub renders them.
3. **What users can do:** 14-slide historical presentation; code-generated documentary movie; Python hypothetical experiment; source drawer and interactive diagrams.
4. **Research question & main conclusion** clearly identified as team's analysis.
5. **Screenshots / visual architecture** and technology list (HTML, CSS, JS, Three.js, Python, Flask).
6. **Requirements and launch commands**, written for an undergraduate who has Python but may not know command-line tools. Include Windows PowerShell instructions and alternatives where necessary; use tested commands only.
7. **How to navigate and interact**, including keyboard arrows and simulator controls.
8. **Technical dataflow diagram:** browser UI → Python API → deterministic model → returned JSON → chart. 3D source → exported video → embedded HTML player.
9. **Historical sources and methodology**, including model-is-not-history disclaimer, source register and license notes.
10. **AI development evidence:** honest history of prompts, PRD, commits, iterations, test report and student editorial control.
11. **Team collaboration and attribution** without student ID numbers, emails or other sensitive details.
12. **Status, current limitations, final assignment-specific steps** (group code eight characters, lecturer access, separate PDF submissions) without claiming these have already been completed.

Use tasteful README formatting and badges sparingly. **Do not fabricate GitHub CI badges, test coverage percentages, or demo GIFs.**

---

# 14. TESTS / ACCEPTANCE CHECKLIST — MUST PASS BEFORE SAYING DONE

Implement these as actual checked outcomes in `docs/testing-report.md`, with columns `ID | test | method | observed result | status | evidence | correction`.

| ID | Minimum acceptance test |
|---|---|
| A-01 | Start local Flask app with documented command and open deck at `/` |
| A-02 | All 14 slides load in exact approved order |
| A-03 | Next, previous, home, slide count, overview and keyboard controls work |
| A-04 | Mixed Hebrew/English/numerals/URLs display without BiDi reversal or cropping |
| A-05 | Distinct, meaningful visual content on every slide; no empty placeholder marketed as finished |
| A-06 | Original real Three.js scene contains actual 3D geometry, moving camera and lighting |
| A-07 | **Recorded** locally stored 3D video exists and plays from slide 09; controls and subtitles/captions are readable |
| A-08 | Working Python server is actually called when simulation is run; returned JSON visibly updates a chart |
| A-09 | Two input settings produce meaningfully different results; repeated same inputs produce identical results |
| A-10 | Inputs 0/100 and invalid strings/out-of-range values do not crash backend |
| A-11 | Support capacities are finite and not silently replenished; indices and budgets remain bounded/nonnegative |
| A-12 | Simulation always has explicit educational disclaimer and hypothetical period labels |
| A-13 | 1983 closure date, 18-day span, 1984 inflation figure and 1985 policy distinction are correct and source-tagged |
| A-14 | Expenditure ~$9.1bn is always explicitly qualified and never presented as the final net loss |
| A-15 | No incorrect 'Aridor alone caused crisis' narrative; correct `שר האוצר` if referenced |
| A-16 | 1986 Bejski report date and inquiry-vs-court distinctions are accurate |
| A-17 | Bibliography links map to real credible sources; each major statistic is traceable |
| A-18 | Keyboard-only navigation and reduced-motion behavior; visible labels and color-independent legends |
| A-19 | No serious layout overlap at 1366×768 / 1920×1080 in target browsers |
| A-20 | Browser console has no uncaught errors during an entire demo; no remote API is essential |
| A-21 | Root README contains actual setup commands, actual screenshots and architectural explanation |
| A-22 | Existing PRD preserved; all actual prompts logged, testing documented, commits meaningful |
| A-23 | No copyrighted archival photos or course PDFs republished without rights verification; credits file exists |
| A-24 | Repository visibility and each student's Moodle PDF are marked pending until people verify/submit them |

### Suggested automated tests

- `python -m unittest discover -s python/tests -v` (or appropriate project-specific test runner).
- Flask test-client health endpoint and happy/invalid POST tests.
- Browser manual or Playwright tests for slide traversal, source drawer, video availability, Python fetch and BiDi layout.
- Smoke-test media MIME and actual video playback, not just file existence.

**Stop condition:** Do not declare release-ready while A-01, A-02, A-06, A-07, A-08, A-12, A-13, A-14, A-17, or A-21 fail. Noncritical visual enhancements may remain optional, but the assignment's core deliverables are mandatory.

---

# 15. RED-TEAM CRITIQUE — HOW TO DO REAL QUALITY CONTROL

After a working candidate is available, give its repository files, real screenshots and test evidence to a **different AI model** if possible, with this instruction:

> Act as a deliberately skeptical review committee consisting of a political-economic historian, financial-market researcher, Hebrew RTL/accessibility specialist, Three.js/film engineer, Python QA engineer and academic-integrity reviewer. Find factual errors, misleading depictions, unsupported numerical claims, false compliance with the HTML/3D/Python assignment, copyright issues, inaccessible controls and code that doesn't run. Classify each finding as CRITICAL/HIGH/MEDIUM/LOW. Cite the file, line or slide and supporting evidence. Do not flatter us. Propose actionable corrections, and distinguish confirmed defects from hypotheses needing verification.

Back in the implementation process: **verify critiques before acting** and record issues, fixes and decisions. Don't blindly implement stylistic suggestions that damage historical clarity or introduce risk.

---

# 16. COLLABORATIVE GIT SAFETY AND DEVELOPMENT TRAIL

- Project already exists and the initial `PRD.md` has been committed by the students. Keep it and all earlier commits intact.
- Respect both collaborators' work. Recommend short-lived feature branches or a simple agreed branch policy if both edit concurrently. Before merging/pushing, fetch and reconcile rather than force-push.
- Commit in useful increments after actual tested milestones (not thousands of meaningless commits). Examples:

```text
docs: record presentation implementation specification
feat: create RTL slide navigation shell
feat: add verified 1983 crisis narrative and visuals
feat: build Three.js financial-crisis animation
feat: export and embed playable 3D documentary video
feat: connect interactive policy lab to Python model
test: cover simulator edge cases and slide navigation
docs: add actual screenshots, sources and testing results
```

- Update `README.md` and `docs/development-log.md` after meaningful changes. `prompts/` entries should be the **actual conversations/instructions used**, with the observed result and targeted improvement in chronological order. Never invent earlier iterations.
- Treat long repository name `polsci01-assignment-01-Project-Black-Thursday` as a GitHub URL, **not** the required eight-character class group identifier; keep group identifier TBD until supplied.
- Treat this prompt as a development artifact and cite its file path in `docs/development-log.md` once actually used.

---

# 17. EXPECTED FINAL HANDOFF FROM YOU, THE CODING AGENT

When implementation finishes or you reach a genuine blocker, reply concisely but concretely in the following form:

**A. Built:** Exact components implemented and paths of major files.  
**B. Run:** Exact install/start commands tested on the current environment and expected browser address.  
**C. Proof:** Local video path, video duration/codec if verified; Python endpoint results; screenshots actually captured.  
**D. QA:** Table of tests attempted, passed, failed, not executed, with why.  
**E. Historical review:** Source claims checked, key cautions retained, conflicts/pending verification.  
**F. Repository:** Git status, commits actually created, whether pushed (do not imply a push that did not happen).  
**G. Next actions:** Short ordered list of only the remaining essential manual tasks.

Avoid vague conclusions like “Everything looks perfect” when the video has not been rendered, the source file isn't present, or the Python endpoint hasn't been called. If the film is still unfinished, label it clearly rather than quietly substituting a rotating 3D image.

---

# 18. FINAL PRIORITY RULE

**Correct history > working core functionality > educational clarity > accessibility > visual polish > optional effects.**

We want a presentation that is **beautiful because its ideas are understandable**, impressive because its technology actually works, and credible because every important historical assertion can be checked.

Do not limit yourself to plain boilerplate visuals. Use ambitious, polished typography, detailed 3D staging and smart interactions *within the practical scope of the assignment*. If pressed for time, reduce optional effects, **never** fake essential deliverables or historical evidence.

**Now inspect the repository, reconcile the PRD and source files, create the application, test it, and document the actual result.**
