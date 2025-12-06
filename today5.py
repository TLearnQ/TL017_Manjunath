import json

sample_files = ["sampleA.json", "sampleB.json"]
processed = 0
failed_test = 0

for name in sample_files:
    try:
        processed += 1
        with open(name) as f:
            json.load(f)
    except:
        failed_test += 1

print("Processed:", processed, "Failed:", failed_test)