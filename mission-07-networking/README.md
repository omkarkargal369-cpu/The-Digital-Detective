# Mission 7 — How computers communicate

## 1. Task / objective
Explain core networking concepts, run connectivity and DNS lookup tests in terminal, and describe step-by-step what happens under the hood when you open a website in a browser.

## 2. Work completed
- Wrote down definitions and examples for LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, and Client-server.
- Tested `ping` and `nslookup` on `example.com`.
- Traced the 7 steps of opening a website from typing the URL to seeing the page rendered.
- Kept personal IP and private network details redacted.
- Used clean bullet points, zero tables.

## 3. Commands / tools used
- `ping -c 3 example.com` - tested if my computer can reach `example.com` and measured latency.
- `nslookup example.com` - queried DNS to find the IP address of `example.com`.

## 4. My understanding

### Task 7.1 — Network Concepts
- **LAN (Local Area Network):**
  - Explanation: A small network connecting devices in a single room, house, or lab.
  - Example: Your home Wi-Fi connecting your laptop, phone, and TV together.
- **MAN (Metropolitan Area Network):**
  - Explanation: A medium-sized network that covers an entire campus, town, or city.
  - Example: A college campus network linking academic blocks, library, and hostels.
- **WAN (Wide Area Network):**
  - Explanation: A massive network covering large geographical areas, countries, or the whole world.
  - Example: The global Internet itself, or a telecom 4G/5G mobile data network.
- **DNS (Domain Name System):**
  - Explanation: The phonebook of the internet that turns human names into computer IP numbers.
  - Example: Converts `example.com` into an IP like `172.66.147.243`.
- **Router:**
  - Explanation: A networking device that directs traffic packets between different networks so data gets to the right destination.
  - Example: The Wi-Fi router sitting in your living room that routes your phone traffic to your ISP.
- **Protocol:**
  - Explanation: An agreed set of rules and formats that computers use to talk to each other without misunderstanding data.
  - Example: HTTPS for secure websites, or TCP/IP for reliable data transport.
- **Packet switching:**
  - Explanation: Breaking down big files or messages into small packets, sending them independently across the internet, and stitching them back together at the other end.
  - Example: Streaming a video where chunks arrive as thousands of separate packets.
- **Client-server:**
  - Explanation: A setup where one device asks for data (client) and another computer delivers it (server).
  - Example: Your browser (client) requesting a web page from a web server.

---

### Task 7.2 — Network Observation
- `ping -c 3 example.com`:
  - Result: 3 packets sent, 3 received, 0% packet loss, average round-trip time ~7.1 ms.
- `nslookup example.com`:
  - Result: Resolved `example.com` to addresses `104.20.23.154` and `172.66.147.243`.

Answers to questions:
- What a connectivity test (`ping`) helps you check:
  It tells you whether your computer can physically reach a remote server across the network, if packets are getting dropped, and how long a round trip takes (latency in milliseconds).
- What information a DNS lookup (`nslookup`) displays:
  It shows which DNS server handled the query and the exact IP address mapped to that domain name.
- Role of DNS when entering a website name:
  Humans remember words like `youtube.com`, but routers and servers only understand numbers like `142.250.190.46`. DNS does the lookup in milliseconds behind the scenes before your browser even sends a single webpage request.

---

### Task 7.3 — What Happens When You Open a Website (Step-by-Step)
1. **User enters URL:** You type `https://example.com` into the browser (the client).
2. **DNS Lookup:** The browser asks the DNS server for the IP address mapped to `example.com`. DNS replies with an IP like `172.66.147.243`.
3. **Establishing Connection:** The client opens a TCP connection with the server at that IP and completes a TLS/SSL cryptographic handshake (the HTTPS protocol).
4. **Sending HTTP Request:** The browser sends an HTTP GET request packet out through the home router and ISP network to the server.
5. **Server Processing:** The web server receives the request, finds the HTML, CSS, and script files, and packages them up.
6. **Data Transmission (Packet Switching):** The server sends the response data back across the internet, split into small packets that travel through routers and arrive at the client.
7. **Page Rendering:** The browser reassembles the packets, parses the HTML, CSS, and JavaScript, and draws the visual webpage on your screen.

## 5. Difficulties faced
No real issues. Just made sure to redact my private home IP address from the notes.

## 6. How I resolved them
Replaced personal local IPs with `[redacted]` as instructed.

## 7. Evidence / files
- `mission-07-networking/README.md`
- Terminal output from `ping` and `nslookup` on `example.com`

## 8. Commit details
- Commit message: "Explain networking concepts and website communication"
- Ready to push to GitHub.
