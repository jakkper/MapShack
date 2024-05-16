import pygame
import pickle
import os
import random

pygame.font.init() 
class Block:
  def __init__(self, name,short,Xpos,Ypos):
    self.country=name
    self.Xpos=Xpos
    self.Ypos=Ypos
    self.Xsize=1520
    self.Ysize=300
    
    self.fnt = pygame.font.Font('fonts/Helvetica-Bold.ttf', 60)
    self.fnt2 = pygame.font.Font('fonts/Helvetica-Bold.ttf', 30)
    # 0-nope 1-visited 2- want to visit
    self.state=0
    self.hover=False
    self.hover2=False
    
    self.title = self.fnt.render(self.country, False, (0,0,0))
    self.visited = self.fnt2.render("Visited        Want to visit", False, (0,0,0))
    self.flag=pygame.image.load("flags/"+short+".svg")
    self.flag=pygame.transform.scale(self.flag,(80,60))
  def render(self,screen,mx,my):
    visited1=pickle.load(open("save/visited.dat", "rb"))
    if visited1[self.country]==1:
      self.state=1
    if visited1[self.country]==0:
      self.state=0
    if visited1[self.country]==2:
      self.state=2
    self.rect=pygame.Rect(self.Xpos,self.Ypos,self.Xsize,self.Ysize)
    pygame.draw.rect(screen,("#E0E0E0"),self.rect)
    screen.blit(self.title, (self.Xpos+100,self.Ypos+15))
    screen.blit(self.visited, (self.Xpos+20,self.Ypos+260))
    screen.blit(self.flag, (self.Xpos+10,self.Ypos+10))
    
    self.border1=pygame.Rect(self.Xpos+122,self.Ypos+260,30,30)
    self.inside1=pygame.Rect(self.Xpos+126,self.Ypos+264,22,22)
    pygame.draw.rect(screen,(0,0,0),self.border1)
    if self.inside1.collidepoint(mx, my):
      pygame.draw.rect(screen,(255,255,255),self.inside1)
      self.hover=True
    else:
      self.hover=False
      if self.state==0:
        pygame.draw.rect(screen,("#E0E0E0"),self.inside1)
      if self.state==1:
        pygame.draw.rect(screen,("#00994C"),self.inside1)
    self.border1=pygame.Rect(self.Xpos+365,self.Ypos+260,30,30)
    self.inside2=pygame.Rect(self.Xpos+369,self.Ypos+264,22,22)
    pygame.draw.rect(screen,(0,0,0),self.border1)
    if self.inside2.collidepoint(mx, my):
      pygame.draw.rect(screen,(255,255,255),self.inside2)
      if self.state==1:
        pygame.draw.rect(screen,("#00994C"),self.inside1)
      else:
        pygame.draw.rect(screen,("#E0E0E0"),self.inside1)
      self.hover2=True
    else:
      self.hover2=False
      if self.state==0 or self.state==1:
        pygame.draw.rect(screen,("#E0E0E0"),self.inside2)
      if self.state==2:
        pygame.draw.rect(screen,("#00994C"),self.inside2)
        pygame.draw.rect(screen,("#E0E0E0"),self.inside1)
    
def random_cou(tab):
  print(tab[random.randint(0,len(tab)-1)])




def load():
  return pickle.load(open("save/visited.dat", "rb"))
countriesEU=['Albania','Andorra', 'Austria','Belarus','Belgium','Bosnia','Bulgaria',
           'Croatia','Czech',"Denmark","Estonia","Finland","France","Germany", "Greece","Hungary"
           ,"Iceland","Ireland","Italy","Kosovo","Latvia","Liechtenstein","Lithuania","Macedonia",
           "Malta", "Moldova","Monaco","Montenegro","Netherlands","Norway","Poland","Portugal","Romania"
           ,"Russia","San Marino","Serbia","Slovakia","Slovenia","Spain","Sweden","Switzerland","Ukraine","UK","Vatican"]

shortcutEU=["al","ad","at","by","be","ba",
          "bg", "hr", "cz","dk","ee","fi","fr","de","gr","hu","is","ie","it"
          ,"xk","lv","li","lt","mk","mt","md","mc","me","nl","no",
          "pl","pt","ro","ru","sm","rs","sk","si",
            "es","se","ch","ua","gb","va"]

countriesNA=["Anguilla","Antigua and Barbuda","Aruba",
             "Barbrados","Belize","Bermuda",
             "British Virgin Islands","Canada",
            "Cayman Islands","Clipperton Islands",
             "Costa Rica","Cuba","Curaçao","Dominica",
             "Dominican Republic","El Salvador",
             "Greenland","Grenada","Guatemala","Haiti","Honduras"
             ,"Jamaica","Mexico","Montserrat","Nicaragua","Panama",
             "Puerto Rico","Saint Barthelemy",
             "Saint Kitts and Nevis","Saint Lucia"
             ,"Saint Martin", "Saint Pierre and Miquelon",
             "Saint Vincent and the Grenadines",
             "Sint Maarten","The Bahamas","Trynidad and Tobago",
             "Turks and Caicos Islands",
             "United States of America",
             "United States Virgin Islands"]

shortcutNA=["ai","ag","aw","bb","bz","bm","vg","ca","ky","cp","cr","cu","cw",
            "dm","do","sv","gl","gd","gt","ht","hn","jm","mx","ms"
            ,"ni","pa","pr","bl","kn","lc","mf","pm"
            ,"vc","sx","bs","tt","tc","us","vi"]

countriesAF=["Algeria","Angola","Benin","Botswana","Burkina Faso","Burundi","Cameroon","Cape Verge",
             "Central African Republic", "Chad","Comoros","Congo","Democratic Republic of Congo",
             "Djibouti","Egypt","Equatorial Guinea","Eritrea","Ethiopia","Gabon", "Gambia",
             "Ghana","Guinea Bissau","Guinea","Ivory Coast","Kenya","Lesotho","Liberia","Libya",
             "Madagascar","Malawi","Mali","Mauritania","Mauritius","Morocco","Mozambique","Namibia",
             "Niger","Nigeria","Rwanda","Sao Tome and Principe","Senegal","Seychelles","Sierra Leone",
             "Somalia","Somaliland","South Africa","South Sudan","Sudan","Swaziland","Togo",
             "Tunisia","Tanzania","Uganda","Western Sahara","Zambia","Zimbabwe"]

shortcutAF=["dz","ao","bj","bw","bf","bi","cm","cv","cf","td","km","cg","cd","dj","eg","gq","er","et",
            "ga","gm","gh","gw","gn","ci","ke","ls","lr","ly","mg","mw","ml","mr","mu","ma","mz"
            ,"na","ne","ng","rw","st","sn","sc","sl","so","xx","za","ss","sd","sz","tg","tn","tz","ug","eh","zm","zw"]

countriesSA=["Argentina","Bolivia","Brazil","Chile","Colombia","Ecuador","Falkland Islands",
             "Guyana","Paraguay","Peru","South Georgia and South Sandwich Islands","Suriname","Uruguay","Venezuela"]
shortcutSA=["ar","bo","br","cl","co","ec","fk","gy","py","pr","gs","sr","uy","ve"]

countriesAS=["Afghanistan","Armenia","Azerbaijan","Bahrain","Bangladesh",
             "Bhutam","Brunei","Cambodia","China","Georgia",
             "Hong Kong","India","Indonesia","Iran",
             "Iraq","Israel","Japan","Jordan","Kazakhstan",
             "Kuwait","Kyrgyzstan","Laos","Lebanon","Macao","Malaysia"
             ,"Maldives","Myanmar","Nepal","North Korea","Oman","Pakistan","Palestine","Philippines","Qatar"
             ,"Saudi Arabia","Singapore","South Korea","Sri Lanka",
             "Syria","Taiwan","Tajikistan","Thailand",
             "Turkey","Turkmenistan","United Arab Emirates","Uzbekistan","Vietnam","Yemen"]
shortcutAS=["af","am","az","bh","bd",
            "bt","bn","kh","cn","ge",
            "hk","in","id","ir","iq",
            "il","jp","jo","kz","kw",
            "kg","la","lb","mo","my",
            "mv","mm","np","kp","om","pk","ps",
            "ph","qa","sa","sg","kr",
            "lk","sy","tw","tj","th",
            "tr","tm","ae","uz","vn",
            "ye"]

countriesAU=["American Samoa","Australia","Cook Islands","East Timor","Federated States of Micronesia",
             "Fiji","French Polynesia","Guam","Kiribati","Marshall Islands","Nauru","New Caledonia",
             "New Zeland","Niue","Norfolk Island","Palau","Papua New Guinea","Samoa","Solomon Islands","Tonga",
             "Tuvalu","Vanuatu","Wallis and Futuna"]
shortcutAU=["as","au","ck","tl","fm","fj","pf","gu","ki","mh","nr","nc","nz","nu","nf"
            ,"pw","pg","ws","sb","to","tv","vu","wf"]
europe=[]
namerica=[]
africa=[]
samerica=[]
asia=[]
oceania=[]

def build(arr,countries,shortcut):
  y=130
  for x in range(0,len(countries),1):
    blockx=Block(countries[x],shortcut[x],200,130+(x*320))
    arr.append(blockx)
  return arr
europe=build(europe,countriesEU,shortcutEU)
namerica=build(namerica,countriesNA,shortcutNA)
africa=build(africa,countriesAF,shortcutAF)
samerica=build(samerica,countriesSA,shortcutSA)
asia=build(asia,countriesAS,shortcutAS)
oceania=build(oceania,countriesAU,shortcutAU)
def create(arr1,arr2,arr3,arr4,arr5,arr6):
  visited={}
  for i in range(0,len(arr1),1):
    visited[arr1[i].country]=0
  for i in range(0,len(arr2),1):
    visited[arr2[i].country]=0
  for i in range(0,len(arr3),1):
    visited[arr3[i].country]=0
  for i in range(0,len(arr4),1):
    visited[arr4[i].country]=0
  for i in range(0,len(arr5),1):
    visited[arr5[i].country]=0
  for i in range(0,len(arr6),1):
    visited[arr6[i].country]=0
  pickle.dump(visited,open("save/visited.dat","wb"))

