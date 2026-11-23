# Team Newts - Phase 2 Final Report

## Run and topology

The captured session spans approximately 23:58 on 23 November to 02:01 on 24 November 2026 (IST). Screenshot filenames indicate capture or sharing times, not precise test start times. HTTP Date headers use GMT. Commands and visible output take precedence over filename timing.

| Machine | Operator | Address | Services |
|---|---|---|---|
| Mac 1 | Aarush | 10.7.21.112 | Primary dnsmasq, UDP/TCP 53 |
| Mac 2 | Deepak | 10.7.12.112 | Primary nginx, HTTPS 8443 |
| Mac 3 | Meet | 10.7.26.162 | Backend A HTTP 3001; backup DNS; standby nginx 8443 |
| Mac 4 | Utkarsh | 10.7.13.255 | Backend B HTTP 3002; test client |

The normal path is client DNS resolution through Mac 1 or Mac 3, followed by HTTPS to Mac 2. nginx terminates TLS and forwards plain HTTP to either backend. During migration the same hostname reaches Mac 3's standby nginx instead.

## Changes from Phase 1

Phase 2 retained the Python backends and trusted HTTPS service. It added equivalent backup DNS records, a 30-second record TTL, passive nginx upstream failure handling, a standby TLS edge, temporary backend isolation using pf, and a wrong-resolver troubleshooting exercise. DHCP addresses had changed since Phase 1; all Phase 2 configurations use the addresses above. The archived Phase 1 nginx configuration retains its original backend addresses as historical evidence.

## Results and evidence

All links below refer to original, unedited captures copied into the evidence directory. Additional screenshots and original filename mappings appear in the evidence index.

| Extension/test | Observation | Evidence |
|---|---|---|
| A: backup DNS | Backup query returns the edge IP; an explicit primary query times out while the system resolver and HTTPS continue working. | [Failover](../evidence/07-phase2/36-utkarsh-backup-dns-failover.jpeg), [dual resolvers](../evidence/07-phase2/04-deepak-dual-dns.png) |
| B: TTL change | Timed lookups retain 10.7.12.112 and later show 10.7.26.162; an explicit primary dig returns the changed record. | [Timed observation](../evidence/07-phase2/40-utkarsh-ttl-and-flush-attempt.jpeg) |
| B: cache flush | Flush commands are captured, but the final before/after pair both show 10.7.12.112. This does not independently prove an immediate old-to-new change caused by flushing. | [Flush attempt](../evidence/07-phase2/40-utkarsh-ttl-and-flush-attempt.jpeg) |
| C: backend isolation | Aarush's capture includes a timeout and successful responses during the troubleshooting/rollback sequence. Deepak's capture shows permitted access to A. Rules for both backend ports and rollback outputs are supplied. | [Timeout/recovery](../evidence/07-phase2/12-aarush-firewall-timeout-and-recovery.png), [edge access](../evidence/07-phase2/02-deepak-backend-a-allowed.png), [Mac 3 rollback](../evidence/07-phase2/27-meet-firewall-mac3-rollback.jpeg), [Mac 4 rollback](../evidence/07-phase2/54-utkarsh-firewall-mac4-clean.jpeg) |
| D: backend failover | Repeated requests show successful B responses during failover, then A/B responses after recovery. | [Failover](../evidence/07-phase2/33-utkarsh-backend-failover.jpeg), [recovery](../evidence/07-phase2/34-utkarsh-balancing-restored.jpeg) |
| E: migration | Direct standby testing and normal primary testing identify different X-Edge values. The cutover loop records the switch to standby, followed by standby responses and primary restoration. The shutdown action is reported by the team; a client header alone does not prove process shutdown. | [Both edges](../evidence/07-phase2/42-utkarsh-both-edges.jpeg), [cutover](../evidence/07-phase2/43-utkarsh-edge-cutover.jpeg), [standby response](../evidence/07-phase2/45-utkarsh-standby-after-primary-stop.jpeg), [restoration](../evidence/07-phase2/46-utkarsh-primary-edge-restored.jpeg) |
| F: wrong DNS drill | A public resolver cannot resolve the private name while direct IP ping and TCP 8443 work. Restoring project resolvers restores DNS and HTTPS. | [Diagnosis](../evidence/07-phase2/55-utkarsh-wrong-dns-drill.jpeg), [recovery](../evidence/07-phase2/56-utkarsh-dns-drill-recovery.jpeg) |

## Learning by extension

**A - Backup DNS.** A second dnsmasq on Mac 3 serves the same project names as Mac 1. Clients list both resolver addresses. The failover test separates a name-service outage from an application outage: HTTPS remains available once the backup supplies the edge address. Resolver selection and retry delays are client-dependent.

**B - TTL.** A record change does not invalidate answers already cached by clients. The timed observations show the old edge address persisting before the standby address appears. Direct dig queries expose the server's current record independently of the system resolver cache. The flush attempt should be recaptured with different before/after addresses to provide conclusive evidence of immediate invalidation.

**C - Isolation.** The backend pf rules allow TCP 3001 or 3002 only from Mac 2 and drop other incoming sources, while preserving loopback traffic. A client timeout is consistent with silent dropping, whereas the edge's successful request demonstrates an allowed path. Initial successful client requests required checking whether pf was enabled and whether old states or rollback affected the test. Saved baseline rules and rollback configuration accompany the submission; captures should be interpreted in sequence rather than assuming every successful response occurred while isolation was active.

**D - Failover.** nginx uses max_fails=2 and fail_timeout=10s, with proxy_next_upstream retries for connection errors, timeouts, and selected upstream HTTP errors. This is passive detection triggered by requests, rather than a separate active health probe. A healthy backend can continue serving requests while its peer is unavailable, and balancing resumes after recovery. The primary edge remains a single point of failure unless a second edge is paired with automatic traffic switching.

**E - Migration.** The standby edge uses the same certificate and upstreams, with X-Edge identifying which nginx responded. Updating DNS moves clients as their cached answers expire, so both edges are kept available during the transition. This test demonstrates a controlled manual migration; it does not implement automatic failover. Firewall isolation follows migration testing because restricting sources to Mac 2 would prevent the standby edge from reaching the remote backend.

**F - Troubleshooting.** The team tested DNS first, then IP reachability and the TCP listener. Failure of the private name at a public resolver, alongside successful IP and port tests, isolates the fault to resolver configuration. Restoring both project resolvers and flushing the cache recovers the service. This exercise demonstrates systematic fault isolation without relying on guessing at application code.

## Submission limitations

- Capture a fresh cache-flush old-IP/new-IP pair if the evaluator requires conclusive evidence for that subtest.
- The clearest dedicated permitted-edge screenshot covers Backend A; baseline captures cover both backends, but do not independently establish both were tested while firewall rules were active.
- Client X-Edge headers establish the responding edge, not the stopped state of the other edge process.
- No new packet capture was supplied for Phase 2; the original Phase 1 packet capture remains available separately.
- Local paths in submitted nginx configs are machine-specific. Certificate private keys and certificate ZIPs are excluded from Git.
