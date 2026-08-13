from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('DocumentLoaders/wild_animals.pdf')

docs = loader.load()

print(len(docs))

print(docs[1].page_content)
print(docs[1].metadata)