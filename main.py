from utils.repo_handler import get_repo_source
from utils.language_detector import detect_languages
from utils.dependency_parser import parse_dependencies

if __name__ == "__main__":
    repo_path = get_repo_source()

    if repo_path:
        print(f"\n[DEBUG] Analyzing repo at: {repo_path}")

        # Step 2: Detect Languages
        languages = detect_languages(repo_path)
        print("\n📦 Languages Detected:")
        for lang, count in languages.items():
            print(f"  - {lang}: {count} file(s)")

        # Step 3: Parse Dependencies
        deps = parse_dependencies(repo_path)
        print("\n📦 Dependencies Detected:")
        if deps:
            for tool, packages in deps.items():
                print(f"\n  🔹 {tool}:")
                for pkg in packages:
                    print(f"    - {pkg}")
        else:
            print("  - No recognized dependency files found.")
