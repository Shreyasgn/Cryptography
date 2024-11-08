4. Write a Python script that performs the Golomb test to the numbers provided below. 
                   101011001010
                   111111000000
   The script should
          - Perform and print the results of the three Golomb tests on the sequence.
          - Print a message indicating whether the sequence passes the Golomb tests or not.

def count_runs(sequence):
    """Count the number of runs of 0s and 1s in the sequence."""
    runs = []
    current_run = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1
    runs.append(current_run)
    return runs

def golomb_test(sequence):
    n = len(sequence)
    ones = sequence.count('1')
    zeros = sequence.count('0')
    runs = count_runs(sequence)
    
    # Test 1: Balance property
    balance = abs(ones - zeros) <= 1
    print(f"Test 1 (Balance property): {'Passed' if balance else 'Failed'}")
    print(f"  Number of 1s: {ones}")
    print(f"  Number of 0s: {zeros}")
    
    # Test 2: Run property
    expected_runs = (n + 1) // 2
    actual_runs = len(runs)
    run_property = abs(actual_runs - expected_runs) <= 2
    print(f"Test 2 (Run property): {'Passed' if run_property else 'Failed'}")
    print(f"  Expected number of runs: {expected_runs}")
    print(f"  Actual number of runs: {actual_runs}")
    
    # Test 3: Run length property
    run_lengths = {i: runs.count(i) for i in range(1, max(runs) + 1)}
    run_length_property = True
    for k in range(1, len(run_lengths)):
        if k+1 in run_lengths:
            if run_lengths[k] < run_lengths[k+1]:
                run_length_property = False
                break
    print(f"Test 3 (Run length property): {'Passed' if run_length_property else 'Failed'}")
    print("  Run lengths:")
    for length, count in run_lengths.items():
        print(f"    Length {length}: {count} runs")
    
    # Overall result
    passed_all = balance and run_property and run_length_property
    print(f"\nOverall result: {'Passed' if passed_all else 'Failed'} all Golomb tests")
    return passed_all

# Test sequences
sequences = [
    "101011001010",
    "111111000000"
]

for i, seq in enumerate(sequences, 1):
    print(f"\nTesting sequence {i}: {seq}")
    print("-" * 50)
    golomb_test(seq)
    print("\n")
