from biocypher import BioCypher, FileDownload
# from template_package.adapters.example_adapter import (
#     ExampleAdapter,
#     ExampleAdapterNodeType,
#     ExampleAdapterEdgeType,
#     ExampleAdapterProteinField,
#     ExampleAdapterDiseaseField,
# )
from template_package.adapters.adapter_syntetic_data import (
    Adapter,
    AdapterNodeType,
    AdapterProteinField,
    AdapterEdgeType
)

# Instantiate the BioCypher interface
# You can use `config/biocypher_config.yaml` to configure the framework or
# supply settings via parameters below
bc = BioCypher()

# Download and cache resources (change the directory in the options if needed)
urls = "https://file-examples.com/wp-content/storage/2017/02/file_example_CSV_5000.csv"
resource = FileDownload(
    name="Example resource",  # Name of the resource
    url_s=urls,  # URL to the resource(s)
    lifetime=7,  # seven days cache lifetime
)
paths = bc.download(resource)  # Downloads to '.cache' by default
print(paths)
# You can use the list of paths returned to read the resource into your adapter

# Choose node types to include in the knowledge graph.
# These are defined in the adapter (`adapter.py`).
node_types = [
    # ExampleAdapterNodeType.PROTEIN,
    # ExampleAdapterNodeType.DISEASE,
    AdapterNodeType.PROTEIN
]

# Choose protein adapter fields to include in the knowledge graph.
# These are defined in the adapter (`adapter.py`).
node_fields = [
    # Proteins
    # ExampleAdapterProteinField.ID,
    # ExampleAdapterProteinField.SEQUENCE,
    # ExampleAdapterProteinField.DESCRIPTION,
    # ExampleAdapterProteinField.TAXON,
    # # Diseases
    # ExampleAdapterDiseaseField.ID,
    # ExampleAdapterDiseaseField.NAME,
    # ExampleAdapterDiseaseField.DESCRIPTION,

    AdapterProteinField.ID,
    AdapterProteinField.PREFERRED_ID,
    AdapterProteinField.GENESYMBOL,
    AdapterProteinField.NCBI_TAX_ID
]

edge_types = [
    # ExampleAdapterEdgeType.PROTEIN_PROTEIN_INTERACTION,
    # ExampleAdapterEdgeType.PROTEIN_DISEASE_ASSOCIATION,
    AdapterEdgeType.PROTEIN_PROTEIN_INTERACTION,
    AdapterEdgeType.BINDING,
    AdapterEdgeType.ACTIVATION,
    AdapterEdgeType.PHOSPHORYLATION,
    AdapterEdgeType.UBIQUITINATION,
    AdapterEdgeType.INHIBITION
]

# Create a protein adapter instance
# adapter = ExampleAdapter(
#     node_types=node_types,
#     node_fields=node_fields,
#     edge_types=edge_types,
#     # we can leave edge fields empty, defaulting to all fields in the adapter
# )
adapter = Adapter(
    node_types=node_types,
    node_fields=node_fields,
    edge_types=edge_types,
)


# Create a knowledge graph from the adapter
bc.write_nodes(adapter.get_nodes())
bc.write_edges(adapter.get_edges())

# Write admin import statement
bc.write_import_call()

# Print summary
bc.summary()
