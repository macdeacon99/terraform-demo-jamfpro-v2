"""script to update a PR or make one, update this soon."""

import os
import sys
from datetime import datetime
from github import Github
from github.GithubException import GithubException

BASE_BRANCH = "main"
HEAD_BRANCH = os.environ.get("HEAD_BRANCH")
TOKEN = os.environ.get("GITHUB_TOKEN")

print(list(os.environ.keys()))

if not TOKEN:
    raise ValueError("GITHUB_TOKEN env var is none")

GH = Github(TOKEN)


def get_or_create_pr(repo_name, head_branch, base_branch="main", github_token=None):
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
    try:
        repo = GH.get_repo(repo_name)

        existing_prs = list(repo.get_pulls(
            state='open',
            head=f"{repo.owner.login}:{HEAD_BRANCH}",
            base=BASE_BRANCH
        ))

        if existing_prs:
            return existing_prs[0]

        return repo.create_pull(
            title=f"Updates from {HEAD_BRANCH}",
            body=f"Automated PR created from {HEAD_BRANCH}",
            head=HEAD_BRANCH,
            base=BASE_BRANCH
        )

    except GithubException as e:
        print(f"GitHub API error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise



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
    repo_name = os.getenv('GITHUB_REPOSITORY')
    head_branch = os.getenv('GITHUB_HEAD_REF') or os.getenv('GITHUB_REF_NAME')
    base_branch = "main"

    try:
        pr = get_or_create_pr(repo_name, head_branch, base_branch)
        print(pr)
        update_pr_with_text(pr)

    except Exception as e:
        print(f"Failed to process PR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
