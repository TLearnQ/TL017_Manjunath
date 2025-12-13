import yaml
import json
import logging

logging.basicConfig(
    filename="parse.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    force=True
)

def log_event(event, data):
    logging.info(json.dumps({"event": event, "data": data}))

log_event("TEST_EVENT", {"status": "ok"})

def parse_openapi(filepath):
    with open("YAML files/TS24283_Lms_Reporting.yaml", "r") as f:
        spec = yaml.safe_load(f)

    api_title = spec.get("info", {}).get("title")
    paths = spec.get("paths", {})
    endpoints = []

    for path, methods in paths.items():
        for method, details in methods.items():
            endpoints.append({
                "path": path,
                "method": method.upper(),
                "summary": details.get("summary"),
                "auth": spec.get("components", {}).get("securitySchemes", {}),
            })

    return {
        "title": api_title,
        "endpoint_count": len(endpoints),
        "endpoints": endpoints,
    }

if __name__ == "__main__":
    result = parse_openapi("TS24283_Lms_Information.yaml")
    print(json.dumps(result, indent=2))
    with open("output.json", "w") as out_file:
        json.dump(result, out_file, indent=2)
        print("JSON output written to output.json")