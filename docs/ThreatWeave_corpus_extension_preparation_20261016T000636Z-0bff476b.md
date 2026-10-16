# Remaining three development reports: source preparation

No model/service calls, graph writes or evaluation scores. Human verification pending.
Frozen source-only selection excludes held-out reports and all previously prepared windows.
Gold triples and QA reference answers were not read. Technical sections end before Mitigations.
The four-relation cap and existing mention/table recognition limits remain diagnostic constraints.

Saved artifacts: S:\ThreatWeave\work\corpus_extension_chunks\20261016T000636Z-0bff476b
Prepared fingerprint: 741eb5d1c093855c3dcab7f8bc62622bfc6afbcc8ae747dfb2d1fc4d0b2e5b34
Extraction plan fingerprint: 4a78a36d24a4195b85256c120b8d5163af46c722041114165d1fe823558c8960

| Report | Windows | Technical source span |
| --- | ---: | --- |
| AA24-038A | 19 | 6032:48255 |
| AA23-144A | 9 | 2866:19961 |
| AA22-321A | 5 | 1806:11131 |

Total windows: 33. Windows without recognized mentions: 2.
Prompt budgets reserve 700 output tokens and 256 chat tokens within the unchanged 8192-token context.
These are estimates, not live formatted-prompt measurements.

## Per-window preflight

| Scope | Source tokens | Mentions | Evidence patterns | Estimated prompt/schema tokens |
| --- | ---: | ---: | ---: | ---: |
| AA24-038A:development:llama500:6032:8859 | 517 | 3 | 0 | 1426 |
| AA24-038A:development:llama500:8540:11244 | 479 | 4 | 1 | 1546 |
| AA24-038A:development:llama500:10885:13980 | 526 | 1 | 0 | 1399 |
| AA24-038A:development:llama500:13617:16082 | 527 | 21 | 10 | 3236 |
| AA24-038A:development:llama500:15793:18394 | 534 | 11 | 7 | 2571 |
| AA24-038A:development:llama500:18096:20499 | 479 | 15 | 4 | 2238 |
| AA24-038A:development:llama500:20222:22508 | 484 | 16 | 9 | 2872 |
| AA24-038A:development:llama500:22202:24566 | 503 | 18 | 4 | 2368 |
| AA24-038A:development:llama500:24254:26777 | 507 | 15 | 5 | 2366 |
| AA24-038A:development:llama500:26482:28837 | 472 | 5 | 0 | 1421 |
| AA24-038A:development:llama500:28528:31303 | 540 | 10 | 3 | 2020 |
| AA24-038A:development:llama500:30941:33296 | 495 | 13 | 6 | 2490 |
| AA24-038A:development:llama500:33045:35669 | 516 | 8 | 2 | 1812 |
| AA24-038A:development:llama500:35388:37325 | 476 | 1 | 0 | 1397 |
| AA24-038A:development:llama500:37047:39344 | 484 | 0 | 0 | 1387 |
| AA24-038A:development:llama500:39055:41394 | 458 | 2 | 0 | 1386 |
| AA24-038A:development:llama500:41087:43719 | 492 | 4 | 2 | 1696 |
| AA24-038A:development:llama500:43343:46216 | 506 | 2 | 0 | 1428 |
| AA24-038A:development:llama500:45851:48255 | 408 | 1 | 0 | 1303 |
| AA23-144A:development:llama500:2866:5312 | 495 | 12 | 1 | 1825 |
| AA23-144A:development:llama500:5058:7282 | 510 | 8 | 0 | 1533 |
| AA23-144A:development:llama500:7090:8977 | 506 | 5 | 1 | 1641 |
| AA23-144A:development:llama500:8817:10877 | 509 | 2 | 0 | 1417 |
| AA23-144A:development:llama500:10640:12844 | 486 | 6 | 0 | 1480 |
| AA23-144A:development:llama500:12637:15219 | 513 | 4 | 0 | 1456 |
| AA23-144A:development:llama500:14842:17098 | 490 | 8 | 0 | 1528 |
| AA23-144A:development:llama500:16923:18755 | 499 | 18 | 0 | 1848 |
| AA23-144A:development:llama500:18586:19961 | 510 | 13 | 0 | 1703 |
| AA22-321A:development:llama500:1806:4233 | 486 | 9 | 4 | 2106 |
| AA22-321A:development:llama500:3953:6298 | 491 | 11 | 4 | 2147 |
| AA22-321A:development:llama500:5976:8313 | 522 | 14 | 1 | 1940 |
| AA22-321A:development:llama500:8030:9146 | 504 | 0 | 0 | 1523 |
| AA22-321A:development:llama500:9038:11131 | 520 | 12 | 1 | 1963 |

Next: operator-run bounded extraction, followed by candidate source review before any import or index refresh.
