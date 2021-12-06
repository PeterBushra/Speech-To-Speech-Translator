import goslate
from WatsonTranslator import *
gs = goslate.Goslate()


def translate(string, language,IsOnline):
   if IsOnline:
      try:
         return get_watson_translation(string,language)
      except Exception as E:
         return "No internet Connection."
   else:
      try:
         return gs.translate(string,language)
      except Exception as E:
         return "Try Online Model."
  # return "انا مصري"