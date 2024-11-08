"""
GitHub Pull Request Management Script

This script handles the creation and updating of GitHub Pull Requests with JSON data 
from workflow outputs. It reads PR information and JSON data from a dropped file 
and posts formatted comments to the specified PR.

Dependencies:
    - PyGithub
    - Valid GitHub authentication credentials
    - outputs.json file with required fields (pr_number, plan_output if applicable)
    - Defined constants: DATA_FILE_FP, REPO_PATH, TYPE

Usage:
    Run the script directly to process the outputs.json file and update
    the corresponding GitHub PR with formatted JSON comments.

Author: Unknown
"""

import os
import github
from github.GithubException import GithubException
import github.PullRequest
print(os.getcwd())
from .shared import *

REPO = os.environ.get("REPO")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
ARTIFACT_PATH = os.environ.get("ARTIFACT_PATH")
TARGET_PR_NUMBER = os.environ.get("TARGET_PR_NUMBER")

ENV_VARS = [
    REPO,
    GITHUB_TOKEN,
    ARTIFACT_PATH,
    TARGET_PR_NUMBER
]

if any(i == "" or i == None for i in ENV_VARS):
    raise KeyError(f"one or more env vars are empty: {ENV_VARS}")


# Global GH connection
GH = github.Github(GITHUB_TOKEN)


def get_pr():
    """
    Retrieves a specific Pull Request from GitHub using the PR number stored in outputs.json.

    The function reads the PR number from a dropped file, then uses the GitHub API
    to fetch the corresponding Pull Request object.

    Returns:
        github.PullRequest.PullRequest: The GitHub Pull Request object if found

    Raises:
        GithubException: If the PR cannot be found or there's a GitHub API error
        FileNotFoundError: If the outputs.json file cannot be found
        Exception: For any other unexpected errors that occur during execution

    Dependencies:
        - Requires valid GitHub authentication setup
        - Requires REPO_PATH constant to be defined
        - Requires outputs.json file with 'pr_number' field
    """

    file = open_artifact(ARTIFACT_PATH)
    target_pr_id = file["pr_number"]
    print(f"LOG: {target_pr_id}")
    try:
        repo = GH.get_repo(REPO)
        pr = repo.get_pull(int(target_pr_id))

        if pr:
            return pr


    except GithubException as e:
        print(f"GitHub API error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

    raise GithubException(f"no pr found at id: {target_pr_id}")



def update_pr_with_text(pr: github.PullRequest):
    """
    Updates a GitHub Pull Request by adding comments containing JSON data from outputs.json.

    If TYPE is "plan", adds both the plan_output and complete JSON data as separate comments.
    Otherwise, only adds the complete JSON data. All JSON is wrapped in Markdown formatting.

    Args:
        pr (github.PullRequest): The Pull Request object to update with comments

    Raises:
        GithubException: If there's an error creating comments on the PR
        FileNotFoundError: If outputs.json cannot be found
        KeyError: If 'plan_output' is missing from json_data when TYPE is "plan"

    Dependencies:
        - Requires TYPE constant to be defined
        - Requires open_artifact() and wrap_json_markdown() functions
        - Requires outputs.json file with appropriate structure

    Example:
        >>> pr = get_pr()
        >>> update_pr_with_text(pr)  # Adds formatted JSON comment(s) to PR
    """


    comments = wrap_json_markdown(open_artifact(ARTIFACT_PATH))

    try:
        pr.create_issue_comment(c)

    except GithubException as e:
        print(f"Error adding comment: {e}")
        raise


def main():
    """
    Main entry point that retrieves a GitHub Pull Request and updates it with JSON data.

    This function orchestrates the workflow by:
    1. Retrieving a PR using the ID from outputs.json
    2. Adding formatted JSON comment(s) to the PR

    Raises:
        GithubException: If PR cannot be found or updated
        FileNotFoundError: If required files are missing
        Exception: For any other unexpected errors

    Dependencies:
        - Requires get_pr() and update_pr_with_text() functions
        - Requires properly configured GitHub authentication
        - Requires outputs.json file with required fields
    """

    update_pr_with_text(get_pr())



if __name__ == "__main__":
    main()
