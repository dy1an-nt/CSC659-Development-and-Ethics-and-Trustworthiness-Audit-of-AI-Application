ACTION_MAP = {
    ("admin", "create", "user"):     "Admin created a user",
    ("admin", "create", "resource"): "Admin created a resource",
    ("admin", "delete", "user"):     "Admin deleted a user",
    ("admin", "delete", "resource"): "Admin deleted a resource",
    ("guest", "read", "post"):       "Guest read a post",
    ("guest", "read", "resource"):   "Guest read a resource",
}

def process_action_clean(user_type: str, action: str, target: str) -> str:
    key = (user_type, action, target)
    if key in ACTION_MAP:
        return ACTION_MAP[key]
    if user_type == "guest" and action != "read":
        return "Guest: action not permitted"
    if user_type not in ("admin", "guest"):
        return "Unknown user type"
    return f"{user_type}: unknown action/target combination"

test_cases = [
    ("admin", "create", "user"),
    ("admin", "delete", "resource"),
    ("guest", "read", "post"),
    ("guest", "delete", "post"),
    ("hacker", "exploit", "db"),
]

print("Results:")
for args in test_cases:
    print(f"  {args} -> {process_action_clean(*args)}")
