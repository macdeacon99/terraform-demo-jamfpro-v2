"""script to update a PR or make one, update this soon."""

import os
import sys
from datetime import datetime
import json
from github import Github
from github.GithubException import GithubException

TOKEN = os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    raise ValueError("GITHUB_TOKEN env var is none")

GH = Github(TOKEN)
DROPFILE_FN = "outputs.json"


def open_drop_file() -> dict:
    with open(DROPFILE_FN, "r", encoding="UTF-8") as f:
        return json.load(f)


def get_pr():
    """
    Get existing PR or create a new one between branches.
    
    Args:
        repo_name (str): Repository name in format "owner/repo"
        head_branch (str): Branch containing changes
        base_branch (str): Target branch for PR (default: main)
        github_token (str): GitHub access token
    
    Returns:
        github.PullRequest.PullRequest: Pull request object
    """
    file = open_drop_file()
    target_pr_id = file["pr_ref"]
    print(f"LOG: {target_pr_id}")
    try:
        repo = GH.get_repo("deploymenttheory/terraform-demo-jamfpro-v2")
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



def update_pr_with_text(pr):
    """
    Add a comment to the PR with specified text.
    
    Args:
        pr: github.PullRequest.PullRequest object
        message (str): Comment text to add
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    comment = f"This is an automatically aded comment: {timestamp}"

    try:
        pr.create_issue_comment(comment)
        print(f"Added comment to PR #{pr.number}")

    except GithubException as e:
        print(f"Error adding comment: {e}")
        raise


def main():
    pr = get_pr()
    update_pr_with_text(pr)



if __name__ == "__main__":
    main()
