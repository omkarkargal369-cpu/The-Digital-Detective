# Mission 7 — How computers communicate

## 1. Task / objective
Explain network terms, run `ping` and `nslookup`, and explain the steps of opening a website.

## 2. Work completed
- Defined LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, and Client-server.
- Ran `ping` and `nslookup` on `example.com`.
- Wrote down the 7 steps of opening a website.
- Kept personal IP addresses redacted.

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested internet reachability and latency.
- `nslookup example.com`: Looked up the IP address for the domain name.

## 4. My understanding

### Task 7.1 — Network Concepts
- LAN: Small local network like home Wi-Fi. Example: Home laptops and phones.
- MAN: Network across a town or campus. Example: College campus network.
- WAN: Big network across regions or the world. Example: The Internet.
- DNS: Translates domain names into IP addresses. Example: `example.com` -> `172.66.147.243`.
- Router: Directs data packets between different networks. Example: Home Wi-Fi router.
- Protocol: Rules for how computers communicate. Example: HTTPS, TCP/IP.
- Packet switching: Breaking data into small packets and sending them across network routes. Example: Streaming video packets.
- Client-server: One device asks (client) and one answers (server). Example: Browser asking a website server.

### Task 7.2 — Network Tests
- `ping -c 3 example.com`: Sent 3 packets, got 3 back, 0% packet loss, ~7 ms delay.
- `nslookup example.com`: Looked up `example.com` and got IP `172.66.147.243`.

Answers:
- Connectivity test (`ping`): Checks if you can reach a server and how fast the reply is.
- DNS lookup (`nslookup`): Shows what IP address belongs to that domain name.
- Role of DNS in browser: Looks up the server IP before the browser can load the page.

### Task 7.3 — Steps to Open a Website
1. You type `https://example.com` in your browser (client).
2. The browser asks DNS for the IP address of `example.com`.
3. DNS returns the IP address (`172.66.147.243`).
4. Browser connects to that IP using TCP and HTTPS protocol.
5. Browser sends an HTTP request asking for the page.
6. Server sends back the page data split into packets over the network.
7. Browser puts the packets together and shows the webpage on screen.

## 5. Difficulties faced
No difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-07-networking/README.md`
- Terminal output from `ping` and `nslookup`

## 8. Commit details
- Commit message: "Explain networking concepts and website communication"
- Pushed to main.
