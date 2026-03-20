import re
import os

def extract_emails():
    input_file = input("Enter input file name (e.g., data.txt): ").strip()

    # Check if file exists
    if not os.path.exists(input_file):
        print("❌ File not found! Make sure it is in the same folder or give full path.")
        return

    try:
        # Read file safely (handles encoding issues)
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
            text = file.read()

        # Extract emails using regex
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+', text)

        # Remove duplicates
        unique_emails = list(set(emails))

        # Save output
        output_file = "extracted_emails.txt"
        with open(output_file, 'w') as file:
            for email in unique_emails:
                file.write(email + "\n")

        print(f"✅ {len(unique_emails)} email(s) extracted and saved to '{output_file}'")

    except Exception as e:
        print("❌ Error:", e)

# Run program
extract_emails()
