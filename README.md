![Status](https://img.shields.io/badge/status-in--progress-orange?style=flat-square)

# 🏠 Real Estate Lead Generation Bot

This bot scrapes FSBO listings from Zillow and emails them daily using SendGrid.

## Features

- Scrapes listings by ZIP code
- Sends email with SendGrid
- Logs results
- Automatable with cron

## Quick Start

1. Upload files to VPS
2. Create Python venv and install:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Edit zillow_scraper.py with your SendGrid API key, email, and ZIP
4. Run manually:
   ```
   python autopilot_leadbot.py
   ```
5. (Optional) Add cron job

## Contact

Developed by: Tech35 / Andrew Lewis
support@tech35.pro
