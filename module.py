import networx as nx
import pandas as pd

def create_graph(df_nodes, df_edges):
    G = nx.Graph()

    #Adiciona os nós
    for i, r in df_nodes.iterrows():
        G.add_node(r["Id"])

    #Faz uma tupla com as arestas
    edges_tuple = [(r["Source"], r["Target"]) for i, r in df_edges.iterrows()]

    #Adiciona as arestas no grafo
    G.add_edges_from(edges_tuple)

    return G