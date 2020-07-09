# Be sure to set ADDRESS, USERNAME, PASSWORD, PORT, and DB_NAME.
from pymongo import MongoClient
import pickle


data = pickle.load(open("CommunityFitNet_updated.pickle", "rb"))
client = MongoClient('mongodb://%s:%s@ADDRESS' % ('USERNAME', 'PASSWORD'), port=PORT)
db = client["networks"]

for _id, name in enumerate(data["network_name"]):
    network_name = str(data["network_name"][_id])
    title = str(data["title"][_id])
    description = str(data["description"][_id])
    network_domain = str(data["networkDomain"][_id])
    sub_domain = str(data["subDomain"][_id])
    citation = str(data["citation"][_id])
    sourceUrl = str(data["sourceUrl"][_id])
    hostedBy = str(data["hostedBy"][_id])
    graphProperties = str(data["graphProperties"][_id]).split(", ")
    
    
    nodeType = str(data["nodeType"][_id]).split(", ")
    edgeType = str(data["edgeType"][_id]).split(", ")

    nodes = data["nodes_id"][_id].tolist()
    edges = data["edges_id"][_id].tolist()
    
    number_nodes = int(data["number_nodes"][_id])
    number_edges = int(data["number_edges"][_id])
    avg_degree = float(data["ave_degree"][_id])
    
    db["DB_NAME"].insert_one({
        "network_name": network_name, 
        "title": title,
        "description": description,
        "network_domain": network_domain,
        "sub_domain": sub_domain,
        "citation": citation,
        "source_url": sourceUrl,
        "hosted_by": hostedBy,
        "graph_properties": graphProperties,
        "node_type": nodeType,
        "edge_type": edgeType,
        "nodes": nodes,
        "edges": edges,
        "number_nodes": number_nodes,
        "number_edges": number_edges,
        "avg_degree": avg_degree
    })
