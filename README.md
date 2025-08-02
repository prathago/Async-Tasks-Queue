# Async Task Queue (Simulated Background Jobs)

## Overview
This project simulates background tasks (like downloading data, processing files, writing logs) using Python's `asyncio` library. It demonstrates non-blocking concurrent execution with an `asyncio.Queue`.

## Key Concepts
- **Asyncio**: A Python library for writing concurrent code using async/await syntax.
- **Event Loop**: Manages execution of async tasks.
- **Asyncio.Queue**: Thread-safe queue for scheduling async jobs.
- **Decorators**: Used to log execution time of each task.

## How to Run
1. Install requirements:
```bash
pip install -r requirements.txt