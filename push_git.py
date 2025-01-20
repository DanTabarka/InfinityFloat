#!/usr/bin/env python3
import subprocess
import sys

def git_push(commit_message):
    try:
        subprocess.run(["git", "add", "."], check=True)
        print("[INFO] All changes added to staging area.")

        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"[INFO] Changes committed with message: {commit_message}")

        subprocess.run(["git", "push"], check=True)
        print("[INFO] Changes pushed to remote repository.")

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Git command failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python push_git.py \"commit message\"")
        sys.exit(1)

    commit_message = sys.argv[1]
    git_push(commit_message)
