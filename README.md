# BE02-GitHub-User-Activity

A simple command-line interface (CLI) tool to retrieve the recent activity of a GitHub user by utilizing the GitHub API. This project helps practice skills like working with APIs, handling JSON data, and building a basic CLI application in Python.

## Features

- Fetches the recent activity of a specified GitHub user.
- Displays user activity such as commits, issues, and starred repositories.
- Handles errors gracefully (invalid usernames, API failures, connection issues).
- Requires no external libraries (uses Python's standard library).

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the `github_activity.py` file.
    ```bash
    git clone https://github.com/your-username/github-activity-cli.git
    cd github-activity-cli
    ```

2. Make sure Python is installed. You can check your Python version with:
    ```bash
    python --version
    ```

3. (Optional) Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

## Usage

Run the script from the command line, passing a GitHub username as an argument:

```bash
python github_activity.py <username>
