################################################################################
############# CSV File cleaning scripts ########################################
############# Harley Williamson         ########################################
################################################################################
import csv
import datetime

#Function to accept original file, clean, and return to main as a cleaned list.
def read_csv(input_path):
    cleaned_file = []
    with open(input_path, newline="", encoding="utf-8") as dirty_file:
        
        file_read = csv.DictReader(dirty_file)

        for row in file_read:
            cleaned_row = {k: v.strip().lower() for k,v in row.items()}
            
            cleaned_file.append(cleaned_row)
    
    return cleaned_file

#Function to accept the cleaned output, write to a new file, and log results.
def write_csv(clean_output, output_path):
    
    if not clean_output:
        print("No data to write.")
        return
    
    fieldnames=clean_output[0].keys()

    with open(output_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clean_output)
        print(f"Processed {len(clean_output)} rows successfully.")

    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d, %H:%M:%S")
    with open("logging.txt", "a") as log_file:
        log_file.write(f"{formatted_date} --- {len(clean_output)} records written successfully.\n")

   
    
            
