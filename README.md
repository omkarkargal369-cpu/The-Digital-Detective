# The Digital Detective

My Diwali assignment repo for exploring computer stuff, terminal commands, OS basics, Python, and Git.

- USN last 4 digits: 8416
- Repo: digital-detective-8416
- Note: Kept private personal info like passwords and IP redacted.
- Note on commits: Each mission was done, documented, and committed one by one in order with its own dedicated commit.

---

## Topics Explored
- Computer fundamentals & the IPOS cycle
- Terminal navigation, file management, flags, and pipes
- Operating system jobs, background processes, paths, and permissions
- Running Python code and comparing compilers with interpreters
- Number conversions (decimal, binary, hex) and text encoding (ASCII/UTF-8)
- Git version control, branching (`update-about`), and pull requests
- Computer networks, ping/DNS lookups, and how websites load

---

## Mission Links

- [Mission 0: Setup](mission-00-setup/README.md) - Repo setup and tool checks
- [Mission 1: Computer Basics](mission-01-computer-basics/README.md) - IPOS, hardware, and software
- [Mission 2: Terminal](mission-02-terminal/README.md) - Basic terminal commands and file stuff
- [Mission 3: Operating System](mission-03-operating-system/README.md) - Processes, storage, and permissions
- [Mission 4: How Programs Run](mission-04-programs/README.md) - Running python and compiler vs interpreter
- [Mission 5: Numbers and Data](mission-05-numbers-data/README.md) - Number conversions and python converter script
- [Mission 6: Git and GitHub](mission-06-git-github/README.md) - Branches and pull requests
- [Mission 7: Networking](mission-07-networking/README.md) - Network types, ping, and dns
- [Mission 8: Final Report](mission-08-final-report/README.md) - Final checklist and summary

---

## How to run the converter
Head into `mission-05-numbers-data` and run:
```bash
python3 number_converter.py
```
Type any positive integer and it prints the binary and hex values.

---

## My Learning
Here are a few key things I picked up while working through these missions:
- Terminal is actually much faster than clicking around folders once you know `cd`, `ls`, and `mkdir`.
- How programs get executed: compilers translate the whole file beforehand to run fast, while interpreters like Python run things line-by-line.
- How Git keeps track of changes with snapshots so you can always see older commits or test stuff safely in branches without breaking `main`.
- How networks talk: DNS is basically just the phonebook that turns web names into IP addresses before packets get sent.
