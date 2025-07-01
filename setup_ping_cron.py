#!/usr/bin/env python3
"""
Script to set up a cron job that pings statuskuo.onrender.com every minute
to prevent the server from going to sleep on free hosting platforms.
"""
import os
import subprocess
import sys
from pathlib import Path

def get_project_path():
    """Get the absolute path to the Django project."""
    return Path(__file__).parent.absolute()

def get_python_path():
    """Get the current Python interpreter path."""
    return sys.executable

def create_cron_entry():
    """Create the cron job entry."""
    project_path = get_project_path()
    python_path = get_python_path()
    
    # Create the cron command
    cron_command = f"* * * * * cd {project_path} && {python_path} manage.py ping_site >> /tmp/django_ping.log 2>&1"
    
    return cron_command

def setup_cron():
    """Set up the cron job."""
    try:
        # Get current crontab
        result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
        current_cron = result.stdout if result.returncode == 0 else ""
        
        # Check if our job already exists
        cron_command = create_cron_entry()
        if "manage.py ping_site" in current_cron:
            print("Ping cron job already exists!")
            return
        
        # Add our cron job
        new_cron = current_cron + cron_command + "\n"
        
        # Write new crontab
        process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE, text=True)
        process.communicate(input=new_cron)
        
        if process.returncode == 0:
            print("✅ Cron job added successfully!")
            print(f"Command: {cron_command}")
            print("The site will be pinged every minute.")
            print("Logs will be written to /tmp/django_ping.log")
        else:
            print("❌ Failed to add cron job")
            
    except FileNotFoundError:
        print("❌ crontab command not found. Please install cron.")
    except Exception as e:
        print(f"❌ Error setting up cron job: {e}")

def remove_cron():
    """Remove the ping cron job."""
    try:
        # Get current crontab
        result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
        if result.returncode != 0:
            print("No crontab found.")
            return
            
        current_cron = result.stdout
        
        # Remove lines containing our ping command
        lines = current_cron.split('\n')
        filtered_lines = [line for line in lines if "manage.py ping_site" not in line]
        new_cron = '\n'.join(filtered_lines)
        
        # Write new crontab
        process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE, text=True)
        process.communicate(input=new_cron)
        
        if process.returncode == 0:
            print("✅ Ping cron job removed successfully!")
        else:
            print("❌ Failed to remove cron job")
            
    except Exception as e:
        print(f"❌ Error removing cron job: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "remove":
        remove_cron()
    else:
        print("Setting up cron job to ping statuskuo.onrender.com every minute...")
        print("This will prevent your Render app from sleeping.")
        print()
        setup_cron()
        print()
        print("To remove this cron job later, run:")
        print(f"python {__file__} remove")