import numpy as np
import string
import random
import sys
sys.path.append("..")
from ex24.ex24_fast_url_search import TSTreeRouter
from ex24.ex24_fast_url_search import DLListRouter
from ex24.ex24_fast_url_search import BSTreeRouter
from ex24.ex24_fast_url_search import pyDictRouter
from ex24.ex24_fast_url_search import DictRouter


def random_url_constuctor():
    url_len = np.random.randint(1, 5)
    word_list = []
    for i in range(url_len):
        word_len = np.random.randint(1, 8)
        letters = string.ascii_lowercase
        word = "".join([random.choice(letters) for i in range(word_len)])
        word_list.append(word)
       # print(word)
    url = "/".join(word_list)
    url = "/"+url+"/"
    return url


def test_url_keys_setup(urls):
#    urls = TSTree()
    urls.add("/apple/", "Apple")
    urls.add("/grape/", "Grape")
    urls.add("/kiwi/", "Kiwi")

    urls.add("/k/", "K")
    urls.add("/lm/", "Lm")

    urls.add("/kumquat/", "Kumquat")
    urls.add("/pineapple/", "Pineapple")
    urls.add("/kiwikiwi/", "KiwiKiwi")
    urls.add("/do/", "/do/")
    urls.add("/do/this/stuff/", "/do/this/stuff/")
    urls.add("/do/this/stuff/now/in/this/way/",
             "/do/this/stuff/now/in/this/way/")

#    assert urls.get("/apple/") == "Apple"
#    assert urls.get("/grape/") == "Grape"
#    assert urls.get("/kiwi/") == "Kiwi"
#
#    assert urls.get("/k/") == "K"
#
#    assert urls.get("/") == None
#
#    return urls
#
def test_find_all(urls):
   # urls = test_url_keys_setup()
    results = sorted([n.value for n in urls.find_all("/k")])
    print(results)
    assert results == sorted(["K", "Kiwi", "KiwiKiwi", "Kumquat"])
    results = [n.value for n in urls.find_all("/")]
    print(results)

def test_find_shortest(urls):
    #urls = test_url_keys_setup()

    assert urls.find_shortest("/k").value == "K"
    assert urls.find_shortest("/ki").value == "Kiwi"
    assert urls.find_shortest("/kiwiki").value == "KiwiKiwi"
    assert urls.find_shortest("/a").value == "Apple"
    print(urls.find_shortest("/").value)
    #assert urls.find_shortest("/").value == "K"


def test_find_longest(urls):
    #urls = test_url_keys_setup()
    # assert urls.find_longest("/").value == "Pineapple"
    assert urls.find_longest("/do/").value == "/do/this/stuff/now/in/this/way/"
    assert urls.find_longest("/pi").value == "Pineapple"

def test_find_part(urls):
    #urls = test_url_keys_setup()
    assert urls.find_part("/kaler").value == "K"
#    assert urls.find_part("/kaler").value == "Kiwi"
    print("test find_part", urls.find_part("/application").value)
    assert urls.find_part("/application").value == "Apple"
  #  print(urls.find_part("/papal").value)
    assert urls.find_part("/papal").value == "Pineapple"
    assert urls.find_part("/apple/120/1000/").value == "Apple"
    assert urls.find_part("/kiwi/user/zedshaw/has/stuff").value == "Kiwi"
    assert urls.find_part("/l").value == "Lm"
    assert urls.find_part("XTREEME") is None
    return None

def test_find_best_match(urls):
   # urls.add("/do/", "/do/")
    assert urls.find_best_match("/do/this/stuff/").value == "/do/this/stuff/"
    assert urls.find_best_match("/do/this/stuff/tomorrow/").value == "/do/this/stuff/"
    #urls.add("/do/", "/do/")
    return None

def test_find_exact_match(urls):
    #print(urls.find_exact_match("/do/this/stuff/").value)
    assert urls.find_exact_match("/do/this/stuff/").value == "/do/this/stuff/"
    assert urls.find_exact_match("/do/this/stuff/tomorrow/") is None
    return None

def test_all(urls):
   # urls = TSTreeRouter()
    test_url_keys_setup(urls)
    test_find_all(urls)
    test_find_shortest(urls)
    test_find_longest(urls)
    test_find_part(urls)
    test_find_best_match(urls)
    test_find_exact_match(urls)
    print("Test finished.")
    return None

def TSTree_test():
    urls = TSTreeRouter()
    test_all(urls)
    random_urls = TSTreeRouter()
    for i in range(20):
        k = random_url_constuctor()
        random_urls.add(k, k)
    print(random_urls.find_part("/a"))
    print(random_urls.find_all("/a"))
    print(random_urls.find_part("/%/"))

def DLList_test():
    urls = DLListRouter()
    test_all(urls)

def BSTree_test():
    urls = BSTreeRouter()
    test_all(urls)

def Dict_test():

#def test_find_all():
#    pass
#def test_find_shortest():
#    pass
#def test_find_longest():
    pass

def pyDict_test():
    urls = pyDictRouter()
    test_all(urls)

def Dict_test():
    urls = DictRouter()
    test_all(urls)
