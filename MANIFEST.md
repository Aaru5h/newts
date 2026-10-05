# Phase 1 Evidence Manifest

This manifest maps every submitted evidence artifact to its purpose and the README section that cites it. Generated documentation/status files are listed separately.

## Source and packet capture

| File | Purpose | README section(s) |
|---|---|---|
| [`backend/backend-a/server.py`](backend/backend-a/server.py) | Submitted Python source for Backend A, including `/api/status`, `X-Backend`, `Cache-Control`, and ETag behavior. | Commands; Evidence mapped; Load balancing and caching |
| [`backend/backend-b/server.py`](backend/backend-b/server.py) | Submitted Python source for Backend B; functionally matches Backend A and is parameterized by environment variables. | Commands; Evidence mapped; Load balancing and caching |
| [`evidence/04-wireshark/phase1_dns_tcp_tls.pcapng`](evidence/04-wireshark/phase1_dns_tcp_tls.pcapng) | Original valid pcapng containing 7,368 packets; includes private DNS and the client-to-nginx TCP/TLS flow. | End-to-end flow; Evidence mapped; Wireshark analysis |

## LAN and topology evidence

| File | Purpose | README section(s) |
|---|---|---|
| [`mac2-lan-and-backend-connectivity.png`](evidence/01-lan-and-topology/mac2-lan-and-backend-connectivity.png) | Shows Mac 2 IP `10.7.1.112`, LAN pings, and HTTP 200 responses from Backend A and B with identifying/cache headers. | Machine table; Evidence mapped |
| [`mac3-backend-a-launch-and-requests.jpeg`](evidence/01-lan-and-topology/mac3-backend-a-launch-and-requests.jpeg) | Shows Mac 3 IP `10.7.14.119`, verified launch command for Backend A on `3001`, and request logs. | Machine table; Commands; Evidence mapped |
| [`mac4-backend-b-launch-and-requests.png`](evidence/01-lan-and-topology/mac4-backend-b-launch-and-requests.png) | Shows Mac 4 IP `10.7.22.175`, ping to nginx, Backend B launch on `3002`, and request logs. | Machine table; Commands; Evidence mapped |

## DNS evidence

| File | Purpose | README section(s) |
|---|---|---|
| [`mac1-dnsmasq-running-and-client-dns.png`](evidence/02-dns/mac1-dnsmasq-running-and-client-dns.png) | Shows dnsmasq validation/start, its LAN binding, direct queries, and project DNS client configuration. | Commands; Evidence mapped |

## HTTPS, load balancing and cache-header evidence

| File | Purpose | README section(s) |
|---|---|---|
| [`mac2-nginx-start-round-robin-and-dns.png`](evidence/03-https-load-balancing-cache/mac2-nginx-start-round-robin-and-dns.png) | Shows nginx install, config validation/start, alternating upstream headers, and DNS resolution. | Commands; Evidence mapped |
| [`mac2-mkcert-nginx-reload-and-https.png`](evidence/03-https-load-balancing-cache/mac2-mkcert-nginx-reload-and-https.png) | Shows mkcert local CA/certificate creation, nginx validation/reload, HTTP 200, and root CA export. | Commands; Evidence mapped |
| [`mac4-trusted-https-round-robin-and-cache-headers.png`](evidence/03-https-load-balancing-cache/mac4-trusted-https-round-robin-and-cache-headers.png) | Shows CA trust setup, HTTPS success without `-k`, alternating A/B responses, cache headers, and TLS 1.2 test. | End-to-end flow; Commands; Evidence mapped; Load balancing and caching |
| [`cache-control-and-etag-headers.png`](evidence/03-https-load-balancing-cache/cache-control-and-etag-headers.png) | Focused HTTP 200, `X-Backend`, `Cache-Control: max-age=60`, and ETag output. | Commands; Evidence mapped; Load balancing and caching |

## Wireshark screenshots

| File | Purpose | README section(s) |
|---|---|---|
| [`dns-query-and-response.png`](evidence/04-wireshark/dns-query-and-response.png) | Shows client A query and DNS-server reply mapping `app.team1.test` to `10.7.1.112`. | End-to-end flow; Evidence mapped; Wireshark analysis |
| [`tcp-handshake-tls-and-application-data.png`](evidence/04-wireshark/tcp-handshake-tls-and-application-data.png) | Shows SYN/SYN-ACK/ACK, TLS exchange, application data, and connection close/reset on port `8443`. | End-to-end flow; Evidence mapped; Wireshark analysis |
| [`tls-handshake-and-encrypted-data.png`](evidence/04-wireshark/tls-handshake-and-encrypted-data.png) | Shows ClientHello with SNI, ServerHello/Certificate, key exchange, and encrypted application data. | End-to-end flow; Evidence mapped; Wireshark analysis |

## Failure evidence

| File | Purpose | README section(s) |
|---|---|---|
| [`both-backends-down-502-then-backend-b-recovery.png`](evidence/05-failure-tests/both-backends-down-502-then-backend-b-recovery.png) | Shows nginx `502 Bad Gateway` followed by HTTP 200 from Backend B after recovery. | Evidence mapped; Failure demonstrations |
| [`wrong-port-8444-connection-failure.png`](evidence/05-failure-tests/wrong-port-8444-connection-failure.png) | Shows connection failure on unused port `8444`. | Commands; Evidence mapped; Failure demonstrations |
| [`public-dns-nxdomain-and-direct-ip-ping.png`](evidence/05-failure-tests/public-dns-nxdomain-and-direct-ip-ping.png) | Shows NXDOMAIN from `8.8.8.8` and successful ping to nginx's IP. | Commands; Evidence mapped; Failure demonstrations |
| [`wrong-dns-record-backend-a-and-8443-failure.png`](evidence/05-failure-tests/wrong-dns-record-backend-a-and-8443-failure.png) | Shows wrong DNS answer `10.7.14.119` and forced HTTPS connection failure on `8443`. | Commands; Evidence mapped; Failure demonstrations |
| [`mac1-wrong-dns-record-change-and-restore.png`](evidence/05-failure-tests/mac1-wrong-dns-record-change-and-restore.png) | Shows Mac 1 command context for changing the dnsmasq record to Backend A and restoring the config. | Failure demonstrations |
| [`wrong-dns-test-context-and-edge-ping.png`](evidence/05-failure-tests/wrong-dns-test-context-and-edge-ping.png) | Provides broader terminal context for wrong-port/wrong-DNS testing and confirms edge IP reachability. | Failure demonstrations |
| [`browser-error-page-fetch-failure.png`](evidence/05-failure-tests/browser-error-page-fetch-failure.png) | Shows a DevTools fetch failure caused by `chrome-error://` page context; retained as contextual evidence only. | Failure demonstrations |

## Recovery evidence

| File | Purpose | README section(s) |
|---|---|---|
| [`project-dns-with-router-fallback-restored.png`](evidence/06-recovery/project-dns-with-router-fallback-restored.png) | Shows Mac 4 configured with project DNS primary and router fallback. | Commands; Recovery |
| [`dns-record-restored-to-nginx-edge.png`](evidence/06-recovery/dns-record-restored-to-nginx-edge.png) | Shows private DNS again returning nginx address `10.7.1.112`. | Evidence mapped; Recovery |
| [`macos-dns-cache-flush.png`](evidence/06-recovery/macos-dns-cache-flush.png) | Shows project DNS settings plus macOS DNS cache flush commands. | Recovery |
| [`dns-and-https-200-recovered.png`](evidence/06-recovery/dns-and-https-200-recovered.png) | Shows restored DNS and successful HTTPS HTTP 200 response. | Evidence mapped; Recovery |
| [`dns-and-https-200-recovered-duplicate.png`](evidence/06-recovery/dns-and-https-200-recovered-duplicate.png) | Duplicate recovery screenshot retained so no original evidence was deleted. | Recovery |

## Generated documentation and status notes

| File | Purpose |
|---|---|
| [`README.md`](README.md) | Main Phase 1 submission narrative and evidence map. |
| [`docs/topology.md`](docs/topology.md) | Mermaid topology, machine/port table, and request-flow explanation. |
| [`configs/dnsmasq/README.md`](configs/dnsmasq/README.md) | Records the missing submitted copy of the dnsmasq configuration. |
| [`configs/nginx/README.md`](configs/nginx/README.md) | Records the missing submitted copy of the nginx configuration. |
| [`configs/tls/README.md`](configs/tls/README.md) | Records the missing submitted TLS artifacts and private-key caution. |

## Missing files / unsupported details

- `cn-phase1-dnsmasq.conf` was demonstrated but not submitted.
- `cn-phase1-nginx.conf` was demonstrated but not submitted.
- `app.team1.test.pem`, `app.team1.test-key.pem`, and `team1-rootCA.pem` were demonstrated but not submitted. The private key should be handled carefully.
- The final `networksetup -setdnsservers Wi-Fi Empty` execution was not captured.
- No runtime evidence shows a `304 Not Modified` response or browser cache hit; the README claims only the cache headers that are visible.
- The surviving-backend screenshot shows service continuing from Backend B, but does not show the command that stopped Backend A.
