2. Write a Python script that implements a simple 4-bit LFSR. The initial state of the register and the tap positions should be user inputs. 
   Simulate 10 steps of the LFSR, displaying the state of the register at each step.

  def get_binary_input(prompt, length):
    """Get a valid binary input of specified length from the user."""
    while True:
        value = input(prompt)
        if set(value) <= {'0', '1'} and len(value) == length:
            return [int(bit) for bit in value]
        else:
            print(f"Invalid input. Please enter a {length}-bit binary number.")

def get_tap_positions():
    """Get tap positions from the user."""
    while True:
        taps = input("Enter tap positions (comma-separated, e.g., 1,3): ")
        try:
            tap_list = [int(tap) for tap in taps.split(',')]
            if all(0 <= tap < 4 for tap in tap_list):
                return tap_list
            else:
                print("Invalid tap positions. Please enter numbers between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter comma-separated numbers.")

def lfsr_step(state, taps):
    """Perform one step of the LFSR."""
    feedback = sum(state[tap] for tap in taps) % 2
    return [feedback] + state[:-1]

# Get initial state from the user
initial_state = get_binary_input("Enter the initial 4-bit state: ", 4)

# Get tap positions from the user
tap_positions = get_tap_positions()

# Simulate 10 steps of the LFSR
current_state = initial_state
print("\nLFSR Simulation:")
print(f"Initial state: {current_state}")

for step in range(1, 11):
    current_state = lfsr_step(current_state, tap_positions)
    print(f"Step {step}: {current_state}")

# Calculate the output sequence
output_sequence = [initial_state[-1]] + [state[-1] for state in [lfsr_step(current_state, tap_positions) for _ in range(9)]]
print(f"\nOutput sequence: {output_sequence}")
