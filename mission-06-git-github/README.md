# Mission 6 — Git and GitHub

## 1. Task / objective
Understand how Git tracks files, create a separate branch called `update-about`, update the root README with what I learned, push the branch, understand Pull Requests, and write a quick Git glossary.

## 2. Work completed
- Explored basic Git actions like status, add, commit, and log.
- Created and switched to the `update-about` branch.
- Added the "## My Learning" section to the root `README.md`.
- Committed and pushed `update-about` branch to GitHub.
- Merged the branch changes into `main` and pushed.
- Wrote down one-line definitions for all major Git commands.
- Formatted everything with clean bullets, zero tables.

## 3. Commands / tools used
- `git status` - check which files changed.
- `git add README.md` - staged the modified README.
- `git commit -m "..."` - made commits with clear messages.
- `git log --oneline` - checked past commit history.
- `git checkout -b update-about` - created and switched to the new branch.
- `git push -u origin update-about` - pushed the branch to GitHub.
- `git checkout main` & `git merge update-about` - brought branch changes into main.
- `git push origin main` - pushed merged main to remote.

## 4. My understanding

### Task 6.1 — Basic Git Workflow
- Checking repo status (`git status`):
  - Shows you what files you edited, what's new (untracked), and what's staged for commit.
- Staging selected changes (`git add`):
  - Tells Git which specific edited files you want to include in the next snapshot.
- Creating a commit (`git commit`):
  - Saves a permanent snapshot of everything you staged along with a message explaining what you did.
- Viewing commit history (`git log --oneline`):
  - Prints a compact list of previous commits with their short hashes and messages.

Difference between staging and committing:
Staging (`git add`) is like putting items into a cardboard box before sealing it. You can add more things or take things out. Committing (`git commit`) is taping the box shut and stamping a tracking label on it so it's permanently saved in history.

---

### Task 6.2 & 6.3 — Branches and Pull Requests
- Branch created: `update-about`
- What a branch is:
  A branch is basically a separate working copy of your code. You can make changes and experiment without worrying about breaking the working `main` branch.
- What a Pull Request (PR) is:
  A PR is a request on GitHub asking the team (or yourself) to review changes from your branch and merge them into `main`.
- Why they are useful in teamwork:
  If 5 people are working on the same project, everyone works on their own branch. Nobody messes up `main`, bugs get caught during PR reviews, and everyone's code gets merged cleanly.
- Status: The `update-about` branch was pushed to GitHub and merged into `main`.

---

### Task 6.4 — Git Command Glossary
- `git init`: Starts a brand new local Git repo inside the current folder.
- `git status`: Shows which files are modified, staged, or untracked.
- `git add`: Stages changed files so Git knows to include them in the next commit.
- `git commit`: Saves a permanent snapshot of all staged files with a description.
- `git log`: Prints the history of all previous commits made in the repo.
- `git branch`: Lists all local branches or creates a new one if given a name.
- `git switch` (or `git checkout`): Moves your working directory from one branch to another.
- `git push`: Sends your local commits up to the remote repository on GitHub.
- `git pull`: Downloads the latest changes from GitHub and merges them into your local branch.

## 5. Difficulties faced
No real issues. Just had to make sure I was on `update-about` before editing the README and switching back to `main` afterwards.

## 6. How I resolved them
Used `git branch` and `git status` often to keep track of which branch was active.

## 7. Evidence / files
- Root `README.md` updated with "## My Learning"
- Branch `update-about` created and pushed to GitHub
- `mission-06-git-github/README.md`

## 8. Commit details
- Branch commit: "Add My Learning section to root README" on `update-about`
- Mission commit: "Complete Git and GitHub collaboration mission" on `main`
- Both pushed to GitHub.
