import requests
import json
import random
import time
import os
from propagator_config import get_config


class EventPropagator:
    def __init__(self, period: int, endpoint: str, events_file: str, working_time:int = 60):
        self.period = period
        self.endpoint = endpoint
        self.events_file = events_file
        self.working_time = working_time
        self.events = self.load_events()

    def load_events(self):
        try:
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.events_file)
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Events file {self.events_file} not found.")

    def propagate_event(self):
        events = self.load_events()
        if not events:
            print("No events to send.")
            return None
        event = random.choice(self.load_events())
        try:
            response = requests.post(self.endpoint, json=event)
            print(f"Sent event: {event}, Response: {response.status_code}, {response.content}")
        except requests.exceptions.RequestException as error:
            print(f"Failed to send event: {error}")

    def start(self):
        start_time = time.time()
        while start_time + self.working_time > time.time():
            self.propagate_event()
            time.sleep(self.period)


if __name__ == '__main__':
    config = get_config()
    propagator = EventPropagator(
        period=config.period,
        endpoint=config.endpoint,
        events_file=config.events_file,
        working_time=config.working_time,
    )
    propagator.start()

