checks = []

def check_router(request):
    parts = request.split()
    if len(parts) < 2:
        return "Bad request format"

    method, path = parts[0], parts[1]

    if method == "POST" and path == "/users":
        id = int(input("Enter id: "))
        checks.append({"id": id})
        return "Check added"

    if method == "GET" and path == "/users":
        return checks

    return "Invalid command"

print(check_router("POST /users"))
print(check_router("GET /users"))