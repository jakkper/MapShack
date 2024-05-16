import pygame
import folium
import webview
import data
import pickle

#stworzenie czcionek
pygame.font.init() 
menuF = pygame.font.Font('fonts/Helvetica-Bold.ttf', 190)
title = menuF.render('MapShack', False, "#00994C")

sections=pygame.font.Font('fonts/Helvetica-Bold.ttf', 100)
statF=pygame.font.Font('fonts/Helvetica-Bold.ttf', 70)
statF2=pygame.font.Font('fonts/Helvetica.ttf', 70)
StatAF = statF.render('Africa', False, "#00994C")
StatEU = statF.render('Europe', False, "#00994C")
StatNA = statF.render('North America', False, "#00994C")
StatSA = statF.render('South America', False, "#00994C")
StatAU = statF.render('Oceania', False, "#00994C")
StatAS = statF.render('Asia', False, "#00994C")
StatW = statF.render('World', False, "#00994C")

EUtitle = sections.render('Europe', False, "#00994C")
NAtitle = sections.render('North America', False, "#00994C")
SAtitle = sections.render('South America', False, "#00994C")
AFtitle = sections.render('Africa', False, "#00994C")
AStitle = sections.render('Asia', False, "#00994C")
AUtitle = sections.render('Oceania', False, "#00994C")
STtitle = sections.render('Statistics', False, "#00994C")
#klasy
class country:
  def __init__(self, name):
    self.name = name
    self.json="geo/"+str(name)+".geojson"

class Button:
  def __init__(self,Xpos,Ypos,Xsize,Ysize,color,hover,text,TXpos,TYpos,Tsize):
    self.text=text
    self.TXpos=TXpos
    self.TYpos=TYpos
    self.Tsize=Tsize
    self.color=color
    self.hover=hover
    self.actual=color
    self.Xpos=Xpos
    self.Ypos=Ypos
    self.Xsize=Xsize
    self.Ysize=Ysize
    self.rect=pygame.Rect(Xpos,Ypos,Xsize,Ysize)
    self.fnt = pygame.font.Font('fonts/Helvetica-Bold.ttf', self.Tsize)
    self.title = self.fnt.render(self.text, False, (255,255,255))
  def render(self,screen):
    pygame.draw.rect(screen,(self.actual),self.rect)
    screen.blit(self.title, (self.TXpos,self.TYpos))
  def collide(self,x,y):
    if x<(self.Xpos+self.Xsize) and x>self.Xpos and y>self.Ypos and y<(self.Ypos+self.Ysize):
      self.actual=self.hover
      return True
    else:
      self.actual=self.color
      return False

class Continent:
  def __init__(self,name):
    self.name=name
    self.file="continents/"+name+".png"
    self.hover="continents/"+name+"hover.png"
    self.view=pygame.image.load(self.file).convert_alpha()
    self.mask=pygame.mask.from_surface(self.view)
    self.state=False
  def ren(self,mx,my):
    try:
      if self.mask.get_at((mx-0, my-210))!=self.state:
        if self.state==False:
          self.state=True
          self.view=pygame.image.load(self.hover).convert_alpha()
        else:
          self.state=False
          self.view=pygame.image.load(self.file).convert_alpha()
    except IndexError:
      pass
  def click(self,mx,my):
    global stage
    try:
      if self.mask.get_at((mx-0, my-210)) and event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          stage=self.name
    except IndexError:
      pass

#funkcje
styleT= {'fillColor': '#00994C', 'color': '#00994C'}
styleF= {'fillColor': '#009999', 'color': '#009999'}

def renderB(arr):
  for obj in arr:
      obj.render(screen,mx,my)
  pygame.draw.rect(screen,(255,255,255),kaseton1)
  pygame.draw.rect(screen,(255,255,255),kaseton2)
  
def map():
  m=folium.Map(location=[42.3601, -71.0589],zoom_start=2)
  visited=data.load()
  work_list=data.europe+data.namerica+data.africa+data.samerica+data.asia+data.oceania
  for obj in work_list:
      if visited.get(obj.country)==1:
        folium.GeoJson("geo/"+obj.country+".geojson", name=(obj.country),style_function=lambda x:styleT).add_to(m)
      if visited.get(obj.country)==2:
        folium.GeoJson("geo/"+obj.country+".geojson", name=(obj.country),style_function=lambda x:styleF).add_to(m)
  m.save('map.html')
  webview.create_window('Map', 'map.html')
  webview.start()
  
def stats_check(arr):
  visited1=pickle.load(open("save/visited.dat", "rb"))
  PR=0
  for obj in arr:
    if visited1[obj.country]==1:
      obj.state=1
    if visited1[obj.country]==0:
      obj.state=0
    if visited1[obj.country]==2:
      obj.state=2
    if obj.state==1:
      PR=PR+1
  return PR
  
def buildB(arr):
  if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 5 and arr[-1].Ypos>650:
            for obj in arr:
              obj.Ypos=obj.Ypos-120
          if event.button == 4 and arr[0].Ypos<130:
            for obj in arr:
              obj.Ypos=obj.Ypos+120
          for obj in arr:
            if event.type == pygame.MOUSEBUTTONDOWN:
              if obj.hover==True and obj.inside1.collidepoint(mx, my) and event.button == 1 and (obj.state==0 or obj.state==2):
                visited=data.load()
                visited[obj.country]=1
                pickle.dump(visited,open("save/visited.dat", "wb"))
              if obj.hover==True and obj.inside1.collidepoint(mx, my) and event.button == 1 and obj.state==1:
                visited=data.load()
                visited[obj.country]=0
                pickle.dump(visited,open("save/visited.dat", "wb"))
              if obj.hover2==True and obj.inside2.collidepoint(mx, my) and event.button == 1 and (obj.state==0 or obj.state==1):
                visited=data.load()
                visited[obj.country]=2
                pickle.dump(visited,open("save/visited.dat", "wb"))
              if obj.hover2==True and obj.inside2.collidepoint(mx, my) and event.button == 1 and obj.state==2:
                visited=data.load()
                visited[obj.country]=0
                pickle.dump(visited,open("save/visited.dat", "wb"))



#deklaracja przycislów
BackButton=Button(50,10,200,80,"#00994C","#006633","Back",70,22,65)
MapButton=Button(50,900,905,100,"#00994C","#006633","Go to map",300,915,80)
Stats=Button(965,900,905,100,"#00994C","#006633","Statistics",1250,915,80)

#zmienne podstawowe
W=1920
H=1030
background_colour = (255,255,255)
(width, height) = (W, H)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('MapShack')
screen.fill(background_colour)
pygame.display.flip()
clock = pygame.time.Clock()
scale=0.08
stage="M"
kaseton1=pygame.Rect(0,0,1920,130)
kaseton2=pygame.Rect(0,890,1920,130)
world_list=data.europe+data.namerica+data.africa+data.samerica+data.asia+data.oceania

#stworzenie kontynentów obiektów
NA=Continent("NA")
SA=Continent("SA")
EU=Continent("EU")
AF=Continent("AF")
AS=Continent("AS")
AU=Continent("AU")
continents=[NA,SA,EU,AS,AF,AU]

running = True

while running:
  screen.fill(background_colour)
  mx, my=pygame.mouse.get_pos()
  
  if stage=="M":
    for obj in continents:
      obj.ren(mx,my)
      screen.blit(obj.view,(0,210))
    screen.blit(title, (460,10))

  if stage=="ST":
    screen.blit(STtitle, (720,10))
    BackButton.render(screen)
    row1=pygame.Rect(150,100,1620,100)
    row2=pygame.Rect(150,210,1620,100)
    row3=pygame.Rect(150,320,1620,100)
    row4=pygame.Rect(150,430,1620,100)
    row5=pygame.Rect(150,540,1620,100)
    row6=pygame.Rect(150,650,1620,100)
    row7=pygame.Rect(150,760,1620,100)
    pygame.draw.rect(screen,("#E0E0E0"),row1)
    pygame.draw.rect(screen,("#E0E0E0"),row2)
    pygame.draw.rect(screen,("#E0E0E0"),row3)
    pygame.draw.rect(screen,("#E0E0E0"),row4)
    pygame.draw.rect(screen,("#E0E0E0"),row5)
    pygame.draw.rect(screen,("#E0E0E0"),row6)
    pygame.draw.rect(screen,("#E0E0E0"),row7)
    screen.blit(StatAF, (210,120))
    screen.blit(StatAS, (210,230))
    screen.blit(StatEU, (210,340))
    screen.blit(StatAU, (210,450))
    screen.blit(StatNA, (210,560))
    screen.blit(StatSA, (210,670))
    screen.blit(StatW, (210,780))
    AfricaPR=statF2.render(("countries visited "+str(africaPR)+"/"+str(len(data.africa))+"   "+str(round(africaPR*100/len(data.africa),1))+"%"), False, "#606060")
    AsiaPR=statF2.render(("countries visited "+str(asiaPR)+"/"+str(len(data.asia))+"   "+str(round(asiaPR*100/len(data.asia),1))+"%"), False, "#606060")
    EuropePR=statF2.render(("countries visited "+str(europePR)+"/"+str(len(data.europe))+"   "+str(round(europePR*100/len(data.europe),1))+"%"), False, "#606060")
    OceaniaPR=statF2.render(("countries visited "+str(oceaniaPR)+"/"+str(len(data.oceania))+"   "+str(round(oceaniaPR*100/len(data.oceania),1))+"%"), False, "#606060")
    NamericaPR=statF2.render(("countries visited "+str(namericaPR)+"/"+str(len(data.namerica))+"   "+str(round(namericaPR*100/len(data.namerica),1))+"%"), False, "#606060")
    SamericaPR=statF2.render(("countries visited "+str(samericaPR)+"/"+str(len(data.samerica))+"   "+str(round(samericaPR*100/len(data.samerica),1))+"%"), False, "#606060")
    WorldPR=statF2.render(("countries visited "+str(worldPR)+"/"+str(len(world_list))+" "+str(round(worldPR*100/len(world_list),1))+"%"), False, "#606060")
    screen.blit(AfricaPR, (820,120))
    screen.blit(AsiaPR, (820,230))
    screen.blit(EuropePR, (820,340))
    screen.blit(OceaniaPR, (820,450))
    screen.blit(NamericaPR, (820,560))
    screen.blit(SamericaPR, (820,670))
    screen.blit(WorldPR, (820,780))
    
 
  if stage=="NA":
    renderB(data.namerica)
    screen.blit(NAtitle, (620,10))
    BackButton.render(screen)
    
  if stage=="SA":
    renderB(data.samerica)
    screen.blit(SAtitle, (610,10))
    BackButton.render(screen)
    
  if stage=="EU":
    renderB(data.europe)
    screen.blit(EUtitle, (770,10))
    BackButton.render(screen)
    
  if stage=="AF":
    renderB(data.africa)
    screen.blit(AFtitle, (830,10))
    BackButton.render(screen)
    
  if stage=="AS":
   renderB(data.asia)
   screen.blit(AStitle, (880,10))
   BackButton.render(screen)
    
  if stage=="AU":
    renderB(data.oceania)
    screen.blit(AUtitle, (775,10))
    BackButton.render(screen)

  MapButton.collide(mx,my)
  BackButton.collide(mx,my)
  Stats.collide(mx,my)
  
  for event in pygame.event.get():
    
    #wykonywane w menu
    if stage=="M":
      for obj in continents:
        obj.click(mx,my)
        
    #wykonywane w EU
    if stage=="EU":
      buildB(data.europe)
    #wykonywane w NA
    if stage=="NA":
      buildB(data.namerica)
    #wykonywane w NA
    if stage=="AF":
      buildB(data.africa)
    #wykonywane w SA
    if stage=="SA":
      buildB(data.samerica)
    #wykonywane w AS
    if stage=="AS":
      buildB(data.asia)
    if stage=="AU":
      buildB(data.oceania)
    #zawsze moga być wykonane
    if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        exit()
    if event.type == pygame.MOUSEBUTTONDOWN and MapButton.collide(mx,my):
          if event.button == 1:
            map()
    if event.type == pygame.MOUSEBUTTONDOWN and Stats.collide(mx,my):
          if event.button == 1:
            stage="ST"
            africaPR=stats_check(data.africa)
            europePR=stats_check(data.europe)
            asiaPR=stats_check(data.asia)
            oceaniaPR=stats_check(data.oceania)
            namericaPR=stats_check(data.namerica)
            samericaPR=stats_check(data.samerica)
            worldPR=stats_check(world_list)
    if event.type == pygame.MOUSEBUTTONDOWN and BackButton.collide(mx,my):
          if event.button == 1:
            stage="M"
            
  MapButton.render(screen)
  Stats.render(screen)
  pygame.display.update()
