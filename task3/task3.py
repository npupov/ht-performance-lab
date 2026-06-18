import sys
import json

def fill_values(test_struct, values_dict):
    if 'id' in test_struct and test_struct['id'] in values_dict:
        test_struct['value'] = values_dict[test_struct['id']]
    
    if 'values' in test_struct:
        for child in test_struct['values']:
            fill_values(child, values_dict)

def main():
    if len(sys.argv) < 4:
        return
    
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]
    
    with open(values_path, 'r') as f:
        values_data = json.load(f)
    
    with open(tests_path, 'r') as f:
        tests_data = json.load(f)
    
    values_dict = {item['id']: item['value'] for item in values_data['values']}
    
    fill_values(tests_data, values_dict)
    
    with open(report_path, 'w') as f:
        json.dump(tests_data, f, indent=2)

if __name__ == "__main__":
    main()
