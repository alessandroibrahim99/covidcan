
import os



## App settings
name = "Forecaster - COVID19 CANADA"

host = "0.0.0.0"

port = int(os.environ.get("PORT", 5000))

debug = False

contacts = "https://www.linkedin.com/in/alessandro-ibrahim-b24640a/"

#code = "https://github.com/alessandroibrahim99/covidcan"
code = "http://www.itforecasts.com/dist/index.html"

fontawesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'



## File system
root = os.path.dirname(os.path.dirname(__file__)) + "/"



## DB
