#!/bin/sh

# Install the required Python packages
pip install -r requirements.txt

# Activate the virtual environment
source venv/bin/activate

# Start the Flask app
python email_spam_detector.py