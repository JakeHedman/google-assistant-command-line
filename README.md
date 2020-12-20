# Google Assistant Command Line

> :warning: This is a **really** ugly hack. It's brittle, inefficient and
> probably unreliable. Please don't do this.

## What?

A dirty setup to trigger any Google Assistant command from the command line.

- Short commands are usually submitted within ~250ms on my machine.
- The response it not captured, so you won't be able to get answers for
  questions or an error description if something goes wrong.
- Requires a virtual android device to be running (or a spare phone I guess).


## Demo

![Demo](demo.gif?raw=true "Demo")

## Why?

The official Google Assistant API doesn't support all commands, e.g. starting a
netflix show on a chromecast. If you **really** want to automate commands like
that, you can try this setup. I wouldn't recommend it though. YMMV!

Example triggers:

- Run Google Assistant commands from your command line (probably over ssh).
- Use Home Assistant (Shell Command) to run Google Assistant commands.
- Use IFTTT (Webhooks) to run Google Assistant commands.

Example commands:

- Start Youtube, Netflix, Disney+ etc show on a Chromecast.
- Start music from Spotify on a nest speaker.
- Turn off/on lights.
- Start music on Sonos speakers.

## How?

- Create a virtual android device.
- Sign in to your Google Account.
- Set your preferred input mode to text.
- Use ADB to automatically type commands in the Google Assistant app.

> *Thanks, I hate it.*
>
> – Everyone

## Instructions

### Create a virtual device

Use [AVD](https://developer.android.com/studio/run/managing-avds) or
[Genymotion](https://www.genymotion.com/) to create a virtual device. AVD can
be started automatically and run in headless mode which is nice, but genymotion
is a lot faster on my machine so that's what i ended up using.

These are the genymotion settings which I used:

![Genymotion settings](genymotion_settings.png?raw=true "Genymotion settings")

Make sure Google Services are installed on the virtual device.

### Sign in

Your virtual device has to be signed in to a Google Account to access your Home
etc.

### Set your preferred input mode

Click your avatar in Google Assistant and open `Settings -> General ->
Preferred input`, choose Keyboard.


### (Optional) Change the default launcher

I installed and changed my default launcher to [Null
Launcher](https://play.google.com/store/apps/details?id=com.notriddle.null_launcer&hl=en&gl=US)
to avoid wasting performance on running some fancy launcher. I'm not sure if it
makes any difference.

### Run script

Install the [uiautomator python
module](https://github.com/xiaocong/uiautomator) and make sure `ANDROID_HOME`
is set.

Download `assistant.py` from this repo and run:

```sh
python3 assistant.py "turn off the lights"
```

## Routines

Using
[routines](https://support.google.com/assistant/answer/7672035?co=GENIE.Platform%3DAndroid&hl=en)
instead of regular commands can be helpful since it allows you to edit which
command is executed from your assistant settings.

Shortcuts to routines can also be added to the home screen, editing
`assistant.py` to launch a shortcut might be more reliable than typing text
into the assistant app.

## Help! It's not working

Try editing `assistant.py`, it might take some trial and error to get this
working for your setup.
