This project demonstrates the implementation of a simple blockchain using Python. The blockchain consists of multiple blocks linked together using cryptographic hash values generated with the SHA-256 algorithm.
The project helps in understanding the core concepts of blockchain such as:
Block creation
Cryptographic hashing
Genesis block
Block linking
Blockchain validation
Immutability
🧱 Features
Creation of blocks with:
Data
Timestamp
Previous Hash
Current Hash
SHA-256 hashing implementation
Genesis Block creation
Blockchain validation
Demonstration of immutability
🛠️ Technologies Used
Python 3.x
hashlib library
datetime library
Visual Studio Code


#output
===== BLOCKCHAIN DETAILS =====

Block 0
Timestamp      : 2026-05-07 18:43:29.535741
Data           : Genesis Block
Current Hash   : 853c727c902b456091a6134ba1f8327936570395a450ff692eceb1a87a558835
Previous Hash  : 0
------------------------------------------------------------
Block 1
Timestamp      : 2026-05-07 18:43:29.536250
Data           : Transaction 1
Current Hash   : 51a5f7b056f130da9139a359c190d0150053562549c4ea9bb797d474f04d3c28
Previous Hash  : 853c727c902b456091a6134ba1f8327936570395a450ff692eceb1a87a558835
------------------------------------------------------------
Block 2
Timestamp      : 2026-05-07 18:43:29.536269
Data           : Transaction 2
Current Hash   : 27dcc62ade577175a5526e9f8c9987e33e5b8a0ac59fc1bbb6edc4de62b96934
Previous Hash  : 51a5f7b056f130da9139a359c190d0150053562549c4ea9bb797d474f04d3c28
------------------------------------------------------------
Block 3
Timestamp      : 2026-05-07 18:43:29.536276
Data           : Transaction 3
Current Hash   : efb3005b882b4128286f1a0e2d6bddc1e8efcf256e8f4653a7bd92b32791732f
Previous Hash  : 27dcc62ade577175a5526e9f8c9987e33e5b8a0ac59fc1bbb6edc4de62b96934
------------------------------------------------------------
Block 4
Timestamp      : 2026-05-07 18:43:29.536281
Data           : Transaction 4
Current Hash   : 2b998b70ff6bd8c22a67f05ac6cc7d90493304c79e2ccf19398f506980cb0e59
Previous Hash  : efb3005b882b4128286f1a0e2d6bddc1e8efcf256e8f4653a7bd92b32791732f
------------------------------------------------------------
