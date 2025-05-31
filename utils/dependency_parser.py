import os
import json
import xml.etree.ElementTree as ET

def parse_requirements_txt(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def parse_package_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
        return list(data.get("dependencies", {}).keys())

def parse_pom_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    ns = {'m': 'http://maven.apache.org/POM/4.0.0'}
    dependencies = []
    for dep in root.findall(".//m:dependency", ns):
        group_id = dep.find("m:groupId", ns)
        artifact_id = dep.find("m:artifactId", ns)
        if group_id is not None and artifact_id is not None:
            dependencies.append(f"{group_id.text}:{artifact_id.text}")
    return dependencies

def parse_dependencies(repo_path):
    results = {}

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            full_path = os.path.join(root, file)

            if file == "requirements.txt":
                results["Python (requirements.txt)"] = parse_requirements_txt(full_path)
            elif file == "package.json":
                results["JavaScript (package.json)"] = parse_package_json(full_path)
            elif file == "pom.xml":
                results["Java (pom.xml)"] = parse_pom_xml(full_path)

    return results
