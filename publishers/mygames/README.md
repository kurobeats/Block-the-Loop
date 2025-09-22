# MY.GAMES - Shared Infrastructure Blocklist

MY.GAMES is a global publisher and platform that owns and operates multiple mobile game studios including Pixonic, BeIngame, Deus Craft, SWAG MASHA, and Whalekit. Their shared infrastructure powers account systems, monetization APIs, cloud saves, and event delivery across titles.

## 🧩 Covers:
- Account linking and authentication
- Monetization endpoints (payment, loot boxes, VIP validation)
- Cloud progression and profile sync
- Event delivery and seasonal content
- Game-specific subdomains (e.g. `*.warrobots.my.games`, `*.lovesick.my.games`)

## 📦 Scope:
This blocklist includes:
- API endpoints (`*.api.my.games`, `*.payment.my.games`)
- CDN and asset delivery (`*.cdn.my.games`, `*.assets.my.games`)
- Static content and patch servers (`*.static.my.games`, `*.patch.my.games`)
- Authentication and profile systems (`*.auth.my.games`, `*.profile.my.games`)
- Wildcard coverage for all subdomains under `my.games`

## 🚫 Excludes:
- Studio-specific domains (e.g. `*.pixonic.com`, `*.beingame.com`)
- Ad networks
- Analytics platforms
- Social media integrations