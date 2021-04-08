import re,string,collections

def find_most_common_words(words):
    cleaned_words=[]
    stopwords=get_stop_words()
    for word in words:
        if word not in stopwords:
            cleaned_words.extend(cleaned_line.split())
    return collections.Counter(cleaned_words).most_common(5)

def get_statistics(data):
    lines=get_lines(data)
    words=get_words(lines)
    unique_words=list(set(words))
    most_common_words=find_most_common_words(words)

def find_most_common_words(words):
    with open('stopwords.txt',r) as fp:
        words=fp.readlines()
        stopwords=[word.strip('\n') for word in words]
        return stopwords


def get_words(lines):
    words=[]
    for line in lines:
        cleaned_line=remove_punctuation(line)
        words.extend(cleaned_line.split())
    return words

def remove_punctuation(line):
    st=str.maketrans("","",string.punctuation)
    return line.translate(st)

def get_lines(data):
    lines=[]
    for para in data:
        para_lines=re.split(r'[.!?]+',para)
        for line in para_lines:
            if line:
                lines.append(para_lines)
    return lines

if __name__=='__main__': 
    data=['fir st line','sec ound? line','third line','so this! is end']
    print(get_statistics(data))

