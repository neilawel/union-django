import subprocess

def run_command(command):
    """Run a command in the shell and print the output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(f"Running command: {command}")
    print("Output:")
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)

def main():
    # Collect static files
    run_command('python manage.py collectstatic --noinput')
    
    # Apply database migrations
    run_command('python manage.py migrate')

if __name__ == "__main__":
    main()
