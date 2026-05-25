# ESP32-S3 Baby Monitor

**My local baby monitor project on ESP32-S3 — live camera + audio with a web dashboard I built on top of a Seeed template.**

This thing streams video and audio over your home WiFi so you can check on the kid from your phone or laptop without sending anything to the cloud.

I started with a template/example from the Seeed GitHub repo (they have solid ESP32-S3 stuff), then modified the hell out of it to get a proper dashboard working and add decent audio streaming with a ring buffer + sound alerts.

---

## What It Does Right Now

- Live camera feed you can watch in the browser
- Audio capture with a ring buffer so it doesn't glitch out
- Sound level monitoring and basic alerts when it hears something loud (cry detection is the goal)
- Nice-ish web dashboard with stream controls and status stuff
- All running locally on your network

It's still very much a work in progress (I'm actively tweaking it), but the core pieces — camera streaming, web server, dashboard, and audio pipeline — are up and running.

Recent stuff I added/fixed:

- Switched everything over to ESP32 Arduino core 3.x (2.x was being a pain)
- Built out the dashboard and hooked up stream controls
- Got audio ring buffer + sound alert logic working
- Tweaked frame size and JPEG quality to get better frame rates
- Cleaned up IP display and general dashboard layout

---

## Hardware I’m Using

- ESP32-S3 board with camera (PSRAM is pretty much required for decent performance)
- I2S Microphone on board.
- Stable power (this thing pulls current when the camera and WiFi are both cooking

---

## How to Get It Running

### 1. Grab the code

```bash
git clone https://github.com/Immrcorn/ESP32S3_Baby_Monitor.git
```

### 2. Open it in Arduino IDE

### 3. Update your secrets & pins (don’t skip this)

You’ll need to put in:

- Your WiFi SSID/password
- The correct camera pin definitions for **your** ESP32-S3 board
- Mic pins and whatever audio settings you’re using
- Sound threshold if you want to tune the alerts

I left placeholders for WiFi. Fill them in or it’s not gonna connect or show video.

### 4. Board settings

- Use **ESP32 Arduino core 3.x** (this project broke on 2.x)
- Enable PSRAM if your board has it
- Pick a partition scheme with enough room

### 5. Upload & watch Serial

Open Serial Monitor at 115200. You should see it connect to WiFi, init the camera, and print the IP address.

Then just go to that IP in your browser on the same network.

---

## Using the Dashboard

Open the IP in Chrome/Firefox/whatever on your phone or computer.

You should get:

- The live video stream
- Audio level display
- Some buttons to control the stream
- Status info (IP, etc.)
- Alerts when sound spikes

It’s responsive enough to use on mobile.

If the stream feels laggy, I already dropped the frame size and played with JPEG quality — you can tweak those values in the code if you want even more performance.

---

## Project Notes & Status (May 2026)

This is actively being worked on.

**Issues:**

- Tuning the sound detection so it actually catches cries without false positives
- Making the dashboard prettier / more reliable
- Adding persistent settings
- Doesn't seem to get enough power from outlet or power bank.
  - Apparently detached from computer the module doesn't establish WiFi connection.
- Not tested with Battery attached.

If you’re building something similar, feel free to steal whatever is useful here.

---

## Troubleshooting (Common Pain Points)

- Camera won’t start → Wrong pins or forgot to enable PSRAM / using core 2.x
- No WiFi → Check the credentials you put in
- Choppy audio → Ring buffer size or sample rate needs tuning
- Dashboard looks broken → Hard refresh or check Serial for errors
- Super low FPS → Play with the frame size / quality numbers I already adjusted

Serial output is your best friend here.

---

## Privacy Note

Everything stays on your local network. No cloud accounts, no “smart” features phoning home. That was the whole point.

If you want remote access, throw it behind a VPN. Don’t expose it directly to the internet.

---

## Credit

Started from a Official Seeed GitHub template/example and then I went to town on it.

Feel free to use/modify. If you make something cool with it, I’d love to hear about it.

---

Open an issue or hit me up on X (@immrcorn) if you have questions or improvements.
