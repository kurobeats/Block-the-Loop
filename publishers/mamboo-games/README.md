# Mamboo Games - Domain Blocklist

Mamboo Games (a MY.GAMES studio) publishes hyper-casual mobile titles designed around ad-driven loops, retry monetization, and rapid dopamine hits. Their games are lightweight, fast-paced, and often use rewarded ads and cosmetic unlocks to drive engagement. This blocklist targets core infrastructure domains used across their catalog.

## 🎮 Covers:
- Shift Race
- Flex Run
- Oh God!
- Idle Police Tycoon

## 📦 Scope:
This blocklist includes:
- API endpoints (`*.api.mamboogames.com`, `*.api.my.games`)
- CDN and asset delivery (`*.cdn.mamboogames.com`, `*.assets.mamboogames.com`)
- Static content and patch servers (`*.static.mamboogames.com`, `*.patch.mamboogames.com`)
- Game-specific subdomains (`*.shift.mamboogames.com`, etc.)
- MY.GAMES account and monetization infrastructure (`*.auth.my.games`, `*.payment.my.games`)
- Wildcard coverage for all subdomains under `mamboogames.com` and `my.games`

## 🚫 Excludes:
- Ad networks (e.g. Unity Ads, AppLovin, IronSource)
- Analytics platforms
- Social media integrations
- Any third-party domains not directly tied to game infrastructure
