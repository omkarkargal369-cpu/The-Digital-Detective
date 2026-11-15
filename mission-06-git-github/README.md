# Mission 6 — Git and GitHub

## 1. Task / objective
Understand Git commands, make a branch called `update-about`, update the root README, and learn about Pull Requests.

## 2. Work completed
- Checked basic Git workflow (`status`, `add`, `commit`, `log`).
- Created branch `update-about` and added "My Learning" to the root README.
- Committed and pushed `update-about` to GitHub.
- Merged the branch into `main` and pushed.
- Wrote down a short Git glossary.

## 3. Commands / tools used
- `git status`: Check changed files.
- `git add`: Stage changes.
- `git commit`: Save a commit snapshot.
- `git log --oneline`: View commit history.
- `git checkout -b update-about`: Make and switch to new branch.
- `git push -u origin update-about`: Push branch to GitHub.
- `git checkout main` and `git merge update-about`: Merge branch to main.

## 4. My understanding

### Task 6.1 — Git Workflow
- `git status`: Shows what files were modified or untracked.
- `git add`: Stages files ready for commit.
- `git commit`: Saves staged files with a message.
- `git log`: Shows past commits.

Difference between staging and committing:
Staging (`git add`) is picking which files you want in the snapshot. Committing (`git commit`) actually saves that snapshot to history.

### Task 6.2 & 6.3 — Branches and Pull Requests
- Branch: A separate line of work so you can change files without messing up the main code.
- Pull Request: Asking to merge changes from your branch into main so others can review it.
- Why useful: Let's multiple people work on different parts at the same time without overwriting each other.
- Status: Created `update-about` branch, pushed to GitHub, and merged into `main`.

### Task 6.4 — Git Glossary
- `git init`: Starts a new local repo.
- `git status`: Shows current file status.
- `git add`: Stages files for commit.
- `git commit`: Saves a snapshot to history.
- `git log`: Shows list of past commits.
- `git branch`: Lists or makes branches.
- `git switch` (or `checkout`): Moves to another branch.
- `git push`: Uploads local commits to GitHub.
- `git pull`: Downloads newest commits from GitHub.

## 5. Difficulties faced
No difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- Root `README.md`
- Branch `update-about`
- `mission-06-git-github/README.md`

## 8. Commit details
- Commit message: "Complete Git and GitHub collaboration mission"
- Pushed to main.
