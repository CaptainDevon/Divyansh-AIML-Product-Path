from collections import deque

history=deque(maxlen=5)

def visit_page(url):
    history.append(url)
    print("visited: ",url)

def go_back():
    if history:
        current=history.pop()
        print('Going back from ',current)

        if history:
            print("Current page is ",history[-1])

        else:
            print("No more pages in history")
    
    else:
        print("No more pages in history")


visit_page("/home")
visit_page("/contract")
visit_page("/about")

go_back()
go_back()