import streamlit as st
from pyvis.network import Network
import networkx as nx
import streamlit.components.v1 as components

# Function to create a network graph
def create_network():
    # Create a graph object
    nx_graph = nx.Graph()

    # Add nodes
    nx_graph.add_node("Node 1")
    nx_graph.add_node("Node 2")
    nx_graph.add_node("Node 3")

    # Add edges
    nx_graph.add_edge("Node 1", "Node 2")
    nx_graph.add_edge("Node 2", "Node 3")
    nx_graph.add_edge("Node 3", "Node 1")

    # Create a Pyvis network from the NetworkX graph
    nt = Network("500px", "500px")
    nt.from_nx(nx_graph)
    return nt

# Streamlit app
def main():
    st.title("Network Visualization Example")

    # Create the network graph
    nt = create_network()

    # Generate an HTML file of the graph
    nt.show("graph.html")

    # Use Streamlit's components.html to display the graph
    HtmlFile = open("graph.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, width=500, height=500)

if __name__ == "__main__":
    main()
