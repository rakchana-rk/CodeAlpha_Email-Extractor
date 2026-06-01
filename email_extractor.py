import re

INPUT_FILE = "sample.txt"
OUTPUT_FILE = "emails.txt"


def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)


def main():
    try:
        with open(INPUT_FILE, "r") as file:
            content = file.read()

        emails = extract_emails(content)

        with open(OUTPUT_FILE, "w") as file:
            for email in emails:
                file.write(email + "\n")

        print("=" * 40)
        print("      EMAIL EXTRACTOR")
        print("=" * 40)
        print(f"Emails Found: {len(emails)}")
        print(f"Results saved to '{OUTPUT_FILE}'")

        if emails:
            print("\nExtracted Emails:")
            for email in emails:
                print(email)

    except FileNotFoundError:
        print(f"Error: '{INPUT_FILE}' not found.")


if __name__ == "__main__":
    main()
