import argparse
from dataclasses import dataclass


def parse_args():
    parser = argparse.ArgumentParser(description="Event Consumer arguments")
    parser.add_argument(
        "--host",
        type=str,
        required=False,
        default="0.0.0.0",
        help="Port for the HTTP API endpoint",
    )
    parser.add_argument(
        "--port",
        type=int,
        required=False,
        default=8000,
        help="Port for the HTTP API endpoint",
    )
    parser.add_argument(
        "--database",
        type=str,
        required=False,
        default="sqlite:///events.db",
        help="Database URL for storing events",
    )
    return parser.parse_args()


@dataclass
class Consumer:
    host: str
    port: int
    database: str


def get_config() -> Consumer:
    args = parse_args()

    consumer = Consumer(
        host=args.host,
        port=args.port,
        database=args.database,
    )
    return consumer
