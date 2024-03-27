try:
    # File Creation
    with open("my_file.txt", "w") as file:
        # Writing three lines of text to the file
        file.write("First line of text.\n")
        file.write("12345\n")
        file.write("Another line with text and numbers.\n")
    print("File creation and writing completed successfully.")

    # File Reading and Display
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            # Reading and displaying the contents of the file
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # File Appending
    try:
        with open("my_file.txt", "a") as file:
            # Appending three additional lines of text to the existing content
            file.write("Fourth line added.\n")
            file.write("Fifth line appended.\n")
            file.write("Last line appended.\n")
        print("File appending completed successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")

