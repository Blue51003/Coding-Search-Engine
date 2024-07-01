import os
import re

qData_folder = "Leetcode-Questions-Scrapper/Qdata"

target_str = "Example 1:"

all_lines = []

for i in range(1,2008):
    file_path = os.path.join(qData_folder, "{}/{}.txt".format(i,i))

    doc = ""
    with open(file_path, "r", encoding='utf-8', errors="ignore") as f:
        lines = f.readlines()
    
    for line in lines:
        if target_str in line:
            break
        else:
            doc+=line

    all_lines.append(doc)

def preprocess(text):
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    terms = [term.lower() for term in text.strip().split()]

    return terms

vocab = {}
documents = []

for (index, line) in enumerate(all_lines):
    tokens = preprocess(line)
    documents.append(tokens)

    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token]=1
        else:
            vocab[token]+=1

vocab = dict(sorted(vocab.items(), key=lambda item : item[1], reverse = True))

print("No of documents : ", len(documents))
print("Size of vocab :", len(vocab))
print("sample document :", documents[100])

with open("TF-IDF/vocab.txt", "w", encoding = 'utf-8', errors = "ignore") as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

with open("TF-IDF/idf-values.txt", "w", encoding = 'utf-8', errors = "ignore") as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])

with open("TF-IDF/documents.txt", "w", encoding = 'utf-8', errors = "ignore") as f:
    for doc in documents:
        f.write("%s\n" % doc)

inverted_index = {}

for(index, doc) in enumerate(documents, start =1):
    for token in doc:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)

with open("TF-IDF/inverted_index.txt" , 'w', encoding='utf-8', errors="ignore") as f:
    for key in inverted_index.keys():
        f.write("%s\n"%key)

        doc_indexes = ' '.join([str(term) for term in inverted_index[key]])
        f.write("%s\n" % doc_indexes)