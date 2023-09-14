# Prompt for file name
file_name = input("Enter the file name: ")

try:
    # Open the file
    file_handle = open(file_name)

    count = 0  # Line count
    total = 0  # Total sum of values

    # Iterate over each line in the file
    for line in file_handle:
        # Check if the line starts with 'X-DSPAM-Confidence:'
        if line.startswith("X-DSPAM-Confidence:"):
            # Extract the floating-point value from the line
            value = float(line.split(":")[1])

            count = count + 1
            total = total + value

    # Close the file
    file_handle.close()

    # Calculate the average
    average = total / count

    # Print the count and average
    print("Count:", count)
    print("Average:", average)

except FileNotFoundError:
    print("File not found:", file_name)
