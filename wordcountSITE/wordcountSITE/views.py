from django.http import HttpResponse
from django.shortcuts import render
import operator


def homePage(request):
    return render(request, 'home.html', )


def count(request):
    fulltextSent = request.GET['fulltext']
    wordList = fulltextSent.split()
    wordDictionary = {}

    for word1 in wordList:
        word1= word1.upper()
        if word1 in wordDictionary:
            wordDictionary[word1.upper()] += 1
        #increase count

        else:
        # add to the dictionary, because it is a new word
            wordDictionary[word1.upper()] = 1


    sortedwordDict = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html' , {'fulltext': fulltextSent , 'count1': len(wordList) , 'sortedWordDict': sortedwordDict})


def about(request):
    return render(request, 'about.html')