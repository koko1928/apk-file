import os
import subprocess

package_name = input("Enter package name: ")

try:
    output = subprocess.check_output(['adb', 'shell', 'pm', 'path', package_name])
    apk_path = output.decode('utf-8').strip().replace('package:', '')
    apk_file = os.path.basename(apk_path)
    subprocess.check_output(['adb', 'pull', apk_path, apk_file])
    print("APK file extracted successfully.")
except subprocess.CalledProcessError:
    print("Error: Failed to extract APK file.")
