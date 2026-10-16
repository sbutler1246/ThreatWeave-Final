# Shared evaluation text-index run

Status: ready

CISA source scopes: 101; ATT&CK references: 190; retrieval chunks: 510.

Source-only shared evaluation index. Retrieval smoke checks are not answer-quality measurements.
Inherited headings retain separate exact document spans; child chunks preserve parent IDs.

Index fingerprint: `0fe7f0c80769a67a158d505df0d72c77e12273c02fa8e6f3dd56da436685de73`

## Retrieval smoke question

According to CISA, what information does Raccoon Stealer steal? Explain the supplied ATT&CK mitigations for its web session cookie technique, citing observations and references separately.

- Rank 1: attack / attack:17.1:relationship--1a5bf948-33fd-4025-aadd-117e99512e6a / 268:510; cosine distance 0.4120; parent `attack:17.1:relationship--1a5bf948-33fd-4025-aadd-117e99512e6a:description`.
- Rank 2: attack / attack:17.1:relationship--248a0d72-d9cd-43d3-985f-a33a49a79e8b / 285:810; cosine distance 0.4361; parent `attack:17.1:relationship--248a0d72-d9cd-43d3-985f-a33a49a79e8b:description`.
- Rank 3: attack / attack:17.1:relationship--44c91929-3473-443c-91be-5afa81582dfa / 289:539; cosine distance 0.4449; parent `attack:17.1:relationship--44c91929-3473-443c-91be-5afa81582dfa:description`.
- Rank 4: attack / attack:17.1:relationship--7a1cf82e-68e5-49ca-89ae-e492cd85dab4 / 290:733; cosine distance 0.4572; parent `attack:17.1:relationship--7a1cf82e-68e5-49ca-89ae-e492cd85dab4:description`.
- Rank 5: attack / attack:17.1:relationship--f780f9d8-1baa-41b7-b7a1-acba717df0ab / 276:605; cosine distance 0.4627; parent `attack:17.1:relationship--f780f9d8-1baa-41b7-b7a1-acba717df0ab:description`.

## Retrieval smoke question

According to CISA, how do Rhysida actors use valid accounts (T1078) for access? Explain the supplied ATT&CK mitigation guidance and cite the sources separately.

- Rank 1: attack / attack:17.1:relationship--555abf76-531f-4d35-9783-ed7c2a3f213b / 276:374; cosine distance 0.4246; parent `attack:17.1:relationship--555abf76-531f-4d35-9783-ed7c2a3f213b:description`.
- Rank 2: cisa / AA23-319A / 19026:19970; cosine distance 0.4624; parent `AA23-319A:development:llama500:19026:21144`.
- Rank 3: attack / attack:17.1:relationship--f2d01f19-b4e7-417a-a936-11af9386b867 / 273:451; cosine distance 0.4696; parent `attack:17.1:relationship--f2d01f19-b4e7-417a-a936-11af9386b867:description`.
- Rank 4: attack / attack:17.1:relationship--c8acdf40-8237-487f-8255-91afa327705d / 283:479; cosine distance 0.4704; parent `attack:17.1:relationship--c8acdf40-8237-487f-8255-91afa327705d:description`.
- Rank 5: attack / attack:17.1:relationship--85b3d881-a9d2-45ff-a980-95d0bd9a3dd1 / 260:401; cosine distance 0.4808; parent `attack:17.1:relationship--85b3d881-a9d2-45ff-a980-95d0bd9a3dd1:description`.

## Retrieval smoke question

According to CISA, how do ALPHV Blackcat affiliates use AnyDesk and Mega sync before data exfiltration?

- Rank 1: cisa / AA23-353A / 5039:5986; cosine distance 0.4131; parent `AA23-353A:development:llama500:5039:6758`.
- Rank 2: cisa / AA23-353A / 3836:4785; cosine distance 0.4902; parent `AA23-353A:development:llama500:3078:5323`.
- Rank 3: cisa / AA23-353A / 3078:4023; cosine distance 0.4957; parent `AA23-353A:development:llama500:3078:5323`.
- Rank 4: cisa / AA23-353A / 9068:9988; cosine distance 0.5311; parent `AA23-353A:development:llama500:9068:11166`.
- Rank 5: cisa / AA24-131A / 12233:13129; cosine distance 0.5693; parent `AA24-131A:evaluation:llama500:10786:13129`.

