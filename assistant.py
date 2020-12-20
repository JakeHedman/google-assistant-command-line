import sys
import time
import os
from uiautomator import device

command = sys.argv[1]

launch_assistant_command = 'am start -S com.google.android.apps.googleassistant/.AssistantActivity'

if not device(resourceId='com.google.android.googlequicksearchbox:id/input_text').exists:
  print('Text input not found, launching assistant app')
  device.server.adb.cmd('shell', launch_assistant_command).wait()
else:
  print('Assistant is already running')

print('Clicking text input')
input_text = device(resourceId='com.google.android.googlequicksearchbox:id/input_text')
input_text.click()

print('Typing text')
device.server.adb.cmd('shell', f'input text "\'{command}\n\'";').wait()

print('Clicking home button to close assistant')
device.server.adb.cmd('shell', 'input keyevent KEYCODE_HOME').wait()

print('Relaunching assistant to prepare for next invocation')
device.server.adb.cmd('shell', launch_assistant_command).wait()
