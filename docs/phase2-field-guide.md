# Team Newts - Phase 2 Field Guide

This is the team's compact operating sheet. The supplied Phase 2 runbook remains the source of truth for exact commands and expected output. Do not continue after an unexpected result; capture the window and diagnose that layer first.

## Fixed machine map

| Mac | Owner | Address | Phase 2 responsibility |
|---|---|---|---|
| Mac 1 | Aarush | `10.7.21.112` | Primary DNS; Extensions A and B; DNS changes for E |
| Mac 2 | Deepak | `10.7.12.112` | Primary nginx edge; Extensions D and E |
| Mac 3 | Meet | `10.7.26.162` | Backend A; backup DNS; standby edge; firewall for `3001` |
| Mac 4 | Utkarsh | `10.7.13.255` | Backend B; test client; firewall for `3002` |

If any address differs on the day, stop. Update every configuration and command that contains the old address before continuing.

## Before the 90-minute run

- Put all four Macs on the same private Wi-Fi and confirm their addresses.
- Confirm Homebrew, `dnsmasq`, `nginx`, `curl`, `dig`, and `nc` are available on the machines that use them.
- Confirm Mac 2 still has `~/cn-phase1-certs/app.team1.test.pem` and its matching private key.
- AirDrop the certificate bundle only to Meet for the temporary standby edge. Never commit or send the private key outside the team.
- Pull the same repository revision on all Macs.
- Give each long-running process its own Terminal window. Do not reuse that window for tests.
- Create a shared screenshot folder before starting. Use the exact evidence names below.
- Read the rollback commands for DNS, nginx, and `pf` before changing any state.

## Ready-to-copy repository files

Copy these files to the paths used by the runbook:

| Destination | Repository source | Owner |
|---|---|---|
| `~/cn-phase2-dnsmasq.conf` | `configs/dnsmasq/cn-phase2-dnsmasq.conf` | Aarush |
| `~/cn-backup-dnsmasq.conf` | `configs/dnsmasq/cn-backup-dnsmasq.conf` | Meet |
| `~/cn-phase2-nginx.conf` | `configs/nginx/cn-phase2-nginx.conf` | Deepak |
| `~/cn-standby-nginx.conf` | `configs/nginx/cn-standby-nginx.conf` | Meet |
| `~/mac3-backend-isolation.rules` | `configs/firewall/mac3-backend-isolation.rules` | Meet |
| `~/mac4-backend-isolation.rules` | `configs/firewall/mac4-backend-isolation.rules` | Utkarsh |

The nginx files intentionally contain `HOMEDIR`. On the destination Mac, replace it with the actual home directory and validate before starting:

```bash
sed -i '' "s|HOMEDIR|$HOME|g" ~/cn-phase2-nginx.conf
nginx -t -c ~/cn-phase2-nginx.conf
```

Use `~/cn-standby-nginx.conf` in both commands on Mac 3.

## Execution order - do not reorder

1. Start Phase 1 and prove six clean alternating responses.
2. Extension D: stop Backend A, prove every request uses B, restart A, wait 12 seconds, prove A/B balancing resumes.
3. Extension A: start identical primary and backup DNS, configure both client resolvers, stop the primary, prove resolution and HTTPS still work, then restore it.
4. Extension B: pause backup DNS, demonstrate the 30-second cached answer, then demonstrate an immediate change after a cache flush.
5. Extension E: start the standby edge, test it directly with `--resolve`, perform the DNS cutover, prove the `X-Edge` transition, stop the primary edge, then restore the primary.
6. Extension C: only after the standby-edge test, load backend firewall rules, prove Mac 1 is blocked and Mac 2 is allowed, prove the normal HTTPS path still works, and roll the rules back immediately.
7. Extension F: practise bottom-up diagnosis and speak the layer aloud.
8. Collect configs and screenshots, complete the report, then perform cleanup.

The ordering matters: Extension B requires the backup resolver to be paused, and Extension E must happen before Extension C because Mac 3's standby edge needs direct backend access.

## Stop/go gates

| Gate | Do not continue until this is true |
|---|---|
| Baseline | Six HTTPS requests return `200` and alternate `X-Backend: A/B` without `-k`. |
| D complete | With A stopped, ten requests return `200` from B; after restart and 12 seconds, A/B alternation returns. |
| A complete | Primary DNS times out, but the system resolver returns `10.7.12.112` through backup DNS and HTTPS returns `200`. |
| B complete | The client visibly keeps the old IP until about 30 seconds, then changes; a separate flush changes it immediately. |
| E complete | Direct standby test shows `X-Edge: mac3-standby`; cutover moves cached traffic from primary to standby; service survives primary-edge shutdown. |
| C complete | Mac 1 times out on direct backend ports, Mac 2 gets `200`, normal HTTPS still alternates, and rollback leaves zero `3001/3002` pf rules. |

## Evidence checklist

Put all files in `evidence/07-phase2/`. A screenshot should show the command and the decisive output.

### D - backend failover

- [ ] `D1-nginx-config.png`
- [ ] `D2-backend-a-down.png` (plus `D2a-meet-ctrlc.png` if needed)
- [ ] `D3-balancing-resumed.png`

### A - backup DNS

- [ ] `A1-primary-dns.png`
- [ ] `A2-backup-dns-running.png`
- [ ] `A3-mac4-two-dns.png`
- [ ] `A3-mac2-two-dns.png`
- [ ] `A4-primary-stopped.png`
- [ ] `A5-failover-works.png`

### B - TTL

- [ ] `B1-ttl-expiry.png`
- [ ] `B2-flush.png`

### E - standby edge and cutover

- [ ] `E1-standby-running.png`
- [ ] `E2-both-edges.png`
- [ ] `E3-cutover.png`
- [ ] `E4-primary-edge-stopped.png`

### C - service isolation

- [ ] `C0-firewall-before-mac3.png`
- [ ] `C0-firewall-before-mac4.png`
- [ ] `C1-rules-mac3.png`
- [ ] `C1-rules-mac4.png`
- [ ] `C2-blocked-from-mac1.png`
- [ ] `C3-allowed-from-mac2.png`
- [ ] `C4-edge-still-works.png`
- [ ] `C5-rollback-done.png`

### F - diagnosis

- [ ] `F1-drill.png`

## Fast demo choice

For final demonstration step 9, show backup DNS failover. It is the shortest, clearest resilience proof:

1. Display both configured resolver addresses.
2. Stop primary dnsmasq on Mac 1.
3. Query the primary explicitly and show that it times out.
4. Flush Mac 4's cache, resolve through the system resolver, and show `10.7.12.112`.
5. Request the HTTPS URL and show `HTTP/1.1 200 OK`.
6. Restart primary dnsmasq.

Keep the TTL and edge-cutover screenshots ready if the evaluator asks for Extensions B or E.

## Troubleshooting ladder

Always test in this order and say the layer before each command:

```bash
nslookup app.team1.test
ping -c 2 10.7.12.112
nc -vz -G 3 10.7.12.112 8443
curl -v https://app.team1.test:8443/api/status 2>&1 | grep -E 'SSL|subject|issuer|HTTP/'
curl -i https://app.team1.test:8443/api/status
```

Interpretation:

- `NXDOMAIN` or resolver timeout: DNS layer.
- Ping fails: IP reachability, wrong address, Wi-Fi, or host problem.
- TCP `refused`: host answered but nothing is listening on that port.
- TCP timeout: packets are being dropped, the address is wrong, or the host is offline.
- Certificate error: TCP worked; inspect hostname, dates, and trust.
- `502 Bad Gateway`: DNS, TCP, and TLS reached nginx; the failure is behind the edge.

## Rollback and cleanup

- Restore primary DNS records to `10.7.12.112` before finishing.
- On Mac 3 and Mac 4, reload `/etc/pf.conf`; if `pf` was originally disabled, disable it again.
- Confirm `sudo pfctl -sr | grep -cE '300[12]'` prints `0`.
- Stop both nginx instances using their own configuration paths.
- Stop foreground dnsmasq and backend processes with `Ctrl+C`.
- On each altered client, run `sudo networksetup -setdnsservers Wi-Fi Empty`.
- Confirm `networksetup -getdnsservers Wi-Fi` reports no DNS servers set.

## Viva answers in one line

| Question | Answer |
|---|---|
| DNS failure vs app failure | DNS failure prevents name resolution; app failure occurs after resolution and appears as connection failure or `502`. |
| Backup DNS | Clients list two equivalent resolvers and try the second after the first times out. |
| TTL | It is the time a DNS answer may be reused without asking again. |
| Real migration | Lower TTL early, change the record, wait one old TTL, cut over, then raise TTL. |
| Backend isolation | `pf` permits backend ports only from Mac 2 and silently drops other sources. |
| `block drop` vs `block return` | Drop causes a timeout; return sends an immediate rejection/reset. |
| nginx failover | Two failed attempts mark an upstream unavailable for 10 seconds; the request retries on the other backend. |
| Remaining single point of failure | Mac 2's edge; remove it with a second edge plus automatic VRRP or health-checked DNS failover. |
| DNS cutover | Change the A record to the standby edge; clients move as their cached answers expire. |
| Diagnostic method | DNS, IP reachability, TCP port, TLS, then application. |
