"""
Log Analyzer - Test Harness

Run with: python3 main.py

This file tests your solution. You don't need to edit this file—
just implement the functions in solution.py!
"""

from solution import (
    parse_log_line,
    parse_log_file,
    filter_by_level,
    filter_by_message,
    filter_by_time_range,
    count_by_level,
    most_frequent_messages,
    detect_error_spikes,
    find_error_sequences,
    detect_anomalies,
)

LOG_FILE = "sample_logs.txt"
SAMPLE_LINE = "[2024-03-15 10:23:45] ERROR: Database connection failed: timeout after 30s"


def run_checkpoint(name, func):
    """Run a checkpoint and handle unimplemented functions gracefully."""
    print(f"\n{'=' * 60}")
    print(f" {name}")
    print('=' * 60)
    
    try:
        result = func()
        if result is None:
            print("Not implemented yet")
            return None
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    print("Log Analyzer - Interview Exercise")
    print("==================================")
    print("Edit solution.py, then re-run this file to see your progress!\n")
    
    # -------------------------------------------------------------------------
    # Checkpoint 1: Parse a single line
    # -------------------------------------------------------------------------
    def checkpoint_1():
        result = parse_log_line(SAMPLE_LINE)
        if result is not None:
            print(f"Input:  {SAMPLE_LINE}")
            print(f"Output: {result}")
        return result
    
    run_checkpoint("Checkpoint 1: Parse Single Line", checkpoint_1)
    
    # -------------------------------------------------------------------------
    # Checkpoint 2: Parse the log file
    # -------------------------------------------------------------------------
    def checkpoint_2():
        entries = parse_log_file(LOG_FILE)
        if entries is not None:
            print(f"Parsed {len(entries)} entries from {LOG_FILE}")
            print(f"\nFirst entry: {entries[0]}")
            print(f"Last entry:  {entries[-1]}")
        return entries
    
    entries = run_checkpoint("Checkpoint 2: Parse Log File", checkpoint_2)
    
    # -------------------------------------------------------------------------
    # Checkpoint 3: Filter logs
    # -------------------------------------------------------------------------
    def checkpoint_3():
        if entries is None:
            print("Need Checkpoint 2 first (entries to filter)")
            return None
        
        # Filter by level
        errors = filter_by_level(entries, "ERROR")
        if errors is not None:
            print(f"Errors only: {len(errors)} entries")
        
        # Filter by message content
        db_logs = filter_by_message(entries, "database")
        if db_logs is not None:
            print(f"Contains 'database': {len(db_logs)} entries")
        
        # Filter by time range
        time_filtered = filter_by_time_range(
            entries, 
            "2024-03-15 10:01:00", 
            "2024-03-15 10:02:00"
        )
        if time_filtered is not None:
            print(f"Between 10:01-10:02: {len(time_filtered)} entries")
        
        return errors or db_logs or time_filtered
    
    run_checkpoint("Checkpoint 3: Filter Logs", checkpoint_3)
    
    # -------------------------------------------------------------------------
    # Checkpoint 4: Aggregate and analyze
    # -------------------------------------------------------------------------
    def checkpoint_4():
        if entries is None:
            print("Need Checkpoint 2 first (entries to analyze)")
            return None
        
        # Count by level
        counts = count_by_level(entries)
        if counts is not None:
            print("Counts by level:")
            for level, count in sorted(counts.items()):
                print(f"  {level}: {count}")
        
        # Most frequent error messages
        frequent = most_frequent_messages(entries, "ERROR", top_n=3)
        if frequent is not None:
            print("\nMost frequent ERROR messages:")
            for msg, count in frequent:
                print(f"  ({count}x) {msg[:60]}...")
        
        # Error spikes
        spikes = detect_error_spikes(entries, window_seconds=60, threshold=3)
        if spikes is not None:
            print(f"\nError spikes detected: {len(spikes)}")
            for spike in spikes[:3]:
                print(f"  {spike}")
        
        return counts or frequent or spikes
    
    run_checkpoint("Checkpoint 4: Aggregate & Analyze", checkpoint_4)
    
    # -------------------------------------------------------------------------
    # Checkpoint 5 (Stretch): Pattern detection
    # -------------------------------------------------------------------------
    def checkpoint_5():
        if entries is None:
            print("Need Checkpoint 2 first")
            return None
        
        sequences = find_error_sequences(entries)
        if sequences is not None:
            print("Recurring error sequences:")
            for seq in sequences[:3]:
                print(f"  {seq}")
        
        anomalies = detect_anomalies(entries)
        if anomalies is not None:
            print(f"\nAnomalies detected: {len(anomalies)}")
            for a in anomalies[:3]:
                print(f"  {a}")
        
        return sequences or anomalies
    
    run_checkpoint("Checkpoint 5 (Stretch): Pattern Detection", checkpoint_5)
    
    print("\n" + "=" * 60)
    print(" Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
