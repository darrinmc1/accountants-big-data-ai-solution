#!/usr/bin/env python3
"""
GitHub Repository Setup and Upload Script

This script helps you create a new GitHub repository and upload the presentation files.
It guides you through the process step by step.

Requirements:
- Git must be installed on your system
- You must have a GitHub account
- You must have the GitHub CLI (gh) installed or be able to authenticate via browser
"""

import os
import subprocess
import sys
import time
import webbrowser
from getpass import getpass

def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 80)
    print(f" {text}")
    print("=" * 80 + "\n")

def run_command(command, description=None, exit_on_error=True):
    """Run a shell command and handle errors."""
    if description:
        print(f"{description}...")
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.stdout.strip():
            print(result.stdout.strip())
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip()}")
        if exit_on_error:
            print("Exiting due to error.")
            sys.exit(1)
        return None

def check_git_installed():
    """Check if Git is installed."""
    try:
        subprocess.run(
            ["git", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_gh_cli_installed():
    """Check if GitHub CLI is installed."""
    try:
        subprocess.run(
            ["gh", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def initialize_git_repo():
    """Initialize a Git repository in the current directory."""
    print_header("Initializing Git Repository")
    
    # Check if .git directory already exists
    if os.path.exists(".git"):
        print("Git repository already initialized.")
        return
    
    run_command("git init", "Initializing Git repository")
    run_command("git add .", "Adding files to Git repository")
    run_command('git commit -m "Initial commit: Accountants Big Data AI Solution"', 
                "Creating initial commit")

def create_github_repo(repo_name, description, private=False):
    """Create a GitHub repository using GitHub CLI."""
    print_header("Creating GitHub Repository")
    
    visibility = "--private" if private else "--public"
    
    if check_gh_cli_installed():
        print("Using GitHub CLI to create repository...")
        # Check if already authenticated
        auth_status = run_command("gh auth status", "Checking GitHub authentication", exit_on_error=False)
        
        if not auth_status or "not logged" in auth_status:
            print("You need to authenticate with GitHub CLI.")
            run_command("gh auth login", "Authenticating with GitHub")
        
        # Create the repository
        run_command(
            f'gh repo create {repo_name} {visibility} --description "{description}" --source=. --remote=origin',
            "Creating GitHub repository"
        )
    else:
        print("GitHub CLI not found. Please create a repository manually:")
        print("1. Go to https://github.com/new")
        print(f"2. Enter '{repo_name}' as the repository name")
        print(f"3. Enter '{description}' as the description")
        print(f"4. Set visibility to {'Private' if private else 'Public'}")
        print("5. Click 'Create repository'")
        print("6. Follow the instructions to push an existing repository from the command line")
        
        webbrowser.open("https://github.com/new")
        input("Press Enter once you've created the repository...")
        
        remote_url = input("Enter the GitHub repository URL: ")
        run_command(f"git remote add origin {remote_url}", "Adding GitHub remote")

def push_to_github():
    """Push the local repository to GitHub."""
    print_header("Pushing to GitHub")
    run_command("git push -u origin main", "Pushing to GitHub")

def enable_github_pages():
    """Enable GitHub Pages for the repository."""
    print_header("Enabling GitHub Pages")
    
    if check_gh_cli_installed():
        run_command(
            "gh api -X PUT repos/:owner/:repo/pages -f source.branch=main -f source.path=/",
            "Enabling GitHub Pages",
            exit_on_error=False
        )
        
        # If the above command fails, provide manual instructions
        print("\nIf GitHub Pages wasn't enabled automatically, please enable it manually:")
    else:
        print("Please enable GitHub Pages manually:")
    
    print("1. Go to your repository on GitHub")
    print("2. Click on 'Settings'")
    print("3. Navigate to 'Pages' in the left sidebar")
    print("4. Under 'Source', select 'Deploy from a branch'")
    print("5. Under 'Branch', select 'main' and '/ (root)'")
    print("6. Click 'Save'")
    
    repo_url = run_command("git remote get-url origin", exit_on_error=False)
    if repo_url:
        # Convert SSH URL to HTTPS if necessary
        if repo_url.startswith("git@github.com:"):
            repo_url = repo_url.replace("git@github.com:", "https://github.com/")
            if repo_url.endswith(".git"):
                repo_url = repo_url[:-4]
        
        settings_url = f"{repo_url}/settings/pages"
        print(f"\nOpening GitHub Pages settings: {settings_url}")
        webbrowser.open(settings_url)

def get_pages_url():
    """Get the GitHub Pages URL for the repository."""
    repo_url = run_command("git remote get-url origin", exit_on_error=False)
    if not repo_url:
        return None
    
    # Convert SSH URL to HTTPS if necessary
    if repo_url.startswith("git@github.com:"):
        repo_url = repo_url.replace("git@github.com:", "https://github.com/")
        if repo_url.endswith(".git"):
            repo_url = repo_url[:-4]
    
    # Extract username and repo name from URL
    parts = repo_url.split("/")
    if len(parts) >= 5:
        username = parts[-2]
        repo_name = parts[-1]
        return f"https://{username}.github.io/{repo_name}/"
    
    return None

def main():
    """Main function to run the script."""
    print_header("GitHub Repository Setup and Upload")
    
    # Check if Git is installed
    if not check_git_installed():
        print("Error: Git is not installed or not in PATH.")
        print("Please install Git and try again.")
        sys.exit(1)
    
    # Get repository information
    repo_name = input("Enter a name for your GitHub repository (default: accountants-big-data-ai-solution): ").strip()
    if not repo_name:
        repo_name = "accountants-big-data-ai-solution"
    
    description = input("Enter a description for your repository (default: AI solution for accountants' big data challenges): ").strip()
    if not description:
        description = "AI solution for accountants' big data challenges"
    
    private_input = input("Make the repository private? (y/N): ").strip().lower()
    private = private_input == 'y' or private_input == 'yes'
    
    # Initialize Git repository
    initialize_git_repo()
    
    # Create GitHub repository
    create_github_repo(repo_name, description, private)
    
    # Push to GitHub
    push_to_github()
    
    # Enable GitHub Pages
    enable_github_pages()
    
    # Provide the GitHub Pages URL
    print_header("Success!")
    
    pages_url = get_pages_url()
    if pages_url:
        print(f"Your presentation will be available at: {pages_url}")
        print("Note: It may take a few minutes for GitHub Pages to deploy your site.")
    else:
        print("Your presentation has been uploaded to GitHub.")
        print("Once GitHub Pages is enabled, your presentation will be available at:")
        print("https://[your-username].github.io/[repository-name]/")
    
    print("\nThank you for using the GitHub Repository Setup and Upload Script!")

if __name__ == "__main__":
    main()
