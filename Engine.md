# Internal Architecture: Protection Engine

## Overview
This document outlines the internal networking and architectural implementation details of the Privacy Protection Suite. These details are strictly meant for developers and should **never** be exposed in the user-facing UI unless it is within a dedicated "Developer Mode" or for debugging purposes.

## Networking Implementation
The core protection is achieved using a local **Android VpnService**. 

### Packet Routing & Inspection
Instead of routing all TCP/UDP traffic (which is resource-intensive and complex), the VPN currently uses **DNS Sinkholing** and **UDP DNS Payload Parsing** as its primary interception technique.
- We establish a local VPN tunnel and route DNS traffic (typically port 53) into the tunnel.
- Using a custom `DnsPacketHelper`, we parse raw IPv4 and UDP headers to extract the requested domain string from DNS packets.
- We map the UDP packet back to the originating Android application using `ConnectivityManager.getConnectionOwnerUid()`.

### Blocklist Engine (Tracker Interception)
- When a DNS request matches our internal tracker blocklist, we immediately drop the packet.
- We construct a synthetic "dummy" DNS response resolving to `0.0.0.0` and send it back through the VPN tunnel to the originating app, neutralizing the tracker instantly without network latency.
- The intercepted attempt is logged to the `TrackerRepository`.

### Upstream DNS (External Resolvers)
- If a DNS query is safe (not on the blocklist), it is forwarded to an external resolver.
- Depending on the user's category toggles (Ads, Malware, Phishing), we dynamically route safe queries to specific upstream servers (e.g., AdGuard DNS, Quad9) as a secondary layer of protection.
- **UI Rule**: The user is NEVER asked to select "Quad9" or "AdGuard". The user toggles "Malware Protection," and the Engine handles the routing internally.

## Future Extensibility
The architecture allows us to add deeper packet inspection (TCP proxying, TLS SNI filtering) in the future without changing the user-facing UI. The user's experience remains a simple "Protection On/Off" toggle.
