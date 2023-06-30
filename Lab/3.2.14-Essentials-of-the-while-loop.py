"""write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
Note: the height is measured by the number of fully completed layers if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately."""

# Read the number of blocks from the user
blocks = int(input("Enter number of blocks: "))
heights = 0  # Initialize the height of the pyramid to 0
total_blocks = 0  # Initialize the total number of blocks used in the pyramid to 0

while total_blocks <= blocks:
    heights += 1  # Increment the height by 1
    total_blocks += heights  # Add the current height to the total blocks used

    if total_blocks > blocks:
        heights -= 1  # Decrement the height by 1 to adjust for exceeding the available blocks
        break  # Exit the loop since the next layer cannot be completed

# Print the calculated height of the pyramid
print("The height of the pyramid:", heights)
