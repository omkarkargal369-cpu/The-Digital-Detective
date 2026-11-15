# Mission 3 — Understand the operating system

## 1. Task / objective
Check out the OS environment on my laptop, look at how processes and storage work, understand absolute vs relative paths and file permissions, and write down what the OS actually does.

## 2. Work completed
- Checked OS version, kernel info, and disk space in terminal.
- Looked into processes and PIDs.
- Tested path types and checked permission bits on `practice.txt`.
- Explained the 6 main OS jobs in simple terms.
- Kept it free of tables and redacted personal user info.

## 3. Commands / tools used
- `sw_vers` - shows macOS product name and version.
- `uname -srm` - prints operating system kernel and chip architecture (arm64).
- `df -h /` - shows total disk space, used space, and free space in GB.
- `whoami` - tells you the current logged-in user account.
- `ls -l` - checks the permission flags on files.

## 4. My understanding

### Task 3.1 — Exploring my OS
- Operating system details:
  - What it tells you: The exact OS release and architecture running on this machine.
  - My observation: Running macOS on an Apple Silicon arm64 chip.
- Current account identity:
  - What it tells you: Shows which user account is active in the current session.
  - My observation: Logged in as user `[redacted]` under staff group.
- Available and used storage:
  - What it tells you: How full your main drive is.
  - My observation: Drive has about 926 GiB total, around 13 GiB used by system volume, and over 800 GiB available.
- System activity snapshot:
  - What it tells you: Shows current CPU load, active background tasks, and how memory is allocated.
  - My observation: Can view live CPU %, idle time, and process list through Activity Monitor or terminal.

---

### Task 3.2 — Processes
- What is a process?
  - A process is just a program that is currently running in memory. When you double click an app or run a script, the OS loads it into RAM and turns it into an active process.
- What does the PID column represent?
  - PID stands for Process ID. It is a unique number that the OS assigns to every running process so it can track, control, or kill it without confusing it with other apps.
- Two examples of processes running:
  - `Finder` (or `launchd`): the core system process managing the macOS desktop and files.
  - `Google Chrome` (or `Terminal`): user application process running tabs and terminal shell.

---

### Task 3.3 — Paths and permissions
- Difference between absolute path and relative path:
  - Absolute path: The full complete path starting from the very top root `/` of the whole drive. It works no matter where your terminal is currently sitting. Example: `/Users/[redacted]/digital-detective-8416/terminal-practice/practice.txt`
  - Relative path: A shortcut path based on wherever you are standing right now. Example: `terminal-practice/practice.txt` or `./practice.txt`.
- Permissions on `terminal-practice/practice.txt`:
  - Output was `-rw-r--r--`.
  - The first dash `-` means it is a regular file (not a folder).
  - The next three characters `rw-` are the owner permissions: Read (`r`) is yes, Write (`w`) is yes, and Execute (`x`) is no (has a dash).
  - So as the owner, I can read and edit the file, but cannot run it as a script.

Meaning of permission letters:
- `r` (Read): Lets you open and view the contents of a file.
- `w` (Write): Lets you edit, modify, or delete contents of a file.
- `x` (Execute): Lets you run the file as a program or script (and on folders, allows you to enter/cd into it).

---

### Task 3.4 — OS Responsibilities
- Process management:
  - Explanation: The OS schedules which program gets to use the CPU and for how many milliseconds, so multiple apps can run without freezing the computer.
  - Example: You can listen to music on Spotify while typing code in VS Code at the same time.
- Memory management:
  - Explanation: Gives each app its own slice of RAM so apps don't accidentally write over each other's data and cause crashes.
  - Example: When you close a heavy browser tab, the OS frees that RAM back up for other programs.
- Device management:
  - Explanation: Talks to hardware components using device drivers so programs don't need to know how hardware works internally.
  - Example: Letting any app send print jobs to an external USB or Wi-Fi printer.
- File management:
  - Explanation: Organizes data into files, folders, and directories on disk and keeps track of where everything is physically saved.
  - Example: Creating, searching, and deleting folders in Finder or Terminal.
- User interface / shell:
  - Explanation: Provides the bridge between the human and the computer, either with graphics/windows or a text terminal.
  - Example: The macOS graphical desktop and the zsh Terminal shell.
- Security and permissions:
  - Explanation: Makes sure users and apps can only access files they are allowed to touch.
  - Example: Asking for your Touch ID or password before an installer modifies system files.

## 5. Difficulties faced
Reading permissions looked like a bunch of random letters at first until I remembered it's grouped in sets of three (owner, group, others).

## 6. How I resolved them
Just broke down `-rw-r--r--` into `rw-` for owner, `r--` for group, and `r--` for others.

## 7. Evidence / files
- `mission-03-operating-system/README.md`
- Permission checks on `terminal-practice/practice.txt`

## 8. Commit details
- Commit message: "Document operating system and file management"
- Ready to push to GitHub.
