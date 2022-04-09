from cs1graphics import*
city=Canvas(4000,1000,"sky blue")
import time

sun=Circle(40,Point(1200,50))
sun.setFillColor("yellow")
sun.setBorderColor("yellow")
city.add(sun)


boss=Layer()
city.add(boss)


#gray road
grroad=Layer()
boss.add(grroad)
street=Rectangle(5000,200,Point(1500,350))
street.setFillColor("Moccasin")
street.setBorderColor("Moccasin")
grroad.add(street)



#addtional point 4
addi=Layer()
boss.add(addi)
adu=Rectangle(1500,500,Point(3373,920))
adu.setFillColor("Moccasin")
adu.setBorderColor("Moccasin")
addi.add(adu)



#in side aspalt
inside=Layer()
boss.add(inside)
ins=Square(650,Point(3300,550))
ins.setFillColor("black")
inside.add(ins)

#square
square=Layer()
boss.add(square)
sq=Circle(100,Point(3300,550))
sq.setFillColor("LimeGreen")
square.add(sq)

#square cover
sc=Layer()
boss.add(sc)
scv=Circle(200,Point(2975,225))
scv.setFillColor("Moccasin")
scv.setBorderColor("Moccasin")
sc.add(scv)

#sky add
semay=Layer()
boss.add(semay)
sky=Rectangle(500,250,Point(3000,120))
sky.setFillColor("sky blue")
sky.setBorderColor("sky blue")
semay.add(sky)


#square cover 2
sc2=Layer()
boss.add(sc2)
scv2=Circle(200,Point(3625,225))
scv2.setFillColor("Moccasin")
scv2.setBorderColor("Moccasin")
sc2.add(scv2)



#sky add other side
semay1=Layer()
boss.add(semay1)
sky1=Rectangle(500,250,Point(3580,120))
sky1.setFillColor("sky blue")
sky1.setBorderColor("sky blue")
semay1.add(sky1)


#square cover 3
sc3=Layer()
boss.add(sc3)
scv3=Circle(200,Point(3625,875))
scv3.setFillColor("Moccasin")
scv3.setBorderColor("Moccasin")
sc3.add(scv3)

#square cover 4
sc4=Layer()
boss.add(sc4)
scv4=Circle(200,Point(2975,875))
scv4.setFillColor("Moccasin")
scv4.setBorderColor("Moccasin")
sc4.add(scv4)


#grass
afer=Layer()
boss.add(afer)
grass=Rectangle(3000,400,Point(1500,800))
grass.setFillColor("Moccasin")
grass.setBorderColor("Moccasin")
afer.add(grass)


#aspalt
aspalt=Layer()
boss.add(aspalt)
road=Rectangle(3000,250,Point(1500,550))
road.setFillColor("black")
aspalt.add(road)

#line
line1=Rectangle(3000,10,Point(1500,540))
line1.setFillColor("yellow")
aspalt.add(line1)


line2=Rectangle(3000,10,Point(1500,560))
line2.setFillColor("yellow")
aspalt.add(line2)

#upper aspalt
aspalt2=Layer()
boss.add(aspalt2)
us=Rectangle(250,300,Point(3300,150))
us.setFillColor("black")
aspalt2.add(us)
#line of the upper aspalt
line1=Rectangle(10,300,Point(3290,150))
line1.setFillColor("yellow")
aspalt2.add(line1)

line2=Rectangle(10,300,Point(3310,150))
line2.setFillColor("yellow")
aspalt2.add(line2)

#aspalt3
aspalt3=Layer()
boss.add(aspalt3)
sas=Rectangle(400,250,Point(3800,550))
sas.setFillColor("black")
aspalt3.add(sas)
#lines
line1=Rectangle(400,10,Point(3800,540))
line1.setFillColor("yellow")
aspalt3.add(line1)

line2=Rectangle(400,10,Point(3800,560))
line2.setFillColor("yellow")
aspalt3.add(line2)

#aspalt 4 ... down ward aspalt
aspalt4=Layer()
boss.add(aspalt4)
as4=Rectangle(250,175,Point(3300,912))
as4.setFillColor("black")
aspalt4.add(as4)

#lines of aspalt 4
line1=Rectangle(10,175,Point(3290,912))
line1.setFillColor("yellow")
aspalt4.add(line1)

line2=Rectangle(10,175,Point(3310,912))
line2.setFillColor("yellow")
aspalt4.add(line2)

#railway
railway=Layer()
boss.add(railway)

r1=Rectangle(10,3000,Point(600,1))
r1.setFillColor("gray")
railway.add(r1)

r2=Rectangle(10,3000,Point(560,1))
r2.setFillColor("gray")
railway.add(r2)


r3=Rectangle(10,3000,Point(650,1))
r3.setFillColor("gray")
railway.add(r3)

r3=Rectangle(10,3000,Point(690,1))
r3.setFillColor("gray")
railway.add(r3)
#horizontal 1
l=Rectangle(40,10,Point(580,100))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,120))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,140))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,160))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,180))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,200))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,220))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,240))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,260))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,280))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,300))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,320))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,340))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,360))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,380))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,400))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)


l=Rectangle(40,10,Point(580,420))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,440))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,460))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,480))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,500))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,520))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,540))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,560))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,580))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,600))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)


l=Rectangle(40,10,Point(580,620))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,640))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,660))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,680))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,700))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,720))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,740))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,760))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,780))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,800))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,820))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,840))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,860))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,880))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,900))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,920))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,940))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,960))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,980))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(580,1000))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)





#horizontal 2
l=Rectangle(40,10,Point(670,100))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,120))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,140))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,160))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,180))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,200))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,220))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,240))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,260))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,280))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,300))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,320))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,340))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,360))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,380))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,400))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)


l=Rectangle(40,10,Point(670,420))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,440))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,460))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,480))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,500))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,520))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,540))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,560))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,580))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,600))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)


l=Rectangle(40,10,Point(670,620))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,640))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,660))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,680))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,700))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,720))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,740))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,760))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,780))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,800))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,820))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,840))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,860))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,880))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,900))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,920))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,940))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,960))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,980))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)

l=Rectangle(40,10,Point(670,1000))
l.setFillColor("DarkKhaki")
l.setBorderColor("DarkKhaki")
railway.add(l)


#zebra

zebra=Layer()
boss.add(zebra)
zeb=Rectangle(100,25,Point(1500,435))
zeb.setFillColor("white")
zeb.setBorderColor("white")
zebra.add(zeb)

zeb=Rectangle(100,25,Point(1500,475))
zeb.setFillColor("white")
zeb.setBorderColor("white")
zebra.add(zeb)

zeb=Rectangle(100,25,Point(1500,515))
zeb.setFillColor("white")
zeb.setBorderColor("white")
zebra.add(zeb)



zeb=Rectangle(100,25,Point(1500,555))
zeb.setFillColor("white")
zeb.setBorderColor("white")
zebra.add(zeb)

zeb=Rectangle(100,25,Point(1500,595))
zeb.setFillColor("white")
zeb.setBorderColor("white")
zebra.add(zeb)

zeb=Rectangle(100,25,Point(1500,635))
zeb.setFillColor("white")
zeb.setBorderColor("white")
zebra.add(zeb)

#birds
birds=Layer()
boss.add(birds)
bird1=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird1.setBorderWidth(10)
bird1.setBorderColor("black")
bird1.setDepth(10)
bird1.moveTo(900, 50)
birds.add(bird1)

bird2=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird2.setBorderWidth(10)
bird2.setBorderColor("black")
bird2.setDepth(10)
bird2.moveTo(950, 100)
birds.add(bird2)

bird3=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird3.setBorderWidth(10)
bird3.setBorderColor("black")
bird3.setDepth(10)
bird3.moveTo(800, 50)
birds.add(bird3)

bird4=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird4.setBorderWidth(10)
bird4.setBorderColor("black")
bird4.setDepth(10)
bird4.moveTo(850, 100)
birds.add(bird4)

bird5=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird5.setBorderWidth(10)
bird5.setBorderColor("black")
bird5.setDepth(10)
bird5.moveTo(820, 90)
birds.add(bird5)

bird6=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird6.setBorderWidth(10)
bird6.setBorderColor("black")
bird6.setDepth(10)
bird6.moveTo(800, 95)
birds.add(bird6)



#building 1
building=Layer()
boss.add(building)
front=Rectangle(150,300,Point(300,400))
front.setFillColor('OrangeRed')
building.add(front)

head=Polygon(Point(100,100),Point(250,100),Point(200,180),Point(50,180))
head.setFillColor('LightPink')
head.move(175,72)
building.add(head)
side=Polygon(Point(100,100),Point(150,20),Point(150,320),Point(100,400))
side.setFillColor('coral')
side.move(273,152)
building.add(side)

win=Square(50,Point(260,300))
win.setFillColor('black')
building.add(win)

win1=Square(50,Point(330,300))
win1.setFillColor('black')
building.add(win1)

win3=Square(50,Point(260,360))
win3.setFillColor('black')
building.add(win3)

win4=Square(50,Point(330,360))
win4.setFillColor('black')
building.add(win4)

win5=Square(50,Point(260,420))
win5.setFillColor('black')
building.add(win5)

win6=Square(50,Point(330,420))
win6.setFillColor('black')
building.add(win6)

win7=Rectangle(90,40,Point(290,490))
win7.setFillColor('LightSeaGreen')
building.add(win7)

door=Rectangle(30,20,Point(100,100))
door.setFillColor('black')
door.rotate(90)
door.move(195,435)
building.add(door)
building.move(-150,-150)

#building2

building=Layer()
boss.add(building)
front=Rectangle(150,300,Point(300,400))
front.setFillColor('OrangeRed')
building.add(front)

head=Polygon(Point(100,100),Point(250,100),Point(200,180),Point(50,180))
head.setFillColor('LightPink')
head.move(175,72)
building.add(head)
side=Polygon(Point(100,100),Point(150,20),Point(150,320),Point(100,400))
side.setFillColor('coral')
side.move(273,152)
building.add(side)

win=Square(50,Point(260,300))
win.setFillColor('black')
building.add(win)

win1=Square(50,Point(330,300))
win1.setFillColor('black')
building.add(win1)

win3=Square(50,Point(260,360))
win3.setFillColor('black')
building.add(win3)

win4=Square(50,Point(330,360))
win4.setFillColor('yellow')
building.add(win4)

win5=Square(50,Point(260,420))
win5.setFillColor('black')
building.add(win5)

win6=Square(50,Point(330,420))
win6.setFillColor('yellow')
building.add(win6)

win7=Rectangle(90,40,Point(290,490))
win7.setFillColor('LightSeaGreen')
building.add(win7)

door=Rectangle(30,20,Point(100,100))
door.setFillColor('black')
door.rotate(90)
door.move(195,435)
building.add(door)
building.move(60,-150)


#axum stile building 3

axum=Layer()
boss.add(axum)
chaf=Polygon(Point(200,200),Point(250,130),Point(300,200))
chaf.setFillColor("DarkKhaki")
axum.add(chaf)

side=Rectangle(100,290,Point(250,345))
side.setFillColor("DarkKhaki")
axum.add(side)

dirib=Polygon(Point(300,200),Point(340,180),Point(340,470),Point(300,490))
dirib.setFillColor("DarkKhaki")
axum.add(dirib)

dirib1=Polygon(Point(250,130),Point(290,110),Point(340,180),Point(300,200))
dirib1.setFillColor("DarkKhaki")
axum.add(dirib1)

dicor=Rectangle(50,30,Point(230,250))
dicor.setFillColor("green")
axum.add(dicor)

dicor=Rectangle(50,30,Point(270,270))
dicor.setFillColor("yellow")
axum.add(dicor)

dicor=Rectangle(50,30,Point(230,290))
dicor.setFillColor("red")
axum.add(dicor)


dicor=Rectangle(100,30,Point(250,330))
dicor.setFillColor("Magenta")
axum.add(dicor)

dicor=Rectangle(100,30,Point(250,370))
dicor.setFillColor("red")
axum.add(dicor)

dicor=Rectangle(100,30,Point(250,410))
dicor.setFillColor("chocolate")
axum.add(dicor)


axum.move(600,-100)



#building 4
bu=Layer()

ll=Polygon(Point(390,270),Point(390,220),Point(420,190))
ll.setFillColor('SeaGreen')
ll.setDepth(29)
bu.add(ll)

hat=Polygon(Point(150,250),Point(200,250),Point(170,280),Point(330,280),Point(360,250),Point(410,250),Point(440,220),Point(390,220),Point(420,190),Point(260,190),Point(230,220),Point(180,220))
hat.setFillColor('DarkRed')
hat.setDepth(4)
bu.add(hat)

haat=Polygon(Point(190,270),Point(330,270),Point(400,200),Point(260,200))
haat.setFillColor('Thistle')
haat.setDepth(3)
bu.add(haat)

bl=Polygon(Point(80,400),Point(80,200),Point(150,200),Point(150,250),Point(200,250),Point(200,400))
bl.setFillColor('DarkRed')
bl.setDepth(29)
bu.add(bl)

bll=Polygon(Point(170,420),Point(170,280),Point(330,280),Point(330,420))
bll.setFillColor('DarkRed')
bll.setDepth(27)
bu.add(bll)

blll=Polygon(Point(360,400),Point(360,250),Point(410,250),Point(410,200),Point(480,200),Point(480,400))
blll.setFillColor('DarkRed')
blll.setDepth(2)
bu.add(blll)

ha=Polygon(Point(330,420),Point(330,280),Point(360,250),Point(360,400))
ha.setFillColor('SeaGreen')
ha.setDepth(29)
bu.add(ha)

haa=Polygon(Point(80,200),Point(110,170),Point(180,170),Point(150,200))
haa.setFillColor('DarkRed')
haa.setDepth(29)
bu.add(haa)

haaa=Polygon(Point(410,200),Point(440,170),Point(510,170),Point(480,200))
haaa.setFillColor('DarkRed')
haaa.setDepth(29)
bu.add(haaa)

le=Polygon(Point(150,250),Point(180,220),Point(180,170),Point(150,200))
le.setFillColor('SeaGreen')
le.setDepth(29)
bu.add(le)

lee=Polygon(Point(480,200),Point(510,170),Point(510,370),Point(480,400))
lee.setFillColor('SeaGreen')
lee.setDepth(29)
bu.add(lee)

door=Polygon(Point(220,420),Point(220,380),Point(260,380),Point(260,420))
door.setFillColor('LightSteelBlue')
door.setDepth(26)
bu.add(door)

wi=Polygon(Point(100,250),Point(130,250),Point(130,220),Point(100,220))
wi.setFillColor('LightSteelBlue')
wi.setDepth(29)
bu.add(wi)

wii=Polygon(Point(430,250),Point(460,250),Point(460,220),Point(430,220))
wii.setFillColor('LightSteelBlue')
wii.setDepth(2)
bu.add(wii)

wib=Polygon(Point(100,350),Point(130,350),Point(130,320),Point(100,320))
wib.setFillColor('LightSteelBlue')
wib.setDepth(29)
bu.add(wib)

wl=Polygon(Point(150,365),Point(170,365),Point(170,335),Point(150,335))
wl.setFillColor('LightSteelBlue')
wl.setDepth(28)
bu.add(wl)

wla=Polygon(Point(80,305),Point(190,305),Point(190,270),Point(80,270))
wla.setFillColor('LightSteelBlue')
wla.setDepth(28)
bu.add(wla)

wiib=Polygon(Point(430,350),Point(460,350),Point(460,320),Point(430,320))
wiib.setFillColor('LightSteelBlue')
wiib.setDepth(2)
bu.add(wiib)

wll=Polygon(Point(380,365),Point(410,365),Point(410,335),Point(380,335))
wll.setFillColor('LightSteelBlue')
wll.setDepth(2)
bu.add(wll)

wllb=Polygon(Point(360,305),Point(480,305),Point(480,270),Point(360,270))
wllb.setFillColor('LightSteelBlue')
wllb.setDepth(2)
bu.add(wllb)

wia=Polygon(Point(175,365),Point(325,365),Point(325,285),Point(175,285))
wia.setFillColor('LightSteelBlue')
wia.setDepth(26)
bu.add(wia)

d=Path(Point(175,325),Point(325,325))
d.setDepth(26)
d.setBorderWidth(4)
bu.add(d)

d=Path(Point(240,420),Point(240,380))
d.setDepth(26)
bu.add(d)
bu.moveTo(-10,-100)
bu.scale(1.2)
boss.add(bu)

bu.move(950,-15)










#building 5
resort=Layer()
boss.add(resort)
resortroof=Polygon(Point(525,3),Point(500,33),Point(660,33),Point(680,13),Point(810,13),Point(790,33),Point(950,33),Point(975,3))
resortroof.setFillColor("chocolate")
resortroof.setDepth(10)
resort.add(resortroof)

resortfrontwall1=Rectangle(160,80,Point(580,73))
resortfrontwall1.setFillColor("cyan")
resortfrontwall1.setDepth(10)
resort.add(resortfrontwall1)

resortfrontwall2=Rectangle(135,80,Point(740,53))
resortfrontwall2.setFillColor("cyan")
resortfrontwall2.setDepth(11)
resort.add(resortfrontwall2)

resortfrontwall3=Rectangle(160,80,Point(870,73))
resortfrontwall3.setFillColor("cyan")
resortfrontwall3.setDepth(10)
resort.add(resortfrontwall3)

resortside1=Polygon(Point(660,33),Point(680,13),Point(680,93),Point(660,113))
resortside1.setFillColor("brown")
resortside1.setDepth(10)
resort.add(resortside1)

resortside2=Polygon(Point(950,33),Point(975,3),Point(975,83),Point(950,113))
resortside2.setFillColor("brown")
resortside2.setDepth(10)
resort.add(resortside2)

resortwindow1=Rectangle(25,30,Point(520,55))
resortwindow1.setFillColor("white")
resortwindow1.setDepth(10)
resort.add(resortwindow1)

resortwindow2=Rectangle(25,30,Point(550,55))
resortwindow2.setFillColor("white")
resortwindow2.setDepth(10)
resort.add(resortwindow2)

resortwindow3=Rectangle(25,30,Point(580,55))
resortwindow3.setFillColor("white")
resortwindow3.setDepth(10)

resortwindow4=Rectangle(25,30,Point(610,55))
resortwindow4.setFillColor("white")
resortwindow4.setDepth(10)
resort.add(resortwindow4)

resortwindow5=Rectangle(25,30,Point(640,55))
resortwindow5.setFillColor("white")
resortwindow5.setDepth(10)
resort.add(resortwindow5)

resortwindow6=Rectangle(25,30,Point(520,95))
resortwindow6.setFillColor("white")
resortwindow6.setDepth(10)
resort.add(resortwindow6)

resortwindow7=Rectangle(25,30,Point(550,95))
resortwindow7.setFillColor("white")
resortwindow7.setDepth(10)
resort.add(resortwindow7)

resortwindow8=Rectangle(25,30,Point(580,95))
resortwindow8.setFillColor("white")
resortwindow8.setDepth(10)

resortwindow9=Rectangle(25,30,Point(610,95))
resortwindow9.setFillColor("white")
resortwindow9.setDepth(10)
resort.add(resortwindow9)

resortwindow10=Rectangle(25,30,Point(640,95))
resortwindow10.setFillColor("white")
resortwindow10.setDepth(10)
resort.add(resortwindow10)

resortwindow11=Rectangle(25,30,Point(810,55))
resortwindow11.setFillColor("white")
resortwindow11.setDepth(9)
resort.add(resortwindow11)

resortwindow12=Rectangle(25,30,Point(840,55))
resortwindow12.setFillColor("white")
resortwindow12.setDepth(9)
resort.add(resortwindow12)

resortwindow13=Rectangle(25,30,Point(870,55))
resortwindow13.setFillColor("white")
resortwindow13.setDepth(9)

resortwindow14=Rectangle(25,30,Point(900,55))
resortwindow14.setFillColor("white")
resortwindow14.setDepth(9)
resort.add(resortwindow14)

resortwindow15=Rectangle(25,30,Point(930,55))
resortwindow15.setFillColor("white")
resortwindow15.setDepth(9)
resort.add(resortwindow15)

resortwindow16=Rectangle(25,30,Point(810,95))
resortwindow16.setFillColor("white")
resortwindow16.setDepth(9)
resort.add(resortwindow16)

resortwindow17=Rectangle(25,30,Point(840,95))
resortwindow17.setFillColor("white")
resortwindow17.setDepth(9)
resort.add(resortwindow17)

resortwindow18=Rectangle(25,30,Point(870,95))
resortwindow18.setFillColor("white")
resortwindow18.setDepth(9)

resortwindow19=Rectangle(25,30,Point(900,95))
resortwindow19.setFillColor("white")
resortwindow19.setDepth(9)
resort.add(resortwindow19)

resortwindow20=Rectangle(25,30,Point(930,95))
resortwindow20.setFillColor("white")
resortwindow20.setDepth(9)
resort.add(resortwindow20)

board=Rectangle(380,30,Point(740,-5))
board.setFillColor("darkgoldenrod")
board.setDepth(10)
resort.add(board)
resortfrontdoor1=Polygon(Point(740,32),Point(770,32),Point(780,40),Point(780,90),Point(740,90))
resortfrontdoor1.setFillColor("white")
resortfrontdoor1.setDepth(10)
resort.add(resortfrontdoor1)

resortfrontdoor2=Polygon(Point(700,40),Point(710,32),Point(740,32),Point(740,90),Point(700,90))
resortfrontdoor2.setFillColor("white")
resortfrontdoor2.setDepth(10)
resort.add(resortfrontdoor2)

resort1= resort.clone()
resort1.move(0, -80)
resort1.setDepth(10)
resort.add(resort1)

resort.move(1100,260)

#train stopper
kelaw=Layer()
boss.add(kelaw)

stick=Rectangle(15,140,Point(300,600))
stick.setFillColor("red")
kelaw.add(stick)

enat=Square(60,Point(300,500))
enat.setFillColor("orange")
kelaw.add(enat)

stick2=Rectangle(15,140,Point(560,100))
stick2.setFillColor("red")
kelaw.add(stick2)

enat2=Square(60,Point(560,200))
enat2.setFillColor("orange")
kelaw.add(enat2)

kelaw.move(200,180)




#hospital buildin 7
hospital=Layer()
f3=Polygon(Point(20,300),Point(80,120),Point(480,120),Point(450,300),Point(320,300),Point(340,240),Point(160,240),Point(140,300),Point(20,300))
f3.setFillColor("white")
hospital.add(f3)
g3=Polygon(Point(480,120),Point(468,350),Point(450,450),Point(320,450),Point(320,300),Point(450,300),Point(450,450))
g3.setFillColor("blue")
hospital.add(g3)
h3=Polygon(Point(20,300),Point(20,450),Point(140,450),Point(160,400),Point(160,240),Point(140,300),Point(140,450))
hospital.add(h3)
i3=Rectangle(118,150,Point(80,375))
i3.setFillColor("blue")
hospital.add(i3)
j3=Path(Point(160,400),Point(320,400))
hospital.add(j3)
k4=Polygon(Point(190,400),Point(100,600),Point(260,600),Point(320,400))
k4.setFillColor("black")
hospital.add(k4)
l4=Polygon(Point(20,315),Point(20,335),Point(140,335),Point(140,315))
l4.setFillColor("white")
hospital.add(l4)
m4=l4.clone()
m4.moveTo(20,350)
hospital.add(m4)
n4=m4.clone()
n4.moveTo(20,385)
hospital.add(n4)
o4=n4.clone()
o4.moveTo(20,420)
hospital.add(o4)
p4=l4.clone()
p4.scale(1.08)
p4.moveTo(320,315)
hospital.add(p4)
q4=p4.clone()
q4.moveTo(320,350)
hospital.add(q4)
r4=q4.clone()
r4.moveTo(320,385)
hospital.add(r4)
s4=r4.clone()
s4.moveTo(320,420)
hospital.add(s4)
boss.add(hospital)
#hospital's window
windowh=Polygon(Point(490,475),Point(490,385),Point(590,385),Point(590,475))
hospital.add(windowh)
windowh.scale(0.3)
windowh.moveTo(175,300)
windowh.setFillColor("white")
wi=windowh.clone()
wi.moveTo(230,300)
hospital.add(wi)
wii=windowh.clone()
wii.moveTo(285,300)
hospital.add(wii)
wi1=windowh.clone()
wi1.moveTo(285,350)
hospital.add(wi1)
wi2=windowh.clone()
wi2.moveTo(175,350)
hospital.add(wi2)
door1=Polygon(Point(260,285),Point(260,375),Point(310,375),Point(310,285))

door1.scale(0.7)
hospital.add(door1)
door1.setFillColor("white")
door1.moveTo(230,337)

hospital.move(2100,-70)

#screen
screen=Layer()
boss.add(screen)

zeng=Rectangle(50,200,Point(450,400))
zeng.setFillColor("gray")
zeng.setBorderColor("black")
zeng.setBorderWidth(5)
screen.add(zeng)

scr=Rectangle(400,200,Point(450,230))
scr.setFillColor("black")
scr.setBorderColor("white")
scr.setBorderWidth(10)
screen.add(scr)

screen.move(2400,-90)



# hospital tapella
hosp=Layer()
boss.add(hosp)
handler=Rectangle(15,100,Point(100,200))
handler.setFillColor("red")
hosp.add(handler)
ht=Rectangle(150,70,Point(100,150))
ht.setFillColor("yellow")
hosp.add(ht)

tx=Text("HOSPITAL",20,Point(96,150))
tx.setFontColor("brown")
tx.setDepth(40)
hosp.add(tx)

hosp.move(2470,170)

#tapella
tapela=Layer()
boss.add(tapela)
tape=Square(60,Point(1650,300))
tape.setFillColor("yellow")
tape.rotate(45)
tapela.add(tape)

zeng=Rectangle(10,100,Point(1650,380))
zeng.setFillColor("gray")
tapela.add(zeng)

# stop text
text1 = Text("STOP",18)
text1.move(1650,300)
text1.setDepth(30)
tapela.add(text1)
tapela.move(-250,0)






#trees
tree=Layer()
boss.add(tree)

gind=Rectangle(10,20,Point(350,310))
gind.setFillColor("OrangeRed")
gind.setBorderColor("OrangeRed")
tree.add(gind)


tr1=Polygon(Point(300,300),Point(350,170),Point(400,300))
tr1.setFillColor("DarkGreen")
tr1.setBorderColor("DarkGreen")
tree.add(tr1)

tr2=Polygon(Point(300,270),Point(350,140),Point(400,270))
tr2.setFillColor("DarkGreen")
tr2.setBorderColor("DarkGreen")
tree.add(tr2)

tr3=Polygon(Point(300,240),Point(350,110),Point(400,240))
tr3.setFillColor("DarkGreen")
tr3.setBorderColor("DarkGreen")
tree.add(tr3)

tree.move(500,650)

tree1=Layer()
boss.add(tree1)

gind=Rectangle(10,20,Point(350,310))
gind.setFillColor("OrangeRed")
gind.setBorderColor("OrangeRed")
tree1.add(gind)


tr1=Polygon(Point(300,300),Point(350,170),Point(400,300))
tr1.setFillColor("DarkGreen")
tr1.setBorderColor("DarkGreen")
tree1.add(tr1)

tr2=Polygon(Point(300,270),Point(350,140),Point(400,270))
tr2.setFillColor("DarkGreen")
tr2.setBorderColor("DarkGreen")
tree1.add(tr2)

tr3=Polygon(Point(300,240),Point(350,110),Point(400,240))
tr3.setFillColor("DarkGreen")
tr3.setBorderColor("DarkGreen")
tree1.add(tr3)

tree1.move(650,600)




tree1=Layer()
boss.add(tree1)

gind=Rectangle(10,20,Point(350,310))
gind.setFillColor("OrangeRed")
gind.setBorderColor("OrangeRed")
tree1.add(gind)


tr1=Polygon(Point(300,300),Point(350,170),Point(400,300))
tr1.setFillColor("DarkGreen")
tr1.setBorderColor("DarkGreen")
tree1.add(tr1)

tr2=Polygon(Point(300,270),Point(350,140),Point(400,270))
tr2.setFillColor("DarkGreen")
tr2.setBorderColor("DarkGreen")
tree1.add(tr2)

tr3=Polygon(Point(300,240),Point(350,110),Point(400,240))
tr3.setFillColor("DarkGreen")
tr3.setBorderColor("DarkGreen")
tree1.add(tr3)

tree1.move(800,650)




tree1=Layer()
boss.add(tree1)

gind=Rectangle(10,20,Point(350,310))
gind.setFillColor("OrangeRed")
gind.setBorderColor("OrangeRed")
tree1.add(gind)


tr1=Polygon(Point(300,300),Point(350,170),Point(400,300))
tr1.setFillColor("DarkGreen")
tr1.setBorderColor("DarkGreen")
tree1.add(tr1)

tr2=Polygon(Point(300,270),Point(350,140),Point(400,270))
tr2.setFillColor("DarkGreen")
tr2.setBorderColor("DarkGreen")
tree1.add(tr2)

tr3=Polygon(Point(300,240),Point(350,110),Point(400,240))
tr3.setFillColor("DarkGreen")
tr3.setBorderColor("DarkGreen")
tree1.add(tr3)

tree1.move(950,600)



tree1=Layer()
boss.add(tree1)

gind=Rectangle(10,20,Point(350,310))
gind.setFillColor("OrangeRed")
gind.setBorderColor("OrangeRed")
tree1.add(gind)


tr1=Polygon(Point(300,300),Point(350,170),Point(400,300))
tr1.setFillColor("DarkGreen")
tr1.setBorderColor("DarkGreen")
tree1.add(tr1)

tr2=Polygon(Point(300,270),Point(350,140),Point(400,270))
tr2.setFillColor("DarkGreen")
tr2.setBorderColor("DarkGreen")
tree1.add(tr2)

tr3=Polygon(Point(300,240),Point(350,110),Point(400,240))
tr3.setFillColor("DarkGreen")
tr3.setBorderColor("DarkGreen")
tree1.add(tr3)

tree1.move(1100,650)



tree1=Layer()
boss.add(tree1)

gind=Rectangle(10,20,Point(350,310))
gind.setFillColor("OrangeRed")
gind.setBorderColor("OrangeRed")
tree1.add(gind)


tr1=Polygon(Point(300,300),Point(350,170),Point(400,300))
tr1.setFillColor("DarkGreen")
tr1.setBorderColor("DarkGreen")
tree1.add(tr1)

tr2=Polygon(Point(300,270),Point(350,140),Point(400,270))
tr2.setFillColor("DarkGreen")
tr2.setBorderColor("DarkGreen")
tree1.add(tr2)

tr3=Polygon(Point(300,240),Point(350,110),Point(400,240))
tr3.setFillColor("DarkGreen")
tr3.setBorderColor("DarkGreen")
tree1.add(tr3)

tree1.move(1250,600)




tree1=Layer()
boss.add(tree1)

gind=Rectangle(10,20,Point(350,310))
gind.setFillColor("OrangeRed")
gind.setBorderColor("OrangeRed")
tree1.add(gind)


tr1=Polygon(Point(300,300),Point(350,170),Point(400,300))
tr1.setFillColor("DarkGreen")
tr1.setBorderColor("DarkGreen")
tree1.add(tr1)

tr2=Polygon(Point(300,270),Point(350,140),Point(400,270))
tr2.setFillColor("DarkGreen")
tr2.setBorderColor("DarkGreen")
tree1.add(tr2)

tr3=Polygon(Point(300,240),Point(350,110),Point(400,240))
tr3.setFillColor("DarkGreen")
tr3.setBorderColor("DarkGreen")
tree1.add(tr3)

tree1.move(1400,650)



tree1=Layer()
boss.add(tree1)

gind=Rectangle(10,20,Point(350,310))
gind.setFillColor("OrangeRed")
gind.setBorderColor("OrangeRed")
tree1.add(gind)


tr1=Polygon(Point(300,300),Point(350,170),Point(400,300))
tr1.setFillColor("DarkGreen")
tr1.setBorderColor("DarkGreen")
tree1.add(tr1)

tr2=Polygon(Point(300,270),Point(350,140),Point(400,270))
tr2.setFillColor("DarkGreen")
tr2.setBorderColor("DarkGreen")
tree1.add(tr2)

tr3=Polygon(Point(300,240),Point(350,110),Point(400,240))
tr3.setFillColor("DarkGreen")
tr3.setBorderColor("DarkGreen")
tree1.add(tr3)

tree1.move(1550,600)


tree1=Layer()
boss.add(tree1)

gind=Rectangle(10,20,Point(350,310))
gind.setFillColor("OrangeRed")
gind.setBorderColor("OrangeRed")
tree1.add(gind)


tr1=Polygon(Point(300,300),Point(350,170),Point(400,300))
tr1.setFillColor("DarkGreen")
tr1.setBorderColor("DarkGreen")
tree1.add(tr1)

tr2=Polygon(Point(300,270),Point(350,140),Point(400,270))
tr2.setFillColor("DarkGreen")
tr2.setBorderColor("DarkGreen")
tree1.add(tr2)

tr3=Polygon(Point(300,240),Point(350,110),Point(400,240))
tr3.setFillColor("DarkGreen")
tr3.setBorderColor("DarkGreen")
tree1.add(tr3)

tree1.move(1700,650)







#traffic lights
traffic=Layer()
boss.add(traffic)
r4=Rectangle(30,150,Point(900,500))
r4.setFillColor("Lavender")
r4.setDepth(-25)
traffic.add(r4)
r1=Circle(10,Point(900,450))
r1.setFillColor("black")
r1.setDepth(-25)
traffic.add(r1)
r2=Circle(10,Point(900,470))
r2.setDepth(-25)
r2.setFillColor("black")
traffic.add(r2)
r3=Circle(10,Point(900,490))
r3.setFillColor("black")
r3.setDepth(-25)
traffic.add(r3)

traffic.move(700,-130)




#check point

check=Layer()
boss.add(check)
p=Rectangle(200,152,Point(452,160))
p.setBorderWidth(3)
p.setFillColor("Tomato")
check.add(p)
tx=Text("CHECK POINT 1",20,Point(450,150))
tx.setFontColor("brown")
tx.setDepth(40)
check.add(tx)
das=Polygon(Point(552,236),Point(582,216),Point(582,64),Point(552,84))
das.setBorderWidth(3)
das.setFillColor("DarkOrange")
check.add(das)
za=Polygon(Point(567,34),Point(602,84),Point(540,120))
za.setBorderWidth(3)
za.setFillColor("burlywood4")
check.add(za)
va=Polygon(Point(540,120),Point(340,120),Point(367,34),Point(567,34))
va.setBorderWidth(3)
va.setFillColor("burlywood4")
check.add(va)


ta=Path(Point(452,145),Point(452,235))
ta.setBorderWidth(3)
ta.setDepth(4)
check.add(ta)
ne=Rectangle(5,10,Point(452,190))
ne.setFillColor("black")
ne.setDepth(4)
check.add(ne)
nt=Path(Point(452,190),Point(460,190))
nt.setBorderWidth(3)
nt.setDepth(4)
check.add(nt)

check.move(-100,630)


#train
train1=Layer()
boss.add(train1)

body1=Rectangle(80,130,Point(580,490))
body1.setFillColor("DarkOliveGreen")
train1.add(body1)

body2=Rectangle(80,130,Point(580,320))
body2.setFillColor("DarkOliveGreen")
train1.add(body2)

body3=Rectangle(80,130,Point(580,150))
body3.setFillColor("DarkOliveGreen")
train1.add(body3)

end1=Circle(40,Point(580,590))
end1.setFillColor("DarkOliveGreen")
train1.add(end1)

end2=Circle(40,Point(580,90))
end2.setFillColor("DarkOliveGreen")
train1.add(end2)

adi=Rectangle(80,50,Point(580,560))
adi.setFillColor("CadetBlue")
train1.add(adi)

adi2=Rectangle(80,60,Point(580,320))
adi2.setFillColor("CadetBlue")
train1.add(adi2)


adi1=Rectangle(80,50,Point(580,110))
adi1.setFillColor("CadetBlue")
train1.add(adi1)

sti=Rectangle(10,40,Point(565,235))
sti.setFillColor("black")
train1.add(sti)

sti1=Rectangle(10,40,Point(595,235))
sti1.setFillColor("black")
train1.add(sti1)

sti=Rectangle(10,40,Point(565,405))
sti.setFillColor("black")
train1.add(sti)

sti=Rectangle(10,40,Point(595,405))
sti.setFillColor("black")
train1.add(sti)

train1.move(0,-1000)





train2=Layer()
boss.add(train2)

body1=Rectangle(80,130,Point(680,490))
body1.setFillColor("DarkOliveGreen")
train2.add(body1)

body2=Rectangle(80,130,Point(680,320))
body2.setFillColor("DarkOliveGreen")
train2.add(body2)

body3=Rectangle(80,130,Point(680,150))
body3.setFillColor("DarkOliveGreen")
train2.add(body3)

end1=Circle(40,Point(680,590))
end1.setFillColor("DarkOliveGreen")
train2.add(end1)

end2=Circle(40,Point(680,90))
end2.setFillColor("DarkOliveGreen")
train2.add(end2)

adi=Rectangle(80,50,Point(680,560))
adi.setFillColor("CadetBlue")
train2.add(adi)

adi2=Rectangle(80,60,Point(680,320))
adi2.setFillColor("CadetBlue")
train2.add(adi2)


adi1=Rectangle(80,50,Point(680,110))
adi1.setFillColor("CadetBlue")
train2.add(adi1)

sti=Rectangle(10,40,Point(665,235))
sti.setFillColor("black")
train2.add(sti)

sti1=Rectangle(10,40,Point(695,235))
sti1.setFillColor("black")
train2.add(sti1)

sti=Rectangle(10,40,Point(665,405))
sti.setFillColor("black")
train2.add(sti)

sti=Rectangle(10,40,Point(695,405))
sti.setFillColor("black")
train2.add(sti)

train2.move(0,1000)


##small people
ppl1=Layer()
boss.add(ppl1)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
ppl1.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("blue")
ppl1.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("white")
leg1.setDepth(-20)
ppl1.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
ppl1.add(leg2)
ppl1.move(100,100)


#ppls cross the zebra on +y
ppl2=Layer()
boss.add(ppl2)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
ppl2.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("blue")
ppl2.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("Navy")
leg1.setDepth(-20)
ppl2.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
ppl2.add(leg2)
ppl2.move(1450,100)

ppl3=Layer()
boss.add(ppl3)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
ppl3.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("violet")
ppl3.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("white")
leg1.setDepth(-20)
ppl3.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
ppl3.add(leg2)
ppl3.move(1478,103)


ppl4=Layer()
boss.add(ppl4)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
ppl4.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("green")
ppl4.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("yellow")
leg1.setDepth(-20)
ppl4.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
ppl4.add(leg2)
ppl4.move(1488,91)


ppl5=Layer()
boss.add(ppl5)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
ppl5.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("purple")
ppl5.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("white")
leg1.setDepth(-20)
ppl5.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
ppl5.add(leg2)
ppl5.move(1504,107)

ppl6=Layer()
boss.add(ppl6)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
ppl6.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("black")
ppl6.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("white")
leg1.setDepth(-20)
ppl6.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
ppl6.add(leg2)
ppl6.move(1509,104)

ppl7=Layer()
boss.add(ppl7)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
ppl7.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("blue")
ppl7.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("black")
leg1.setDepth(-20)
ppl7.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
ppl7.add(leg2)
ppl7.move(1519,104)

ppl8=Layer()
boss.add(ppl8)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
ppl8.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("orange")
ppl8.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("red")
leg1.setDepth(-20)
ppl8.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
ppl8.add(leg2)
ppl8.move(1510,107)

#ppls cross zebra on -y
ppla=Layer()
boss.add(ppla)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
ppla.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("blue")
ppla.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("Navy")
leg1.setDepth(-20)
ppla.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
ppla.add(leg2)
ppla.move(1450,390)

pplb=Layer()
boss.add(pplb)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
pplb.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("violet")
pplb.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("white")
leg1.setDepth(-20)
pplb.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
pplb.add(leg2)
pplb.move(1478,393)


pplc=Layer()
boss.add(pplc)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
pplc.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("green")
pplc.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("yellow")
leg1.setDepth(-20)
pplc.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
pplc.add(leg2)
pplc.move(1488,391)


ppld=Layer()
boss.add(ppld)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
ppld.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("purple")
ppld.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("white")
leg1.setDepth(-20)
ppld.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
ppld.add(leg2)
ppld.move(1504,397)

pple=Layer()
boss.add(pple)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
pple.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("black")
pple.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("white")
leg1.setDepth(-20)
pple.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
pple.add(leg2)
pple.move(1509,394)

pplf=Layer()
boss.add(pplf)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
pplf.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("blue")
pplf.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("black")
leg1.setDepth(-20)
pplf.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
pplf.add(leg2)
pplf.move(1519,400)

pplg=Layer()
boss.add(pplg)
head=Circle(5, Point(10,270))
head.setDepth(-15)
head.setFillColor("Coral")
pplg.add(head)
body=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
body.setDepth(-25)
body.setFillColor("orange")
pplg.add(body)
leg1=Rectangle(5,15,Point(7,300))
leg1.setFillColor("red")
leg1.setDepth(-20)
pplg.add(leg1)
leg2=leg1.clone()
leg2.moveTo(10,300)
pplg.add(leg2)
pplg.move(1510,405)


# 3d car 2
cara1=Layer()
ac=Path(Point(110,400),Point(120,380),Point(160,380),Point(190,360),
           Point(230,360),Point(260,380),Point(300,380),Point(290,400))
ac.setBorderColor("yellow")
ad=Path(Point(300,380),Point(300,410),Point(290,430))
ab=Polygon(Point(110,400),Point(150,400),Point(180,380),Point(220,380),
           Point(250,400),Point(290,400),Point(290,430),Point(110,430))
ab.setBorderColor("yellow")
ab.setFillColor("blue")
ak=Polygon(Point(260,380),Point(300,380),Point(290,400),Point(250,400))
ak.setFillColor("blue")
ak.setBorderColor("yellow")           
af=Polygon(Point(190,360),Point(230,360),Point(220,380),Point(180,380))
af.setFillColor("white")
af.setBorderColor("yellow")
ah=Polygon(Point(120,380),Point(160,380),Point(150,400),Point(110,400))
ah.setFillColor("blue")
ah.setBorderColor("yellow")
ag=Path(Point(220,380),Point(180,380))
ag.setBorderColor("yellow")
ai=Path(Point(230,360),Point(190,360))
ai.setBorderColor("yellow")
tire1=Circle(10,Point(150,430))
tire1.setFillColor("gray")
tire2=Circle(10,Point(250,430))
tire2.setFillColor("gray")
cara1.add(ab)
cara1.add(ac)
cara1.add(ad)
cara1.add(af)
cara1.add(ag)
cara1.add(ah)
cara1.add(ak)           
cara1.add(ai)
cara1.add(tire1)
cara1.add(tire2)
city.add(cara1)
cara1.move(-350,200)





#bajaj movement
bajaj=Layer()
city.add(bajaj)
body=Polygon(Point(30,30), Point(130,30), Point(150,60), Point(150,100), Point(30,100))
body.setFillColor('transparent')
body.setDepth(60)
bajaj.add(body)
tire1=Circle(15,Point(50,100))
tire1.setFillColor('black')
bajaj.add(tire1)
tire2=Circle(15,Point(150,100))
tire2.setFillColor('black')
bajaj.add(tire2)
back=Polygon(Point(30,100), Point(30,30),Point(50,30), Point(50,60), Point(70,70), Point(70,100))
back.setFillColor('blue')
back.setDepth(60)
bajaj.add(back)
a=Rectangle(2,70, Point(90,65))
a.setFillColor('blue')
bajaj.add(a)
c=Polygon(Point(91,76), Point(121,76), Point(121,100), Point(116,100), Point(116,81), Point(91,81))
c.setFillColor('white')
bajaj.add(c)
tire1=Circle(10,Point(50,100))
tire1.setFillColor('darkgray')
tire1.setDepth(25)
bajaj.add(tire1)
tire2=Circle(10,Point(150,100))
tire2.setFillColor('darkgray')
bajaj.add(tire2)
d=Rectangle(20,30, Point(40,45))
d.setFillColor('white')
bajaj.add(d)
e=Polygon(Point(150,65), Point(160,72), Point(163,90), Point(150,85))
e.setFillColor('blue')
bajaj.add(e)
 
bajaj.move(0,540)




# 3d car
cara=Layer()
ac=Path(Point(110,400),Point(120,380),Point(160,380),Point(190,360),
           Point(230,360),Point(260,380),Point(300,380),Point(290,400))
ac.setBorderColor("yellow")
ad=Path(Point(300,380),Point(300,410),Point(290,430))
ab=Polygon(Point(110,400),Point(150,400),Point(180,380),Point(220,380),
           Point(250,400),Point(290,400),Point(290,430),Point(110,430))
ab.setBorderColor("yellow")
ab.setFillColor("blue")
ak=Polygon(Point(260,380),Point(300,380),Point(290,400),Point(250,400))
ak.setFillColor("blue")
ak.setBorderColor("yellow")           
af=Polygon(Point(190,360),Point(230,360),Point(220,380),Point(180,380))
af.setFillColor("white")
af.setBorderColor("yellow")
ah=Polygon(Point(120,380),Point(160,380),Point(150,400),Point(110,400))
ah.setFillColor("blue")
ah.setBorderColor("yellow")
ag=Path(Point(220,380),Point(180,380))
ag.setBorderColor("yellow")
ai=Path(Point(230,360),Point(190,360))
ai.setBorderColor("yellow")
tire1=Circle(10,Point(150,430))
tire1.setFillColor("gray")
tire2=Circle(10,Point(250,430))
tire2.setFillColor("gray")
cara.add(ab)
cara.add(ac)
cara.add(ad)
cara.add(af)
cara.add(ag)
cara.add(ah)
cara.add(ak)           
cara.add(ai)
cara.add(tire1)
cara.add(tire2)
cara.move(1600,70)
city.add(cara)



#taxi
taxi=Layer()
city.add(taxi)
body=Rectangle(200,50,Point(300,300))
body.setFillColor("yellow")
taxi.add(body)

side=Rectangle(300,50,Point(300,350))
side.setFillColor("yellow")
side.setBorderColor("yellow")
taxi.add(side)


wheel1=Circle(25,Point(200,380))
wheel1.setFillColor("black")
taxi.add(wheel1)

inside1=Circle(20,Point(200,380))
inside1.setFillColor("white")
taxi.add(inside1)


wheel2=Circle(25,Point(400,380))
wheel2.setFillColor("black")
taxi.add(wheel2)

inside2=Circle(20,Point(400,380))
inside2.setFillColor("white")
taxi.add(inside2)


sign=Polygon(Point(100,100),Point(125,75),Point(175,75),Point(200,100))
sign.setFillColor("yellow")
taxi.add(sign)
sign.move(150,175)


txt=Text("TAXI",18,Point(300,262))
taxi.add(txt)

door=Rectangle(50,75,Point(260,320))
door.setBorderWidth(3)
taxi.add(door)


door1=Rectangle(50,75,Point(340,320))
door1.setBorderWidth(3)
taxi.add(door1)


adu=Circle(32,Point(300,326))
adu.setFillColor("yellow")
taxi.add(adu)

adu2=Rectangle(60,30,Point(300,350))
adu2.setFillColor("yellow")
adu2.setBorderColor("yellow")
taxi.add(adu2)

mid=Rectangle(26,20,Point(299,300))
mid.setFillColor("yellow")
mid.setBorderColor("yellow")
taxi.add(mid)


taxi.move(700,130)




# street lights
light=Layer()
boss.add(light)
bulb1=Path(Point(220,480),Point(220,400),Point(270,405))
bulb1.setBorderWidth(6)
bulb1.setBorderColor("blue")
bulb1.setDepth(5)
light.add(bulb1)
bulb2=Path(Point(420,480),Point(420,400),Point(470,405))
bulb2.setBorderWidth(6)
bulb2.setBorderColor("blue")
bulb2.setDepth(5)
light.add(bulb2)
bulb3=Path(Point(595,480),Point(595,400),Point(645,405))
bulb3.setBorderWidth(6)
bulb3.setBorderColor("blue")
bulb3.setDepth(5)
light.add(bulb3)
bulb4=Path(Point(820,480),Point(820,400),Point(870,405))
bulb4.setBorderWidth(6)
bulb4.setBorderColor("blue")
bulb4.setDepth(5)
light.add(bulb4)
bulb5=Path(Point(1020,480),Point(1020,400),Point(1070,405))
bulb5.setBorderWidth(6)
bulb5.setBorderColor("blue")
bulb5.setDepth(5)
light.add(bulb5)
bulb6=Path(Point(1240,480),Point(1240,400),Point(1270,405))
bulb6.setBorderWidth(6)
bulb6.setBorderColor("blue")
bulb6.setDepth(5)
light.add(bulb6)
b2=bulb1.clone()
b2.moveTo(20,250)
light.add(b2)
b3=bulb1.clone()
b3.moveTo(390,250)
light.add(b3)
b4=bulb1.clone()
b4.moveTo(533,250)
light.add(b4)
b1=bulb1.clone()
b1.moveTo(220,250)
light.add(b1)
b5=bulb1.clone()
b5.moveTo(880,250)
light.add(b5)
b6=bulb1.clone()
b6.moveTo(1050,250)
light.add(b6)
b7=bulb1.clone()
b7.moveTo(1220,250)
light.add(b7)
b8=bulb3.clone()
b8.moveTo(20,480)
light.add(b8)
t1=Circle(7,Point(270,410))
t1.setDepth(4)
t1.setFillColor("yellow")
t1.setBorderColor("yellow")
light.add(t1)
t2=Circle(7,Point(470,410))
t2.setDepth(4)
t2.setFillColor("yellow")
t2.setBorderColor("yellow")
light.add(t2)
t3=Circle(7,Point(645,410))
t3.setDepth(4)
t3.setFillColor("yellow")
t3.setBorderColor("yellow")
light.add(t3)
t4=Circle(7,Point(870,410))
t4.setDepth(4)
t4.setFillColor("yellow")
t4.setBorderColor("yellow")
light.add(t4)
t5=Circle(7,Point(1070,410))
t5.setDepth(5)
t5.setFillColor("yellow")
t5.setBorderColor("yellow")
light.add(t5)
t6=Circle(7,Point(1270,410))
t6.setDepth(6)
t6.setFillColor("yellow")
t6.setBorderColor("yellow")
light.add(t6)
t7=Circle(7,Point(70,410))
t7.setDepth(4)
t7.setFillColor("yellow")
t7.setBorderColor("yellow")
light.add(t7)
t8=Circle(7,Point(70,180))
t8.setDepth(4)
t8.setFillColor("yellow")
t8.setBorderColor("yellow")
light.add(t8)
t10=Circle(7,Point(270,180))
t10.setDepth(4)
t10.setFillColor("yellow")
t10.setBorderColor("yellow")
light.add(t10)
t11=Circle(7,Point(440,180))
t11.setDepth(4)
t11.setFillColor("yellow")
t11.setBorderColor("yellow")
light.add(t11)
t12=Circle(7,Point(583,180))
t12.setDepth(4)
t12.setFillColor("yellow")
t12.setBorderColor("yellow")
light.add(t12)
t13=Circle(7,Point(930,180))
t13.setDepth(4)
t13.setFillColor("yellow")
t13.setBorderColor("yellow")
light.add(t13)
t9=Circle(7,Point(1100,180))
t9.setDepth(4)
t9.setFillColor("yellow")
t9.setBorderColor("yellow")
light.add(t9)
t14=Circle(7,Point(1270,180))
t14.setDepth(4)
t14.setFillColor('yellow')
t14.setBorderColor("yellow")
light.add(t14)

light.move(100,190)



#traffic lights ye adebabau
traffic2=Layer()
boss.add(traffic2)
rd=Rectangle(30,150,Point(900,500))
rd.setFillColor("Lavender")
rd.setDepth(-25)
traffic2.add(rd)
ra=Circle(10,Point(900,450))
ra.setFillColor("black")
ra.setDepth(-25)
traffic2.add(ra)
rb=Circle(10,Point(900,470))
rb.setDepth(-25)
rb.setFillColor("black")
traffic2.add(rb)
rc=Circle(10,Point(900,490))
rc.setFillColor("black")
rc.setDepth(-25)
traffic2.add(rc)

traffic2.move(2140,210)


#traffic lights ye adebabau 3
traffic3=Layer()
boss.add(traffic3)
rh=Rectangle(30,150,Point(900,500))
rh.setFillColor("Lavender")
rh.setDepth(-25)
traffic3.add(rh)
re=Circle(10,Point(900,450))
re.setFillColor("black")
re.setDepth(-25)
traffic3.add(re)
rf=Circle(10,Point(900,470))
rf.setDepth(-25)
rf.setFillColor("black")
traffic3.add(rf)
rg=Circle(10,Point(900,490))
rg.setFillColor("black")
rg.setDepth(-25)
traffic3.add(rg)

traffic3.move(2680,-160)





#traffic lights ye adebabau 4
traffic4=Layer()
boss.add(traffic4)
rw=Rectangle(30,150,Point(900,500))
rw.setFillColor("Lavender")
rw.setDepth(-25)
traffic4.add(rw)
rx=Circle(10,Point(900,450))
rx.setFillColor("black")
rx.setDepth(-25)
traffic4.add(rx)
ry=Circle(10,Point(900,470))
ry.setDepth(-25)
ry.setFillColor("black")
traffic4.add(ry)
rz=Circle(10,Point(900,490))
rz.setFillColor("black")
rz.setDepth(-25)
traffic4.add(rz)

traffic4.move(2140,-160)


#traffic lights ye adebabau 5
traffic5=Layer()
boss.add(traffic5)
rs=Rectangle(30,150,Point(900,500))
rs.setFillColor("Lavender")
rs.setDepth(-25)
traffic5.add(rs)
rt=Circle(10,Point(900,450))
rt.setFillColor("black")
rt.setDepth(-25)
traffic5.add(rt)
ru=Circle(10,Point(900,470))
ru.setDepth(-25)
ru.setFillColor("black")
traffic5.add(ru)
rv=Circle(10,Point(900,490))
rv.setFillColor("black")
rv.setDepth(-25)
traffic5.add(rv)

traffic5.move(2680,210)





for i in range (95):
    bird1.flip (90)
    bird2.flip(90)
    bird3.flip(90)
    bird4.flip(90)
    bird5.flip(90)
    bird6.flip(90)
    
    bird1.move(-20,0)
    bird2.move(-10,0)
    bird3.move(-20,0)
    bird4.move(-10,0)
    bird5.move(-10,0)
    bird6.move(-20,0)
    
    
    bird1.scale(0.95)
    bird2.scale(0.95)
    bird3.scale(0.95)
    bird4.scale(0.95)
    bird5.scale(0.95)
    bird6.scale(0.95)
    time.sleep (0.1)




    bajaj.move(11,0)
    cara.move(-12,0)
    taxi.move(-11,0)
    cara1.move(12,0)

for i in range(100):
    bajaj.move(25,0)
    cara1.move(29,0)
    cara.move(-20,0)
    taxi.move(-15,0)

    

#lemozin
lemozin=Layer()
city.add(lemozin)
body=Rectangle(230,80,Point(300,300))
body.setFillColor("white")
lemozin.add(body)

side=Rectangle(300,50,Point(300,340))
side.setFillColor("white")
lemozin.add(side)

shade=Ellipse(20,50,Point(450,340))
shade.setFillColor("white")
shade.setBorderColor("white")
lemozin.add(shade)

shade1=Ellipse(20,50,Point(150,340))
shade1.setFillColor("white")
shade1.setBorderColor("white")
lemozin.add(shade1)

wheel1=Circle(30,Point(220,378))
wheel1.setFillColor("black")
lemozin.add(wheel1)

whe=Circle(20,Point(220,378))
whe.setFillColor("white")
lemozin.add(whe)

wheel2=Circle(30,Point(390,378))
wheel2.setFillColor("black")
lemozin.add(wheel2)

whe2=Circle(20,Point(390,378))
whe2.setFillColor("white")
lemozin.add(whe2)

she=Rectangle(226,10,Point(300,318))
she.setFillColor("white")
she.setBorderColor("white")
lemozin.add(she)


win1=Square(40,Point(380,290))
win1.setFillColor("sky blue")
lemozin.add(win1)

win1=Square(40,Point(330,290))
win1.setFillColor("sky blue")
lemozin.add(win1)

win1=Square(40,Point(280,290))
win1.setFillColor("sky blue")
lemozin.add(win1)

win1=Square(40,Point(225,290))
win1.setFillColor("sky blue")
lemozin.add(win1)


lemozin.move(1070,110)




#lada

lada=Layer()
boss.add(lada)
body1=Rectangle(150,50,Point(300,300))
body1.setFillColor("white")
lada.add(body1)

side1=Rectangle(220,50,Point(300,350))
side1.setFillColor("MediumBlue")
side1.setBorderColor("MediumBlue")
lada.add(side1)


wheel3=Circle(25,Point(240,380))
wheel3.setFillColor("black")
lada.add(wheel3)

inside3=Circle(20,Point(240,380))
inside3.setFillColor("white")
lada.add(inside3)


wheel3=Circle(25,Point(360,380))
wheel3.setFillColor("black")
lada.add(wheel3)

inside3=Circle(20,Point(360,380))
inside3.setFillColor("white")
lada.add(inside3)


door3=Rectangle(50,75,Point(260,320))
door3.setBorderWidth(3)
lada.add(door3)


door4=Rectangle(50,75,Point(340,320))
door4.setBorderWidth(3)
lada.add(door4)


adu3=Circle(32,Point(300,326))
adu3.setFillColor("MediumBlue")
lada.add(adu3)

adu4=Rectangle(60,30,Point(300,350))
adu4.setFillColor("MediumBlue")
adu4.setBorderColor("MediumBlue")
lada.add(adu4)

mid1=Rectangle(26,20,Point(299,300))
mid1.setFillColor("white")
mid1.setBorderColor("white")
lada.add(mid1)

lada.move(1770,120)



#truck
truck=Layer()
city.add(truck)

body=Rectangle(250,130,Point(300,285))
body.setFillColor("red")
truck.add(body)

front=Polygon(Point(120,100),Point(200,100),Point(240,140),Point(280,140),Point(280,200),Point(120,200))
front.setFillColor("blue")
truck.add(front)
front.move(330,150)


hand=Rectangle(24,10,Point(437,345))
hand.setFillColor("black")
truck.add(hand)

glass=Polygon(Point(100,100),Point(160,100),Point(200,135),Point(100,135))
glass.setFillColor("sky blue")
glass.move(360,157)
truck.add(glass)

wheel1=Circle(35,Point(220,370))
wheel1.setFillColor("black")
truck.add(wheel1)

wheel1=Circle(28,Point(220,370))
wheel1.setFillColor("white")
truck.add(wheel1)


wheel2=Circle(35,Point(340,370))
wheel2.setFillColor("black")
truck.add(wheel2)

wheel2=Circle(28,Point(340,370))
wheel2.setFillColor("white")
truck.add(wheel2)

wheel2=Circle(35,Point(540,370))
wheel2.setFillColor("black")
truck.add(wheel2)

wheel2=Circle(28,Point(540,370))
wheel2.setFillColor("white")
truck.add(wheel2)
truck.move(-600,230)





#autobus
autobus=Layer()
city.add(autobus)
body=Polygon(Point(250,290),Point(426,290),Point(468,340),Point(510,340),Point(510,390),Point(250,390))
body.setFillColor("Blue")
autobus.add(body)

wheel1=Circle(25,Point(300,400))
wheel1.setFillColor("black")
autobus.add(wheel1)

ins1=Circle(20,Point(300,400))
ins1.setFillColor("white")
autobus.add(ins1)

wheel2=Circle(25,Point(445,400))
wheel2.setFillColor("black")
autobus.add(wheel2)

ins2=Circle(20,Point(445,400))
ins2.setFillColor("white")
autobus.add(ins2)

glass1=Polygon(Point(90,100),Point(115,100),Point(150,140),Point(90,140))
glass1.setFillColor("PowderBlue")
autobus.add(glass1)
glass1.move(300,200)

win1=Square(40,Point(365,320))
win1.setFillColor("PowderBlue")
autobus.add(win1)

win1=Square(40,Point(320,320))
win1.setFillColor("PowderBlue")
autobus.add(win1)

win1=Square(40,Point(275,320))
win1.setFillColor("PowderBlue")
autobus.add(win1)
autobus.move(-470,230)



#motor cycle
motor=Layer()
boss.add(motor)

body=Rectangle(180,40,Point(300,300))
body.setFillColor("Lavender")
motor.add(body)

wheel=Circle(26,Point(360,335))
wheel.setFillColor("black")
motor.add(wheel)

ins=Circle(22,Point(360,335))
ins.setFillColor("Lavender")
motor.add(ins)

wheel1=Circle(26,Point(240,335))
wheel1.setFillColor("black")
motor.add(wheel1)

ins1=Circle(22,Point(240,335))
ins1.setFillColor("Lavender")
motor.add(ins1)

mekemecha=Rectangle(27,70,Point(377,245))
mekemecha.setFillColor("Lavender")
motor.add(mekemecha)

meri=Rectangle(14,45,Point(220,256))
meri.setFillColor("Lavender")
motor.add(meri)

meri1=Rectangle(50,10,Point(253,238))
meri1.setFillColor("Lavender")
motor.add(meri1)


sew=Rectangle(24,60,Point(340,252))
sew.setFillColor("red")
motor.add(sew)

leg=Rectangle(60,10,Point(322,277))
leg.setFillColor("blue")
motor.add(leg)

leg2=Rectangle(10,40,Point(312,293))
leg2.setFillColor("blue")
leg2.rotate(320)
motor.add(leg2)

eg=Rectangle(60,6,Point(305,240))
eg.setFillColor("red")
motor.add(eg)

head=Circle(15,Point(341,203))
head.setFillColor("PeachPuff")
motor.add(head)

motor.move(3800,170)







# cars for vertical
carz=Layer()
boss.add(carz)
body=Square(80,Point(300,300))
body.setFillColor("red")
carz.add(body)

front=Rectangle(80,40,Point(300,240))
front.setFillColor("blue")
carz.add(front)

back=Rectangle(80,40,Point(300,360))
back.setFillColor("blue")
carz.add(back)
carz.move(3090,600)

# cars for vertical 2
carz1=Layer()
boss.add(carz1)
body=Square(80,Point(300,300))
body.setFillColor("white")
carz1.add(body)

front=Rectangle(80,40,Point(300,240))
front.setFillColor("green")
carz1.add(front)

back=Rectangle(80,40,Point(300,360))
back.setFillColor("green")
carz1.add(back)

carz1.move(2940,-400)


for i in range(100):
    autobus.move(4,0)
    lemozin.move(-4,0)
    truck.move(4,0)
    
#closing the train gate
for i in range(50):
    stick.move(0,-3)
    stick2.move(0,3)
    time.sleep (0.1)


for i in range(700):
    train1.move(0,3)
    train2.move(0,-3)
    
#opening the trains gate
for i in range(30):
    stick.move(0,3)
    stick2.move(0,-3)
    time.sleep (0.1)

#canvas moving
for i in range(100):
    boss.move(-6,0)
    lemozin.move(-17,0)

for i in range(100):
    autobus.move(4,0)
    truck.move(3,0)
    lada.move(-4,0)


for i in range(750):
    r1.setFillColor("red")
for i in range(100):
    ppl2.move(0,3)
    ppla.move(0,-3)
    ppl3.move(0,3)
    pplb.move(0,-3)
    ppl4.move(0,3)
    pplc.move(0,-3)
    ppl5.move(0,3)
    ppld.move(0,-3)
    ppl6.move(0,3)
    pple.move(0,-3)
    ppl7.move(0,3)
    pplf.move(0,-3)
    ppl8.move(0,3)
    pplg.move(0,-3)
    
    


    
    
r1.setFillColor("black")
for i in range(800):
    r2.setFillColor("yellow")
r2.setFillColor("black")
for i in range(750):
    r3.setFillColor("green")



for i in range(100):
     ppl2.move(3,0)
     ppl2.move(-3,0)
     ppld.move(-3,0)
     ppla.move(3,0)
     ppl4.move(3,0)
     pplb.move(-3,0)
     ppl5.move(-3,0)
     pplc.move(3,0)
     ppl6.move(3,0)



#lemozin
lemozin2=Layer()
boss.add(lemozin2)
body=Rectangle(230,80,Point(300,300))
body.setFillColor("white")
lemozin2.add(body)

side=Rectangle(300,50,Point(300,340))
side.setFillColor("white")
lemozin2.add(side)

shade=Ellipse(20,50,Point(450,340))
shade.setFillColor("white")
shade.setBorderColor("white")
lemozin2.add(shade)

shade1=Ellipse(20,50,Point(150,340))
shade1.setFillColor("white")
shade1.setBorderColor("white")
lemozin2.add(shade1)

wheel1=Circle(30,Point(220,378))
wheel1.setFillColor("black")
lemozin2.add(wheel1)

whe=Circle(20,Point(220,378))
whe.setFillColor("white")
lemozin2.add(whe)

wheel2=Circle(30,Point(390,378))
wheel2.setFillColor("black")
lemozin2.add(wheel2)

whe2=Circle(20,Point(390,378))
whe2.setFillColor("white")
lemozin2.add(whe2)

she=Rectangle(226,10,Point(300,318))
she.setFillColor("white")
she.setBorderColor("white")
lemozin2.add(she)


win1=Square(40,Point(380,290))
win1.setFillColor("sky blue")
lemozin2.add(win1)

win1=Square(40,Point(330,290))
win1.setFillColor("sky blue")
lemozin2.add(win1)

win1=Square(40,Point(280,290))
win1.setFillColor("sky blue")
lemozin2.add(win1)

win1=Square(40,Point(225,290))
win1.setFillColor("sky blue")
lemozin2.add(win1)
lemozin2.move(2400,100)


for i in range(150):
    lada.move(-19,0)
    boss.move(-10,0)
    lemozin2.move(-9,0)


for i in range(750):
    ra.setFillColor("red")
    re.setFillColor("red")    


for i in range(85):
    boss.move(-3,0)
    autobus.move(-3,0)
    truck.move(-3,0)
    motor.move(-5,0)

for i in range(750):
    rz.setFillColor("green")
    rv.setFillColor("green")



for i in range(100):
    carz.move(0,-2)
for i in range(650):
    carz1.move(0,0.7)
for i in range (300):
    carz.move(0.5,-0.5)
    carz1.move(-0.5,0.5)
for i in range (350):
    carz.move(-0.5,-0.5)
    carz1.move(0.5,0.5)
for i in range(900):
    carz.move(0,-0.5)
    carz1.move(0,0.5)


rz.setFillColor("black")
rv.setFillColor("black")
ra.setFillColor("black")
re.setFillColor("black")
for i in range(800):
    ry.setFillColor("yellow")
    ru.setFillColor("yellow")
ry.setFillColor("black")
ru.setFillColor("black")
for i in range(750):
    rx.setFillColor("red")
    rt.setFillColor("red")
rx.setFillColor("black")
rt.setFillColor("black")



for i in range(800):
    rb.setFillColor("yellow")
    rf.setFillColor("yellow")
rb.setFillColor("black")
rf.setFillColor("black")
for i in range(800):
    ra.setFillColor("green")
    re.setFillColor("green")


for i in range(100):
    motor.move(-3.5,-2)
    autobus.move(3.5,2)
for i in range(100):
     motor.move(-3.7,2)
     autobus.move(3.7,-2)

for i in range(170):
     motor.move(-3.7,0)
     autobus.move(3.7,0)

for i in range(140):
    truck.move(1,0)

for i in range(100):
    truck.move(3.5,2)
for i in range(100):
     truck.move(3.7,-2)
for i in range(180):
    truck.move(3,0)


ra.setFillColor("black")
re.setFillColor("black")











medemer=Layer()
boss.add(medemer)

#helicopter
h=Layer()
e=Ellipse(200,100,Point(500,300))
e.setFillColor('DarkRed')
h.add(e)
v=Path(Point(490,225),Point(360,225))
v.setDepth(-5)
v.setBorderWidth(10)
v.setBorderColor('dark gray')
h.add(v)

v2=Path(Point(490,225),Point(630,225))
v2.setDepth(-5)
v2.setBorderWidth(10)
v2.setBorderColor('dark gray')
h.add(v2)

v3=Path(Point(490,225),Point(360,225))
v3.setDepth(-5)
v3.setBorderWidth(10)
v3.setBorderColor('dark gray')
h.add(v3)

v4=Path(Point(490,225),Point(630,225))
v4.setDepth(-5)
v4.setBorderWidth(10)
v4.setBorderColor('dark gray')

h.add(v4)

se=Ellipse(180,80,Point(500,300))
se.setFillColor('black')
h.add(se)
p=Polygon(Point(500,250),Point(300,250),Point(275,200),Point(250,200),Point(250,270),Point(400,300),Point(435,335),Point(500,350))
p.setFillColor('DarkRed')
p.setBorderColor('DarkRed')
h.add(p)
k=Polygon(Point(525,250),Point(510,225),Point(475,225),Point(450,250))
k.setFillColor('DarkRed')
h.add(k)
g=Path(Point(420,300),Point(490,300))
g.setBorderWidth(5)
g.setDepth(1)
h.add(g)
l=Path(Point(500,300),Point(590,300))
l.setBorderWidth(5)
h.add(l)
j=Path(Point(440,340),Point(420,380),Point(530,380),Point(550,340))
j.setBorderWidth(5)
h.add(j)
gt=Path(Point(445,340),Point(470,370),Point(580,370),Point(560,340))
gt.setBorderWidth(5)
h.add(gt)
d=Polygon(Point(490,340),Point(490,260),Point(420,260),Point(420,300),Point(450,340),Point(490,340))
d.setFillColor('black')
h.add(d)
##lt=Ellipse(270,40,Point(490,225))
##lt.setFillColor('gray')
##
##h.add(lt)
s=Ellipse(50,10,Point(490,225))
s.setFillColor('DarkRed')
s.setDepth(-5)
h.add(s)

r=Layer()
b=Circle(30,Point(260,250))
b.setFillColor('white')
b.setBorderWidth(8)
b.setBorderColor('DarkRed')
r.add(b)
m=Path(Point(260,250),Point(260,280))
m.setBorderWidth(8)
m.setBorderColor('dark gray')
r.add(m)
n=Path(Point(260,250),Point(260,220))
n.setBorderColor('dark gray')
n.setBorderWidth(8)
r.add(n)
o=Path(Point(260,250),Point(290,250))
o.setBorderColor('dark gray')
o.setBorderWidth(8)
r.add(o)
w=Path(Point(260,250),Point(230,250))
w.setBorderColor('dark gray')
w.setBorderWidth(8)
r.add(w)
h.add(r)
h.setDepth(-15)

medemer.add(h)





#group member
group=Layer()
a=Rectangle(530,300,Point(700,1300))
a.setFillColor("blue")
a.setBorderColor("blue")
group.add(a)
semu1=Text('GROUP 16',22,Point(700,1100))
semu1.setFontColor("white")
group.add(semu1)
semu2=Text('GROUP MEMBERS',22,Point(700,1185))
semu2.setFontColor("white")
group.add(semu2)
semu3=Text('No                 NAME                                        ID No',16,
         Point(690,1208))
semu3.setFontColor("white")
group.add(semu3)
medemer.add(group)
fikru=Text('1-   Fikremariam Dessalegn             UGR/19542/12 ',18,
         Point(690,1225))
fikru.setFontColor("white")
group.add(fikru)
myk=Text('2-   Remzi Mehdi                              UGR/19983/12 ',18,
         Point(690,1245))
myk.setFontColor("white")
group.add(myk)
mel=Text('3-   Abriham Aneteneh                      UGR/19920/12',18,
         Point(690,1265))
mel.setFontColor("white")
group.add(mel)
nao=Text('4-   Yordanos Fikre                         UGR/20046/12',18,
         Point(690,1285))
nao.setFontColor("white")
group.add(nao)
sem=Text('5-   Elias Beyene                            UGR/20525/12 ',18,
         Point(690,1305))
sem.setFontColor("white")
group.add(sem)

semu2=Text('Submition date: Dec 31,2020 G.C.',16,
         Point(780,1395))
semu2.setFontColor("white")
group.add(semu2)
semu4=Text('Project1 For ASTU Department of COMPUTING',18,Point(680,1425))
semu4.setFontColor("white")
medemer.add(semu4)

group.move(-900,-1000)


#senselet
senselet=Layer()
medemer.add(senselet)


chain1=Ellipse(22,10,Point(300,300))
chain1.setFillColor("white")
senselet.add(chain1)

chain2=Rectangle(17,5,Point(317,300))
chain2.setFillColor("black")
senselet.add(chain2)

chain3=Ellipse(22,10,Point(330,300))
chain3.setFillColor("white")
senselet.add(chain3)

chain4=Rectangle(17,5,Point(348,300))
chain4.setFillColor("black")
senselet.add(chain4)

chain3=Ellipse(22,10,Point(358,300))
chain3.setFillColor("white")
senselet.add(chain3)

chain4=Rectangle(17,5,Point(375,300))
chain4.setFillColor("black")
senselet.add(chain4)

chain1=Ellipse(22,10,Point(390,300))
chain1.setFillColor("white")
senselet.add(chain1)

chain2=Rectangle(17,5,Point(405,300))
chain2.setFillColor("black")
senselet.add(chain2)

chain3=Ellipse(22,10,Point(420,300))
chain3.setFillColor("white")
senselet.add(chain3)

chain4=Rectangle(17,5,Point(435,300))
chain4.setFillColor("black")
senselet.add(chain4)

chain3=Ellipse(22,10,Point(450,300))
chain3.setFillColor("white")
senselet.add(chain3)

chain4=Rectangle(17,5,Point(465,300))
chain4.setFillColor("black")
senselet.add(chain4)

senselet.move(-228,-50)
for i in range(20):
    b.setFillColor('gray')
    m.setBorderColor('black')
    n.setBorderColor('black')
    o.setBorderColor('black')
    p.setBorderColor('black')
    medemer.move(0.5,-2)
    h.rotate(0.09)
    v.rotate(100000)
    v2.rotate(100000)
    v3.rotate(-100000)
    v4.rotate(-100000)
    m.rotate(1000)
    n.rotate(1000)
    o.rotate(1000)
    w.rotate(1000)


  
for i in range(93):
    b.setFillColor('gray')
    m.setBorderColor('black')
    n.setBorderColor('black')
    o.setBorderColor('black')
    p.setBorderColor('black')
    medemer.move(20,0)
    v.rotate(100000)
    v2.rotate(100000)
    v3.rotate(-100000)
    v4.rotate(-100000)
    m.rotate(1000)
    n.rotate(1000)
    o.rotate(1000)
    w.rotate(1000)

for i in range(300):
    b.setFillColor('gray')
    m.setBorderColor('black')
    n.setBorderColor('black')
    o.setBorderColor('black')
    p.setBorderColor('black')
    medemer.move(5,0)
    v.rotate(100000)
    v2.rotate(100000)
    v3.rotate(-100000)
    v4.rotate(-100000)
    m.rotate(1000)
    n.rotate(1000)
    o.rotate(1000)
    w.rotate(1000)


for i in range(150):

    senselet.move(0,2)    
    b.setFillColor('gray')
    m.setBorderColor('black')
    n.setBorderColor('black')
    o.setBorderColor('black')
    p.setBorderColor('black')
    h.move(3,0)
    v.rotate(100000)
    v2.rotate(100000)
    v3.rotate(-100000)
    v4.rotate(-100000)
    m.rotate(1000)
    n.rotate(1000)
    o.rotate(1000)
    w.rotate(1000)


#gratitude
thank=Text("THANK YOU FOR WATCHING ",0.80,Point(3370,450))
boss.add(thank)
thank.setDepth(-10000)
thank.setFontColor("OrangeRed")
for i in range(400):
    thank.scale(1.01)
time.sleep(2)










































