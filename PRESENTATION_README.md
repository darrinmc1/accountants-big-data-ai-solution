# Online Presentation: Accountants' Big Data Challenges - AI-Powered Solutions

This folder contains a presentation about accountants' pain points related to big data and a proposed AI solution to address these challenges.

## Viewing the Presentation Online

### Option 1: Run the Local Web Server (Recommended)

#### Prerequisites:
1. Make sure you have Python installed on your computer
   - Python 3.6 or higher is recommended
   - No additional packages are required (see `requirements.txt`)

#### Windows Users:
1. Double-click the `start_presentation.bat` file
   - Or open Command Prompt, navigate to this folder, and run `start_presentation.bat`

#### Mac/Linux Users:
1. Open Terminal and navigate to this folder
2. Make the script executable: `chmod +x start_presentation.sh`
3. Run the script: `./start_presentation.sh`

#### Manual Start (All Platforms):
1. Open a terminal/command prompt
2. Navigate to this folder
3. Run: `python start_presentation_server.py` (or `python3` on Mac/Linux)

5. The presentation will automatically open in your default web browser
6. The server will run at http://localhost:8000
   - You can access the presentation by visiting http://localhost:8000 or http://localhost:8000/index.html
   - This will automatically redirect to the presentation
7. To stop the server, press Ctrl+C in the terminal

### Option 2: Access from Other Devices on Your Network

Once the server is running:

1. Find your computer's IP address:
   - Windows: Open Command Prompt and type `ipconfig`
   - Mac/Linux: Open Terminal and type `ifconfig` or `ip addr`

2. On other devices (phones, tablets, other computers), open a web browser and go to:
   ```
   http://YOUR_IP_ADDRESS:8000
   ```
   Replace `YOUR_IP_ADDRESS` with your actual IP address (e.g., 192.168.1.5)
   
   This will automatically redirect to the presentation. Alternatively, you can use:
   ```
   http://YOUR_IP_ADDRESS:8000/Accountants_Big_Data_AI_Solution_Presentation.html
   ```

### Option 3: Open the HTML File Directly

You can also simply open the HTML file directly in any web browser:

1. Navigate to this folder
2. Double-click on `Accountants_Big_Data_AI_Solution_Presentation.html`

Note: This option won't allow access from other devices on your network.

## Hosting Online (For Wider Access)

### Option 1: Upload to GitHub Pages (Recommended)

This repository includes scripts to help you easily upload the presentation to GitHub Pages:

#### Prerequisites:
1. Git must be installed on your system
2. You must have a GitHub account
3. GitHub CLI (gh) is recommended but not required

#### Windows Users:
1. Double-click the `upload_to_github.bat` file
   - Or open Command Prompt, navigate to this folder, and run `upload_to_github.bat`

#### Mac/Linux Users:
1. Open Terminal and navigate to this folder
2. Make the script executable: `chmod +x upload_to_github.sh`
3. Run the script: `./upload_to_github.sh`

#### What the Script Does:
1. Initializes a Git repository in this folder
2. Creates a new GitHub repository (public or private, you choose)
3. Pushes all files to the GitHub repository
4. Helps you enable GitHub Pages for the repository
5. Provides the URL where your presentation will be available online

Once completed, your presentation will be available at:
`https://[your-username].github.io/[repository-name]/`

Note: It may take a few minutes for GitHub Pages to deploy your site after setup.

### Option 2: Other Web Hosting Services

You can also manually upload the files to other web hosting services:

1. Upload the `Accountants_Big_Data_AI_Solution_Presentation.html` file and `index.html` to a web hosting service
2. Some free options include:
   - Netlify
   - Vercel
   - Amazon S3
   - Google Cloud Storage

## Contents

- `Accountants_Big_Data_AI_Solution.md` - Detailed document about the solution
- `Accountants_Big_Data_AI_Solution_Presentation.html` - Visual presentation
- `index.html` - Redirect page to the presentation
- `start_presentation_server.py` - Python script to run a local web server
- `start_presentation.bat` - Windows batch file to easily start the server
- `start_presentation.sh` - Mac/Linux shell script to easily start the server
- `upload_to_github.py` - Python script to upload to GitHub Pages
- `upload_to_github.bat` - Windows batch file to easily run the GitHub upload script
- `upload_to_github.sh` - Mac/Linux shell script to easily run the GitHub upload script
- `requirements.txt` - List of Python dependencies (none required beyond standard library)
- `PRESENTATION_README.md` - This file with instructions
