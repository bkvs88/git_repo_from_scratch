# Git From Scratch — Python Calculator

A tiny Python calculator project used to demonstrate the **Git basics**:
`git init`, `git status`, `git add`, `git commit`, `git log`, `git diff`,
and `.gitignore` — with **both Git CLI and VS Code Source Control** options.

It also contains a complete, reproducible walkthrough of **`git stash`**:
interrupting a half-finished feature, shipping an urgent fix on a separate
branch, then safely restoring the parked work — see
[the `git stash` exercise](#stash-exercise).

## 🛠️ Git vs. GitHub: What's the Difference?

**Git and GitHub are not the same thing.** Git is the local version control software you install on your computer, while GitHub is an online hosting service that stores your Git repositories in the cloud and adds collaboration tools.

### At a Glance

| Feature | Git 💾 | GitHub 🌐 |
| :--- | :--- | :--- |
| **What is it?** | A local command-line software tool. | A cloud-based web service. |
| **Primary Purpose** | Tracks code history and manages file changes. | Hosts Git code repositories and facilitates team teamwork. |
| **Environment** | Runs entirely on your local machine. | Hosted on the web in the cloud. |
| **Internet Required?**| No. Works offline. | Yes. Requires internet access. |
| **Interface** | Command Line Interface (CLI) or local GUI tools. | Graphical Web User Interface. |
| **Key Features** | Commits, branching, merging, history logs. | Pull requests, issue tracking, project boards, actions. |

### Summary
* **Git** is the actual engine that takes snapshots of your project files as you make changes. It doesn't require an account or an internet connection to work.
* **GitHub** acts like a "social network" or cloud drive for your Git repositories. It lets you share your local Git work online, back it up securely, and collaborate smoothly with developers across the globe.


---

## 📂 Project Files

Every file below is **committed to this repository**, including the hidden
`.gitignore`. To confirm, run `git ls-files` — hidden files are not shown in
GitHub's default file browser.

| File              | Purpose                                             |
| ----------------- | --------------------------------------------------- |
| `readdata.py`     | Reads two integers (`a`, `b`) from the user.        |
| `addition.py`     | Defines `add(a, b)` — returns the sum.              |
| `substraction.py` | Defines `sub(a, b)` — returns `a - b`.              |
| `multiplication.py` | Defines `multiply(a, b)` — returns `a * b`.        |
| `division.py`     | Defines `div(a, b)` — returns `a / b`; guards `b == 0`. |
| `power.py`        | Defines `power(a, b)` — returns `a ** b`.          |
| `calculator.py`   | Entry point — calls all five operations.            |
| `.gitignore`      | Tells Git which files to **never track**.           |

Run it with:

```bash
python calculator.py
```

It prompts for two numbers, then prints all five results:

```
Enter first number :  10
Enter second number : 4
Data Capture completed
Basic Calculator
Addition of 10 and 4 is : 14
substraction of 10 and 4 is : 6
Division of 10 and 4 is : 2.5
multiplication of 10 and 4 is : 40
Power of 10 raised to 4 is : 10000
```

---

## 1️⃣ `git init` — Create a Repository

**Option A — Git command**

```bash
cd git_repo_from_scratch
git init
git status
```

**Option B — VS Code**

1. Open the folder in VS Code (`File > Open Folder...`).
2. Press `Cmd + Shift + P` → type **"Git: Initialize Repository"** → Enter.
3. Or just click the **Source Control icon** (branch icon, left sidebar) →
   click **"Initialize Repository"**.

> ✅ Both create a hidden `.git/` folder. Everything Git needs lives inside it.

---

## 2️⃣ `git status` — See What's Going On

**Option A — Git command**

```bash
git status
```

Typical output at the start:

```
Untracked files:
  addition.py
  division.py
  multiplication.py
  substraction.py
  calculator.py
  readdata.py
  .gitignore
```

**Option B — VS Code**

- Open the **Source Control panel** (`Ctrl/Cmd + Shift + G`).
- Unstaged files appear under **"Changes"** with a `U` (untracked) badge.
- Staged files appear under **"Staged Changes"**.

---

## 3️⃣ `git add` — Stage Files

**Option A — Git command**

```bash
# Stage specific files
git add readdata.py

# Stage everything except ignored files
git add .
```

**Option B — VS Code**

- In the Source Control panel, hover a file under **"Changes"** and click the
  **`+`** button to stage it.
- Or right-click → **Stage Changes**.
- Or stage them all: hover the **"Changes"** header → click the **`+`**.

---

## 4️⃣ `git commit` — Save a Snapshot

**Option A — Git command**

```bash
git commit -m "Add readdata module to accept two numbers"
```

**Option B — VS Code**

- Type your message in the **Message box** at the top of the Source Control
  panel, then click the **✔ (Check)** button — or press `Cmd + Enter`.

---

## 5️⃣ `git log` — View Commit History

**Option A — Git command**

```bash
git log                 # full history
git log --oneline       # compact one-line-per-commit view
git log --oneline -5    # last 5 commits
```

**Option B — VS Code**

- Open the **Timeline** view: Explorer sidebar → scroll to the bottom →
  **Timeline** → **Git History**.
- Click any entry to open a diff of that commit.

> 📌 This repo was built incrementally over a series of meaningful commits (see below).

---

## 6️⃣ `git diff` — Compare Changes

**Option A — Git command**

```bash
git diff                # unstaged changes (working tree vs. index)
git diff --staged       # staged changes (index vs. last commit)
git diff HEAD~1 HEAD    # changes introduced by the last commit
```

**Option B — VS Code**

- Click any file under **"Changes"** in the Source Control panel — a
  side-by-side editor opens with **green (+) / red (-)** gutters.
- To stage a *hunk* (part of a file): hover the hunk → click the **`+`** icon.

---

## 7️⃣ `.gitignore` — Keep Files Out of Git

Files listed in `.gitignore` are **never staged or committed**.

```gitignore
# Python bytecode and caches
__pycache__/
*.py[cod]

# macOS
.DS_Store

# Virtual environments
.venv/
venv/

# IDE / editor files
.vscode/
.idea/
```

**Why it matters here:** `__pycache__/` and `.DS_Store` are auto-generated junk.
Without `.gitignore`, `git status` would keep showing them as untracked files.

**Option A — Git command**

```bash
git status                 # ignored files are NOT listed
git status --ignored       # see them listed under "Ignored files"
```

**Option B — VS Code**

- Ignored files are shown **greyed out / dimmed** in the Explorer.
- VS Code also offers **"Add to .gitignore"**: right-click a file in Source
  Control → **Add to .gitignore**.

---

<a id="stash-exercise"></a>

## 8️⃣ The `git stash` Exercise

**The scenario:** you are halfway through building a new feature when a
production bug demands your attention *right now*. You cannot commit
half-finished work, and you cannot leave the working tree dirty or you will not
be able to switch branches. `git stash` is the tool for exactly this: it parks
your work in a temporary commit, hands you back a clean tree, and lets you
restore that work later.

Everything below is the **real transcript** of this repository, not a
reconstruction.

### The Situation

| | |
| :--- | :--- |
| **Original branch** | `main` |
| **Feature in progress** | add a new `power` operation (`power.py` + wire-up in `calculator.py`) |
| **Interruption** | a division-by-zero bug that must be fixed immediately |
| **Hotfix branch** | `hotfix/division-by-zero` |

---

### Step 1 — Start the feature, but do NOT commit it

Create the new operation module:

```python
# power.py
from readdata import a, b


def power(a, b):
    c = a ** b
    print(f"Power of {a} raised to {b} is : {c}")
    return c
```

Wire it into the entry point:

```python
# calculator.py
from power import power

def main():
    print("Basic Calculator")
    add(a, b)
    sub(a, b)
    div(a, b)
    multiply(a, b)
    power(a, b)   # <-- new
```

Confirm it works, then **stop before committing**:

```bash
printf '2\n10\n' | python calculator.py
```

```
multiplication of 2 and 10 is : 20
Power of 2 raised to 10 is : 1024
```

```bash
git status --short
```

```
 M calculator.py
?? power.py
```

`M` = modified but unstaged, `??` = untracked (brand-new file).
**Neither change is committed.** This is the state we need to park.

---

### Step 2 — `git stash` the work

```bash
git stash push -u -m "WIP: add power operation (exponent) to calculator"
```

```
Saved working directory and index state On main: WIP: add power operation (exponent) to calculator
```

```bash
git status --short
```

```
```

The working tree is **clean**. The feature is safe, invisible to
`git status`, and recoverable. You are free to switch branches.

> ⚠️ **Why `-u`? This matters.**
>
> A plain `git stash` only stashes **tracked** files. A *new* file like
> `power.py` is untracked, so a plain stash **silently leaves it behind** —
> no error, no warning. This was actually observed in this repository:
>
> ```bash
> git stash push -m "WIP: plain stash"
> git status --short
> ```
>
> ```
> ?? power.py        <-- still here! the stash missed it
> ```
>
> Always use `git stash push -u` (or `-a` to also include ignored files) when
> your work contains new files. Verify with `git status` afterwards.

---

### Step 3 — Switch branches and ship the urgent fix

```bash
git checkout -b hotfix/division-by-zero
```

Reproduce the bug — note the operands the user actually typed (`10` and `0`)
vanished from the output:

```bash
printf '10\n0\n' | python calculator.py
```

```
cannot division by zero hence change value of b to 1
Division of 0 and 1 is : 0.0          <-- a fabricated, misleading result
```

> ⚠️ **Note for readers picking this up on the current `main`:** the bug above
> is **already fixed**, so you will *not* see that output any more. Dividing by
> zero now correctly reports
> `Error: cannot divide 10 by zero. Division skipped.` The transcript below is
> the **historical record** of the exercise as it was performed, kept for
> teaching purposes.
>
> If you want to reproduce the bug yourself, check out the commit just before
> the fix and run it there:
>
> ```bash
> git show 8dc6f4f:division.py     # the original buggy version
> printf '10\n0\n' | python calculator.py   # on that older checkout
> ```

The old code did this:

```python
if b == 0:
    print("cannot division by zero hence change value of b to 1")
    a = 0      # overwrites the user's numbers
    b = 1
c = a / b
```

It silently **overwrote both operands** and printed a confident-looking
`Division of 0 and 1 is : 0.0` for numbers the user never entered. The urgent
fix reports the error honestly and leaves the real operands intact:

```python
# division.py
from readdata import a, b


def div(a, b):
    if b == 0:
        print(f"Error: cannot divide {a} by zero. Division skipped.")
        return None
    c = a / b
    print(f"Division of {a} and {b} is : {c}")
    return c
```

Verify both the bug case and the normal case:

```bash
printf '10\n0\n' | python calculator.py   # the bug case
```

```
Error: cannot divide 10 by zero. Division skipped.
```

```bash
printf '10\n4\n' | python calculator.py   # normal division still fine
```

```
Division of 10 and 4 is : 2.5
```

Commit and push the hotfix:

```bash
git add division.py
git commit -m "Fix division by zero to report error instead of returning false result"
git push -u origin hotfix/division-by-zero
```

The urgent fix is shipped **without the half-finished feature** ever touching
`main`. That is the entire point of stashing.

---

### Step 4 — Return to the original branch

```bash
git checkout main
git stash list
```

```
stash@{0}: On main: WIP: add power operation (exponent) to calculator
```

The parked work survived the branch switch and is waiting for us.

---

### Step 5 — `git stash list` — what is parked?

```bash
git stash list
```

```
stash@{0}: On main: WIP: add power operation (exponent) to calculator
```

Each line is one stash entry, **newest first**. The `stash@{N}` part is the
reference you pass to the other commands.

| Command | What it does |
| :--- | :--- |
| `git stash list` | List all parked stashes, newest first |
| `git stash show` | Show **what changes** a stash contains |
| `git stash apply` | Restore the work, **keep** the stash entry |
| `git stash pop` | Restore the work **and delete** the entry |
| `git stash drop` | **Delete** the entry without restoring anything |

> 🔎 `stash@{0}` is the **most recent** stash. After you `pop` or `drop` one,
> every older stash **renumbers** — what was `stash@{1}` becomes `stash@{0}`.
> Re-run `git stash list` instead of trusting a remembered index.

---

### Step 6 — `git stash show` — what is inside it?

Default view — a summary of **tracked** file changes:

```bash
git stash show stash@{0}
```

```
 calculator.py | 2 ++
 1 file changed, 2 insertions(+)
```

Full patch:

```bash
git stash show -p stash@{0}
```

```diff
diff --git a/calculator.py b/calculator.py
index 730be14..6c31f73 100644
--- a/calculator.py
+++ b/calculator.py
@@ -3,12 +3,14 @@ from readdata import a , b
 from addition import add
 from substraction import sub
 from division import div
 from multiplication import multiply
+from power import power
 def main():
     print("Basic Calculator")
     add(a,b)
     sub(a,b)
     div(a,b)
     multiply(a,b)
+    power(a,b)
```

> ⚠️ **The new file is missing from that output.** `git stash show` only
> reports *tracked* files by default, so the brand-new `power.py` is invisible.
> This mistake is easy to make, because the summary looks plausible while
> quietly omitting a whole file.
>
> Always add `--include-untracked` when the stash was created with `-u`:
>
> ```bash
> git stash show --include-untracked stash@{0}
> ```
>
> ```
>  calculator.py | 2 ++
>  power.py      | 7 +++++++
>  2 files changed, 9 insertions(+)
> ```

Useful variations:

```bash
git stash show --stat stash@{0}              # summary (same as default)
git stash show -p stash@{0}                  # full patch, tracked files only
git stash show -p --include-untracked        # full patch, including new files
git stash show -p stash@{1}                  # inspect an older stash
```

---

### Step 7 — `git stash apply` — restore the work, keep the stash

```bash
git stash apply stash@{0}
```

```
On branch main
Changes not staged for commit:
	modified:   calculator.py

Untracked files:
	power.py
```

The feature is back and the calculator runs again:

```bash
printf '2\n10\n' | python calculator.py
```

```
Power of 2 raised to 10 is : 1024
```

Now the important part — **check whether the stash is still there**:

```bash
git stash list
```

```
stash@{0}: On main: WIP: add power operation (exponent) to calculator
```

**`apply` left the entry in place.** Nothing was consumed.

---

### Step 8 — `git stash drop` — delete an entry without restoring it

`drop` removes a stash entry. It touches **only the stash list** — it does not
change your working tree at all:

```bash
git stash drop stash@{0}
```

```
Dropped refs/stash@{0} (2bf77d883dddfbff500e632c94f9ad6fab95473b)
```

```bash
git stash list
```

```
```

Empty — no stashes remain. And the working tree is untouched:

```bash
git status --short
```

```
 M calculator.py
?? power.py
```

`drop` is the **only destructive command** in this set. Use it to throw away a
stash you no longer want.

> 🚨 **A mistake that actually happened here — and how it was undone.**
>
> Early in this exercise a stash was created with a plain `git stash` (no `-u`)
> and therefore held **only** the `calculator.py` change, while `power.py` sat
> untracked in the working tree. That stash was then `drop`ped to start over —
> which **permanently destroyed the only copy of the `calculator.py` change**:
>
> ```bash
> git stash drop
> ```
>
> ```
> Dropped refs/stash@{0} (d6b6defcd0c763262ebc7d4f094979fced28b212)
> ```
>
> The tell-tale symptom appeared on the next stash: `git stash show` printed an
> **empty diff**, because the new stash had captured nothing but a file.
>
> **Recovery.** `drop` only deletes a *reference*; the commits themselves linger
> as unreachable objects for a while. The hash Git printed
> (`d6b6def...`) can be used directly:
>
> ```bash
> git checkout d6b6def -- calculator.py   # restore the file from the lost stash
> ```
>
> If you never recorded the hash, hunt for it:
>
> ```bash
> git fsck --unreachable --no-reflogs    # find dangling stash commits
> git reflog stash                       # stash-specific reflog, if still present
> ```
>
> **Lesson:** before `drop`ping a stash, make sure its contents are already
> committed, applied, or safely backed up. `drop` is not undoable by `git`.

---

### Step 9 — `git stash pop` — restore the work and delete the entry

Stash the feature once more, then pop it:

```bash
git stash push -u -m "WIP: add power operation (exponent) to calculator"
git stash list
```

```
stash@{0}: On main: WIP: add power operation (exponent) to calculator
```

```bash
git stash pop
```

```
On branch main
Changes not staged for commit:
	modified:   calculator.py

Untracked files:
	power.py

Dropped refs/stash@{0} (2438fdaaf76dd52ec071bbf9f31c39bc048f14c8)
```

Note the final line: **`Dropped refs/stash@{0}`**. `pop` removed the entry.

```bash
git stash list
```

```
```

Empty — the stash was applied *and* consumed. Your work is in the working tree
and the stash list is clean.

---

## 🔑 `apply` vs `pop` — the difference

They do the **same restoration**. The *only* difference is what happens to the
stash entry afterwards.

| | `git stash apply` | `git stash pop` |
| :--- | :--- | :--- |
| Restores the work to the working tree | ✅ Yes | ✅ Yes |
| Removes the entry from `git stash list` | ❌ **No — it stays** | ✅ **Yes — it is dropped** |
| Stash can be applied a second time | ✅ Yes, as many times as you like | ❌ No — one shot only |
| Typo in `stash@{N}` recoverable later | ✅ Still there | ❌ **Gone** |
| Equivalent manual command | `apply` + `git stash drop` | `apply` + `git stash drop` |
| Best used when | you want to **inspect/compare** before committing | you are **sure** and want a clean list |

In one line: **`pop` = `apply` + `drop`.**

### Which should you use?

**Use `pop` when you are certain** the restored work is what you want. It is the
common default because a clean `git stash list` is nice, and in the common
case you stashed something, switched away, and are now unconditionally putting
it back.

**Use `apply` when there is any doubt** — particularly:

- You stashed several times and want to work through them one at a time,
  comparing each against the current state.
- You want to restore the work, run the tests, and *then* decide whether to
  keep it or throw it away.
- You suspect you may need to re-apply the same work twice (e.g. restoring it
  onto two different branches).

```bash
# cautious path — nothing is lost, you decide afterwards
git stash apply stash@{0}
# ... run tests, inspect the diff ...
git stash drop stash@{0}    # only now, once you are satisfied
```

### The safest habit

Default to **`apply`**, verify the result, and finish with a deliberate `drop`.
The cost is one extra command. The alternative — a mistyped `pop` — costs you
the work, as the [Step 8 recovery](#step-8--git-stash-drop--delete-an-entry-without-restoring-it)
above demonstrates.

---

## 🧩 Other Useful Stash Commands

```bash
git stash push -u -m "msg"     # save, including untracked files, with a label
git stash push --keep-index    # stash only the UNstaged changes, keep staged
git stash push --patch         # interactively pick which hunks to stash
git stash branch fix-div-zero  # pop the stash onto a NEW branch in one step
git stash save "msg"           # legacy alias of `git stash push`
git stash clear                # delete ALL stash entries at once
```

### Recovering a lost stash

```bash
git fsck --unreachable --no-reflogs   # find dangling stash commits
git reflog                            # HEAD reflog, may mention the stash
git show <hash>                       # inspect a recovered stash commit
git stash apply <hash>                # restore from it directly
```

> 💡 **Anatomy of a stash.** A stash is not one object but a small set of
> commits:
>
> - `stash@{0}` — the **stash commit** itself (your working-tree changes).
> - `stash@{0}^2` — an **index snapshot**, so `--index` / `--keep-index` can be
>   reproduced.
> - `stash@{0}^3` — present **only for `-u` stashes**: the **untracked files**.
>
> That third parent is exactly why a default `git stash show` hides your new
> files, and it is where to look when recovering a dropped stash:
>
> ```bash
> git ls-tree -r --name-only stash@{0}^3   # untracked files inside the stash
> git log -1 --format='%p' stash@{0}       # list a stash's parent commits
> ```
>
> Because `drop` only removes the *reference*, that object graph survives as
> unreachable data for a while — which is what makes recovery possible.

---

## 9️⃣ Bringing It Together — Merge the Hotfix

Back on `main` with the feature committed and the urgent fix sitting on
`hotfix/division-by-zero`:

```bash
git merge --no-ff hotfix/division-by-zero -m "Merge hotfix/division-by-zero: correct division by zero handling"
```

`--no-ff` keeps the hotfix as a visible merge commit, preserving the fact that
the fix was developed separately:

```bash
git log --oneline --graph
```

```
*   Merge hotfix/division-by-zero: correct division by zero handling
|\
| * Fix division by zero to report error instead of returning false result
* | Add power operation and wire it into the calculator
* | Sync README commit log with actual git history
* | Update commit messages and README content
|/
* Wrap calculator execution in a main function guard
* Add .gitignore to exclude bytecode, caches, and local files
* Add README documenting the calculator project
* Add calculator main entry point that runs all operations
* Add multiplication and division operations
* Add addition and substraction operations
* Add readdata module to capture user input
```

> ℹ️ **A note on what happened next to this history.** A later
> `git pull --rebase origin main` — run to pick up upstream README changes —
> found that `main` had diverged and **replayed the local commits on top**,
> which discarded the merge commit and produced a linear history instead. The
> hotfix commit is still there and still reachable from `main`; only the
> merge marker is gone, and its SHA changed as a result.
>
> This is standard `rebase` behaviour, not data loss, but it is worth knowing:
> **a rebase rewrites commit SHAs.** If you had already shared the old SHAs in
> a PR, a message, or a wiki, they would now be stale.

Final verification — the feature **and** the fix are both live on `main`:

```bash
printf '10\n4\n' | python calculator.py   # all five operations
printf '10\n0\n' | python calculator.py   # urgent fix: honest error
printf '2\n10\n' | python calculator.py   # new feature: power
```

### Where the hotfix branch went

The `hotfix/division-by-zero` branch described in this section is **still
published**, so the workflow can be verified directly from GitHub rather than
inferred from the commit log:

```bash
git log --oneline -1 origin/hotfix/division-by-zero
```

```
671ddc6 Fix division by zero to report error instead of returning false result
```

> ⚠️ **The branch points at `671ddc6`, not at the original `621ac5b`.**
>
> A later `git pull --rebase` rewrote the hotfix commit, so the fix reached
> `main` as `671ddc6`. The branch was moved to that commit deliberately,
> because `671ddc6` is an **ancestor of `main`**:
>
> ```bash
> git diff main...hotfix/division-by-zero     # no output
> ```
>
> That makes the branch safe to keep around — a pull request from it to `main`
> is empty and cannot reintroduce anything.

Four annotated tags pin the commits involved, so the incident stays auditable
even though branches come and go:

| Tag | Commit | What it marks |
| :--- | :--- | :--- |
| `division-by-zero-fix` | `671ddc6` | The fix as it lives in `main`. **Safe.** |
| `hotfix-original` | `621ac5b` | The original hotfix tip, before the rebase. **Do not merge.** |
| `main-outage` | `9b233f1` | The commit that shipped the broken `main`. |
| `outage-fix` | `3168b93` | The commit that repaired it. |

Inspect them with:

```bash
git show division-by-zero-fix     # the fix
git show main-outage              # what broke
git show outage-fix               # what repaired it
```

> 🚨 **`hotfix-original` (`621ac5b`) is a historical artefact, not usable code.**
> Its `division.py` still contains `from readdata import a, b`, which the
> import-time refactor deleted. Merging or checking it out reproduces the
> `ImportError` outage on purpose — that is exactly what happened when PR #2
> merged the stale branch. It is tagged only so the original commit stays
> reachable; before it was tagged, a fresh clone could not see it at all.

---

## 🔟 Verifying Changes Manually

### The outage that motivated this

The exercise above parked work with `git stash` and merged a long-lived
`hotfix/division-by-zero` branch into `main`. That second action caused a real
outage: because the hotfix branch was created **before** the import-time
refactor, merging it back **resurrected** a line the refactor had deleted.

```python
from readdata import a, b   # resurrected by the stale merge
```

`main` stopped working entirely:

```
ImportError: cannot import name 'a' from 'readdata'
```

> ⚠️ **This repository has no automated tests or CI.** The test suite and
> GitHub Actions workflow that briefly guarded against this have since been
> removed, so **nothing** now prevents a similar regression from reaching
> `main`. Run the checks below by hand after any change.

### The checks to run by hand

Run all four before pushing:

```bash
# 1. Every module must import with no stdin attached.
#    Catches the import-time input() and stale-import class of bug.
for m in addition substraction multiplication division power readdata calculator; do
  python -c "import $m" < /dev/null || echo "FAILED: $m"
done

# 2. No stale readdata imports (only read_data may be imported).
if grep -rnE 'from readdata import .*(^|[ ,(])(a|b)([ ,)]|$)' --include='*.py' .; then
  echo "FAILED: someone imports a or b from readdata"
fi

# 3. The CLI must work end to end.
printf '10\n4\n'  | python calculator.py   # normal
printf '10\n0\n'  | python calculator.py   # zero divisor
printf '2\n10\n'  | python calculator.py   # power

# 4. Everything must byte-compile.
python -m compileall -q .
```

Expected output for check 3:

```
Addition of 10 and 4 is : 14
substraction of 10 and 4 is : 6
Division of 10 and 4 is : 2.5
multiplication of 10 and 4 is : 40
Power of 10 raised to 4 is : 10000
Error: cannot divide 10 by zero. Division skipped.
Power of 2 raised to 10 is : 1024
```

### Why the import-time bug was possible at all

The original `readdata.py` called `input()` at **module scope**, and every
operation module imported it at import time. That made each operation depend on
a human at the keyboard, so the functions could not be reused or unit tested.

The refactor fixed it: `read_data()` contains the prompts, `main()` calls it,
and the operation modules import nothing. Check 1 above is what keeps it that
way.

### Branch protection

`main` is still protected against direct pushes, so changes reach it through a
pull request:

```bash
gh api repos/bkvs88/git_repo_from_scratch/branches/main/protection
```

> 🔎 Earlier this repository required a `Tests` status check before merging.
> That check was produced by the now-deleted workflow, so the requirement was
> removed at the same time — otherwise every pull request would have been
> blocked forever waiting for a check that could never run. PR-only protection
> remains; the automated gate does not.

---

## 🚀 Publish to GitHub

### Option A — Git commands (HTTPS remote)

```bash
# Create the repo on GitHub (skip if you already created it)
gh repo create git_repo_from_scratch --public --source=. --remote=origin --push
```

Or manually:

```bash
git branch -M main
git remote add origin https://github.com/<your-username>/git_repo_from_scratch.git
git push -u origin main
```

Later updates:

```bash
git add .
git commit -m "Describe your change"
git push
```

### Option B — VS Code

1. Open the Source Control panel (`Cmd + Shift + G`).
2. Click **"Publish Branch"** (top of the panel).
3. Choose **"GitHub"** → pick **Private / Public** → sign in if asked.
4. VS Code creates the remote repo, sets the origin, and pushes — all for you.

After publishing, every sync is one click: the **↻ (Refresh/Sync)** arrows at
the bottom-left of the Source Control panel.

---

## 📝 The Commits

Every commit below is a real commit on this repository's `main` branch, listed
newest first exactly as `git log --oneline` reports it. The short SHA is shown
so each one can be verified individually.

| #   | SHA     | Commit message                                                                | Files |
| --- | ------- | ----------------------------------------------------------------------------- | ----- |
| 1   | `b909a58` | `Remove test suite and CI workflow (#6)`                                    | 6 |
| 2   | `d8c99b0` | `Remove test suite and CI workflow (#5)`                                    | 1 |
| 3   | `c6c860e` | `Add pytest suite and CI workflow to catch import-time regressions (#4)`     | 8 |
| 4   | `4d69cea` | `Note that Step 3's bug is already fixed on main, with repro steps`          | 1 |
| 5   | `3168b93` | `Fix ImportError: remove stale 'from readdata import a, b' from division.py (#3)` — 🏷️ `outage-fix` | 1 |
| 6   | `9b233f1` | `Fix division by zero to report error instead of returning false result (#2)` — 🏷️ `main-outage` | 1 |
| 7   | `aa2bdde` | `Remove import-time input() side effects from operation modules (#1)`         | 7 |
| 8   | `2c28a16` | `Note that the commit table cannot list its own SHA`                          | 1 |
| 9   | `240a561` | `Correct commit table to match rebased history and document SHA rewrite`      | 1 |
| 10  | `b857640` | `Document the git stash exercise: list, show, apply, pop, drop`               | 1 |
| 11  | `671ddc6` | `Fix division by zero to report error instead of returning false result` — 🏷️ `division-by-zero-fix` | 1 |
| 12  | `3aaf5ac` | `Add power operation and wire it into the calculator`                         | 2 |
| 13  | `1e9337e` | `Sync README commit log with actual git history`                              | 1 |
| 14  | `a1cc5d9` | `Update commit messages and README content`                                    | 1 |
| 15  | `8dc6f4f` | `Wrap calculator execution in a main function guard`                           | 1 |
| 16  | `dc6882c` | `Add .gitignore to exclude bytecode, caches, and local files`                  | 1 |
| 17  | `50ed391` | `Add README documenting the calculator project`                                 | 1 |
| 18  | `43c059f` | `Add calculator main entry point that runs all operations`                     | 1 |
| 19  | `4ef7426` | `Add multiplication and division operations`                                    | 2 |
| 20  | `b705def` | `Add addition and substraction operations`                                     | 2 |
| 21  | `39e87a3` | `Add readdata module to capture user input`                                    | 1 |

Commits 21–12 build up the calculator itself; 11 is the stashed feature (see
[Step 1](#step-1--start-the-feature-but-do-not-commit-it)) and 10 documents the
whole stash exercise. Commits 9–8 are README corrections. Commits 7–5 are the
pull requests: **6** merged the stale hotfix branch and broke `main`, and **5**
repaired it. Commits 3–1 added CI and then removed it again.

Verify them yourself:

```bash
git log --oneline --graph
```

```
b909a58 Remove test suite and CI workflow (#6)
d8c99b0 Remove test suite and CI workflow (#5)
c6c860e Add pytest suite and CI workflow to catch import-time regressions (#4)
4d69cea Note that Step 3's bug is already fixed on main, with repro steps
3168b93 Fix ImportError: remove stale 'from readdata import a, b' from division.py (#3)
9b233f1 Fix division by zero to report error instead of returning false result (#2)
aa2bdde Remove import-time input() side effects from operation modules (#1)
2c28a16 Note that the commit table cannot list its own SHA
240a561 Correct commit table to match rebased history and document SHA rewrite
b857640 Document the git stash exercise: list, show, apply, pop, drop
671ddc6 Fix division by zero to report error instead of returning false result
3aaf5ac Add power operation and wire it into the calculator
1e9337e Sync README commit log with actual git history
a1cc5d9 Update commit messages and README content
8dc6f4f Wrap calculator execution in a main function guard
dc6882c Add .gitignore to exclude bytecode, caches, and local files
50ed391 Add README documenting the calculator project
43c059f Add calculator main entry point that runs all operations
4ef7426 Add multiplication and division operations
b705def Add addition and substraction operations
39e87a3 Add readdata module to capture user input
```


> 🔎 Commits 1–21 above are this repository's **actual** `git log --oneline`
> history. GitHub's **Commits** tab shows the same log — click any SHA in the
> table to open its diff, or run `git log --stat` locally to see the per-file
> change counts.
>
> The table deliberately stops short of the tip: a commit **cannot record its
> own SHA**, since amending it to add the SHA would change the SHA again. The
> newest commit — the one that maintains this table — is therefore always
> missing from it. Run `git log --oneline -1` for the current tip.
>
> The hotfix commit is **11** (`671ddc6`). It was originally `621ac5b`; a later
> `git pull --rebase` (see [Step 9](#9️⃣-bringing-it-together--merge-the-hotfix))
> replayed the local commits and rewrote the SHA, which is why the history is
> linear. A rebase rewrites SHAs — read them from `git log`, never transcribe
> them from an old document.
>
> Three commits carry 🏷️ tags so they stay easy to find and cannot be lost when
> branches are deleted:

```bash
git show division-by-zero-fix   # 11 — the hotfix fix, safe
git show main-outage            #  6 — the commit that broke main
git show outage-fix             #  5 — the commit that repaired it
git show hotfix-original        # the pre-rebase original; DO NOT MERGE
```

> See [Where the hotfix branch went](#where-the-hotfix-branch-went) for why the
> `hotfix/division-by-zero` branch points at commit 11 rather than the original.

---

## 🧠 Quick Command Cheat Sheet

| Action              | Git CLI                          | VS Code                                  |
| ------------------- | -------------------------------- | ---------------------------------------- |
| Init repo           | `git init`                       | `Git: Initialize Repository` (Cmd⇧P)     |
| Check status        | `git status`                     | Source Control panel (Cmd⇧G)             |
| Stage a file        | `git add <file>`                 | Click `+` on the file                    |
| Stage everything    | `git add .`                      | Click `+` on "Changes"                   |
| Commit              | `git commit -m "message"`        | Type message → ✔ (Cmd+Enter)             |
| View history        | `git log --oneline`              | Timeline → Git History                   |
| Compare changes     | `git diff`                       | Click a file under "Changes"             |
| Push                | `git push`                       | Sync / Publish Branch button             |
| Ignore a file       | add name to `.gitignore`         | Right-click file → Add to .gitignore     |
| Park work           | `git stash push -u -m "msg"`     | Source Control → ⋯ → Stash All Changes  |
| List stashes        | `git stash list`                 | Source Control → ⋯ → Stash List         |
| Inspect a stash     | `git stash show -p --include-untracked` | —                                  |
| Restore, keep stash | `git stash apply`                | Source Control → ⋯ → Pop / Apply         |
| Restore, drop stash | `git stash pop`                  | Source Control → ⋯ → Pop Stash           |
| Delete a stash      | `git stash drop`                 | —                                        |

### Stash decision in one glance

```
Need to park work and switch branches?  →  git stash push -u -m "why"
What have I parked?                     →  git stash list
What is inside it?                      →  git stash show -p --include-untracked
Want it back but want a safety net?    →  git stash apply      (keeps the entry)
Want it back and committed to?         →  git stash pop        (consumes the entry)
Never want it?                         →  git stash drop       (destroys the entry)
```

---

## 📚 License

Free to use for learning purposes.
