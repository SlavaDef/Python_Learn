import webbrowser

#def validator(func):  # це сам декоратор, перевірялка на коректність відкриття сайтів
  #  def wrapper(url: str):
    #    print('Before validation')
     #   func(url)
     #   print('After validation')
   # return wrapper

def validator(func):  # це сам декоратор, перевірялка на коректність відкриття сайтів
       def wrapper(url: str):
           if url.startswith('http'):
               func(url)
           else:
               print('Invalid URL')
       return wrapper



@validator
def open_url(url):
    webbrowser.open(url)

open_url('https://senior-pomidor.com.ua/') # відбувіеться відкриття сайту