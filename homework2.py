
# siteleri tuple'da depolar, değişmemesi gereken indexler içerir
sites = ("https://www.borusancat.com/",
         "https://transaytransfer.com/",
         "http://borusaninsan.com/",
         "https://thebclog.com/",
         "https://borusancat.edcast.com/",
         "https://transaytransfer.com/",
         "http://seyahat.theborusans.com/tasks/list",
         "https://processportal.borusancat.com/ProcessPortal",
         "https://thebclog.com/tr/experiences",
         "https://prod.borusancat.com/survey/?survey=8934ac10-8c60-405c-8398-a90c5ccedbc6"
         )

# response kodları ile beraber siteleri depolamak için dictionary yaratır
sitesWithResponses = {}
for i in sites:
    sitesWithResponses[i] = 0 #inital olarak 0 atarh

# function
import random
# sitelere istek atıp response kodlarını çekmiş gibi düşünmemiz için fonksiyon
def requestGenerator():
    return random.choice([200, 401, 404])

# hata alan siteleri ekrana basar
for i in sitesWithResponses:
    sitesWithResponses[i] = requestGenerator() #responları dictionary'ye key olarak ekler
    if sitesWithResponses[i] == 401:
        print(f"{i} is unauthorized.")
    elif sitesWithResponses[i] == 404:
        print(f"{i} is not found.")

