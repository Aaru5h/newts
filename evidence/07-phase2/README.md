# Phase 2 capture index

57 unedited screenshots from the team session. Names describe visible subject matter; numeric prefixes are stable identifiers, not global chronology. Original filenames below preserve approximate capture/sharing times in IST. See [the final report](../../docs/phase2-report.md) for conclusions and evidence limitations.

## Quick evaluator navigation

| Extension | Start here |
|---|---|
| A - backup DNS | 18, 35, 36; Deepak dual DNS: 04 |
| B - TTL and flush attempt | 38-40; record changes: 15-16 |
| C - isolation and rollback | 12, 02, 21-27, 47-54 |
| D - failover and recovery | 03, 33-34 |
| E - standby edge and migration | 19-20, 41-46 |
| F - diagnosis and recovery | 55-56 |

## Every capture and its source

| Capture | Original path / approximate timestamp | SHA-256 |
|---|---|---|
| [00-deepak-baseline-backends.png](00-deepak-baseline-backends.png) | Evidence 2/Screenshot 2026-11-23 at 11.59.48 PM.png | `adbdc4f1f59eeecbe416a321979df1b8102ed17d1f0b9616e09e8909cb96f004` |
| [01-deepak-dns-and-edge-tests.png](01-deepak-dns-and-edge-tests.png) | Evidence 2/Screenshot 2026-11-24 at 1.30.57 AM.png | `251f699fe90739d49f4fdea8e54ac3260acbfd5a3e9dd8d33dd7cb929c8eb092` |
| [02-deepak-backend-a-allowed.png](02-deepak-backend-a-allowed.png) | Evidence 2/Screenshot 2026-11-24 at 1.44.51 AM.png | `25f61483af46cab7b6bc8e3f8f8ae9bddd790f3afb8f16c03956d490c064ac12` |
| [03-deepak-nginx-config.png](03-deepak-nginx-config.png) | Evidence 2/Screenshot 2026-11-24 at 12.10.05 AM.png | `711e4ae0231ff9a26a95ecdc5ef8b133d885153159ce86c74c9acb3c2700923f` |
| [04-deepak-dual-dns.png](04-deepak-dual-dns.png) | Evidence 2/Screenshot 2026-11-24 at 12.28.31 AM.png | `455ccb7116cf9914efd488c1bd1a2b4f54637e6636ac3ba7934521066ccfc183` |
| [05-deepak-dns-cleanup.png](05-deepak-dns-cleanup.png) | Evidence 2/Screenshot 2026-11-24 at 2.01.10 AM.png | `0322daa947c63f435ad4bd00e5084d8257b4f1fea6b89f47813b5feead73a08f` |
| [06-aarush-dns-and-backend-context.png](06-aarush-dns-and-backend-context.png) | Screenshot 2026-11-24 at 1.03.21 AM.png | `2b68206fbfae4516a048be6e51870ff62b760e4fdd79b9c294dd79a7394e0077` |
| [07-aarush-dns-and-backend-context.png](07-aarush-dns-and-backend-context.png) | Screenshot 2026-11-24 at 1.17.21 AM.png | `ea70009c2da9f576a97df30c21a7a3aecee81843e8235dbd6633ca778ce3b3f3` |
| [08-aarush-dns-process-context.png](08-aarush-dns-process-context.png) | Screenshot 2026-11-24 at 1.23.31 AM.png | `563a3a4098f9cc49423f0254db587e940eb858d4972d67469529d1a2b9d7554e` |
| [09-aarush-dns-process-context.png](09-aarush-dns-process-context.png) | Screenshot 2026-11-24 at 1.26.27 AM.png | `64d9803c55e5de42fdec2459913d5c1c1548bab525803e3b3f4db4dc189b81c5` |
| [10-aarush-backend-connectivity.png](10-aarush-backend-connectivity.png) | Screenshot 2026-11-24 at 1.27.50 AM.png | `b39aa89c697231632f583b7623925ba26c545a866074d9e50d8ebf9598dd57af` |
| [11-aarush-firewall-troubleshooting.png](11-aarush-firewall-troubleshooting.png) | Screenshot 2026-11-24 at 1.38.49 AM.png | `46ceacfa3afc84be122a5b80f87302f3d6638430dce921bf523b20595d93abd9` |
| [12-aarush-firewall-timeout-and-recovery.png](12-aarush-firewall-timeout-and-recovery.png) | Screenshot 2026-11-24 at 1.42.47 AM.png | `1a12b0ccb665c95bb7f4d760ff5a37b3c57e1f4263ed1e9480274b2ace95a8a5` |
| [13-aarush-backend-recovery.png](13-aarush-backend-recovery.png) | Screenshot 2026-11-24 at 1.47.47 AM.png | `e319840da38e749ae09a9a0495a1f0f0f2a068a31ecd6f3dd860d05d707d4730` |
| [14-aarush-primary-dns-config.png](14-aarush-primary-dns-config.png) | Screenshot 2026-11-24 at 12.26.28 AM.png | `ce2d457ccb16a18ba41eb1217c5765e3de5027af325c5efe0a2b865652dd9160` |
| [15-aarush-dns-record-change.png](15-aarush-dns-record-change.png) | Screenshot 2026-11-24 at 12.33.21 AM.png | `89828b24ccde6c89e793ee89c3859eeb555a4868819a1b992e44ed9cf6a57b00` |
| [16-aarush-dns-record-restoration.png](16-aarush-dns-record-restoration.png) | Screenshot 2026-11-24 at 12.42.03 AM.png | `05fad49aeb91351f653886c954498f387a84423ac8641014622b20f4d06a2613` |
| [17-meet-backend-a-launch.jpeg](17-meet-backend-a-launch.jpeg) | meet-ss/WhatsApp Image 2026-11-23 at 23.58.51.jpeg | `c1b98d6bfa3ef578bdb17c54ea55ed30fa8acc2eaa265bba457835e46b5a4ff6` |
| [18-meet-backup-dns-running.jpeg](18-meet-backup-dns-running.jpeg) | meet-ss/WhatsApp Image 2026-11-24 at 00.22.24.jpeg | `b270be09154c337b9a3d71946bd9622f316b9dc2fdde45bbec6b68690ddc90d5` |
| [19-meet-standby-nginx-setup.jpeg](19-meet-standby-nginx-setup.jpeg) | meet-ss/WhatsApp Image 2026-11-24 at 00.50.25.jpeg | `d35c431ddae76688ea8cd96b3488ff2c46dd9b328d556b508a9b2becc5c83862` |
| [20-meet-standby-nginx-running.jpeg](20-meet-standby-nginx-running.jpeg) | meet-ss/WhatsApp Image 2026-11-24 at 00.59.31.jpeg | `bcb1d1f0fbbc86da9cd0448a95223e5fe82b9403b1bf7f9101680b46e0d32d8c` |
| [21-meet-firewall-mac3-rules.jpeg](21-meet-firewall-mac3-rules.jpeg) | meet-ss/WhatsApp Image 2026-11-24 at 01.01.17.jpeg | `cf24efcf0bbbdbac441a8138d2dbbdada6138c53a479ed2f40ef43f99f6d6c04` |
| [22-meet-firewall-mac3-rules.jpeg](22-meet-firewall-mac3-rules.jpeg) | meet-ss/WhatsApp Image 2026-11-24 at 01.02.45.jpeg | `6291e2cd2b7f6b8512542d81b6ba135e0095ac75a879a0ea8b3a74a8efa18a5b` |
| [23-meet-firewall-mac3-reload.jpeg](23-meet-firewall-mac3-reload.jpeg) | meet-ss/WhatsApp Image 2026-11-24 at 01.31.53.jpeg | `76fada0869e026c1963fd3f5b2b99c23de91f70c5861c412b0dc59a27177ed6e` |
| [24-meet-firewall-mac3-reload.jpeg](24-meet-firewall-mac3-reload.jpeg) | meet-ss/WhatsApp Image 2026-11-24 at 01.32.29.jpeg | `0402ce22cd3500ee7ba9ae19d5b7db5c192ed1c1b8cb33b1a6f7b8d11604e90a` |
| [25-meet-firewall-mac3-state.jpeg](25-meet-firewall-mac3-state.jpeg) | meet-ss/WhatsApp Image 2026-11-24 at 01.34.33.jpeg | `066dde3033962c55c37f787a709fa74b5ec3c1f8c3dc7a7a406f4759727f7dc9` |
| [26-meet-firewall-mac3-enabled.jpeg](26-meet-firewall-mac3-enabled.jpeg) | meet-ss/WhatsApp Image 2026-11-24 at 01.40.25.jpeg | `52a08bda9c94a8a6b1bcc2a4e8cce338533389357e3969732263954c5b95795b` |
| [27-meet-firewall-mac3-rollback.jpeg](27-meet-firewall-mac3-rollback.jpeg) | meet-ss/WhatsApp Image 2026-11-24 at 01.46.25.jpeg | `376c72e0281b86973d8f1e3a84f5a178f056fd4052ba99d00e57adc755d29025` |
| [28-utkarsh-backend-b-launch.jpeg](28-utkarsh-backend-b-launch.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.01.54.jpeg | `20a8762169fdbd68c92e861076b60f1aa9632601dd7a09258233f895a73ae3fb` |
| [29-utkarsh-baseline-dns.jpeg](29-utkarsh-baseline-dns.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.13.12.jpeg | `f05a34887292e051a5cc3ffb305d546768312859c131e772139688f34a31df7d` |
| [30-utkarsh-client-dns-settings.jpeg](30-utkarsh-client-dns-settings.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.14.36.jpeg | `72e680b329bd215cf29099ba91e81bc763f7eb70ef4257f20645d1656b51fb3f` |
| [31-utkarsh-trusted-https.jpeg](31-utkarsh-trusted-https.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.15.23.jpeg | `2947f8687d21207424075b493b23a916ecab704e19dd6389d5a93fff1dccf4f9` |
| [32-utkarsh-baseline-balancing.jpeg](32-utkarsh-baseline-balancing.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.15.45.jpeg | `3588198b524c204d74d45e1faf3174be4519839f40d9c7e1f32aef75a28b6022` |
| [33-utkarsh-backend-failover.jpeg](33-utkarsh-backend-failover.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.17.37.jpeg | `17ebee877846f45c16a5354ad379257c1f7257fc83bf9319ae61ab73418b4308` |
| [34-utkarsh-balancing-restored.jpeg](34-utkarsh-balancing-restored.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.20.20.jpeg | `161d317d699cabdae6e7472756f76a040170681fa81ea1a3c13ff9646e88a13d` |
| [35-utkarsh-backup-dns-settings.jpeg](35-utkarsh-backup-dns-settings.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.27.40.jpeg | `4685ebc932538d566283414c0df1d1abd590472e9e132b49a318a980c56bacf4` |
| [36-utkarsh-backup-dns-failover.jpeg](36-utkarsh-backup-dns-failover.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.28.21.jpeg | `5e041185fb759b8fadf8b6583db707d9f4e37c8b033bc873ba69ff06404cb13d` |
| [37-utkarsh-dns-and-ttl-preparation.jpeg](37-utkarsh-dns-and-ttl-preparation.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.31.40.jpeg | `37504b39b68fcf858b4aab5f8cbbedfc668f832a99d4b1146cb82128ed4dea91` |
| [38-utkarsh-ttl-observation.jpeg](38-utkarsh-ttl-observation.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.40.42.jpeg | `33ddb20f9239da7fef6d6fd13732f294de572e53eea84d282e0e9a54f30ed752` |
| [39-utkarsh-ttl-observation.jpeg](39-utkarsh-ttl-observation.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.41.58.jpeg | `38c4560fd39b09a585b8d9ded6dd43277562223f7545bd0e0dce11291e1db4a9` |
| [40-utkarsh-ttl-and-flush-attempt.jpeg](40-utkarsh-ttl-and-flush-attempt.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.44.23.jpeg | `ab709b87095aa4719f2dbc265e2d0bdef7e830f968f0b809f2c5269e74e83e8b` |
| [41-utkarsh-both-edges.jpeg](41-utkarsh-both-edges.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.51.22.jpeg | `b008c10723af8cc4c0bea1a0c49fa1e044002fab0878a3cbf1d69017f6b38470` |
| [42-utkarsh-both-edges.jpeg](42-utkarsh-both-edges.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.51.55.jpeg | `8b1cf46ab96c26179cf05137a73d3192bbbf6892bba5c1be36b9fc1b0ebe7e5b` |
| [43-utkarsh-edge-cutover.jpeg](43-utkarsh-edge-cutover.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.54.20.jpeg | `0d45890e241d1f3b45432fe1bb2cbc0ed9edf9d0ce755aa40f984079c741dc7a` |
| [44-utkarsh-edge-cutover.jpeg](44-utkarsh-edge-cutover.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.56.13.jpeg | `8e4c0ab2ad608d3d20513321a4f69cf50844891226fb591197e11563c208d1cc` |
| [45-utkarsh-standby-after-primary-stop.jpeg](45-utkarsh-standby-after-primary-stop.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 00.57.16.jpeg | `d3b149ba5f33957c8ae6631b04df8c4f25b78a013e1db23527bc419ce7e7608b` |
| [46-utkarsh-primary-edge-restored.jpeg](46-utkarsh-primary-edge-restored.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.04.51.jpeg | `f353050bfad7794b3f21aa76094fe572eca19f9afc6df8b654695c0fa0a2eb52` |
| [47-utkarsh-firewall-mac4-rules.jpeg](47-utkarsh-firewall-mac4-rules.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.06.00.jpeg | `63d86881e1b92d4cb27476d238b9cb9c098d77d1195505aa654de93f8eb2434e` |
| [48-utkarsh-firewall-mac4-rules.jpeg](48-utkarsh-firewall-mac4-rules.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.07.55.jpeg | `b8f22e7ff492fcf6b7310bab09d3c99f5eb576962cd9f9d98ba67cfaa3190da2` |
| [49-utkarsh-firewall-and-https.jpeg](49-utkarsh-firewall-and-https.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.30.52.jpeg | `1782e674b5d00795cadf8625421ea1a0aa0cae75ffbc101f4a4090c13aa3ade2` |
| [50-utkarsh-firewall-and-https.jpeg](50-utkarsh-firewall-and-https.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.31.47.jpeg | `baf8ac757fab283b9facacd869b25264c23fcc6de01d54cf28f138ef9c86f094` |
| [51-utkarsh-firewall-and-https.jpeg](51-utkarsh-firewall-and-https.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.32.25.jpeg | `4fecfcb2a464307da446bb1bcbddca68e5ad8e88f0a5980b9a3f71b864b398f3` |
| [52-utkarsh-firewall-mac4-rollback.jpeg](52-utkarsh-firewall-mac4-rollback.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.34.49.jpeg | `7debb7eb28e0a280141385112ef1927ae0af743088c47f2b4df033785972027f` |
| [53-utkarsh-firewall-mac4-rollback.jpeg](53-utkarsh-firewall-mac4-rollback.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.36.16.jpeg | `7b15255fec58b274d68b93cad8c18cf4579388540d11e32faf94897c5dabbd82` |
| [54-utkarsh-firewall-mac4-clean.jpeg](54-utkarsh-firewall-mac4-clean.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.37.26.jpeg | `26bc384fed67c87c79417f587b36fab77c7f85e9f0739b6126993b5dd0e0743e` |
| [55-utkarsh-wrong-dns-drill.jpeg](55-utkarsh-wrong-dns-drill.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.51.23.jpeg | `2c6a06aa8f9076da549a9066c8ed5132fb57250754edd136588751bb619c934c` |
| [56-utkarsh-dns-drill-recovery.jpeg](56-utkarsh-dns-drill-recovery.jpeg) | utkarsh-ss/WhatsApp Image 2026-11-24 at 01.54.45.jpeg | `cbf0387c04e11bf0c5f6f204102ffd69fb21cda66de964436d03ac1ad621bbd4` |

## Configuration provenance

- `configs/dnsmasq/cn-phase2-dnsmasq.conf`: Aarush's actual home-directory configuration, restored to the primary edge.
- `configs/dnsmasq/cn-backup-dnsmasq.conf`: supplied backup configuration.
- `configs/nginx/`: submitted Deepak primary and Meet standby files; historical Phase 1 config retained separately.
- `configs/firewall/`: submitted per-Mac rules and baseline/rollback files.
- Raw imports, certificate keys/archives, and duplicate repository are preserved locally under ignored `useless/phase-2-originals/`.
