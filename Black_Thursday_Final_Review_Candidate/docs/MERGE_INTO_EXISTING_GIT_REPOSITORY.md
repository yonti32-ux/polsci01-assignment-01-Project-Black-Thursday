# Merge the Clean Candidate into Your Actual Git Clone — Windows / Cursor

**Important:** This folder is **a clean file snapshot, without `.git`**. Do **not** replace your existing `.git` directory or reinitialize Git; your previous meaningful commits and Liron's work are grading evidence. **We did not push anything to GitHub.**

## 0. Why this merge matters

The uploaded snapshot had three competing code trees: `Project-Black-Thursday-deliverable/` (old), `Black_Thursday_v04_Selective_Update/` (partial patch), and `Black_Thursday_v05_COMPLETE_Ready_to_Run/` (current v3 film). The clean candidate provides **one canonical active build** under `Project-Black-Thursday-deliverable/` and retains selected research/history files in `docs/history/`. It should replace the confusing duplication **only after you protect uncommitted work**.

## 1. Confirm actual repository and back up

Open the folder you use in Cursor for the actual cloned repository and run:

```powershell
git status --short
git branch --show-current
git remote -v
git log -5 --oneline
```

**Issue identified in the uploaded ZIP:** Five paths were uncommitted/modified, and the Git remote in the ZIP used an `AI-Vibe-coding--assignment...` URL while earlier conversation gave a `polsci01-assignment...` URL. **Determine which is actually correct** from your GitHub account; don't overwrite the remote blindly.

If `git status` is non-empty, **save/commit the legitimate changes or create a separate backup**. Do not run `git reset --hard`, `git clean -fd`, or destructive commands without verifying where those edits came from.

Make a ZIP backup of your current repo folder (including `.git` privately) before restructuring.

## 2. Create an integration branch

```powershell
git switch -c docs/final-review-and-consolidation
```

If that name exists, choose another. Avoid doing the cleanup directly on a collaborator's active branch.

## 3. Copy this candidate's contents into the repo root

From the extracted `Black_Thursday_Final_Review_Candidate` directory, copy its **files and folders** into the actual repository root (the location that contains its `.git` directory). Allow replacement **only after** backing up current files. The full v3 film and launcher are already included.

New root objects should include `README.md`, `PRD.md`, `.gitignore`, `START_BLACK_THURSDAY.bat`, `START_BLACK_THURSDAY.sh`, `launch_presentation.py`, `Project-Black-Thursday-deliverable/`, `docs/`, and `prompts/`.

### Old redundant folders to remove from the active branch **after verifying the new version**

- `Black_Thursday_v04_Selective_Update/`
- `Black_Thursday_v05_COMPLETE_Ready_to_Run/`
- `black-thursday-phase3/` — its original research/film plan has been preserved at `docs/history/`.
- `phase 6/` — initial audit is preserved at `docs/history/`.
- `presentation - phase 5/` — its PDF and significant prompt were preserved in `docs/history/` / `prompts/`.
- Older root `PRD 0.1.md` — preserved at `docs/history/PRD-original-v0.1.md`.

**Only delete those paths after comparing them for any genuinely newer collaborator changes.** Deleting tracked working-tree copies after backup does not erase the old file contents from Git history.

## 4. Smoke test the canonical project

From the **actual repo root**, double-click `START_BLACK_THURSDAY.bat`. Then:

- Watch slide 9's full v3 movie.
- Run and change the Python model on slide 13.
- Navigate all 14 slides.
- Verify screenshot links in root README after pushing.

Or run:

```powershell
cd Project-Black-Thursday-deliverable
python -m unittest discover -s python/tests -v
python python/app.py
```

Open `http://127.0.0.1:8000/`.

## 5. Review, commit and push

```powershell
git status --short
git diff --stat
git diff -- README.md PRD.md
git add -A
git commit -m "docs: consolidate final candidate and preserve research history"
git push -u origin docs/final-review-and-consolidation
```

Review that branch (with Liron) and merge to `main` in GitHub when satisfied. The original Git history remains intact, and GitHub's root README will automatically show the final implementation's screenshots and launch instructions. Confirm the lecturer sees the **correct** repository URL.

## 6. After Gemini

Save actual Gemini feedback to `docs/reviews/`, update `docs/SELF_ASSESSMENT.md` with your own grade and rationale, address critical issues, and commit/push that **additional** verified iteration. Then submit the **official** university PDF form privately via Moodle, **each student separately**.
