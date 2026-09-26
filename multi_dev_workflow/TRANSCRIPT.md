# Simulation Transcript — Two Developers, One Repository

Every command below was executed for real against
**<https://github.com/bkvs88/git_repo_from_scratch>**. Output is verbatim.

| | |
| :-- | :-- |
| Remote | `https://github.com/bkvs88/git_repo_from_scratch.git` |
| Developer A (owner / reviewer) | this directory, `multi_dev_simulation/` |
| Developer B (contributor) | `multi_dev_simulation/dev_b_clone/` |
| Pull Request | <https://github.com/bkvs88/git_repo_from_scratch/pull/8> |
| Merge commit | `9956659` |
| Review record | [`CODE_REVIEW.md`](CODE_REVIEW.md) |

**Timeline:** A pushes the initial scaffold → B clones → B branches → B pushes →
B opens PR #8 → A reviews (3 blocking comments) → B pushes a fix commit → A
approves → A merges → both developers sync.

---

## Phase 0 — Developer A creates the initial repository

A is the only developer so far, so A works **directly on `main`** and pushes.
No branch and no PR: with one developer there is nobody to review for.

```bash
$ git remote -v
origin	https://github.com/bkvs88/git_repo_from_scratch.git (fetch)
origin	https://github.com/bkvs88/git_repo_from_scratch.git (push)

$ git config user.name "Developer A"
$ git config user.email "dev-a@git-repo-from-scratch.local"

$ git add multi_dev_workflow/README.md
$ git commit -m "docs: add multi-developer Git and GitHub workflow guide"
2143e90 docs: add multi-developer Git and GitHub workflow guide

$ git push origin main
   4ffd134..2143e90  main -> main

$ git status -sb
## main...origin/main
```

`4ffd134..2143e90` is a **fast-forward** (`..`). A push that has to print `...`
instead means `main` moved on the remote and Git refuses until you `git pull`
first.

---

## Phase 1 — Developer B clones the remote

```bash
$ git clone https://github.com/bkvs88/git_repo_from_scratch.git dev_b_clone
Cloning into 'dev_b_clone'...

$ cd dev_b_clone && git remote -v
origin	https://github.com/bkvs88/git_repo_from_scratch.git (fetch)
origin	https://github.com/bkvs88/git_repo_from_scratch.git (push)

$ git log --oneline -3
2143e90 docs: add multi-developer Git and GitHub workflow guide
4ffd134 Restore hotfix branch visibility and tag the incident commits (#7)
b909a58 Remove test suite and CI workflow (#6)
```

B's clone already contains A's `2143e90` commit, and `origin` is configured
automatically — `git clone` is all the setup a new developer needs.

```bash
$ git fetch origin --dry-run && git pull
Already up to date.
```

### Start a feature branch

```bash
$ git switch -c feature/statistics
Switched to a new branch 'feature/statistics'

$ git branch -vv
* feature/statistics 2143e90 docs: add multi-developer Git and GitHub workflow guide
  main               2143e90 [origin/main] docs: add multi-developer Git and GitHub workflow guide
```

B is now isolated from `main`. Anything committed here cannot reach `main`
without going through a Pull Request.

---

## Phase 2 — B implements the feature

```bash
$ python3 -m pytest test_stats.py -q
........                                                                 [100%]
8 passed in 0.01s

$ printf '10\n4\n' | python3 calculator.py
Enter first number :  Enter second number : Data Capture completed
Basic Calculator
Addition of 10 and 4 is : 14
substraction of 10 and 4 is : 6
Division of 10 and 4 is : 2.5
multiplication of 10 and 4 is : 40
Power of 10 raised to 4 is : 10000
Mean of 10 and 4 is : 7.0
Median of 10 and 4 is : 7.0
Minimum of 10 and 4 is : 4
Maximum of 10 and 4 is : 10
```

---

## Phase 3 — B commits and pushes the branch

```bash
$ git status --short
 M calculator.py
?? stats.py
?? test_stats.py

$ git add stats.py test_stats.py calculator.py
$ git commit -m 'Add statistics operations (mean, median, min, max)'

$ git push -u origin feature/statistics
remote:
remote: Create a pull request for 'feature/statistics' on GitHub by visiting:
remote:      https://github.com/bkvs88/git_repo_from_scratch/pull/new/feature/statistics
remote:
To https://github.com/bkvs88/git_repo_from_scratch.git
 * [new branch]      feature/statistics -> feature/statistics
branch 'feature/statistics' set up to track 'origin/feature/statistics'.
```

`git add calculator.py` staged the **modification**; the two new files had to be
named explicitly (`git add .` would also work). `-u` (**--set-upstream**) records
the branch pairing, which is why plain `git push`/`git pull` work from now on:

```bash
$ git branch -vv
* feature/statistics 0ebe9f6 [origin/feature/statistics] Add statistics operations (mean, median, min, max)
  main               2143e90 [origin/main] docs: add multi-developer Git and GitHub workflow guide
```

---

## Phase 4 — B opens the Pull Request

```bash
$ gh pr create --base main --head feature/statistics \
    --title "Add statistics operations (mean, median, min, max)" \
    --body "## What ..."

https://github.com/bkvs88/git_repo_from_scratch/pull/8

$ gh pr view 8 --json head,base,additions,changedFiles,mergeable
{"additions":71,"base":"main","changedFiles":3,"head":"feature/statistics","mergeable":true}
```

Note the `remote:` hint GitHub printed at push time
(`.../pull/new/feature/statistics`) — pushing a branch is often all it takes to
start a PR from the web UI.

---

## Phase 5 — Developer A reviews

Full detail in [`CODE_REVIEW.md`](CODE_REVIEW.md). A reviews **locally first**:

```bash
$ git fetch origin
 * [new branch]      feature/statistics -> origin/feature/statistics

$ git log --oneline main..origin/feature/statistics
0ebe9f6 Add statistics operations (mean, median, min, max)

$ git diff --stat main...origin/feature/statistics
 calculator.py |  5 +++++
 stats.py      | 22 ++++++++++++++++++++++
 test_stats.py | 44 +++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 71 insertions(+)
```

`git fetch` created `origin/feature/statistics` locally, so A can diff the
contributor's work **without checking it out**. The **three-dot** form
(`main...feature`) diffs from the *merge base* — only the changes this branch
introduces. Two dots would also show everything that landed on `main` in the
meantime, which is noise when reviewing someone else's work.

Then A leaves three **inline** comments on the exact lines, via the API:

```bash
$ gh api -X POST repos/bkvs88/git_repo_from_scratch/pulls/8/comments \
    -f body='median is byte-for-byte the same computation as mean...' \
    -f commit_id=0ebe9f6... -f path=stats.py -F line=7 -f side=RIGHT
stats.py:7     -> .../pull/8#discussion_r4112044072
test_stats.py:27 -> .../pull/8#discussion_r4112044130
test_stats.py:22 -> .../pull/8#discussion_r4112044197
```

and submits the review verdict:

```bash
$ gh pr review 8 --request-changes --body '...'
failed to create review: GraphQL: Review Can not request changes on your own pull request
```

Both roles share the single `bkvs88` token, and GitHub refuses to let an author
change-request or approve their own PR. A therefore records the verdict in a
`--comment` review. In a real two-account setup this is a `CHANGES_REQUESTED`
review, and a branch protection rule on `main` would make the gate enforceable.

---

## Phase 6 — B pushes a fix commit to the same branch

```bash
$ python3 -m pytest -q
..........                                                               [100%]
10 passed in 0.01s

$ git status --short
 M stats.py
 M test_stats.py
?? test_division.py

$ git add -A && git commit -m 'Address review comments on #8'

$ git push
To https://github.com/bkvs88/git_repo_from_scratch.git
   0ebe9f6..e0ea73f  feature/statistics -> feature/statistics
```

No new branch, no new PR, no force-push — a plain forward push to the same
branch. **This is why Pull Requests are safe to review iteratively**: the diff on
the PR updates automatically.

---

## Phase 7 — A verifies, approves, and merges

A checks out the branch in a **scratch worktree** and runs the tests before
approving — the reviewer does not take the author's word for it:

```bash
$ git fetch origin
   0ebe9f6..e0ea73f  feature/statistics -> origin/feature/statistics

$ git log --oneline main..origin/feature/statistics
e0ea73f Address review comments on #8
0ebe9f6 Add statistics operations (mean, median, min, max)

$ git worktree add --detach <tmp> origin/feature/statistics
$ cd <tmp> && python3 -m pytest -q
..........                                                               [100%]
10 passed in 0.01s
```

`git worktree` checks out a second branch in a second directory while staying on
the current one — the reviewer's version of `gh pr checkout`, but it works for
any branch, not just an open PR.

```bash
$ gh pr review 8 --comment --body 'Re-reviewed e0ea73f. All three items are addressed... **APPROVED**'

$ gh pr merge 8 --merge --delete-branch

$ gh pr view 8 --json state,mergedAt,mergeCommit
state=MERGED  mergedAt=2026-09-26T16:50:26Z  mergeCommit=9956659
```

`--merge` keeps both feature commits visible on `main`; `--delete-branch` cleans
up `feature/statistics` on the remote in the same step.

---

## Phase 8 — Both developers sync

**A** pulls the merge:

```bash
$ git pull --rebase
   2143e90..9956659  main     -> origin/main
Updating 2143e90..9956659
Fast-forward
 calculator.py    |  5 +++++
 stats.py         | 35 +++++++++++++++++++++++++++++++++++
 test_division.py |  9 +++++++++
 test_stats.py    | 42 ++++++++++++++++++++++++++++++++++++++++++
 4 files changed, 91 insertions(+)
 create mode 100644 stats.py
 create mode 100644 test_division.py
 create mode 100644 test_stats.py
```

**B** fetches, discovers the remote branch is gone, and syncs `main`:

```bash
$ git fetch --prune
From https://github.com/bkvs88/git_repo_from_scratch
 - [deleted]         (none)     -> origin/feature/statistics
   2143e90..9956659  main       -> origin/main

$ git status -sb        # B is still on the deleted feature branch
## feature/statistics...origin/feature/statistics [gone]

$ git switch main && git pull --rebase
Switched to branch 'main'
Your branch is behind 'origin/main' by 3 commits, and can be fast-forwarded.
```

`[gone]` is Git reporting that the upstream branch was deleted.
`git fetch --prune` removes the stale `origin/feature/statistics` entry — without
it, the ghost branch lingers in `git branch -a` forever.

"Behind by **3** commits" is B's two feature commits plus the merge commit. That
is why B must pull *after* merging: the merge is not in B's local `main` yet.

```bash
$ git branch -a
  feature/statistics
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/hotfix/division-by-zero
  remotes/origin/main

$ python3 -m pytest -q
..........                                                               [100%]
10 passed in 0.01s

$ git branch -d feature/statistics    # safe delete: already merged
Deleted branch feature/statistics (was e0ea73f).
```

`git branch -d` (lowercase) only deletes a branch Git can prove is merged — a
safety net. `-D` skips that check.

### The result, end to end

```bash
$ git log --oneline --graph --decorate -6
*   9956659 (HEAD -> main, origin/main, origin/HEAD) Merge pull request #8 from bkvs88/feature/statistics
|\
| * e0ea73f Address review comments on #8
| * 0ebe9f6 Add statistics operations (mean, median, min, max)
|/
* 2143e90 docs: add multi-developer Git and GitHub workflow guide
* 4ffd134 Restore hotfix branch visibility and tag the incident commits (#7)
* b909a58 Remove test suite and CI workflow (#6)
```

The `|\` / `|/` shape is a **merge commit**: the two feature commits remain
visible as their own line of work, and the merge commit ties them into `main`.
That is what `--merge` (the default) buys you, and what `--squash` would have
flattened into one commit.

A's `main` and B's `main` now point at the same commit `9956659`, from two
different working directories, with the feature's history fully traceable.

---

## Phase 9 — The same flow on the GitHub web UI

| CLI | Web UI |
| :--- | :--- |
| `gh pr create` | **Pull requests → New pull request** |
| `gh pr view 8` | open the PR page |
| `gh pr diff 8` | **Files changed** tab |
| `gh pr review 8 --comment` | the **Review** box under **Conversation** |
| inline comment | hover the `+` next to a line in **Files changed** |
| `gh pr merge 8 --merge` | the green **Merge pull request** button |

---

## Reproducing this from scratch

```bash
# Developer A — the owner
git clone https://github.com/bkvs88/git_repo_from_scratch.git
cd git_repo_from_scratch
git config user.name "Developer A" && git config user.email "you@example.com"
# ... edit on main ...
git add -A && git commit -m "your change"
git push origin main

# Developer B — the contributor
git clone https://github.com/bkvs88/git_repo_from_scratch.git
cd git_repo_from_scratch
git switch -c feature/my-work
# ... edit, test ...
python3 -m pytest -q
git add -A && git commit -m "implement my feature"
git push -u origin feature/my-work
gh pr create --base main --head feature/my-work --title "..." --body "..."

# Developer A — review and merge
git fetch origin
git diff main...origin/feature/my-work
gh pr review <n> --request-changes --body "..."   # or --approve
gh pr merge <n> --merge --delete-branch
```
