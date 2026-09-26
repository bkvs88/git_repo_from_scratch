# Git From Scratch — Python Calculator

A tiny Python calculator project used to demonstrate the **Git basics**:
`git init`, `git status`, `git add`, `git commit`, `git log`, `git diff`,
and `.gitignore` — with **both Git CLI and VS Code Source Control** options.

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
| `division.py`     | Defines `div(a, b)` — returns `a / b`.              |
| `calculator.py`   | Entry point — calls all four operations.            |
| `.gitignore`      | Tells Git which files to **never track**.           |

Run it with:

```bash
python calculator.py
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

> 📌 This repo was built with **5 meaningful commits** (see below).

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

## 📝 The 5 Meaningful Commits

| #   | Commit message                                            | Files added                          |
| --- | --------------------------------------------------------- | ------------------------------------ |
| 1   | `Add readdata module to capture user input`           | `readdata.py`             |
| 2   | `Add addition and substraction operations`                | `addition.py`, `substraction.py`      |
| 3   | `Add multiplication and division operations`               | `multiplication.py`, `division.py`     |
| 4   | `Add calculator main entry point that runs all operations`                | `calculator.py`     |
| 5   | `Add README documenting the calculator project`   | `README.md`                   |
| 6|`Add .gitignore to exclude bytecode, caches, and local files`|`.gitignore` 


Verify them yourself:

```bash
git log --oneline
```

```
Add calculator entry point that runs all operations
Add multiplication and division modules
Add addition and subtraction modules
Add readdata module to accept two numbers
Initial commit: project README and .gitignore
```

> 🔎 This is this repository's **actual** `git log --oneline` history (GitHub's
> **Commits** tab shows the same five commits).

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

---

## 📚 License

Free to use for learning purposes.
