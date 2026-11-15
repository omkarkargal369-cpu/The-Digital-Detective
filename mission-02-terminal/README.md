# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Try out basic terminal commands, do safe file operations inside a practice folder, test out flags and pipes, and check out the package manager.

## 2. Work completed
- Ran commands like `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, and `cat`.
- Made a `terminal-practice` folder and tested `>` vs `>>` so I don't accidentally overwrite files.
- Tried out `ls -lah` and piped it into `head -n 5`.
- Checked Homebrew version and installed packages.
- Wrote down all observations below with zero tables.

## 3. Commands / tools used
- `pwd` - print current folder path
- `ls` and `ls -l` - list files normally and in detailed view
- `cd` - change directory
- `mkdir` - make new directory
- `touch` - make empty file
- `cp` - copy file
- `mv` - move or rename file
- `cat` - print file content on screen
- `head` - view just the top few lines
- `|` (pipe) - send output of one command into another
- `brew` - package manager for mac

## 4. My understanding

### Task 2.1 — Basic Terminal Operations
- `pwd` (Current-directory display):
  - What it does: Shows where you are right now in terminal.
  - What I observed: Printed `/Users/[redacted]/digital-detective-8416`.
- `ls` (Directory listing):
  - What it does: Shows all files and folders in the current spot.
  - What I observed: Showed README.md, evidence, and mission folders.
- `ls -l` (Detailed listing):
  - What it does: Shows file permissions, file size, owner, and modified date.
  - What I observed: Printed long lines starting with `-rw-r--r--`.
- `cd ..` (Change directory):
  - What it does: Moves one step up to the parent folder.
  - What I observed: Moved from repo up to my home directory, then typed `cd digital-detective-8416` to get back.
- `mkdir terminal-practice` (Create directory):
  - What it does: Makes a new folder.
  - What I observed: Created the new `terminal-practice` folder without any fuss.
- `touch practice.txt` (Create empty file):
  - What it does: Creates an empty text file or updates timestamps.
  - What I observed: Made a 0-byte file named `practice.txt`.
- `cp practice.txt practice_backup.txt` (Copy file):
  - What it does: Makes an exact duplicate copy of a file.
  - What I observed: Now had two separate files with the same content.
- `mv practice_backup.txt practice_backup_renamed.txt` (Move / rename file):
  - What it does: Renames the file or moves it to a new location.
  - What I observed: The old name disappeared and the new name showed up.
- `cat practice.txt` (Display file contents):
  - What it does: Dumps the contents of the file right onto the terminal screen.
  - What I observed: Displayed the lines of text I typed into it.

---

### Task 2.2 — Practising file changes safely
Ran these in `terminal-practice`:
```bash
echo "First line: Terminal practice is going okay." > practice.txt
echo "Second line: Appending text without overwriting line one." >> practice.txt
cat practice.txt
```
Both lines showed up fine.

Answers to questions:
- Difference between replacing (`>`) and appending (`>>`):
  - `>` wipes out whatever was in the file and replaces it with the new text.
  - `>>` keeps whatever was already there and just tacks the new line onto the very end.
- Difference between copying (`cp`) and moving (`mv`):
  - Copy leaves the original file where it was and makes a second copy.
  - Move just moves the file to a new spot or renames it, so you still only have one file.
- What info does current-directory display (`pwd`) give?
  - It gives you the full absolute path from the root `/` down to where your terminal is currently sitting.
- Why is directory listing (`ls`) useful?
  - Because in terminal you don't have a visual mouse folder window open, so `ls` is the only way to see what files exist and avoid typos.

---

### Task 2.3 — Flags and pipes
- Normal `ls` just gives file names in a couple columns.
- `ls -lah`:
  - `-l` makes it a detailed vertical list with permissions and dates.
  - `-a` shows all files including hidden files starting with a dot (like `.git`).
  - `-h` turns ugly byte sizes into readable units like KB and MB.
- Pipe test: `ls -la | head -n 5`
  - The pipe `|` takes the output from `ls -la` and instead of printing hundreds of lines to screen, feeds it straight into `head -n 5`.
  - `ls -la` on the left generates the full list, and `head -n 5` on the right cuts it down to just the first 5 lines.

---

### Task 2.4 — Package managers
Checked brew:
- Version: `Homebrew 7.0.7`
- Installed formulae: `gettext`, `git`, `json-c`, `libunistring`, `pcre2`.

Why package managers are useful:
Instead of searching Google, downloading a random `.dmg` or `.pkg` installer, dragging icons to Applications, and manually updating everything, Homebrew lets you install, update, or remove command-line tools with one quick terminal command. It also handles all background dependencies automatically so you don't have to figure them out yourself.

## 5. Difficulties faced
Almost used `>` instead of `>>` by muscle memory which would have wiped line 1, but caught it in time.

## 6. How I resolved them
Just double-checked before hitting enter and used `>>` to append properly.

## 7. Evidence / files
- `terminal-practice/practice.txt`
- `terminal-practice/practice_backup_renamed.txt`
- `mission-02-terminal/README.md`

## 8. Commit details
- Commit message: "Complete Terminal and file management mission"
- Ready to push to GitHub.
