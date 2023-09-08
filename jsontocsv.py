
import json
import csv

def convert_json_to_csv_file(input_json_file, output_csv_file_path):
    csv_columns = ["Employee ID", "Full Legal Name", "userID", "personGUID", "curriculumID", "curriculumStatus", "assignmentDate", "expirationDate", "nextActionDate", "remainingDays", "totalCount", "rootCurriculaID"]
    
    try:
        with open(input_json_file, 'r') as json_file:
            json_data = json.load(json_file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return
    
    try:
        with open(output_csv_file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            
            for record in json_data:
                base_data = {key: record.get(key, None) for key in csv_columns if '.' not in key and '@' not in key}
                data_values = record.get('Data', {}).get('value', [{}])
                for data_value in data_values:
                    row_data = base_data.copy()
                    for key in csv_columns:
                        if key in data_value:
                            row_data[key] = data_value.get(key, None)
                    writer.writerow(row_data)
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

# Example usage
input_json_file = "input.json"
output_csv_file_path = "output.csv"

convert_json_to_csv_file(input_json_file, output_csv_file_path)
