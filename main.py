from utils.repo_handler import get_repo_source

if __name__ == "__main__":
    repo_path = get_repo_source()
    if repo_path:
        print(f"[DEBUG] Repository available at: {repo_path}")
        # Next steps will go here later
