from neo4j import GraphDatabase


# -------------------------------
# 1. Connect to Neo4j
# -------------------------------


driver = GraphDatabase.driver(
    "neo4j://127.0.0.1:7687",
    auth=("neo4j", "neo4j2003")   # change password
    # auth=("neo4j", "demo1234")   # change password
)


# -------------------------------
# 2. Dummy Research Data
# -------------------------------


# papers = [


#     {
#         "title": "Deep Learning for Healthcare",
#         "authors": ["Andrew Ng"],
#         "methods": ["Neural Networks", "CNN"],
#         "domain": "Healthcare"
#     },


#     {
#         "title": "Transformers in NLP",
#         "authors": ["Ashish Vaswani"],
#         "methods": ["Transformer", "Attention"],
#         "domain": "Natural Language Processing"
#     },


#     {
#         "title": "Computer Vision using CNN",
#         "authors": ["Fei Fei Li"],
#         "methods": ["CNN", "Image Classification"],
#         "domain": "Computer Vision"
#     }


# ]


# # -------------------------------
# # 3. Create Graph Function
# # -------------------------------


# def create_graph(tx, paper):


#     title = paper["title"]
#     authors = paper["authors"]
#     methods = paper["methods"]
#     domain = paper["domain"]


#     # create paper node
#     tx.run(
#         """
#         MERGE (p:Paper {title:$title})
#         """,
#         title=title
#     )


#     # create author relationship
#     for author in authors:


#         tx.run(
#             """
#             MERGE (a:Author {name:$author})
#             MERGE (p:Paper {title:$title})
#             MERGE (a)-[:WROTE]->(p)
#             """,
#             author=author,
#             title=title
#         )


#     # create method relationship
#     for method in methods:


#         tx.run(
#             """
#             MERGE (m:Method {name:$method})
#             MERGE (p:Paper {title:$title})
#             MERGE (p)-[:USES]->(m)
#             """,
#             method=method,
#             title=title
#         )


#     # create domain relationship


#     tx.run(
#         """
#         MERGE (d:Domain {name:$domain})
#         MERGE (p:Paper {title:$title})
#         MERGE (p)-[:BELONGS_TO]->(d)
#         """,
#         domain=domain,
#         title=title
#     )


# # -------------------------------
# # 4. Insert Data into Neo4j
# # -------------------------------


# with driver.session() as session:


#     for paper in papers:
#         session.execute_write(create_graph, paper)


# print("Knowledge Graph Created!")


# # -------------------------------
# # 5. Query Graph
# # -------------------------------


with driver.session() as session:


    result = session.run(
        """

        MATCH (p:Paper)-[:USES]->(m:Method)
        RETURN p,m
        """
    )


    for record in result:
        print(record)


# Show All Nodes in the Graph
# MATCH (n)
# RETURN n


# Show All Papers
# MATCH (p:Paper)
# RETURN p


# Show Authors and Their Papers
# MATCH (a:Author)-[:WROTE]->(p:Paper)
# RETURN a,p


# Show Paper and Method Used
# MATCH (p:Paper)-[:USES]->(m:Method)
# RETURN p,m


# Show Paper and Method Used
# MATCH (p:Paper)-[:USES]->(m:Method)
# RETURN p,m


# Find Papers by a Specific Author
# MATCH (a:Author {name:"Andrew Ng"})-[:WROTE]->(p:Paper)
#         RETURN p
        
# MATCH (a:Author)-[:WROTE]->(p:Paper)-[:USES]->(m:Method)
# RETURN a.name AS author, p.title AS paper, m.name AS method        

