#!/usr/bin/env python3
"""
AERIS - Aviation Enterprise Resource Intelligence Suite
Launch script
"""

import subprocess
import os
import sys

def main():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    █████╗ ███████╗██████╗ ██╗███████╗                       ║
    ║   ██╔══██╗██╔════╝██╔══██╗██║██╔════╝                       ║
    ║   ███████║█████╗  ██████╔╝██║███████╗                       ║
    ║   ██╔══██║██╔══╝  ██╔══██╗██║╚════██║                       ║
    ║   ██║  ██║███████╗██║  ██║██║███████║                       ║
    ║   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝                       ║
    ║                                                              ║
    ║   Aviation Enterprise Resource Intelligence Suite           ║
    ║   Manager Resource Planning & Analysis                      ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(script_dir, "ui", "app.py")
    
    if not os.path.exists(app_path):
        print("❌ Error: ui/app.py not found. Make sure the file exists.")
        sys.exit(1)
    
    print("🚀 Launching AERIS Dashboard...")
    subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])

if __name__ == "__main__":
    main()
