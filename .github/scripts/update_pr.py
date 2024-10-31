"""script to update a PR or make one, update this soon."""

import os
import json
from github import Github
from github.GithubException import GithubException

TOKEN = os.environ.get("GITHUB_TOKEN")
DROPFILE_PATH = os.environ.get("ARTIFACT_PATH")
TYPE = os.environ.get("RUN_TYPE")

ENV_VARS = [TOKEN, DROPFILE_PATH, TYPE]

if any(i == "" for i in ENV_VARS):
    raise KeyError(f"one or more env vars are empty: {ENV_VARS}")

GH = Github(TOKEN)

def open_drop_file() -> dict:
    """opens the drop file"""
    with open(DROPFILE_PATH + "/outputs.json", "r", encoding="UTF-8") as f:
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
    target_pr_id = file["pr_number"]
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
    comments = []
    with open(DROPFILE_PATH + "/outputs.json", "r", encoding="UTF-8") as f:
        json_data = json.load(f)

        if TYPE == "plan":
            comments.append(json.dumps(json_data["plan_output"], indent=2))

        comments.append(json.dumps(json_data, indent=2))

    try:
        for c in comments:
            pr.create_issue_comment(c)

    except GithubException as e:
        print(f"Error adding comment: {e}")
        raise


def main():
    """main"""
    pr = get_pr()
    update_pr_with_text(pr)



if __name__ == "__main__":
    main()
