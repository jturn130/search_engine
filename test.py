
# def ngrams(input, n):
#     input = input.split(' ')
#     output = []

#     for i in range(len(input)-n+1):
#         output.append(input[i:i+n])
#     print output

# # [' '.join(x) for x in ngrams('I am your worst nightmare! This is not about revenge. This is about justice. They were just sucked into space. Some days you get the bear, and some days the bear gets you. Maybe if we felt any human loss as keenly as we feel one of those close to us, human history would be far less bloody. You enjoyed that.', 3)]

# [' '.join(x) for x in ngrams('nightmare', 3)]


def word_ngrams(input, n):
    # input = input.split()
    output = []

    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output


test = word_ngrams('nightmare', 3)
