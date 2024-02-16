import subprocess
import datetime
import random

def create_random_commits():
    try:
        # Change to your repository directory
        repo_path = "c:/Users/tamagn/Documents/Amazon-clone"
        
        # Define the date range for the last 365 days from the current date
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=365)
        
        current_date = start_date
        commits_count = 0
        
        while current_date <= end_date:
            # Skip committing on Sundays (day 6, where Monday is day 0)
            if current_date.weekday() == 6:  # Sunday is day 6 in the weekday() method
                current_date += datetime.timedelta(days=1)
                continue
            
            # Generate a random number of commits for the current week
            commits_per_week = 2
            
            # Check if the current day is within a commit week
            if commits_count < commits_per_week:
                # Generate a random time within the current day
                random_time = datetime.timedelta(seconds=random.randint(0, 86399))
                commit_date = current_date + random_time
                
                # Format the commit date
                commit_date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
                
                # Create a new commit with the commit message "test commit"
                command = f'git commit --allow-empty --date="{commit_date_str}" -m "test commit"'
                subprocess.run(command, cwd=repo_path, shell=True, check=True)
                
                commits_count += 1
            
            # Move to the next day
            current_date += datetime.timedelta(days=1)
            
            # Reset the commits count at the beginning of a new week
            if commits_count == commits_per_week:
                commits_count = 0
        
        print(f"Random commits created for the last 365 days.")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    create_random_commits()
