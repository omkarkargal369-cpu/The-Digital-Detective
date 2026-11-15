# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Learn basic terminal commands, do file practice in a folder, check flags and pipes, and check the package manager.

## 2. Work completed
- Ran commands: `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, and `cat`.
- Created `terminal-practice` folder, tested `>` vs `>>`, and made a backup file.
- Tested `ls -lah` and piped it into `head -n 5`.
- Checked Homebrew.

## 3. Commands / tools used
- `pwd`: Print current working directory.
- `ls`: List files.
- `cd`: Change directory.
- `mkdir`: Make folder.
- `touch`: Make an empty file.
- `cp`: Copy a file.
- `mv`: Rename or move a file.
- `cat`: Print file contents to terminal.
- `head`: Show first few lines.
- `|`: Pipe output from one command to another.
- `brew`: Homebrew package manager.

## 4. My understanding

### Task 2.1 — Terminal Operations
- `pwd`: Prints where you are right now. Observed: `/Users/[redacted]/digital-detective-8416`.
- `ls`: Lists files. Observed: Showed all folders and files in current folder.
- `ls -l`: Lists details. Observed: Showed permissions, size, and dates.
- `cd ..`: Goes up one folder. Observed: Moved to parent directory.
- `mkdir`: Makes folder. Observed: Made `terminal-practice`.
- `touch`: Makes empty file. Observed: Made `practice.txt`.
- `cp`: Copies file. Observed: Made a copy named `practice_backup.txt`.
- `mv`: Renames file. Observed: Renamed backup to `practice_backup_renamed.txt`.
- `cat`: Shows file content. Observed: Printed the lines inside `practice.txt`.

### Task 2.2 — File Practice Questions
- `>` vs `>>`:
  - `>` replaces the whole file with new text.
  - `>>` appends new text at the end without deleting anything.
- Copy vs move:
  - Copy makes a duplicate so you have two files.
  - Move just moves or renames it, so you still have one file.
- What does `pwd` show:
  - The full path to your current location.
- Why is `ls` useful:
  - So you can see what files exist in the folder.

### Task 2.3 — Flags and Pipes
- `ls -lah`: `-l` gives a detailed list, `-a` includes hidden files, and `-h` makes file sizes easy to read (like KB/MB).
- `ls -la | head -n 5`: The pipe `|` sends the output of `ls` to `head`, so only the first 5 lines get printed.

### Task 2.4 — Package Managers
- Homebrew version: `Homebrew 7.0.7`
- Packages: `git`, `gettext`, etc.
- Why useful: It lets you install and update terminal tools with one command instead of downloading installers from the web.

## 5. Difficulties faced
Had to remember to use `>>` instead of `>` so I didn't overwrite my text.

## 6. How I resolved them
Used `>>` to append the second line safely.

## 7. Evidence / files
- `terminal-practice/practice.txt`
- `terminal-practice/practice_backup_renamed.txt`
- `mission-02-terminal/README.md`

## 8. Commit details
- Commit message: "Complete Terminal and file management mission"
- Pushed to main.
