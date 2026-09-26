# Multi-Developer Git & GitHub Workflow

A hands-on guide to collaborating on a shared repository: **clone → remote → fetch →
pull → push → branch → Pull Request → code review → merge**.

Every command in this document was actually executed against
**<https://github.com/bkvs88/git_repo_from_scratch>** while producing this guide.
The real transcript of that run lives in [`TRANSCRIPT.md`](TRANSCRIPT.md).

---

## 📖 The Scenario

| Actor | Role | Working copy |
| :--- | :--- | :--- |
| **Developer A** | Repository owner. Creates the project, reviews and merges contributions. | this directory (`multi_dev_simulation/`) |
| **Developer B** | Contributor. Clones the project, builds features on a branch, opens a PR. | `dev_b_clone/` |

The Python code in the project root (`addition.py`, `calculator.py`, `division.py`,
`multiplication.py`, `power.py`, `readdata.py`, `substraction.py`) is the shared
application both developers work on.

---

## 1️⃣ The Remote Repository

A **remote** is a named bookmark for a URL that lives *outside* your computer
(GitHub, GitLab, a self-hosted server). The default name is `origin`.

```bash
git remote -v
```

Typical output:

```
origin  https://github.com/bkvs88/git_repo_from_scratch.git (fetch)
origin  https://github.com/bkvs88/git_repo_from_scratch.git (push)
```

* `(fetch)` is the URL used by `git fetch` / `git pull` to **download** work.
* `(push)` is the URL used by `git push` to **upload** your work.

### Common remote commands

```bash
git remote                                   # list remote names
git remote -v                                # list remotes with URLs
git remote add origin <url>                  # add a new remote
git remote rename origin upstream            # rename a remote
git remote set-url origin <url>              # change a remote's URL
git remote remove <name>                     # delete a remote
```

> 💡 A repository can have several remotes — e.g. `origin` (your fork) and
> `upstream` (the original project) when you contribute to code you don't own.

---

## 2️⃣ Clone — Getting the Code

`git clone` does three things at once: it **downloads** the repository, it
**creates** a local directory with a full `.git` history, and it **automatically
adds a remote** called `origin` pointing at the URL you cloned from.

```bash
git clone https://github.com/bkvs88/git_repo_from_scratch.git
```

Developer B's exact command in this simulation:

```bash
git clone https://github.com/bkvs88/git_repo_from_scratch.git dev_b_clone
```

### Useful clone variants

```bash
git clone <url>                              # into a folder named after the repo
git clone <url> my-folder                    # into a folder you choose
git clone --branch feature/login <url>       # check out a specific branch
git clone --depth 1 <url>                    # shallow clone (fastest, no history)
git clone --recurse-submodules <url>         # also fetch git submodules
```

Verify the clone:

```bash
cd dev_b_clone
git remote -v          # origin already configured for you
git log --oneline -5   # the full shared history
```

---

## 3️⃣ Fetch vs Pull

Both commands **download** changes, but they differ in what they do afterwards.

| | `git fetch` | `git pull` |
| :--- | :--- | :--- |
| Downloads new commits | ✅ | ✅ |
| Updates your local branches | ✅ | ✅ |
| Merges into your current branch | ❌ | ✅ |
| Can lose uncommitted work | Never | Yes (via the merge) |
| Use when | You want to *look* before deciding | You are ready to *use* the update |

**`git pull` is literally `git fetch` + `git merge` (or `git rebase`).**

```bash
# Safe: download and inspect, change nothing in your working tree
git fetch origin
git log --oneline HEAD..origin/main    # what am I missing?
git diff main origin/main              # how does it differ?

# Ready: download and integrate in one step
git pull                              # fetch + merge origin/main into main
git pull --rebase                     # fetch + replay my commits on top (linear history)
git pull --rebase origin feature/xyz  # update a feature branch from its remote
```

If you prefer to review first, the safe pattern is:

```bash
git fetch origin
git diff main origin/main   # inspect
git merge origin/main       # integrate only when happy
```

---

## 4️⃣ Push — Sharing Your Work

`git push` uploads commits from your machine to the remote.

```bash
git push                          # push the current branch to its upstream
git push -u origin feature/stats  # first push: also SET the upstream (tracking) link
git push --force-with-lease       # rewrite your branch — SAFER than --force
git push origin main              # push local main to remote main explicitly
git push --all                    # push every branch you have
```

* The `-u` / `--set-upstream` flag is what lets plain `git push` and plain
  `git pull` work afterwards without typing the branch name.
* Prefer `--force-with-lease` over `--force`; it refuses to overwrite work you
  have not seen.

---

## 5️⃣ Branch Workflow

Branches let several people work in parallel without stepping on each other.
The long-lived branch is `main`; short-lived `feature/*` branches carry the work
until it is reviewed and merged.

```bash
git branch                          # list local branches (* = current)
git branch -a                       # list local AND remote-tracking branches
git branch -r                       # list remote branches only
git switch -c feature/statistics    # create a branch and move into it
git switch main                     # move back to main
git switch -                        # jump to the previous branch
git branch -d feature/statistics    # delete a merged branch (safe)
git branch -D feature/statistics    # force-delete (even if unmerged)
git push origin --delete feature/statistics   # delete the branch on the remote
```

### The daily loop for a contributor

```bash
git switch main            # start from the latest main
git pull                   # bring in teammates' merged work
git switch -c feature/x    # branch off — work in isolation
#   ... edit, test ...
git add .
git commit -m "Add feature x"
git push -u origin feature/x
#   ... open a Pull Request, get it reviewed ...
git switch main
git pull                   # get the merged result
git branch -d feature/x    # tidy up
```

> 🔀 Never develop directly on `main` once more than one person is pushing. A
> branch is a safe, disposable label on a line of work.

---

## 6️⃣ Pull Request (PR)

A **Pull Request** is a request to merge one branch into another. It carries the
code diff, a discussion thread, CI results and the approval gate.

```bash
# List PRs
gh pr list
gh pr list --state merged

# Create one (head branch -> base branch)
gh pr create --base main --head feature/statistics \
  --title "Add statistics operations" \
  --body "Adds mean/median/min/max and wires them into calculator.py."

# Inspect
gh pr view 8
gh pr diff 8
gh pr checkout 8        # check the PR out locally
```

The same PR can be created from the GitHub web UI: **Pull requests → New pull
request**. Reviewers are assigned there.

---

## 7️⃣ Code Review

Review is where the *quality* of the merge is decided. GitHub makes it explicit
and auditable — nothing merges without a human deciding it should.

**Reviewing locally first** (fast, no network needed):

```bash
git fetch origin
git diff main...origin/feature/statistics     # three-dot = changes introduced
git log --oneline main..origin/feature/statistics
```

**Reviewing on GitHub** (leave feedback, approve, or request changes):

```bash
gh pr review 8 --comment  --body "Looks good; one naming nit."
gh pr review 8 --approve --body "Approved: tests cover the new paths."
gh pr review 8 --request-changes --body "Please add a test for division by zero."
gh pr view 8 --comments
```

A good review checks: correctness, tests, naming/style consistency with the
existing code, backwards compatibility, and whether the change is focused.

Inline (line-level) comments are posted from the **Files changed** tab of the PR
on GitHub, or with `gh api`.

---

## 8️⃣ Merge

Once approved, merge the PR into `main`.

```bash
gh pr merge 8 --merge      # merge commit  (default) — keeps full history
gh pr merge 8 --squash    # squash        — one tidy commit on main
gh pr merge 8 --rebase    # rebase        — replay commits, no merge commit
gh pr merge 8 --merge --delete-branch   # merge and clean up the branch
```

Locally, without GitHub:

```bash
git switch main
git pull
git merge --no-ff feature/statistics   # --no-ff keeps a merge commit
git push origin main
```

### Merge strategies

| Strategy | Result on `main` | Use when |
| :--- | :--- | :--- |
| `--merge` (merge commit) | All commits + one merge commit | Default; preserves how the work actually happened |
| `--squash` | One single commit | Chore/typo/branch-cleanup PRs |
| `--rebase` | Commits replayed linearly | Long-lived branches, to avoid repeated merges of main |

### Resolving a merge conflict

```bash
git merge feature/statistics
# CONFLICT (content): Merge conflict in calculator.py
git status                       # see which files conflicted
# edit the file: keep <<<<<<< / ======= / >>>>>>> markers out of the final text
git add calculator.py
git commit          # finish the merge
```

```bash
# During a rebase
git rebase --continue
git rebase --abort        # give up and restore the original state
```

After a merge, everyone syncs:

```bash
git fetch origin
git pull --rebase origin main
git branch -d feature/statistics   # delete the now-merged local branch
git push origin --delete feature/statistics   # delete it on the remote too
```

---

## 🔁 End-to-End Cheat Sheet

| Goal | Command |
| :--- | :--- |
| Get the code | `git clone <url>` |
| See remotes | `git remote -v` |
| Download only | `git fetch origin` |
| Download + integrate | `git pull --rebase` |
| Upload | `git push -u origin <branch>` |
| New branch | `git switch -c feature/x` |
| Open a PR | `gh pr create --base main --head feature/x --title "..." --body "..."` |
| Review a PR | `gh pr view <n>` / `gh pr review <n> --approve` |
| Merge a PR | `gh pr merge <n> --merge --delete-branch` |
| Read history | `git log --oneline --graph --all --decorate` |
| See what changed | `git diff main...feature/x` |
| Undo a local commit | `git reset --soft HEAD~1` |
| Stash WIP | `git stash push -m "wip"` / `git stash pop` |

---

## 🧭 Cheat Sheet: `gh` CLI

```bash
gh repo clone <owner>/<repo>       # clone
gh repo view --web                # open the repo in the browser
gh pr create | list | view | diff | review | merge | checkout
gh pr ready <n>                   # mark a draft PR ready for review
gh pr revert <n>                  # revert a merged PR
gh api repos/<owner>/<repo>       # anything the CLI does not wrap
gh auth status                    # confirm you are logged in
```

---

## ⚠️ Common Mistakes

| Symptom | Cause | Fix |
| :--- | :--- | :--- |
| `fatal: not a git repository` | No `.git` here | `cd` into the project, or `git clone` it |
| `Permission denied (publickey)` | SSH key not registered | `ssh-keygen` + add the key in GitHub → Settings → SSH keys |
| `rejected ... non-fast-forward` | Remote has commits you don't | `git pull --rebase` then `git push` |
| `Your branch is behind 'origin/main'` | Teammates merged work | `git pull` |
| `fatal: refusing to merge unrelated histories` | Cloning into a non-empty folder | `git pull origin main --allow-unrelated-histories` |
| `error: failed to push some refs` (hint: verify) | Pre-push hook rejected the commit | Fix the hook's complaint, then push again |
| Diverged `main` | Someone force-pushed or rebased `main` | `git pull --rebase` and re-run your tests |
