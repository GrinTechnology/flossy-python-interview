# Log Analyzer Interview

We're going to build a log analyzer together. This is a collaborative exercise, so think of it as pair programming with a colleague, not a distant assessment of your skills.

**Note**: We likely won't finish everything, and that's fine. The goal is to write clean, working code together and have good discussions along the way.

## Setup

No dependencies needed. Just Python 3.8+.

**Files:**
- `solution.py` — Where we'll write our code (function stubs are ready to implement)
- `main.py` — Test harness that checks our progress (no need to edit this)
- `sample_logs.txt` — Log data to work with

**To run:**
```bash
python3 main.py
```

You'll see output for each checkpoint. Initially, everything shows "Not implemented yet"—that's expected! As we implement each function in `solution.py`, more output will appear.

## The Problem

We have application logs in a standard format. We need to build tools to parse, filter, and analyze them.

### Log Format

Each line follows this pattern:
```
[TIMESTAMP] LEVEL: MESSAGE
```

Example:
```
[2024-03-15 10:23:45] INFO: User alice logged in
[2024-03-15 10:23:46] ERROR: Database connection failed: timeout after 30s
[2024-03-15 10:23:47] WARNING: Memory usage at 85%
```

## Checkpoints

### Checkpoint 1: Parse a Single Log Line
Given a log line string, extract the timestamp, level, and message. Return them in a structure we can work with programmatically (e.g., a dictionary, named tuple, or class).

### Checkpoint 2: Parse a Log File  
Read `sample_logs.txt` and parse all lines into a list of structured log entries.

### Checkpoint 3: Filter Logs
Implement filtering by:
- Log level (e.g., only ERRORs)
- Time range (e.g., logs between 10:00 and 11:00)
- Message content (e.g., contains "database")

### Checkpoint 4: Aggregate & Analyze
- Count logs by level
- Find the most frequent error messages
- Identify "spikes" (many errors in a short time window)

### Checkpoint 5 (Stretch): Pattern Detection
- **Recurring sequences**: Do certain errors always follow each other? For example, in our logs, database timeouts lead to connection loss, then failover. Can we detect that pattern automatically?
- **Anomalies**: Are there time windows with unusually high (or low) log activity? The brute force attack at 10:03 generates a burst of errors—can we flag that?
