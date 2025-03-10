get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].discard(event.user)
    return machines
  
  def generate_reports(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print(f"{machine}: {user_list}")

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


events = [
    Event('2020-01-21 12:45:46', 'login', 'my_workstation.local', 'Jordan'),
    Event('2020-01-22 15:33:42', 'logout', 'webserver.local', 'Jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'James'),
    Event('2020-01-22 10:25:34', 'logout', 'my_workstation.local', 'Jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'Jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mail_server.local', 'Chris'),
    Event('2020-01-23 11:24:35', 'login', 'mail_server.local', 'Sarah'),
    Event('2020-01-23 11:24:35', 'logout', 'webserver.local', 'James')
]
users = current_users(events)
print(users)
generate_reports(users)



