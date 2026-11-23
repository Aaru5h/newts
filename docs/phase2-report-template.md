# Team Newts - Phase 2 Final Report

> Complete observed results only after the live run. Replace every bracketed field and link each evidence filename.

## 1. What changed from Phase 1

Phase 1 provided private DNS on Mac 1, a trusted HTTPS nginx edge on Mac 2, and two HTTP backends on Macs 3 and 4. Phase 2 added a backup DNS resolver, short-TTL DNS changes, backend firewall isolation, passive upstream failover, a standby nginx edge, DNS-based edge migration, and a systematic troubleshooting drill. The client-facing name and HTTPS path remained `https://app.team1.test:8443`; the extensions hardened the same system rather than replacing it.

## 2. Resilience test results

| Test | Expected result | Observed result | Evidence |
|---|---|---|---|
| Primary DNS stopped | Name resolves through backup | [complete after test] | `A5-failover-works.png` |
| TTL 30 seconds; record changed | Old IP remains until TTL expiry, then new IP appears | [complete after test] | `B1-ttl-expiry.png` |
| DNS cache flushed | New IP appears immediately | [complete after test] | `B2-flush.png` |
| Backend A stopped | All requests succeed through B | [complete after test] | `D2-backend-a-down.png` |
| Backend A restarted | A/B balancing resumes | [complete after test] | `D3-balancing-resumed.png` |
| Direct backend access from Mac 1 | Requests time out | [complete after test] | `C2-blocked-from-mac1.png` |
| Direct backend access from Mac 2 | Both requests return `200` | [complete after test] | `C3-allowed-from-mac2.png` |
| DNS cutover to standby edge | Cached client moves from primary to standby after TTL | [complete after test] | `E3-cutover.png` |

## 3. Extension A - Backup DNS

[Aarush and Meet: in 3-5 sentences, state what was configured, the explicit query/failover commands used, what happened when primary DNS stopped, and why DNS-service failure differs from application failure.]

## 4. Extension B - DNS TTL and controlled change

[Aarush: in 3-5 sentences, describe the 30-second TTL, the old and new IPs, the timed observation, the direct `dig` result, and the effect of flushing the macOS cache.]

## 5. Extension C - Service isolation

[Utkarsh: in 3-5 sentences, describe the two pf allow/drop rules, the blocked Mac 1 test, the allowed Mac 2 test, continued HTTPS operation, and confirmed rollback.]

## 6. Extension D - Backend failover

[Deepak: in 3-5 sentences, describe `max_fails`, `fail_timeout`, `proxy_next_upstream`, the all-B result while A was stopped, and resumed round-robin behavior after A returned. Identify Mac 2 as the remaining single point of failure.]

## 7. Extension E - Controlled edge migration

[Meet: in 3-5 sentences, describe the standby nginx edge, the `X-Edge` proof, the DNS record change, TTL-delayed client movement, and continued service after the primary edge stopped.]

## 8. Extension F - Troubleshooting findings

[Utkarsh: in 3-5 sentences, name the injected fault(s), show the bottom-up DNS/IP/TCP/TLS/application sequence, state the first failing layer, and give the corrective action.]

## 9. Learning summary

The experiments showed that availability is a chain of independent layers. Redundant DNS protects name resolution but does not repair a failed application; nginx upstream failover protects against one backend failure but does not remove the edge as a single point of failure. DNS changes are intentionally non-instant because resolvers cache answers for the TTL. Service isolation reduces attack surface by forcing backend traffic through the edge, while a repeatable bottom-up diagnostic method prevents the team from guessing at the wrong layer.

## 10. Cleanup confirmation

- [ ] Primary DNS records restored to `10.7.12.112`.
- [ ] Original `pf` configuration restored on Mac 3 and Mac 4.
- [ ] No temporary backend isolation rules remain.
- [ ] Temporary nginx and dnsmasq processes stopped after the demonstration.
- [ ] Client DNS settings restored to `Empty`/DHCP defaults.
- [ ] No private key file is tracked by Git.
