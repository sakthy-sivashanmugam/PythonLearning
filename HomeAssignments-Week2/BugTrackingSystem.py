class BugTracker:
    def __init__(self):
        self.bugs = {}
     
    def add_bug(self, bug_id, description, severity):
        self.bugs[bug_id] = {
            'description': description,
            'severity': severity,
            'status': 'open'
        }
        print(f"Bug {bug_id} added successfully.")

    def update_bug(self, bug_id, new_status):
        if bug_id in self.bugs:
            self.bugs[bug_id]['status'] = new_status
            print(f"Bug {bug_id} updated to status: {new_status}.")
        else:
            print(f"Bug {bug_id} not found.")
    
    def list_all_bugs(self):
        print("Bugs List:")
        for bug_id, details in self.bugs.items():
            print(f"ID: {bug_id}, Description: {details['description']}, Severity: {details['severity']}, Status: {details['status']}")

if __name__ == "__main__":
    tracker = BugTracker()
    tracker.add_bug(101, "Login button not working", "High")
    tracker.add_bug(102, "Page crashes on load", "Critical")
    tracker.list_all_bugs()
    tracker.update_bug(101, "in progress")
    tracker.list_all_bugs()
    tracker.update_bug(103, "closed")  # Trying to update a non-existing bug
