import os
import sys
import fnmatch
import re
import pprint

## get all files from folder recursively
def getFiles(folder):
  if not folder[-1] == '/':
    folder += '/' 

  matches = []
  for root, dirnames, filenames in os.walk(folder):
      for filename in fnmatch.filter(filenames, '*'):
          matches.append(os.path.join(root, filename))
  return matches

## count words inside of a content
def countWordsInContent(content, words):
  result = {}
  for word in words:
    count = sum(1 for match in re.finditer(r'\b' + word + r'\b', content))
    result[word] = count
  return result

## display a result
def displayResult(result):
  for filename in result:
    print '[*] filename: ' + filename
    for word in result[filename]:
      print '    -> "' + word + '": ' + str(result[filename][word]) 

## script starts in this function
def main():
  if len(sys.argv) < 3:
    print 'error: please specify parameters'
    print 'usage: python wordsearch.py <folder> <word1> [<word2> ... <wordN>]'
    quit()

  folder = sys.argv[1]
  searchWords = sys.argv[2:]

  if not os.path.isdir(folder):
    print 'error: folder not found'
    quit()

  files = getFiles(folder)

  result = {}
  for file in files:
    with open(file) as f:
      content = f.read()
      result[file] = countWordsInContent(content, searchWords)

  displayResult(result)


if __name__ == '__main__':
  main()