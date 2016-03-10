import os

from collections import defaultdict

import string


def word_ngrams(input, n):
    output = []

    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output


# [' '.join(x) for x in word_ngrams('nightmare', 3)]


def normalize_text(s):
    exclude = set(string.punctuation)

    s = ''.join(ch for ch in s if ch not in exclude).lower()

    return s


def match_query(word_dict):
    user_query = raw_input("Search: ")

    normalized_query = normalize_text(user_query)

    query_list = normalized_query.split()

    full_query_list = []

    for word in query_list:
        full_query_list.append(word)
        full_query_list.extend(word_ngrams(word, 3))

    print "n gram query_list", full_query_list

    file_and_counts = []

    for word in full_query_list:
        # query_n_gram_list = word_ngrams(word, 3)
        file_and_counts.extend(word_dict[word].items())

    print "file_and_counts", file_and_counts

    total_counts = defaultdict(int)

    for f in file_and_counts:
        total_counts[f[0]] += f[1]

    total_counts = total_counts.items()

    total_counts_list = []

    for t in total_counts:
        total_counts_list.append(list(t))

    total_counts_list.sort(key=lambda x: x[1], reverse=True)

    print "total_counts_list", total_counts_list

    for t in total_counts_list:
        print t[0] + "\n"

    more = raw_input("Do you want to search something else? (Y/N): ")

    if more.upper() == 'Y':
        match_query(word_dict)
    else:
        return


def walk_through_directory(file_path):

    dir_info = [d for d in os.walk(file_path)]

    file_names = dir_info[0][2]

    word_dict = defaultdict(lambda: defaultdict(int))

    for f in file_names:
        with open(os.path.join(file_path, f)) as text_file:
            raw_text = text_file.read()
            text = normalize_text(raw_text)

            text_length = len(text)

            for word in text.split():

                n_gram_list = word_ngrams(word, 3)

                for n in n_gram_list:
                    word_dict[n][f] += (1.0/text_length)

                word_dict[word][f] += 2.0

    # print word_dict
    match_query(word_dict)


walk_through_directory('/Users/justineturnbull/Desktop/bloomberg_search_engine/text_files')
