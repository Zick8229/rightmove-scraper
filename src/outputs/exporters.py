thonimport json

def export_data(data, filename="properties.json"):
    """
    Function to export the extracted data to a JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)