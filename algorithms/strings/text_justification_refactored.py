"""
Given an array of words and a width maxWidth, format the text such that each line
has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line do not divide evenly between words, the empty slots
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is
inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
"""


def text_justification_refactored(words, max_width):
    '''
    :type words: list
    :type max_width: int
    :rtype: list
    '''
    ret = []  # return value
    index = 0  # the index of current word in words
    
    while index < len(words):
        # Get all words fitting on a row.  
        row_words, row_len = fit_max_words_to_row(index, max_width, words)
        index += len(row_words)

        # Justify all words with spaces
        row = justify_row(index, words, row_words, max_width, row_len)
        ret.append(row)
    return ret

def fit_max_words_to_row(index, max_width, words):
    row_len = -1  # current length of strs in a row
    row_words = []  # current words in a row

    while row_len <= max_width and index < len(words):
        if len(words[index]) > max_width:
            raise ValueError("there exists word whose length is larger than max_width")

        tmp = row_len
        row_words.append(words[index])
        tmp += len(words[index]) + 1

        if tmp > max_width:
            row_words.pop()
            break

        row_len = tmp
        index += 1
    return row_words, row_len


def justify_row(index, words, row_words, max_width, row_len):
    # if the row is the last
    if index == len(words):
        return justify_last_row(row_words, max_width)

    # not the last row and more than one word
    elif len(row_words) != 1:
        return justify_multiple_word_row(max_width, row_len, row_words)

    # row with only one word
    else:
        return row_words[0] + ' ' * (max_width - len(row_words[0]))

def justify_last_row(row_words, max_width):
    row = ""

    for word in row_words:
            row += (word + ' ')
            
    row = row[:-1]
    row += ' ' * (max_width - len(row))
    return row

def justify_multiple_word_row(max_width, row_len, row_words):
    row = ""

    space_num = max_width - row_len
    space_num_of_each_interval = space_num // (len(row_words) - 1)
    space_num_rest = space_num - space_num_of_each_interval * (len(row_words) - 1)

    for j in range(len(row_words)):
        row += row_words[j]

        if j != len(row_words) - 1:
            row += ' ' * (1 + space_num_of_each_interval)

        if space_num_rest > 0:
            row += ' '
            space_num_rest -= 1

    return row