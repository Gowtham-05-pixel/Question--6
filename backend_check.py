import time

def run_backend_check():
    print("Starting backend checks...")
    
    # Each script should sleep for 4 seconds
    time.sleep(4)
    
    # Write its own result file (backend_report.txt)
    output_filename = "backend_report.txt"
    with open(output_filename, "w") as report_file:
        report_file.write("Backend Check Report\n")
        report_file.write("Status: SUCCESS\n")
        report_file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        report_file.write("All backend assertions passed.\n")
        
    print(f"Backend checks completed. Report written to {output_filename}")

if __name__ == "__main__":
    run_backend_check()