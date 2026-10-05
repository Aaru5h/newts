# Computer Networks Phase 1 — Private DNS, HTTPS Reverse Proxy and Load Balancing

**Team Newts**

## Team

| Computer | Team member | Student ID |
|---|---|---|
| PC1 / Mac 1 | Aarush Gupta | 2401020001 |
| PC2 / Mac 2 | Deepak Mishra | 2401010142 |
| PC3 / Mac 3 | Meet Ahuja | 2401010273 |
| PC4 / Mac 4 | Utkarsh | 2401010484 |

## Objective

This Phase 1 demonstration builds a four-Mac service entirely on one private Wi-Fi/LAN. A private DNS server resolves `app.team1.test`; nginx terminates trusted HTTPS on port `8443` and load-balances requests across two HTTP backends. The evidence also demonstrates response cache headers, selected failure modes, recovery, and packet-level DNS/TCP/TLS behavior.

No cloud hosting was used. Claims below are limited to what the submitted source files and screenshots show. See the [evidence manifest](MANIFEST.md) for a file-by-file index.

## Architecture and topology

**Normal path:** Mac 4 client → Mac 1 DNS → Mac 2 nginx HTTPS edge → Backend A on Mac 3 **or** Backend B on Mac 4.

The detailed [topology diagram, machine table, and request flow](docs/topology.md) are maintained separately.

## Machine, role, IP and port table

| Machine | Operator | IP | Role | Port(s) |
|---|---|---:|---|---:|
| Mac 1 / PC1 | Aarush Gupta | `10.7.18.100` | Private DNS using dnsmasq | UDP/TCP `53` |
| Mac 2 / PC2 | Deepak Mishra | `10.7.1.112` | nginx HTTPS reverse proxy/load balancer | TCP `8443` |
| Mac 3 / PC3 | Meet Ahuja | `10.7.14.119` | Backend A | HTTP TCP `3001` |
| Mac 4 / PC4 | Utkarsh | `10.7.22.175` | Backend B and test client | HTTP TCP `3002`; ephemeral client ports |

The LAN/backend connectivity screenshot records Mac 2 at `10.7.1.112` and successful direct HTTP responses from both backends: [Mac 2 LAN and backend connectivity](evidence/01-lan-and-topology/mac2-lan-and-backend-connectivity.png). Backend launch evidence is available for [Backend A](evidence/01-lan-and-topology/mac3-backend-a-launch-and-requests.jpeg) and [Backend B](evidence/01-lan-and-topology/mac4-backend-b-launch-and-requests.png).

## End-to-end request flow

1. **DNS:** Mac 4 asks Mac 1 (`10.7.18.100`) for `app.team1.test`; the normal A record is `10.7.1.112` ([DNS packet evidence](evidence/04-wireshark/dns-query-and-response.png)).
2. **TCP:** Mac 4 opens a TCP connection to `10.7.1.112:8443`. Wireshark shows `SYN → SYN-ACK → ACK` ([TCP/TLS packet evidence](evidence/04-wireshark/tcp-handshake-tls-and-application-data.png)).
3. **TLS:** The client sends a ClientHello with SNI `app.team1.test`; nginx returns ServerHello and Certificate, followed by encrypted handshake/application data ([TLS packet evidence](evidence/04-wireshark/tls-handshake-and-encrypted-data.png)).
4. **nginx:** nginx terminates TLS and selects Backend A (`10.7.14.119:3001`) or Backend B (`10.7.22.175:3002`).
5. **Backend:** The selected Python HTTP service answers `/api/status` with JSON and response headers including `X-Backend`, `Cache-Control`, and `ETag`.
6. **Response:** nginx relays the HTTP response over the established encrypted connection. The final client proof returned HTTP 200 without `curl -k` ([trusted HTTPS evidence](evidence/03-https-load-balancing-cache/mac4-trusted-https-round-robin-and-cache-headers.png)).

## Protocol-to-layer mapping

| Layer | Protocol/evidence | Function |
|---|---|---|
| Application | DNS, HTTP | Resolves the private hostname and exchanges `/api/status` requests/responses. |
| Security/presentation | TLS 1.2 | Authenticates the HTTPS edge and encrypts HTTP traffic. |
| Transport | UDP (DNS), TCP (HTTPS/backends) | Carries DNS and provides reliable connections for HTTPS/HTTP. |
| Network | IPv4 | Routes between the four private `10.7.x.x` addresses on the LAN. |
| Link | Ethernet framing over Wi-Fi | Delivers frames on the shared private LAN; Wireshark displays Ethernet II framing. |

## Commands Used During Setup and Testing

Commands are assigned only where the supplied instructions or evidence establish the machine and purpose.

### Mac 1 — private DNS

To run dnsmasq in the foreground so `app.team1.test` resolves to the nginx edge IP:

```bash
sudo dnsmasq --no-daemon --conf-file="$HOME/cn-phase1-dnsmasq.conf"
```

To query the team DNS server explicitly and verify its answer from a client:

```bash
nslookup app.team1.test 10.7.18.100
```

The first command is visible in [dnsmasq running](evidence/02-dns/mac1-dnsmasq-running-and-client-dns.png). The submitted evidence does not contain the dnsmasq configuration file itself.

### Mac 2 — nginx HTTPS edge

nginx used `~/cn-phase1-nginx.conf`. The screenshot verifies these exact validation, start, and reload commands:

```bash
nginx -t -c ~/cn-phase1-nginx.conf
nginx -c ~/cn-phase1-nginx.conf
nginx -s reload -c ~/cn-phase1-nginx.conf
```

They validate the file, start nginx with it, and reload the running service after the HTTPS configuration is applied. Evidence: [nginx start and test](evidence/03-https-load-balancing-cache/mac2-nginx-start-round-robin-and-dns.png) and [nginx HTTPS reload](evidence/03-https-load-balancing-cache/mac2-mkcert-nginx-reload-and-https.png).

To stop nginx safely after the demonstration:

```bash
nginx -s stop -c ~/cn-phase1-nginx.conf
```

This stop command is part of the supplied project procedure; no screenshot of its execution was submitted.

### Mac 3 — Backend A

The submitted terminal screenshot verifies the launch command and shows the service listening on port `3001`:

```bash
BACKEND_ID=A PORT=3001 python3 server.py
```

Run it from the directory containing [Backend A source](backend/backend-a/server.py). Evidence: [Backend A launch and requests](evidence/01-lan-and-topology/mac3-backend-a-launch-and-requests.jpeg).

### Mac 4 — Backend B and test client

The submitted terminal screenshot verifies Backend B's launch command:

```bash
BACKEND_ID=B PORT=3002 python3 server.py
```

Run it from the directory containing [Backend B source](backend/backend-b/server.py). Evidence: [Backend B launch and requests](evidence/01-lan-and-topology/mac4-backend-b-launch-and-requests.png).

To set Mac 1 as the project DNS server while retaining the router as fallback internet DNS:

```bash
networksetup -setdnsservers Wi-Fi 10.7.18.100 10.7.0.1
```

To show normal private-domain resolution:

```bash
nslookup app.team1.test
```

To prove a trusted TLS 1.2 HTTPS request works without `-k`:

```bash
curl --tlsv1.2 --tls-max 1.2 -i https://app.team1.test:8443/api/status
```

To demonstrate nginx round-robin behavior across six separate requests:

```bash
for i in {1..6}; do curl -s -D - -o /dev/null https://app.team1.test:8443/api/status | grep X-Backend; done
```

To display the response status, selected backend, and cache-related headers:

```bash
curl -s -D - -o /dev/null https://app.team1.test:8443/api/status | grep -Ei 'HTTP/|X-Backend|Cache-Control|ETag'
```

Evidence for these normal tests: [trusted HTTPS, round-robin and cache headers](evidence/03-https-load-balancing-cache/mac4-trusted-https-round-robin-and-cache-headers.png) and [focused cache headers](evidence/03-https-load-balancing-cache/cache-control-and-etag-headers.png).

To generate clean DNS and TLS traffic for Wireshark:

```bash
nslookup app.team1.test
curl --tlsv1.2 --tls-max 1.2 -i https://app.team1.test:8443/api/status
```

To demonstrate the wrong-destination-port failure, where DNS still resolves but no service listens on `8444`:

```bash
curl -i https://app.team1.test:8444/api/status
```

To demonstrate that a public/wrong resolver returns NXDOMAIN while direct IP connectivity still works:

```bash
nslookup app.team1.test 8.8.8.8
ping -c 2 10.7.1.112
```

To demonstrate a wrong DNS record by forcing the hostname to Backend A instead of the nginx edge:

```bash
curl --connect-timeout 5 --resolve app.team1.test:8443:10.7.14.119 -i https://app.team1.test:8443/api/status
```

Failure evidence: [wrong port](evidence/05-failure-tests/wrong-port-8444-connection-failure.png), [public DNS NXDOMAIN and successful direct ping](evidence/05-failure-tests/public-dns-nxdomain-and-direct-ip-ping.png), and [wrong record/port failure](evidence/05-failure-tests/wrong-dns-record-backend-a-and-8443-failure.png).

### Every Mac — restore normal DNS after the demo

On each Mac that had project DNS configured, restore DHCP/router-provided DNS:

```bash
networksetup -setdnsservers Wi-Fi Empty
```

This restoration command is part of the supplied project procedure; no screenshot of `Empty` being executed was submitted. Mac 4 evidence does show project DNS plus router fallback being restored with `networksetup -setdnsservers Wi-Fi 10.7.18.100 10.7.0.1` ([DNS settings recovery](evidence/06-recovery/project-dns-with-router-fallback-restored.png)).

## Evidence mapped to Phase 1 tasks

| Task | Verified observation | Evidence |
|---|---|---|
| LAN addressing/connectivity | Machines use private `10.7.x.x` addresses; direct connectivity and backend responses are shown. | [Mac 2 LAN/backend test](evidence/01-lan-and-topology/mac2-lan-and-backend-connectivity.png), [Mac 4 address/ping/backend](evidence/01-lan-and-topology/mac4-backend-b-launch-and-requests.png) |
| Private DNS | `app.team1.test` normally resolves via `10.7.18.100` to `10.7.1.112`. | [dnsmasq/client query](evidence/02-dns/mac1-dnsmasq-running-and-client-dns.png), [DNS query/reply packets](evidence/04-wireshark/dns-query-and-response.png) |
| Backend services | Backend A listens on `3001`; Backend B listens on `3002`; both answer `/api/status`. | [Backend A](evidence/01-lan-and-topology/mac3-backend-a-launch-and-requests.jpeg), [Backend B](evidence/01-lan-and-topology/mac4-backend-b-launch-and-requests.png), [source A](backend/backend-a/server.py), [source B](backend/backend-b/server.py) |
| HTTPS/TLS | nginx answers on `8443`; trusted curl succeeds without `-k`; mkcert setup is shown. | [mkcert/nginx/HTTPS](evidence/03-https-load-balancing-cache/mac2-mkcert-nginx-reload-and-https.png), [client trusted HTTPS](evidence/03-https-load-balancing-cache/mac4-trusted-https-round-robin-and-cache-headers.png) |
| Load balancing | Repeated requests alternate `X-Backend: A` and `X-Backend: B`. | [round-robin sequence](evidence/03-https-load-balancing-cache/mac4-trusted-https-round-robin-and-cache-headers.png) |
| Cache metadata | Responses contain `Cache-Control: max-age=60` and backend-specific ETags. | [cache-header output](evidence/03-https-load-balancing-cache/cache-control-and-etag-headers.png) |
| Packet analysis | The original capture and screenshots show DNS query/reply, TCP handshake, TLS ClientHello, ServerHello/Certificate, and application data. | [original capture](evidence/04-wireshark/phase1_dns_tcp_tls.pcapng), [DNS](evidence/04-wireshark/dns-query-and-response.png), [TCP/TLS](evidence/04-wireshark/tcp-handshake-tls-and-application-data.png), [TLS detail](evidence/04-wireshark/tls-handshake-and-encrypted-data.png) |
| Failures | Wrong port, wrong resolver, wrong record, and both-backends-down behavior are evidenced. | [failure evidence directory](evidence/05-failure-tests/) |
| Recovery | DNS returns to `10.7.1.112`; HTTPS returns HTTP 200. | [DNS restored](evidence/06-recovery/dns-record-restored-to-nginx-edge.png), [full recovery](evidence/06-recovery/dns-and-https-200-recovered.png) |

## Wireshark analysis

The submitted [original Wireshark capture](evidence/04-wireshark/phase1_dns_tcp_tls.pcapng) is a valid pcapng file containing 7,368 packets. Inspection confirms 190 UDP/53 packets and a 22-packet TCP `8443` flow between the client and nginx. The capture and screenshots show:

- a DNS A query from `10.7.22.175` to `10.7.18.100` for `app.team1.test`, followed by a response containing `10.7.1.112`;
- a TCP connection from an ephemeral client port to destination port `8443`, including SYN, SYN-ACK, and ACK;
- a TLS ClientHello with SNI `app.team1.test`;
- ServerHello and Certificate traffic, key exchange/handshake messages, and encrypted application data.

The capture independently confirms two A queries for `app.team1.test` that receive `10.7.1.112`, and the displayed HTTPS flow begins with the TCP three-way handshake between `10.7.22.175:58110` and `10.7.1.112:8443`.

## Load balancing and caching

Repeated requests show the `X-Backend` response header alternating A, B, A, B, A, B, which is consistent with nginx round-robin selection. The endpoint responses expose `Cache-Control: max-age=60` and ETags such as `"phase1-backend-A-v1"` or `"phase1-backend-B-v1"`.

This evidence proves the presence of cache-control metadata. It does **not** prove that a client performed a cache hit or that the server returned `304 Not Modified`; neither appears in the submitted terminal output. Although the backend source contains conditional `If-None-Match` logic, runtime behavior is not claimed without execution evidence.

## Failure demonstrations

| Scenario | Observation | Explanation | Evidence |
|---|---|---|---|
| One backend unavailable | HTTPS still returns HTTP 200 from Backend B during recovery testing. | nginx can use the surviving upstream. The screenshot establishes continued service from B, although it does not capture the backend-stop command itself. | [502 then Backend B HTTP 200](evidence/05-failure-tests/both-backends-down-502-then-backend-b-recovery.png) |
| Both backends unavailable | nginx returns `HTTP/1.1 502 Bad Gateway`. | The HTTPS edge is reachable but no configured upstream can produce a response. | [502 output](evidence/05-failure-tests/both-backends-down-502-then-backend-b-recovery.png) |
| Wrong destination port `8444` | curl reports it could not connect to the server. | DNS succeeds, but no HTTPS service is listening on `8444`. | [wrong-port failure](evidence/05-failure-tests/wrong-port-8444-connection-failure.png) |
| Wrong/public DNS resolver | `8.8.8.8` returns NXDOMAIN, while ping to `10.7.1.112` succeeds with 0% packet loss. | The private name exists only on the team DNS server; IP connectivity remains healthy. | [NXDOMAIN and ping](evidence/05-failure-tests/public-dns-nxdomain-and-direct-ip-ping.png) |
| Wrong DNS record | DNS is shown returning Backend A's `10.7.14.119`; HTTPS to port `8443` fails. | Backend A serves HTTP on `3001`, not nginx HTTPS on `8443`. | [wrong-record failure](evidence/05-failure-tests/wrong-dns-record-backend-a-and-8443-failure.png), [Mac 1 record change/restore](evidence/05-failure-tests/mac1-wrong-dns-record-change-and-restore.png) |
| Browser error context | DevTools reports a fetch from a `chrome-error://` page cannot load `/api/status`. | This is browser error-page context, not proof of a network-layer cache behavior. | [browser error](evidence/05-failure-tests/browser-error-page-fetch-failure.png) |

## Recovery and normal Wi-Fi restoration

Recovery evidence shows the A record restored to nginx at `10.7.1.112`, macOS DNS caches flushed, and a subsequent request returning HTTP 200 with Backend A, `Cache-Control`, and `ETag` headers: [restored DNS](evidence/06-recovery/dns-record-restored-to-nginx-edge.png), [cache flush](evidence/06-recovery/macos-dns-cache-flush.png), and [HTTP recovery](evidence/06-recovery/dns-and-https-200-recovered.png).

After the demonstration, each Mac with project DNS configured should run `networksetup -setdnsservers Wi-Fi Empty` to resume DHCP/router DNS. Execution of this final `Empty` command is not present in the evidence.

## How to reproduce the live demonstration

1. Put all four Macs on the same private Wi-Fi/LAN and confirm the addresses in the topology table.
2. On Mac 1, install/use the project dnsmasq configuration and start dnsmasq with the documented command. Confirm `app.team1.test → 10.7.1.112`.
3. On Mac 3, from the Backend A directory, run `BACKEND_ID=A PORT=3001 python3 server.py`.
4. On Mac 4, from the Backend B directory, run `BACKEND_ID=B PORT=3002 python3 server.py`.
5. On Mac 2, ensure the mkcert certificate/key and nginx configuration are at the paths expected by `~/cn-phase1-nginx.conf`; validate and start nginx using the verified commands.
6. Trust the mkcert root CA on the client Mac(s), then configure Mac 4 DNS with Mac 1 primary and the router fallback.
7. On Mac 4, run normal DNS, trusted TLS 1.2, round-robin, and header tests from the command section.
8. Capture the clean DNS and TLS test sequence in Wireshark; compare it with the submitted [original capture](evidence/04-wireshark/phase1_dns_tcp_tls.pcapng).
9. Perform the failure tests one at a time, restore the normal configuration after each, and verify DNS plus HTTP 200 recovery.
10. Stop project services and restore normal DNS with `networksetup -setdnsservers Wi-Fi Empty` on every changed Mac.

Reproduction currently requires files that were not submitted: the dnsmasq config, nginx config, and TLS certificate/key/root CA. Their status is recorded in [MANIFEST.md](MANIFEST.md).
