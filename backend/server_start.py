"""
server_start.py
- creates an application instance and runs the dev server
"""

if __name__ == '__main__':
    from onboard_computer_api.__init__ import create_app
    app = create_app()
    app.run()