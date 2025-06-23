import os  # Import the os module to handle directory operations

def table():
    # Define the folder path where the table files will be stored
    folder_path = "D:/Prep/Python/Chapters/Chapter 9/txt files/Tables"

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Loop through numbers 2 to 20 to generate multiplication tables
    for i in range(2, 21):
        # Construct the full file path with file name like "table-of-2.txt", "table-of-3.txt", etc.
        filename = os.path.join(folder_path, f"table-of-{i}.md")

        # Open the file in write mode ("w"), which creates or overwrites the file
        with open(filename, "w") as f:
            # Write the title/header line for the table
            f.write(f"table of {i}\n")

            # Write the multiplication table lines from 1 to 10
            for j in range(1, 11):
                f.write(f"{i} X {j} = {i*j}\n")

            # Add a blank line at the end for better formatting
            f.write("\n")

# Call the function to generate and save all the tables
table()

# Confirmation message after all files are created
print("folder and files created")
