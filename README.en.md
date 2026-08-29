# Port Scanner

A multi-threaded scanner that detects open ports on a target host.

## What Does It Do?

It detects which ports are open on a server and which services run on them. Open ports are a system's doors to the outside world; mapping them is the first step of a security assessment.

## Features

- Scans common ports and their services
- Multi-threaded scanning (fast)
- Reports open ports and services

## Usage

    python port_scanner.py

## How It Works

It attempts a connection to each port. If the connection succeeds, the port is open. Each port is scanned in a separate thread so all are tried simultaneously, making the scan much faster than sequential checking.

## Legal Notice

Only use on your own systems or targets you have permission to test. Unauthorized port scanning is illegal in many countries.

## Author

Muhammed Emin Şeker — Computer Engineering Student
GitHub: https://github.com/muhammedeminsekerr
