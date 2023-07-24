import sys
import re

names = []

def extract_names(filename):
    with open(filename, 'r') as file:
        html_content = file.read()

        # Use regular expressions to find the names in the HTML content
        # This pattern assumes that the name is in the second column of a table.
        pattern = r'<tr align="right"><td>\d+</td><td>(\w+)</td><td>\w+</td>'
        matches = re.findall(pattern, html_content)

        # Extend the 'names' list with the extracted names
        names.extend(matches)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python babynames.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    extract_names(filename)

    # Print the extracted names
    for i, name in enumerate(names, start=1):
        print(f"Rank #{i}: {name}")
