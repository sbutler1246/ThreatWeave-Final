# Seven held-out reports: source preparation

No model/service calls, graph writes or evaluation scores. Human verification pending.
Frozen source-only selection includes the seven held-out reports only. No benchmark labels or reference answers are loaded.
Gold triples and QA reference answers were not read. Technical sections end before Mitigations.
The four-relation cap and existing mention/table recognition limits remain diagnostic constraints.

Saved artifacts: S:\ThreatWeave\work\evaluation_corpus_chunks\20261016T040604Z-bccf59fb
Prepared fingerprint: 687258c21650ca1e12d809d6dc73140029efd6538b6e38ec19c73f280e694dd2
Extraction plan fingerprint: 89764a8af84a83b36f3aa17425775142376c305bddfd9ce07fc7019ded39945b

| Report | Windows | Technical source span |
| --- | ---: | --- |
| AA23-165A | 14 | 2310:28843 |
| AA23-061A | 25 | 4148:35790 |
| AA24-131A | 7 | 4174:17845 |
| AA24-109A | 21 | 4787:39746 |
| AA25-071A | 15 | 4851:32570 |
| AA23-352A | 17 | 3851:24531 |
| AA23-075A | 15 | 2065:25424 |

Total windows: 114. Windows without recognized mentions: 13.
Prompt budgets reserve 700 output tokens and 256 chat tokens within the unchanged 8192-token context.
These are estimates, not live formatted-prompt measurements.

## Per-window preflight

| Scope | Source tokens | Mentions | Evidence patterns | Estimated prompt/schema tokens |
| --- | ---: | ---: | ---: | ---: |
| AA23-165A:evaluation:llama500:2310:4719 | 512 | 4 | 0 | 1472 |
| AA23-165A:evaluation:llama500:4484:6401 | 493 | 11 | 1 | 1764 |
| AA23-165A:evaluation:llama500:6168:8098 | 497 | 3 | 0 | 1553 |
| AA23-165A:evaluation:llama500:7876:9874 | 458 | 5 | 0 | 1488 |
| AA23-165A:evaluation:llama500:9561:12066 | 523 | 8 | 1 | 1689 |
| AA23-165A:evaluation:llama500:11762:14040 | 499 | 12 | 1 | 1959 |
| AA23-165A:evaluation:llama500:13738:15981 | 497 | 14 | 8 | 2963 |
| AA23-165A:evaluation:llama500:15691:17884 | 494 | 16 | 0 | 1924 |
| AA23-165A:evaluation:llama500:17571:19802 | 497 | 10 | 0 | 1707 |
| AA23-165A:evaluation:llama500:19556:21857 | 498 | 10 | 0 | 1692 |
| AA23-165A:evaluation:llama500:21591:23692 | 497 | 16 | 1 | 2035 |
| AA23-165A:evaluation:llama500:23461:25646 | 499 | 22 | 5 | 2634 |
| AA23-165A:evaluation:llama500:25345:27570 | 503 | 18 | 3 | 2318 |
| AA23-165A:evaluation:llama500:26834:28843 | 500 | 19 | 2 | 2209 |
| AA23-061A:evaluation:llama500:4148:6616 | 500 | 15 | 8 | 2808 |
| AA23-061A:evaluation:llama500:6346:8622 | 503 | 20 | 12 | 3423 |
| AA23-061A:evaluation:llama500:8314:10530 | 498 | 11 | 3 | 2074 |
| AA23-061A:evaluation:llama500:10300:11484 | 503 | 2 | 0 | 1666 |
| AA23-061A:evaluation:llama500:11361:12517 | 501 | 2 | 0 | 1660 |
| AA23-061A:evaluation:llama500:12363:13460 | 514 | 7 | 2 | 1893 |
| AA23-061A:evaluation:llama500:13347:14347 | 498 | 5 | 3 | 1889 |
| AA23-061A:evaluation:llama500:14225:15219 | 493 | 15 | 13 | 3469 |
| AA23-061A:evaluation:llama500:15072:16294 | 517 | 13 | 13 | 3429 |
| AA23-061A:evaluation:llama500:16175:17122 | 500 | 11 | 0 | 1622 |
| AA23-061A:evaluation:llama500:17023:18422 | 530 | 16 | 0 | 1791 |
| AA23-061A:evaluation:llama500:18102:19740 | 492 | 40 | 1 | 2526 |
| AA23-061A:evaluation:llama500:19628:21225 | 485 | 9 | 7 | 2575 |
| AA23-061A:evaluation:llama500:21018:22127 | 513 | 12 | 0 | 1695 |
| AA23-061A:evaluation:llama500:21984:23147 | 511 | 18 | 0 | 1808 |
| AA23-061A:evaluation:llama500:23031:24536 | 494 | 24 | 2 | 2243 |
| AA23-061A:evaluation:llama500:24400:25638 | 500 | 8 | 0 | 1765 |
| AA23-061A:evaluation:llama500:25468:26522 | 485 | 22 | 0 | 1945 |
| AA23-061A:evaluation:llama500:26384:27829 | 495 | 22 | 28 | 5888 |
| AA23-061A:evaluation:llama500:27654:29231 | 498 | 1 | 0 | 1440 |
| AA23-061A:evaluation:llama500:28955:31241 | 497 | 12 | 0 | 1791 |
| AA23-061A:evaluation:llama500:30968:32954 | 504 | 10 | 0 | 1779 |
| AA23-061A:evaluation:llama500:32858:33890 | 497 | 0 | 0 | 1431 |
| AA23-061A:evaluation:llama500:33746:34826 | 502 | 0 | 0 | 1451 |
| AA23-061A:evaluation:llama500:34320:35790 | 500 | 0 | 0 | 1484 |
| AA24-131A:evaluation:llama500:4174:6733 | 553 | 18 | 12 | 3410 |
| AA24-131A:evaluation:llama500:6550:8835 | 489 | 28 | 15 | 4065 |
| AA24-131A:evaluation:llama500:8514:10969 | 510 | 16 | 18 | 4177 |
| AA24-131A:evaluation:llama500:10786:13129 | 492 | 27 | 14 | 3906 |
| AA24-131A:evaluation:llama500:12807:15323 | 510 | 16 | 11 | 3296 |
| AA24-131A:evaluation:llama500:15045:17380 | 518 | 20 | 5 | 2648 |
| AA24-131A:evaluation:llama500:15803:17845 | 500 | 13 | 3 | 2223 |
| AA24-109A:evaluation:llama500:4787:6854 | 495 | 12 | 5 | 2318 |
| AA24-109A:evaluation:llama500:6537:8882 | 490 | 25 | 10 | 3294 |
| AA24-109A:evaluation:llama500:8607:10825 | 493 | 26 | 14 | 3954 |
| AA24-109A:evaluation:llama500:10612:12792 | 490 | 33 | 22 | 5143 |
| AA24-109A:evaluation:llama500:12528:14948 | 511 | 14 | 9 | 2902 |
| AA24-109A:evaluation:llama500:14693:17032 | 493 | 9 | 1 | 1747 |
| AA24-109A:evaluation:llama500:16749:19037 | 498 | 22 | 3 | 2302 |
| AA24-109A:evaluation:llama500:18804:21019 | 500 | 20 | 16 | 4027 |
| AA24-109A:evaluation:llama500:20761:22564 | 488 | 14 | 7 | 2683 |
| AA24-109A:evaluation:llama500:22442:23336 | 497 | 4 | 2 | 1710 |
| AA24-109A:evaluation:llama500:23225:24336 | 510 | 11 | 3 | 2067 |
| AA24-109A:evaluation:llama500:24217:25330 | 499 | 13 | 3 | 2163 |
| AA24-109A:evaluation:llama500:25188:26526 | 509 | 15 | 0 | 1875 |
| AA24-109A:evaluation:llama500:26404:27411 | 497 | 9 | 6 | 2361 |
| AA24-109A:evaluation:llama500:27250:29059 | 497 | 23 | 6 | 2783 |
| AA24-109A:evaluation:llama500:28777:31133 | 496 | 16 | 4 | 2372 |
| AA24-109A:evaluation:llama500:30823:33030 | 499 | 11 | 1 | 1874 |
| AA24-109A:evaluation:llama500:32784:35082 | 498 | 19 | 5 | 2611 |
| AA24-109A:evaluation:llama500:34797:37085 | 498 | 24 | 10 | 3349 |
| AA24-109A:evaluation:llama500:36883:38919 | 499 | 19 | 9 | 3119 |
| AA24-109A:evaluation:llama500:37679:39746 | 500 | 22 | 10 | 3332 |
| AA25-071A:evaluation:llama500:4851:6963 | 473 | 5 | 3 | 1860 |
| AA25-071A:evaluation:llama500:6767:8826 | 466 | 2 | 0 | 1382 |
| AA25-071A:evaluation:llama500:8653:10741 | 490 | 19 | 8 | 2926 |
| AA25-071A:evaluation:llama500:10438:12511 | 462 | 8 | 3 | 1904 |
| AA25-071A:evaluation:llama500:12220:14519 | 570 | 16 | 7 | 2811 |
| AA25-071A:evaluation:llama500:14289:16172 | 469 | 16 | 7 | 2634 |
| AA25-071A:evaluation:llama500:16025:18061 | 504 | 16 | 7 | 2657 |
| AA25-071A:evaluation:llama500:17810:20469 | 572 | 10 | 5 | 2332 |
| AA25-071A:evaluation:llama500:20162:22243 | 504 | 1 | 0 | 1505 |
| AA25-071A:evaluation:llama500:22047:23538 | 493 | 5 | 0 | 1681 |
| AA25-071A:evaluation:llama500:23412:24966 | 495 | 14 | 0 | 1807 |
| AA25-071A:evaluation:llama500:24695:26937 | 497 | 22 | 4 | 2565 |
| AA25-071A:evaluation:llama500:26712:28840 | 500 | 20 | 6 | 2755 |
| AA25-071A:evaluation:llama500:28548:30967 | 517 | 12 | 0 | 1799 |
| AA25-071A:evaluation:llama500:30061:32570 | 500 | 2 | 0 | 1399 |
| AA23-352A:evaluation:llama500:3851:6199 | 532 | 33 | 25 | 5758 |
| AA23-352A:evaluation:llama500:5924:7968 | 437 | 15 | 7 | 2613 |
| AA23-352A:evaluation:llama500:7618:10055 | 500 | 8 | 7 | 2500 |
| AA23-352A:evaluation:llama500:9760:11935 | 512 | 11 | 15 | 3729 |
| AA23-352A:evaluation:llama500:11828:12848 | 497 | 10 | 1 | 1745 |
| AA23-352A:evaluation:llama500:12733:14443 | 503 | 10 | 8 | 2731 |
| AA23-352A:evaluation:llama500:14145:16344 | 498 | 20 | 19 | 4512 |
| AA23-352A:evaluation:llama500:16080:17724 | 500 | 5 | 5 | 2249 |
| AA23-352A:evaluation:llama500:17529:18539 | 590 | 1 | 1 | 1586 |
| AA23-352A:evaluation:llama500:18455:19130 | 483 | 0 | 0 | 1272 |
| AA23-352A:evaluation:llama500:19034:19853 | 500 | 0 | 0 | 1290 |
| AA23-352A:evaluation:llama500:19771:20652 | 560 | 0 | 0 | 1330 |
| AA23-352A:evaluation:llama500:20528:21542 | 591 | 0 | 0 | 1367 |
| AA23-352A:evaluation:llama500:21415:22258 | 500 | 0 | 0 | 1274 |
| AA23-352A:evaluation:llama500:22179:22895 | 431 | 0 | 0 | 1201 |
| AA23-352A:evaluation:llama500:22768:24022 | 558 | 1 | 1 | 1482 |
| AA23-352A:evaluation:llama500:23163:24531 | 500 | 1 | 1 | 1428 |
| AA23-075A:evaluation:llama500:2065:4310 | 477 | 5 | 1 | 1581 |
| AA23-075A:evaluation:llama500:4080:6201 | 498 | 24 | 8 | 3016 |
| AA23-075A:evaluation:llama500:5977:8086 | 496 | 21 | 7 | 2831 |
| AA23-075A:evaluation:llama500:7876:9861 | 501 | 21 | 0 | 2088 |
| AA23-075A:evaluation:llama500:9606:11457 | 496 | 4 | 8 | 2724 |
| AA23-075A:evaluation:llama500:11240:12930 | 504 | 2 | 0 | 1532 |
| AA23-075A:evaluation:llama500:12712:14097 | 492 | 0 | 0 | 1380 |
| AA23-075A:evaluation:llama500:13954:15486 | 506 | 0 | 0 | 1397 |
| AA23-075A:evaluation:llama500:15300:16716 | 491 | 0 | 0 | 1382 |
| AA23-075A:evaluation:llama500:16524:18208 | 499 | 0 | 0 | 1545 |
| AA23-075A:evaluation:llama500:17999:19572 | 485 | 2 | 0 | 1713 |
| AA23-075A:evaluation:llama500:19385:20727 | 517 | 3 | 0 | 1461 |
| AA23-075A:evaluation:llama500:20640:22313 | 501 | 9 | 0 | 1750 |
| AA23-075A:evaluation:llama500:22086:24117 | 501 | 16 | 0 | 1976 |
| AA23-075A:evaluation:llama500:23852:25424 | 418 | 15 | 0 | 1771 |

Next: operator-run bounded extraction, followed by candidate source review before any isolated evaluation import or index refresh; no tuning from held-out outputs.
