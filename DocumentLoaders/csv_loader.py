from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='DocumentLoaders/employees.csv')

docs = loader.load()

print(len(docs))
print(docs[1])