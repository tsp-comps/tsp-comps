import networkx as nx
import pandas as pd

# take a .tsv file from the STRING database and return a clean version with just nodes and edge weights
def clean_protein_data(filename):
    protein_data = pd.read_csv(filename, sep='\t')
    columns_to_delete = ['node1_string_id','node2_string_id','neighborhood_on_chromosome',
                         'gene_fusion','phylogenetic_cooccurrence','homology',
                         'coexpression','experimentally_determined_interaction',
                         'database_annotated','automated_textmining']
    protein_data.drop(columns=columns_to_delete, inplace=True)
    protein_data['combined_score'] = 1 - protein_data['combined_score']
    return protein_data

# turn the processed protein data from clean_protein_data into an nx graph
def graph_protein_data(raw_data):
    G = nx.Graph()
    for index, row in raw_data.iterrows():
        G.add_edge(row['#node1'], row['node2'], weight=row['combined_score'])
    return G

def main():
    filename = 'datasets/proteins/YALD2-n11e45.tsv'
    raw_data = clean_protein_data(filename)
    print(raw_data)
    g = graph_protein_data(raw_data)
    print(g)

if __name__ == "__main__":
    main()