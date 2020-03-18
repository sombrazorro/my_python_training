from ex23.ex23_ternary_search_tree import TSTree


def test_TSTree_get_set():
    urls = TSTree()
    urls.set("/apple/", "Apple")
    urls.set("/grape/", "Grape")
    urls.set("/kiwi/", "Kiwi")

    urls.set("/k/","K")
    urls.set("/lm/", "lm")

    urls.set("/kumquat/", "Kumquat")
    urls.set("/pineapple/", "Pineapple")

    assert urls.get("/apple/") == "Apple"
    assert urls.get("/grape/") == "Grape"
    assert urls.get("/kiwi/") == "Kiwi"

    assert urls.get("/k/") == "K"

    assert urls.get("/") == None

    return urls

def test_TSTree_find_all():
    urls = test_TSTree_get_set()
    results = [n.value for n in urls.find_all("/k")]
    print(results)
    assert results == ["K", "Kiwi", "Kumquat"]
    results = [n.value for n in urls.find_all("/")]
    print(results)

def test_TSTree_find_shortest():
    urls = test_TSTree_get_set()
    urls.set("/kiwikiwi/", "KiwiKiwi")
    assert urls.find_shortest("/k").value == "K"
    assert urls.find_shortest("/ki").value == "Kiwi"
    assert urls.find_shortest("/kiwiki").value == "KiwiKiwi"
    assert urls.find_shortest("/a").value == "Apple"
    print(urls.find_shortest("/").value)
    #assert urls.find_shortest("/").value == "K"


def test_TSTree_find_longest():
    urls = test_TSTree_get_set()
    assert urls.find_longest("/").value == "Pineapple"


def test_TSTree_find_part():
    urls = test_TSTree_get_set()
    assert urls.find_part("/kaler").value == "K"
#    assert urls.find_part("/kaler").value == "Kiwi"
    assert urls.find_part("/application").value == "Apple"
  #  print(urls.find_part("/papal").value)
    assert urls.find_part("/papal").value == "Pineapple"
    assert urls.find_part("/apple/120/1000/").value == "Apple"
    assert urls.find_part("/kiwi/user/zedshaw/has/stuff").value == "Kiwi"
   # print(urls.find_part("/l").value)
    assert urls.find_part("/l").value == "lm"

    assert urls.find_part("XTREEME") == None
