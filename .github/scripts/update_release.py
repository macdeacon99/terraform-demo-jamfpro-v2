"""script to update the text on a release"""

import os
import json
import github
from github.GithubException import GithubException

REPO_PATH = "deploymenttheory/terraform-demo-jamfpro-v2"

TOKEN = os.environ.get("GITHUB_TOKEN")
DROPFILE_PATH = os.environ.get("ARTIFACT_PATH")
GIT_TAG = os.environ.get("GIT_TAG")

ENV_VARS = [TOKEN, DROPFILE_PATH, GIT_TAG]

if any (i == "" for i in ENV_VARS):
    raise KeyError(f"one or more env vars are empty: {ENV_VARS}")


GH = github.Github(TOKEN)

def open_drop_file() -> dict:
    """opens the drop file"""
    with open(DROPFILE_PATH + "/outputs.json", "r", encoding="UTF-8") as f:
        return json.load(f)
    

def get_update_release():
    """gets a tag"""
    try:
        repo = GH.get_repo(REPO_PATH)
        release = repo.get_release(GIT_TAG)

    except GithubException as e:
        print(f"GitHub API error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

    file = open_drop_file()
    message = f"{release.body}\nApply Result: {file["status"]}"
    release.update_release(
        name=release.tag_name,
        message=message
    )


def main():
    get_update_release()


if __name__ == "__main__":
    main()

    