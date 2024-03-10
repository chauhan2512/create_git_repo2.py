import os
import subprocess

def create_git_repository(directory):
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Navigate to the directory
    os.chdir(directory)
    
    # Initialize Git repository
    subprocess.run(['git', 'init'])
    
    # Create README file
    with open('README.md', 'w') as file:
        file.write('# My Git Repository\nThis is a sample README file for my Git repository.')
    
    # Add README to staging area
    subprocess.run(['git', 'add', 'README.md'])
    
    # Commit changes
    subprocess.run(['git', 'commit', '-m', 'Initial commit'])
    
    # Push to GitHub (replace <username> and <repository> with your GitHub username and repository name)
    subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/<username>/<repository>.git'])
    subprocess.run(['git', 'push', '-u', 'origin', 'master'])
    
    print("Git repository created and pushed to GitHub successfully.")

# Replace 'my_project' with the desired directory name
create_git_repository('my_project')
