# Storyboard v1.0 — יום חמישי השחור: הכלכלה הפוליטית של משבר מניות הבנקים (1983)

**Deliverable:** 14-slide Hebrew RTL HTML documentary, Three.js 3D video embedded on slide 9, Python-based *hypothetical* interactive model on slide 13.  
**Design:** documentary + analytical dashboard; dignified archival tone (navy/cream/amber, crisis red used sparingly), simple kinetic typography, real chronology rather than sensational allegations.  
**Sources:** `[Sxx]` source IDs point to `../research/sources.md`; `[Cxx]` to `../research/claim-register.csv`.  
**Editorial convention:** **[FACT]** supported historical claim; **[ANALYSIS]** team's interpretation; **[ILLUSTRATION]** symbolic scene; **[SIMULATION]** hypothetical teaching model. Speaker notes are research-informed drafting suggestions; students approve and revise all substantive political-science conclusions.

## Slide 01 — הפתיחה: מה באמת קרס?
- **Purpose:** Engage audience and frame the research problem, not blame a named person.
- **On-screen Hebrew (draft):**
  > **יום חמישי השחור — אוקטובר 1983**  
  > כיצד מניות של בנקים שנראו בטוחות הפכו לאיום על יציבות המערכת הפיננסית בישראל?  
  > **שאלת המחקר:** מי קיבל החלטות, מי פיקח, ומי נשא בסיכון?
- **Speaker note:** The story begins with a seemingly stable investment, moves into bank incentives, regulatory choices and investor expectations, and ends with a state-funded arrangement. Explain that the narrative concerns **bank shares**, not the automatic disappearance of bank deposits. [S01; S04]
- **Visual:** Three original low-poly bank towers at night; slowly forming fault lines in a glowing price line; camera moves toward a calendar marked `6.10.1983`.
- **Interaction:** `התחל`; small `מידע על מקורות` badge.
- **Claims:** C01, C02. **Classification:** FACT + analytical question.

## Slide 02 — ישראל והמשק בתחילת שנות ה־80
- **Purpose:** Set macroeconomic context without false cause attribution.
- **On-screen Hebrew (draft):**
  > **אינפלציה מהירה, שקל נשחק, וציבור שמחפש יציבות.**  
  > על רקע עליית מחירים ופיחותי מטבע, מניות הבנקים נתפסו בעיני רבים כאפיק השקעה יציב יחסית.  
  > **שימו לב:** שיא אינפלציה שנתי של **445%** שייך לשנת **1984**, לא לשנת 1983. [S01; S05]
- **Speaker note:** Inflation, capital needs and exchange-rate expectations helped shape incentives. We should not suggest that a 1984 annual figure describes the first week of October 1983. Avoid unsupported annual 1983 inflation numbers. [S01; S05]
- **Visual:** Archival-inspired currency and prices timeline. **No invented actual data series**. The 445% 1984 point may be shown *only* as later contextual continuation clearly dated 1984, or omitted for tighter focus.
- **Interaction:** Hover `אינפלציה`, `פיחות`, `מניה` for short definitions.
- **Claims:** C03, C04. **Classification:** FACT.

## Slide 03 — השחקנים: מי היה אחראי על מה?
- **Purpose:** Political-science institutional map.
- **On-screen Hebrew (draft):**
  > **הציבור** החזיק ומכר מניות.  
  > **הבנקים המעורבים** פעלו לתמיכת שערי מניותיהם.  
  > **בנק ישראל ורשויות הפיקוח** נשאו בסמכויות פיקוח שונות.  
  > **הממשלה** קיבלה החלטות במשבר ונטלה התחייבויות ציבוריות. [S01a; S02; S04]
- **Speaker note:** Do not homogenize all banks. Main participating groups included Leumi, Hapoalim, Discount and Mizrahi, with related issuers. Yale identifies First International Bank as a large bank that did **not** take part. Distinguish the central bank, banking supervisor, securities regulator and Ministry of Finance. [S01a]
- **Visual:** 3D/2D hybrid network of four actor groups with directed, **labeled** arrows. Avoid a single 'evil politician' red silhouette.
- **Interaction:** Click an actor to reveal `תמריץ`, `סמכות`, `שאלת אחריות` (the latter framed as a question where contested).
- **Claims:** C05, C06. **Classification:** FACT + explanatory model.

## Slide 04 — מה פירוש "ויסות מניות הבנקים"?
- **Purpose:** Explain exact mechanism before describing crisis.
- **On-screen Hebrew (draft):**
  > **ויסות** הוא הכינוי שניתן לפעולות ממושכות שבאמצעותן תמכו בנקים בשערי מניותיהם.  
  > כאשר גבר הרצון למכור, גופים הקשורים לבנקים רכשו מניות והגדילו את הביקוש.  
  > כך נוצרה מראית עין של יציבות שלא שיקפה בהכרח את כוחות השוק. [S01a; S02]
- **Speaker note:** Yale describes affiliated funds, credit channels, subsidiaries, brokerage recommendations and stock purchases. The animation simplifies this complex network; no real purchase records are implied. [S01a]
- **Visual:** Two simplified charts side-by-side: schematic free-market supply/demand versus purchases that artificially support the price; axes titled `המחשה בלבד — לא נתוני מסחר`.
- **Interaction:** Toggle `ללא תמיכת בנק` / `עם תמיכה` to illustrate the mechanism using **synthetic** graph points.
- **Claims:** C07. **Classification:** FACT + ILLUSTRATION.

## Slide 05 — המנגנון מאחורי הקלעים
- **Purpose:** Show institutional conflicts of interest, not a money-printing caricature.
- **On-screen Hebrew (draft):**
  > מערכת הבנקאות לא רק מכרה מניות; היא גם השפיעה על המסחר בהן.  
  > הפצת מניות, המלצות ללקוחות, קרנות וגופים קשורים ורכישות תומכות יצרו **ניגוד עניינים**. [S01a; S02]
- **Speaker note:** Emphasize that actors could profit from rising share values and maintain access to equity, while customer expectations were shaped by banks' activities. Use the phrase 'potential and documented conflicts of interest' but don't claim every individual employee knowingly misled investors. [S01a; S02]
- **Visual:** 3D transaction loops among bank, investor, affiliated fund, market; arrows have distinct semantic colors; tooltip `סכמטי — אינו משחזר עסקאות מסוימות`.
- **Interaction:** Hover arrows to reveal `תמיכה בשער`, `מכירת מניות`, `ניגוד עניינים`.
- **Claims:** C08. **Classification:** FACT + explanatory interpretation.

## Slide 06 — המחיר של יציבות מלאכותית
- **Purpose:** Make the basic resource-constraint argument tangible.
- **On-screen Hebrew (draft):**
  > מחיר נתמך דורש קונים שיספגו את ההיצע.  
  > כאשר הציבור מוכר יותר ויותר, הבנק נדרש להשקיע משאבים גדלים ברכישת מניותיו.  
  > **משאבי התמיכה אינם בלתי מוגבלים.** [S01a; S03]
- **Speaker note:** At the crisis peak the banks could no longer absorb the public's sales. Distinguish limited capacity for purchasing shares from a claim that every participating bank had negative total assets. [S01a; S03]
- **Visual:** 3D reserve tank gradually declines while incoming 'share' objects grow. The units MUST say `יחידות להמחשה`.
- **Interaction:** User scrubs a simplified illustrative stress dial; reset button.
- **Claims:** C09. **Classification:** FACT + ILLUSTRATION.

## Slide 07 — 1983: האזהרות התגברו
- **Purpose:** Show the build-up, not surprise 'overnight collapse'.
- **On-screen Hebrew (draft):**
  > בתחילת 1983 נרשמו ירידות חדות במניות שאינן בנקאיות.  
  > מניות הבנקים המשיכו ליהנות מתמיכה, אך משקיעים הלכו והעדיפו נכסים במטבע חוץ.  
  > הביקוש שהבנקים נדרשו לייצר כדי לבלום את המכירות הלך וגדל. [S01a]
- **Speaker note:** Separate the earlier market weakness from the October bank-share crisis. If adding precise monthly numbers, source and verify separately; none required for core lesson.
- **Visual:** Timeline 1970s → Jan 1983 → Sep 1983 → early Oct, built from objects, not an invented continuous daily price series.
- **Interaction:** Click timeline milestones for one-line source-backed explanations.
- **Claims:** C10, C11. **Classification:** FACT.

## Slide 08 — 6 באוקטובר 1983: נקודת השבר
- **Purpose:** Explain what happened that day and why the exchange suspended trading.
- **On-screen Hebrew (draft):**
  > **6 באוקטובר 1983**  
  > לאחר שבועות של היצעי מכירה משמעותיים במניות הבנקים, הופסק המסחר בבורסה בתל־אביב.  
  > הפסקת המסחר נמשכה **18 ימים** — ובמהלכה גובש פתרון ממשלתי למשבר. [S01; S03]
- **Speaker note:** Make clear suspension was a crisis-management step, not proof all banks were liquidated. Some sources diverge on the exact resumption day (24 or 25 October); we can safely say trading resumed after the suspension without pinning the ending moment here. [S01a; S07; S10]
- **Visual:** Real historical newspaper *style* recreated with original typesetting (not false facsimile labeled as real); clock stops; show date stamp `6.10.1983`.
- **Interaction:** `צפו בסרטון ההמחשה` link to slide 09.
- **Claims:** C12. **Classification:** FACT.

## Slide 09 — איך משבר מניות הפך למשבר מערכתי?
- **Purpose:** Mandatory embedded *genuine Three.js-derived 3D video*, target 60 seconds.
- **On-screen Hebrew (draft):**
  > **סרט תלת־ממד: שרשרת האירועים**  
  > תמריצי הבנקים ← תמיכה בשערים ← לחץ מכירות ← מגבלת משאבים ← התערבות המדינה.  
  > **המחשה חזותית — לא תיעוד היסטורי ולא גרף של נתוני מסחר.**
- **Speaker note:** Video is an explanatory model, not authentic 1983 footage. Factually anchor scene cards to S01a / S02 / S04; narration never claims reconstructed volumes, prices or individual conversations.
- **Visual:** Embedded `<video>` containing the 3D scene. Show thumbnail and captions; fallback explanatory still if video not playable, but delivery is **not accepted** unless actual playable video works in primary browser.
- **Interaction:** Play, pause, replay, progress, volume, Hebrew captions; optionally open original Three.js scene separately.
- **Claims:** C07, C09, C12, C13. **Classification:** FACT sequence shown through ILLUSTRATION.

## Slide 10 — האם המדינה הצילה את הבנקים — או את בעלי המניות?
- **Purpose:** Explain 1983 *arrangement* and its political trade-offs.
- **On-screen Hebrew (draft):**
  > הממשלה קידמה **הסדר מניות בנקים** שנועד לבלום סיכון למשק ולתת מענה למחזיקי מניות זכאים.  
  > המדינה התחייבה לפדיונות עתידיים, ובהמשך רכשה אחזקות נרחבות בבנקים.  
  > **בעלות ממשלתית אינה זהה לניהול ממשלתי ישיר.** [S01a; S02]
- **Speaker note:** Do not show simultaneous redemption of every share or government instantly directing bank operations. Optional political sidebar: Yoram Aridor, the **finance minister**, resigned **13 Oct** amid dollarization controversy — a separate but concurrent macroeconomic policy episode. [S08]
- **Visual:** Timeline `6 Oct closure → Oct arrangement → future redemption windows → ownership/share management`; state-guarantee arrow shown as **future obligation**, not as a stack of instant cash.
- **Interaction:** Toggle `הגנה על יציבות` and `התחייבות ציבורית` to see trade-off labels.
- **Claims:** C13, C14, C15. **Classification:** FACT + ANALYSIS.

## Slide 11 — מה היה המחיר? ומי באמת שילם?
- **Purpose:** Explain financial accounting carefully.
- **On-screen Hebrew (draft):**
  > מבקר המדינה דיווח על **כ־9.1 מיליארד דולר הוצאה מצטברת** לצורך ההסדר עד סוף אוקטובר 1991, **כולל עלות מימון** עד אז.  
  > **זו אינה בהכרח ההפסד הסופי נטו למדינה:** יש להביא בחשבון את התמורה ממכירת מניות הבנקים. [S02]
- **Speaker note:** Do not silently substitute Yale's $6.9bn 'program value/peak utilization' or $9.2bn cumulative figure. Different estimates use different definitions. If a large number appears, place a compact footnote 'הוצאה מצטברת לרבות מימון, לא הפסד נטו'. Add longer detail in notes. [S01a; S02]
- **Visual:** *One large number with footnote* + balanced diagram `הוצאה לרכישות ומימון` ↔ `מניות שהמדינה קיבלה ותמורה אפשרית בעת מכירתן` (no unsupported quantified proceeds).
- **Interaction:** `מה ההבדל בין הוצאה להפסד?` opens an explanatory card.
- **Claims:** C16, C17. **Classification:** FACT + accounting explanation.

## Slide 12 — מי נושא באחריות? ועדת בייסקי
- **Purpose:** Political-science analysis meets a formal inquiry.
- **On-screen Hebrew (draft):**
  > המשבר עורר ביקורת ציבורית ובחינה ממסדית.  
  > ועדת החקירה בראשות השופט **משה בייסקי** הגישה את דו"חה ב־**16 באפריל 1986**.  
  > השאלה שלנו: כיצד מתחלקת אחריות בין מנהלי בנקים, פיקוח מדינתי ומקבלי החלטות? [S04; S06]
- **Speaker note:** Distinguish: inquiries reported findings and recommendations; criminal actions and appeals happened later and are legally separate. Invite students to evaluate regulatory oversight without manufacturing a single verdict that all actors shared the same liability. [S02; S04; S06]
- **Visual:** Accountability matrix with four columns `בנקים`, `מפקחים`, `ממשלה`, `משקיעים`; rows `סמכות`, `תמריץ`, `מידע`, `שאלת אחריות`. Questions in fourth row must appear with question marks unless supported by specific findings.
- **Interaction:** Show/hide `ממצא מתועד` versus `שאלת ניתוח`.
- **Claims:** C18, C19. **Classification:** FACT + ANALYSIS.

## Slide 13 — מעבדת המדיניות: ניסוי מחשבתי (Python)
- **Purpose:** Mandatory Python computation and active viewer engagement.
- **On-screen Hebrew (draft):**
  > **מה קורה למערכת פשוטה כאשר לחץ המכירות גובר ויכולת התמיכה מוגבלת?**  
  > שנו הנחות על אמון המשקיעים, לחץ המכירות, כושר התמיכה ותזמון התערבות ציבורית.  
  > **סימולציה לימודית בלבד — אינה שחזור היסטורי, תחזית או מדידה של מדד מניות 1983.**
- **Speaker note:** Python executes a deterministic unitless model; interpret trends *inside this model only*. All graphs use `תקופה 1...12`, never historical dates. Show input parameters and a visible `מודל היפותטי` badge. If Flask is unavailable, show a clear 'Python service offline' message rather than static results passed off as live.
- **Visual:** Two scenario panels, line chart with axis `מדד יציבות מדומה (ללא יחידות)` and period 1–12; support-budget meter; visible intervention timing marker.
- **Interaction:** confidence, selling pressure, bank capacity, intervention `none/delayed/early`; `הרץ`, `השווה`, `אפס`.
- **Claims:** C20. **Classification:** SIMULATION only. No historical source can substantiate arbitrary numerical model outputs.

## Slide 14 — מסקנות: מה נשאר מהמשבר?
- **Purpose:** Answer research question, summarize limits, cite evidence.
- **On-screen Hebrew (draft):**
  > **שלושה לקחים לדיון:**  
  > (1) תמריצים וניגודי עניינים עלולים לעוות את התנהגות השוק.  
  > (2) פיקוח ואמון ציבורי הם חלק מהיציבות הפיננסית.  
  > (3) התערבות ממשלתית יכולה לייצב — אך מעלה שאלות על אחריות וחלוקת עלויות.  
  > **מסקנות אנליטיות של צוות הסטודנטים; מבוססות על המקורות, אינן ציטוט.**
- **Speaker note:** End with the precise political-economy research question and answer rather than 'everything was Aridor's fault'. Mention 1985 stabilization only as a separate later event if relevant. Provide source panel: S01/S02/S03/S04/S05/S06/S08, links to complete bibliography and GitHub methodology.
- **Visual:** Three pillar cards with hover-to-source references; final credits.
- **Interaction:** `מקורות מלאים`, `שיטת העבודה`, `הפעל מצגת מחדש`, `עבור ל-GitHub`.
- **Claims:** C21. **Classification:** ANALYSIS informed by facts.

---

## Content QA matrix before handing to a coding agent

| Risk / check | Blocker condition | Remedy |
|---|---|---|
| Invented historical prices | Any realistic 1983-style unlabeled numbers or time-series | Remove / use sourced actual data with units, or mark synthetic |
| Single-villain explanation | Narrator says Aridor 'caused' the crash alone | Reframe multiple actors and long-run system, add Aridor correct role |
| Inflated fiscal cost | $9.1bn labeled 'net taxpayer loss' | Explain gross program outlays versus later asset values |
| Wrong sequence | 1985 stabilization conflated with 1983 rescue | Separate event dates |
| Claim of universal bank participation | First International shown participating without evidence | Limit to implicated participants |
| Sham 'Python' integration | Chart hardcoded in JS despite promising backend | Make real API request and demonstrate changing response |
| Sham '3D' | Flat video with no 3D source scene | Genuine Three.js geometry, perspective, camera movement and recorded output |
| Historical photo with unknown rights | Cropped newspaper photo used without permission | Original artwork, public-domain or permission-granted source |
| No traceable evidence | Historical numbers missing Sxx reference and claim ID | Add to claim register or delete the number |
| Poor Hebrew BiDi | Numeric/currency tokens reorder in RTL rendering | Use semantic HTML `<bdi>`/`dir=ltr` and screenshot testing |

## Authoring rule for implementers

The `On-screen Hebrew` is a **researched draft** for editorial approval, not a finalized academic conclusion. Retain core factual wording, source labels and legal/financial qualifications unless the team requests a change. Do **not** fabricate specific quotes, real-time data, historical footage or 1983 market prices for visual drama. Keep independent variations and reviewer edits in Git history.
