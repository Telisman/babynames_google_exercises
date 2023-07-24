import re
import sys

def extract_names(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Extract the year from the filename using regular expressions
    year_match = re.search(r'baby(\d{4})\.html', filename)
    if year_match:
        year = year_match.group(1)
    else:
        print(f"Could not extract the year from {filename}")
        return []

    # Extract names and rank numbers using regular expressions
    name_rank_pattern = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', content)

    # Sort the name-rank strings in alphabetical order
    name_rank_list = sorted(
        [f"{boy_name} {rank}", f"{girl_name} {rank}"] for rank, boy_name, girl_name in name_rank_pattern)

    # Flatten the list and prepend the year
    result_list = [year] + [item for sublist in name_rank_list for item in sublist]

    return result_list


# List of HTML files
html_files = [
    "baby1990.html",
    "baby1992.html",
    "baby1994.html",
    "baby1996.html",
    "baby1998.html",
    "baby2000.html",
    "baby2002.html",
    "baby2004.html",
    "baby2006.html",
    "baby2008.html"
]

# # Build and print the [year, 'name rank', ... ] list for each HTML file
# for filename in html_files:
#     data_list = extract_names(filename)
#     print(data_list)


def main():
    # Command-line parsing
    arguments = sys.argv[1:]  # Get all command-line arguments except the script name

    if not arguments:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Check if the first argument is '--summaryfile'
    if arguments[0] == '--summaryfile':
        summary_file_mode = True
        # The summary data will be written to a file named 'summary.txt'
        output_file = 'summary.txt'
        files = arguments[1:]  # Skip the '--summaryfile' argument
    else:
        summary_file_mode = False
        files = arguments

    # Process each file
    for filename in files:
        data_list = extract_names(filename)

        # Prepare the output text
        output_text = '\n'.join(data_list)

        if summary_file_mode:
            # Write the output to the summary file
            with open(output_file, 'a') as file:
                file.write(output_text + '\n')
        else:
            # Print the output to the console
            print(output_text)

if __name__ == "__main__":
    main()

