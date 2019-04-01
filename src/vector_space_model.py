from math import pow, sqrt


def count_words(dict):
    nb = 0
    for value in dict:
        nb = nb + value[1]
    return nb


def create_vector(dict1: dict, dict2: dict):
    for value in dict2:
        if value not in dict1:
            dict1[value] = 0
    return dict1


def vector_multiplication(dict1: dict, query: dict):
    result = 0
    for k, v in dict1.items():
        result = result + v * query[k]
    return result


def norm_vector(vector: dict):
    result = 0
    for value in vector:
        result = result + pow(vector[value], 2)
    result = sqrt(result)
    return result


def cosine_calculation(dict1, dict2, query, query_name, doc_name1, doc_name2):
    dict1 = create_vector(dict1, dict2)
    dict2 = create_vector(dict2, dict1)
    query = create_vector(query, dict2)
    vector_multiplication(dict1, query)
    result_doc1 = vector_multiplication(dict1, query) / (norm_vector(dict1) * norm_vector(query))
    result_doc2 = vector_multiplication(dict2, query) / (norm_vector(dict2) * norm_vector(query))
    print("Result for the query \"", query_name, "\":", sep='')
    print(result_doc1, "-->", doc_name1)
    print(result_doc2, "-->", doc_name2)
