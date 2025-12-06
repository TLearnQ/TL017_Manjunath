students = [
    {"name": "A", "attendance": 88, "avg": 77},
    {"name": "B", "attendance": 65, "avg": 88},
    {"name": "C", "attendance": 42, "avg": 48},
    {"name": "D", "attendance": 42, "avg": 48}
]

for s in students:
    if s["attendance"] >= 75 and s["avg"] >= 80:
        result = "Excellent"
    elif s["attendance"] >= 60 and s["avg"] >= 60:
        result = "On Track"
    elif s["attendance"] >=40 and s["avg"] >= 50:
        result = "At Risk"
    else:
        result = "Failing"
    print(s["name"], "->", result)