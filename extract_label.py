from bs4 import BeautifulSoup
import re

def parse_sas_html(file_path):
    with open(file_path, "r", encoding="windows-1252") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Dictionary to store SAS variable names and their labels
    sas_variables = {}
    # Dictionary to store value labels for each SAS variable
    value_labels = {}

    # Find all variable definition tables
    tables = soup.find_all("table", class_="table")

    for table in tables:
        var_name = None
        var_label = None

        # Look for the first `td` that contains the SAS Variable Name and Label
        var_info_td = table.find("td", class_="l m linecontent")
        if var_info_td:
            text = var_info_td.get_text(" ", strip=True)  # Normalize text
            text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space

            # Extract Label
            label_match = re.search(r"Label:\s*(.+?)\s*Section", text, re.IGNORECASE)
            var_label = label_match.group(1).strip() if label_match else None

            # Extract SAS Variable Name
            var_match = re.search(r"SAS Variable Name:\s*([\w\d_]+)", text, re.IGNORECASE)
            var_name = var_match.group(1).strip() if var_match else None

            # Store only if both exist
            if var_name and var_label:
                sas_variables[var_name] = var_label

        # Extract Value Labels
        if var_name:
            value_table = table.find("tbody")
            if value_table:
                rows = value_table.find_all("tr")[:]  # Skip header row
                for row in rows:
                    cols = row.find_all("td")
                    if len(cols) >= 2:
                        value = cols[0].get_text(strip=True)
                        label = cols[1].get_text(strip=True)

                        # Store value labels
                        if var_name not in value_labels:
                            value_labels[var_name] = {}
                        value_labels[var_name][value] = label

    return sas_variables, value_labels

if __name__ == "__main__":
    # Example usage
    file_path = "Original Data/USCODE23_LLCP_091024.HTML"  # Update this with the correct file path
    sas_variables, value_labels = parse_sas_html(file_path)

    # Print results
    print("SAS Variables and Labels:")
    for var, label in sas_variables.items():
        print(f"{var}: {label}")

    print("\nValue Labels:")
    for var, values in value_labels.items():
        print(f"\n{var}:")
        for val, val_label in values.items():
            print(f"  {val}: {val_label}")
