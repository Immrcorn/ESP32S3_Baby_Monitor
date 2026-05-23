# Project: Baby Monitor 23/05/2026

## Definition

- Continuous/on-demand view of the video from browser on local network.
- Ambient sound monitoring with auto detection of significant loud events
- Notfications for when detections occur
- timestamped snapshots of events
- battery monitoring so as to know when the battery needs charged

## High-Level Architecture

**Nursery Unit (Xiao ESP32S3 Sense)**

- Camera (OV3660) -> MJPEG Stream endpoint
- I2S digital microphone -> continuous sampling task that computes amplitude/energy over short windows.
- Detection engine: Configurable threshold + debounce/cooldown. On trigger -> timestamped event + optional JPEG snapshot to SD.
- Web layer: AsyncWebServer (or equivalent) + WebSocket endpoint for real-time alerts and config.
- SD card: Event log + per-event snapshots. Simple FAT management with basic cleanup.
- Wi-Fi client with reconnect + watchdog.

**Parent Side**

- Browser dashboard (served from the ESP or static files) showing:
  - live MJPEG stream.
  - real-time sound level indicator
  - alert panel that lights up
  - basic controls (threshold, camera settings, manual snapshots).
- Optimized for phone browser with multiple viewers supported via WebSocket broadcast

Data Flow (v1)

1. ESP boots → camera + mic tasks start → webserver + WebSocket ready.
2. Parent opens dashboard → stream loads + WebSocket connects.
3. Mic task runs continuously → calculates level → compares to threshold.
4. Threshold crossed (with confirmation window) → ESP:
5. Sends JSON alert over WebSocket to all connected clients.
6. Saves timestamped JPEG to SD (optional).
7. Updates internal event counters.

Browser receives alert → visual highlight + optional Notification API + plays short alert tone.
User sees live view or reviews stored snapshot.
