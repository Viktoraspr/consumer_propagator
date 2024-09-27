import argparse
from dataclasses import dataclass


def parse_args():
    parser = argparse.ArgumentParser(description="Event Propagator arguments")
    parser.add_argument(
        "--period",
        type=int,
        required=False,
        default=3,
        help="Time period between sending events in seconds",
    )
    parser.add_argument(
        "--endpoint",
        type=str,
        required=False,
        default="http://localhost:8000/event",
        help="HTTP API endpoint for sending events",
    )
    parser.add_argument(
        "--events_file",
        type=str,
        required=False,
        default="evens/evens.json",
        help="Path to the JSON events file",
    )
    parser.add_argument(
        "--working_time",
        type=int,
        required=False,
        default=10,
        help="Running script time",
    )
    return parser.parse_args()

@dataclass
class Propagator:
    period: int
    endpoint: str
    events_file: str
    working_time: int


def get_config() -> Propagator:
    args = parse_args()

    propagator = Propagator(
        period=args.period,
        endpoint=args.endpoint,
        events_file=args.events_file,
        working_time=args.working_time,
    )
    return propagator


