## Goal

- Reliable I2S microphone capture + continuous level metering + threshold detection logic running on the ESP, with the threshold value changeable from the browser and level visible on the dashboard. Audio burst streaming can be stubbed or added at the end of this chunk once the metering works.

## What success looks like after Goal 1

- ESP boots, camera stream still works.
- Mic samples continuously in its own task.
- Level (e.g. 0–100 or dB-ish) updates in browser every 200–500 ms via lightweight messages.
- Slider in dashboard changes threshold live; ESP reacts.
- When threshold crossed: serial print + LED or simple flag (we can wire the short audio start here or in a quick follow-up).
- No crashes, stable heap, clean reconnect behavior.

### Key elements

- I2S config: standard 16 kHz (or 8 kHz to start), 16-bit, mono or stereo as supported by the digital mic on the Sense board. Use the correct pins for this variant.
- FreeRTOS task or high-priority loop for sampling + level calculation (RMS over ~100–300 ms windows). Keep it lightweight.
- Simple threshold comparison with debounce (ignore re-triggers for N seconds after one event).
- WebSocket (or your current mechanism) for two directions: ESP → browser for level + events; browser → ESP for new threshold value.
- Non-volatile storage (Preferences) for last threshold so it survives reboot.
- Dashboard JS: slider + live level bar + status text. Fullscreen + wake helper can be added in the same HTML pass.
