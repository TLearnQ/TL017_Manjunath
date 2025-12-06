pages = [[100, 200], [300, 400], []]
log_list = [
"INFO: Connection Successfull",
"ERROR:Timeout",
"INFO: Retry"
 ]
results = []

for p in pages:
    log_list.append("Reading page...")
    if not p:
        log_list.append("Ending pagination")
        break
    results.extend(p)

print(results)
print("Log steps:")
for entry in log_list:
    print(entry)