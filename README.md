# Block the Loop

**Block the Loop** is a project born from frustration, love and deep saddness.

Mobile games are engineered to trap players in psychological loops - reward cycles, time-gated upgrades, alliance pressure, and endless microtransactions. These loops are designed to be compulsive, monetized, and hard to escape.

This repository exists to help you - or someone you care about - break that loop.

## 🎯 Purpose

Whether you're trying to support a loved one, protect a child, or escape the grind yourself, this blocklist offers a technical layer of defense. It targets infrastructure domains used by the most addictive mobile games across genres and publishers.

But let’s be clear: **blocking is not healing**.

## 🧩 One Piece of the Puzzle

This repo is a tool - not a cure.

If you or someone close to you is struggling with mobile game addiction, please consider:
- Talking to a mental health professional
- Exploring digital wellness tools
- Setting device-level limits and boundaries
- Seeking community support

Technical intervention can interrupt harmful patterns. But healing takes time, support, and self-compassion.

## 📝 Statistics

Publishers: 49

Games Covered: 135

Domains Blocked (by wildcard): 488

## 🧱 Structure

- `publishers/` - Organized by game publisher (e.g. Lilith Games, FunPlus, King)
- Each folder contains:
  - `blocklist.txt` - Domain rules in adblocker format (`||domain.com^`)
  - `README.md` - Game coverage, scope, and usage notes
- `block-the-loop.txt` - Combined blocklist for all publishers

## 🔧 Usage

This blocklist uses standard adblocker syntax (`||domain.com^`) which is compatible with:

| Tool | Compatibility | Instructions |
|------|--------------|--------------|
| **uBlock Origin** | ✅ Full | Add to "My filters" in dashboard |
| **AdGuard** | ✅ Full | Add as custom filter list |
| **AdBlock Plus** | ✅ Full | Add as custom filter list |
| **Pi-hole** | ✅ Full | Add URL to blocklist |
| **NextDNS** | ✅ Full | Add to denylist |

### Quick Setup

**For browser adblockers (uBlock Origin, AdGuard, AdBlock Plus):**
```
https://raw.githubusercontent.com/YOUR_USERNAME/Block-the-Loop/main/block-the-loop.txt
```

**For Pi-hole:**
Add the URL above to your Pi-hole's blocklist.

**For NextDNS:**
Add the URL to your denylist configuration.

## ⚠️ Disclaimer

This repo does not block ads, trackers, or third-party integrations. It focuses strictly on game infrastructure. Blocking may break login, updates, or gameplay. Use with care and test per title.

This is NOT an exhaustive list of predatory games, you can find that over at [Dark Pattern Games](https://www.darkpattern.games/).

## ⚙️ Contributing

Pull requests are MOST welcome!

Don't know how to contribute but want a publisher or game added? Create an Issue and I'll add it.
