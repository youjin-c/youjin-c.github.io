---
layout: project
title: Purro Stick
---

# Purro Stick

<div class="side-by-side-images">
<img src="/images/Purro-Stick/device_smile.jpg" alt="Purro Stick in hand, Purro smiling above a list of recent tool calls" style="max-width: 48%;">
<video src="/images/Purro-Stick/approve.mp4" poster="/images/Purro-Stick/approve_poster.jpg" autoplay loop muted playsinline controls style="max-width: 48%; height: auto; border-radius: 8px;"></video>
</div>

Purro Stick is a desk pet for Claude Code. A small orange cat lives on an M5StickC Plus next to my keyboard and shows what my coding agent is doing: it looks busy while tools are running, perks up when the agent needs my attention, and falls asleep when the session ends. When Claude Code asks for permission to run something, I can approve or deny it by pressing a button on the stick. In the video above, Claude Code is waiting for approval to run a command; I press the front button and the terminal carries on.

## Why I Built It

The idea comes from Anthropic's open-source [claude-desktop-buddy](https://github.com/anthropics/claude-desktop-buddy) and Felix Rieseberg's demo of a physical pet that reacts to Claude. In that setup the Claude desktop app is the Bluetooth bridge to the device. I work in the Claude Code CLI, so I did not want a desktop app running in the background just to keep a pet alive.

The firmware's Bluetooth protocol is fully documented, so I wrote the host side myself: a small Python daemon that listens to Claude Code and talks to the stick directly.

## How It Works

<div style="display:flex;flex-direction:column;gap:0.6rem;margin:2rem 0;">
<div style="background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:1rem 1.25rem;"><strong>Claude Code CLI</strong><br><span style="color:var(--text-secondary);">Any number of terminal windows. HTTP hooks fire on session start, tool use, notifications, stop, and permission requests.</span></div>
<div style="text-align:center;color:var(--text-muted);">HTTP on localhost &darr;</div>
<div style="background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:1rem 1.25rem;"><strong>Bridge daemon (Python)</strong><br><span style="color:var(--text-secondary);">Runs in the background and restarts on login. Merges events from every session into one state, counts output tokens from the session transcripts, and holds a permission request open until a button is pressed.</span></div>
<div style="text-align:center;color:var(--text-muted);">Bluetooth LE, Nordic UART &darr;&uarr;</div>
<div style="background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:1rem 1.25rem;"><strong>Purro (M5StickC Plus)</strong><br><span style="color:var(--text-secondary);">Official firmware with a custom character pack. Shows the pet's mood, recent activity, and a prompt when approval is needed.</span></div>
</div>

Every state change is sent to the device as a small JSON heartbeat:

```json
{
  "total": 1, "running": 1, "waiting": 0,
  "msg": "approve: Bash",
  "entries": ["10:42 git push"],
  "tokens": 184502, "tokens_today": 31200,
  "prompt": {"id": "perm_xxx", "tool": "Bash", "hint": "rm -rf /tmp/foo"}
}
```

When I press a button, the answer travels back the same way and becomes the response to Claude Code's permission request.

The stick has an info screen that shows the same state the bridge is sending: how many sessions are open, how many are running or waiting, and how long ago the last message arrived.

<img src="/images/Purro-Stick/device.jpg" alt="Info screen on the stick: one session, one running, connected over encrypted Bluetooth" style="max-width: 360px; width: 100%; display: block; margin: 2rem auto; border-radius: 8px;">

## What It Does

- **Mood follows the agent.** Idle, busy, needs attention, celebrating, asleep.
- **Buttons answer permission requests.** The front button approves, the side button denies.
- **Tokens are food.** The bridge counts output tokens, and the pet fills up and levels as the agent works.
- **It reacts to being handled.** Shake it and it gets dizzy. Lay it face down and it naps.
- **It tracks every session.** Several Claude Code windows feed the same pet.

## Drawing Purro

<div class="image-grid" style="grid-template-columns: repeat(4, 1fr);">
<img src="/images/Purro-Stick/idle.gif" alt="Purro, idle" style="image-rendering: pixelated;">
<img src="/images/Purro-Stick/busy.gif" alt="Purro, busy" style="image-rendering: pixelated;">
<img src="/images/Purro-Stick/attention.gif" alt="Purro, needs attention" style="image-rendering: pixelated;">
<img src="/images/Purro-Stick/celebrate.gif" alt="Purro, celebrating" style="image-rendering: pixelated;">
<img src="/images/Purro-Stick/heart.gif" alt="Purro, happy" style="image-rendering: pixelated;">
<img src="/images/Purro-Stick/dizzy.gif" alt="Purro, dizzy" style="image-rendering: pixelated;">
<img src="/images/Purro-Stick/sleep.gif" alt="Purro, asleep" style="image-rendering: pixelated;">
</div>

The character is generated by a Python script instead of drawn by hand. The script composes each face from small parts (eyes, mouth, extras like hearts or sparkles) on a pixel grid, exports the frames as GIFs, and packs them for the device. Changing the palette or adding an expression is a few lines of code and one flash over USB. The animations come from the same parts: a blink is two frames with different eyes, a bounce is the same cat drawn a few pixels higher.

*M5StickC Plus (ESP32), Python (bleak, aiohttp, Pillow), Claude Code hooks*
