# Code Review Record — PR #8

**PR:** <https://github.com/bkvs88/git_repo_from_scratch/pull/8>
**Title:** Add statistics operations (mean, median, min, max)
**Author:** Developer B · `dev-b@git-repo-from-scratch.local`
**Reviewer:** Developer A · `dev-a@git-repo-from-scratch.local`
**Result:** 2 review rounds → 3 blocking comments → all resolved → **APPROVED** → merged as `9956659`

---

## What the PR changed

| File | Change |
| :--- | :--- |
| `stats.py` | **new** — `mean`, `median`, `minimum`, `maximum` |
| `test_stats.py` | **new** — pytest coverage for the four operations |
| `test_division.py` | **new** (round 2) — division happy path + divide-by-zero |
| `calculator.py` | +5 lines — import and call the four new operations |

`+91 / -0` across 4 files, 2 commits.

---

## Round 1 — Review

Developer A first reviewed the change **locally**, before reading the PR on
GitHub — the fast feedback loop:

```bash
git fetch origin
git log --oneline main..origin/feature/statistics     # 0ebe9f6 Add statistics operations
git diff --stat main...origin/feature/statistics
#  calculator.py |  5 +++++
#  stats.py      | 22 ++++++++++++++++++++++
#  test_stats.py | 44 ++++++++++++++++++++++++++++++++++++++++++++
git diff main...origin/feature/statistics             # the three-dot form: what THIS branch adds
```

> **Why three dots?** `git diff A...B` shows the diff from the *merge base* of
> `A` and `B` to `B` — i.e. only the changes this branch introduces. `git diff A B`
> would also show every change that landed on `A` in the meantime, which is
> noise when you are reviewing someone else's work.

### Inline comments left on the diff

| # | Location | Comment | Verdict |
| :-- | :--- | :--- | :-- |
| 1 | [`stats.py:7`](https://github.com/bkvs88/git_repo_from_scratch/pull/8#discussion_r4112044072) | `median` is byte-for-byte the same computation as `mean`. A reader cannot tell that is intentional — document the equivalence or drop one of them. | blocking (doc) |
| 2 | [`test_stats.py:27`](https://github.com/bkvs88/git_repo_from_scratch/pull/8#discussion_r4112044130) | The `div(5, 0)` test exercises `division.py`, not `stats.py`. A failure here would send a future debugger to the wrong module — move it to `test_division.py`. | blocking |
| 3 | [`test_stats.py:22`](https://github.com/bkvs88/git_repo_from_scratch/pull/8#discussion_r4112044197) | Coverage gap: `mean`/`median` are only asserted with positive, unequal inputs. `(a + b) / 2` is exactly where a sign error would hide. | blocking |

### Verdict: REQUESTING CHANGES

> Thanks @dev-b — the feature itself is sound and `calculator.py` is wired up
> correctly. Three small things before this lands (details in my inline comments):
>
> 1. Document that `median` is identical to `mean` for two inputs.
> 2. Move the `div(5, 0)` test out of `test_stats.py` into `test_division.py`.
> 3. Add a mixed-sign / negative test for `mean` and `median`.
>
> One process note: this repo previously dropped its test suite (see #4, #5, #6).
> Reintroducing tests is welcome — I just want the `test_*.py` files at the repo
> root, matching the flat layout of the existing modules, rather than a new
> `tests/` package.
>
> **Verdict: REQUESTING CHANGES** (items 1-3, all in the same branch). Push once
> more and I'll re-review.

---

## Round 2 — Author responds, reviewer verifies

Developer B pushed `e0ea73f` **to the same branch** — no new PR, no force-push:

```bash
git add -A
git commit -m "Address review comments on #8"
git push            # 0ebe9f6..e0ea73f  feature/statistics -> feature/statistics
```

Developer A re-reviewed and, this time, **ran the contributor's code** before
approving — using a throwaway worktree so the reviewer's own `main` stayed clean:

```bash
git fetch origin
git log --oneline main..origin/feature/statistics
#   e0ea73f Address review comments on #8
#   0ebe9f6 Add statistics operations (mean, median, min, max)

git worktree add --detach <tmp> origin/feature/statistics
cd <tmp> && python3 -m pytest -q
#  ..........  [100%]
#  10 passed in 0.01s
```

> **`git worktree`** lets you check out a second branch in a second directory
> while staying on your current one. It is the reviewer's equivalent of
> `gh pr checkout` — but it works for any branch, not just an open PR, and it
> does not need to change your current branch.

| Comment | Resolution in `e0ea73f` | Status |
| :--- | :--- | :-- |
| 1 | `median` gained a docstring and now `return mean(a, b)` — the equivalence is explicit in code | ✅ |
| 2 | `test_division.py` created with the divide-by-zero test **and** a happy-path test | ✅ |
| 3 | `test_operations_handle_negatives` / `..._reversed` cover mixed signs; `test_equal_values` covers `(0,0)`, `(7,7)`, `(-4,-4)` | ✅ |
| — | `pytest.mark.parametrize` replaced with a plain loop — `pytest` import no longer needed | ✅ (drive-by) |

### Verdict: APPROVED → merged

```bash
gh pr merge 8 --merge --delete-branch
# state=MERGED  mergeCommit=9956659
```

---

## Post-merge verification (both developers)

```bash
# A
$ git pull --rebase
Fast-forward  2143e90..9956659  main
$ python3 -m pytest test_stats.py test_division.py -q
10 passed

# B
$ git fetch --prune
 - [deleted]  (none) -> origin/feature/statistics     # branch deleted by the merge
$ git switch main && git pull --rebase
Your branch was behind 'origin/main' by 3 commits
$ python3 -m pytest -q
10 passed
$ git branch -d feature/statistics
Deleted branch feature/statistics (was e0ea73f).
```

---

## Final history on `main`

```bash
$ git log --oneline --graph --decorate -6
*   9956659 (HEAD -> main, origin/main) Merge pull request #8 from bkvs88/feature/statistics
|\
| * e0ea73f Address review comments on #8
| * 0ebe9f6 Add statistics operations (mean, median, min, max)
|/
* 2143e90 docs: add multi-developer Git and GitHub workflow guide
* 4ffd134 Restore hotfix branch visibility and tag the incident commits (#7)
* b909a58 Remove test suite and CI workflow (#6)
```

The `|\` / `|/` shape is a **merge commit**: the two feature commits stay visible
as their own line of work, and the merge commit ties them into `main`. That is
what `--merge` (the default) buys you, and what a `--squash` merge would have
flattened into a single commit.

---

## Two honest caveats about this run

1. **One GitHub account, two roles.** Both roles ran through the `bkvs88` token,
   so the GitHub API refused `gh pr review --request-changes` and `--approve` on
   A's own PR (*"Review Can not request changes on your own pull request"*). The
   review verdicts are therefore stated explicitly in the review bodies, and the
   inline comments are real. With two real accounts these would be
   `CHANGES_REQUESTED` and `APPROVED` states, and `main` would need a branch
   protection rule to *enforce* the gate.
2. **`median` prints twice.** Because `median()` delegates to `mean()`, running
   the calculator prints `Mean of ...` for both calls:

   ```
   Mean of 10 and 4 is : 7.0
   Mean of 10 and 4 is : 7.0     <- this line is median()
   ```

   Correct, but confusing for a first-time reader. The proper fix is to separate
   the calculation from the printing, e.g. `stats.py` returning values and
   `calculator.py` doing the `print()` — worth a follow-up issue rather than
   holding up this PR.
