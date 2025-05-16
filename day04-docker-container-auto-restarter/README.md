# í°³ Day 4 â€“ Docker Container Auto-Restarter

## í³Œ Project: Automatically Restart Crashed or Unhealthy Docker Containers

This script ensures Docker containers are always running and healthy. It detects:
- Containers that have **stopped (exited)**
- Containers that are **unhealthy** (via Docker health checks)

And **restarts them automatically**.

### âœ… Features:
- Detects and restarts `exited` containers
- Checks `health` status for running containers
- Uses Python `docker` SDK

### í³¦ Requirements:
Install Docker SDK for Python:
```bash
pip install docker

