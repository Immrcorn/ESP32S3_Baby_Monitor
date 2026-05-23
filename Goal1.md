## Goal

- Reliable I2S microphone capture + continuous level metering + threshold detection logic running on the ESP, with the threshold value changeable from the browser and level visible on the dashboard. Audio burst streaming can be stubbed or added at the end of this chunk once the metering works.

## What success looks like after Goal 1

- ESP boots, camera stream still works.
- Mic samples continuously in its own task.
- Level (e.g. 0–100 or dB-ish) updates in browser every 200–500 ms via lightweight messages.
- Slider in dashboard changes threshold live; ESP reacts.
- When threshold crossed: serial print + LED or simple flag (we can wire the short audio start here or in a quick follow-up).
- No crashes, stable heap, clean reconnect behavior.
