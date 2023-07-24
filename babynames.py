import re


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

# Build and print the [year, 'name rank', ... ] list for each HTML file
for filename in html_files:
    data_list = extract_names(filename)
    print(data_list)
