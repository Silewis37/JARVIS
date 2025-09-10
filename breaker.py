import json
import os

def split_domains(input_file, output_dir="domains"):
    # Make output directory if not exists
    os.makedirs(output_dir, exist_ok=True)

    # Load the main JSON file
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Iterate through each domain entry
    for entry in data:
        domain = entry.get("domain")
        services = entry.get("services", {})

        # Structure new JSON
        domain_data = {
            "Domain": domain,
            "Services": services
        }

        # Save to file
        output_path = os.path.join(output_dir, f"{domain}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(domain_data, f, indent=4, ensure_ascii=False)

        print(f"Created {output_path}")

if __name__ == "__main__":
    split_domains("ha_services.json")
