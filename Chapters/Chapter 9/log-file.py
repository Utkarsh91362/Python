# Open the file 'log.html' from the 'txt files' folder and read its content
with open("txt files/log.md") as f:
    content = f.read()

# Check if the word "python" is present anywhere in the file content
if ("python" in content):
    print("Yes python is present")

    # Reopen the file to read it line by line
    with open("txt files/log.md") as f:
        line_no = 1  # Initialize line number counter

        # Loop through each line in the file
        for line in f:
            # If "python" is found in the current line, print it with line number
            if "python" in line:
                print("Line", line_no, ":", line.strip())  # .strip() removes extra spaces and newlines
            line_no += 1  # Move to the next line number after each loop
else:
    # If "python" is not found in the file
    print("Python not present")
