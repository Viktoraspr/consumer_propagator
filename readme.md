# Event System

This project consists of two services: `Event Propagator` and `Event Consumer`. The `Event Propagator` periodically sends predefined JSON events to a specific HTTP API endpoint, and the `Event Consumer` accepts these events and persists them to a database.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10 or higher
- Poetry (Package manager for Python)

### Installing

1. **Clone the repository**

   ```shell
   git clone <repository-url>
   cd event_system

2**Install dependencies**

   poetry install

### Running
You can use the Makefile to run both the Event Consumer and Event Propagator.
Needs to run in different terminals.

make run-consumer
make run-propagator
   
### Config

Consumer: consumer/consumer_config.py
Propagator: propagator/propagator.py