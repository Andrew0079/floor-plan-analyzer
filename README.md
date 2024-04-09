### Apartment and Chair Analyzer: Automated Floor Plan Furniture Analysis (Old School)

The Apartment and Chair Analyzer is a command-line tool designed for Apartment And Chair Delivery Limited. It automates chair counting and categorization from floor plans, improving accuracy and efficiency in furniture planning and delivery.

### Info

Apartment And Chair Delivery Limited, known for residential construction and furnishing, faces manual chair counting issues due to outdated processes and legacy systems. This tool automates chair type extraction from floor plans, addressing inaccuracies and enhancing customer satisfaction.

### Solution

The Apartment and Chair Analyzer utilizes the Breadth-First Search (BFS) algorithm to systematically identify chair positions in floor plans, ensuring precise enumeration of the following chari types:

W: wooden chair
P: plastic chair
S: sofa chair
C: china chair

This approach generates detailed chair counts tailored to apartment layouts, offering seamless integration with legacy systems and meeting the company's need for comprehensive and error-free chair placement analysis.

### Usage

python3 main.py A default path is provided to use if a file a path is not specified
Or
python3 main.py /path/to/room.txt

### Example 

room.txt (default floor plan)
+-----------+------------------------------------+
|           |                                    |
| (closet)  |                                    |
|         P |                            S       |
|         P |         (sleeping room)            |
|         P |                                    |
|           |                                    |
+-----------+    W                               |
|           |                                    |
|        W  |                                    |
|           |                                    |
|           +--------------+---------------------+
|                          |                     |
|                          |                W W  |
|                          |    (office)         |
|                          |                     |
+--------------+           |                     |
|              |           |                     |
| (toilet)     |           |             P       |
|   C          |           |                     |
|              |           |                     |
+--------------+           +---------------------+
|              |           |                     |
|              |           |                     |
|              |           |                     |
| (bathroom)   |           |      (kitchen)      |
|              |           |                     |
|              |           |      W   W          |
|              |           |      W   W          |
|       P      +           |                     |
|             /            +---------------------+
|            /                                   |
|           /                                    |
|          /                          W    W   W |
+---------+                                      |
|                                                |
| S                                   W    W   W |
|                (living room)                   |
| S                                              |
|                                                |
|                                                |
|                                                |
|                                                |
+--------------------------+---------------------+
                           |                     |
                           |                  P  |
                           |  (balcony)          |
                           |                 P   |
                           |                     |
                           +---------------------+

Call python3 main.py or python3 main.py /path/to/file

Output:

total:
W: 14, P: 7, S: 3, C: 1
balcony:
W: 0, P: 2, S: 0, C: 0
bathroom:
W: 0, P: 1, S: 0, C: 0
closet:
W: 0, P: 3, S: 0, C: 0
kitchen:
W: 4, P: 0, S: 0, C: 0
living room:
W: 7, P: 0, S: 2, C: 0
office:
W: 2, P: 1, S: 0, C: 0
sleeping room:
W: 1, P: 0, S: 1, C: 0
toilet:
W: 0, P: 0, S: 0, C: 1

### SUM
The Apartment and Chair Analyzer efficiently counts and categorizes chair types from floor plans for Apartment And Chair Delivery Limited, enhancing operational efficiency and customer satisfaction.