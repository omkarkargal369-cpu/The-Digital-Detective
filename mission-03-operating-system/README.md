# Mission 3 — Understand the operating system

## 1. Task / objective
Check OS details, processes, storage, paths, permissions, and list the jobs of the operating system.

## 2. Work completed
- Checked OS version (`macOS`), user (`[redacted]`), and free disk space.
- Wrote down what a process and a PID are.
- Checked permissions on `practice.txt` (`-rw-r--r--`).
- Explained 6 OS responsibilities with simple examples.

## 3. Commands / tools used
- `sw_vers` - check macOS version.
- `uname -srm` - check kernel and CPU type.
- `df -h /` - check hard drive storage.
- `whoami` - check current user.
- `ls -l` - check file permissions.

## 4. My understanding

### Task 3.1 — OS Exploration
- OS info: Running macOS on Apple Silicon (arm64).
- User identity: Logged in as `[redacted]`.
- Storage: 926 GiB total disk size with over 800 GiB free.
- Activity: Can see CPU and memory in Activity Monitor or terminal.

### Task 3.2 — Processes
- What is a process: A program that is currently running.
- What is PID: Process ID, a unique number given by the OS to identify each running program.
- Two examples: `Finder` and `Terminal`.

### Task 3.3 — Paths and Permissions
- Absolute path: The full path from the root `/`. Example: `/Users/[redacted]/digital-detective-8416/terminal-practice/practice.txt`.
- Relative path: Path from where you are right now. Example: `terminal-practice/practice.txt`.
- Permissions on `practice.txt`: Shows `-rw-r--r--`.
  - Owner has `rw-` (can read and write, but cannot execute).
  - Group has `r--` (can read only).
  - Others have `r--` (can read only).
- Permission letters:
  - `r`: Read (open and view file).
  - `w`: Write (edit or save changes).
  - `x`: Execute (run program or script).

### Task 3.4 — OS Responsibilities
- Process management: Controls which program runs on the CPU. Example: Running Chrome and music player together.
- Memory management: Allocates RAM to apps and frees it when closed. Example: Giving RAM to VS Code.
- Device management: Talks to hardware using drivers. Example: Printing to a printer.
- File management: Organizes files into folders on the drive. Example: Saving files in Finder.
- User interface: Lets humans interact with the computer. Example: macOS desktop and Terminal.
- Security and permissions: Protects files so only authorized users can open them. Example: Asking for password before editing system files.

## 5. Difficulties faced
Understanding the permission letters at first.

## 6. How I resolved them
Learned that permissions are grouped in 3s: owner, group, others.

## 7. Evidence / files
- `mission-03-operating-system/README.md`

## 8. Commit details
- Commit message: "Document operating system and file management"
- Pushed to main.
