import os
import platform
import subprocess
import shutil

def get_confirmation():
    user_input = input("Are you sure you want to shut down the computer? (yes/no): ").lower()
    return user_input == 'yes'

def cleanup_before_shutdown():
    # Add your cleanup actions here
    directory_to_delete = "/path/to/your/directory"
    if os.path.exists(directory_to_delete):
        shutil.rmtree(directory_to_delete)
        print(f"Deleted {directory_to_delete}")
    else:
        print(f"{directory_to_delete} does not exist. Skipping cleanup.")

def factory_reset():
    try:
        # Add your factory reset actions here for specific operating systems
        operating_system = platform.system()
        
        if operating_system == 'Windows':
            # Example: Using systemreset command for Windows (this may vary by Windows version)
            subprocess.run(['systemreset', '/factoryreset', '/quiet'], check=True)
            print("Factory reset initiated.")
        elif operating_system == 'Linux' or operating_system == 'Darwin':
            print("Factory reset is not supported on Linux or macOS.")
        else:
            print(f"Operating system {operating_system} not supported for factory reset.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred while trying to perform a factory reset: {e}")

def shutdown_computer(delay=None, force=False, confirm=True):
    try:
        operating_system = platform.system()

        if confirm and not get_confirmation():
            print("Shutdown and factory reset aborted.")
            return

        # Perform cleanup actions before shutdown
        cleanup_before_shutdown()

        # Perform factory reset before shutdown (specific to Windows in this example)
        factory_reset()

        # Shutdown the computer
        command = None
        if operating_system == 'Windows':
            command = ['shutdown', '/s']
            if delay is not None:
                command.extend(['/t', str(delay)])
            if force:
                command.append('/f')
        elif operating_system == 'Linux' or operating_system == 'Darwin':
            command = ['shutdown', '-h', 'now']
            if delay is not None:
                print("Delay option is not supported on Linux or macOS. Ignoring.")
        else:
            print(f"Operating system {operating_system} not supported.")
            return

        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred while trying to shut down the computer: {e}")

# Example usage:
shutdown_computer(confirm=True)
