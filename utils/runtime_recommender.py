import os
import json
import xml.etree.ElementTree as ET

def recommend_runtime(repo_path):
    recommendations = []

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            path = os.path.join(root, file)

            if file == "requirements.txt":
                # Python typically
                recommendations.append("🐍 Python 3.10+ (virtualenv recommended)")

            elif file == "package.json":
                try:
                    with open(path, "r") as f:
                        data = json.load(f)
                        engines = data.get("engines", {})
                        if "node" in engines:
                            recommendations.append(f"🟢 Node.js {engines['node']} (from package.json)")
                        else:
                            recommendations.append("🟢 Node.js 18+ (LTS)")
                except Exception:
                    recommendations.append("🟢 Node.js 18+ (LTS)")

            elif file == "pom.xml":
                recommendations.append("☕ Java 17+ (Maven project)")

            elif file == "build.gradle":
                recommendations.append("☕ Java 17+ (Gradle project)")

            elif file == "environment.yml":
                recommendations.append("🐍 Python (conda environment)")

    # Remove duplicates while keeping order
    seen = set()
    unique_recommendations = []
    for rec in recommendations:
        if rec not in seen:
            seen.add(rec)
            unique_recommendations.append(rec)

    return unique_recommendations
