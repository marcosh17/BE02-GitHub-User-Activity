import json
import urllib.request
import argparse

# Function to handle command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Retrieve recent activity of a GitHub user")
    parser.add_argument("username", help="GitHub username")
    return parser.parse_args()

# Function to fetch GitHub activity using the API
def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read().decode('utf-8')
                return json.loads(data)
            else:
                print(f"Error: Could not retrieve activity (status code {response.status})")
                return None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: The user '{username}' was not found.")
        else:
            print(f"Error: Could not retrieve activity ({e.reason})")
        return None
    except urllib.error.URLError as e:
        print(f"Error: Could not connect to GitHub. ({e.reason})")
        return None

# Function to display activity in the terminal
def display_activity(events):
    if not events:
        print("No recent events found.")
        return

    # Iterate over the events and show relevant information
    for event in events:
        event_type = event.get('type')
        repo_name = event['repo']['name']
        
        if event_type == "PushEvent":
            commit_count = len(event['payload']['commits'])
            print(f"Pushed {commit_count} commits to {repo_name}")
        elif event_type == "IssuesEvent":
            action = event['payload']['action']
            print(f"{action.capitalize()} an issue in {repo_name}")
        elif event_type == "WatchEvent":
            print(f"Starred {repo_name}")
        else:
            print(f"{event_type.replace('Event', '')} event in {repo_name}")

# Main function to execute the CLI
if __name__ == "__main__":
    args = parse_args()  # Get the username from command-line arguments
    events = fetch_github_activity(args.username)  # Fetch user activity
    display_activity(events)  # Display the activity in the terminal
