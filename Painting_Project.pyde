def setup():
    size(800, 800)
    background(255)

    
    #darkgreen
    fill(0, 100, 0)
    rect(250, 100, 50, 50)
    
    #darkolivegreen
    fill(85, 107, 47)
    rect(250, 150, 50, 50)
    
    #randomcolor
    fill(random(255), random(255), random(255))
    rect(250, 250, 50, 50)
    
    #eraser
    fill(255)
    rect(250, 300, 50, 50)
    
    
    
def draw():
    if mousePressed and mouseX > 50:
        strokeWeight(10)
        line(mouseX, mouseY, pmouseX, pmouseY)
    
def mouseClicked():
    if mouseClicked:
        if mouseX > 250 and mouseX < 300 and mouseY > 0 and mouseY < 100:
            stroke(0,100,0)
    if mouseClicked:
        if mouseX > 250 and mouseX < 300 and mouseY > 200 and mouseY < 250:
            stroke(85, 107, 47)
    if mouseClicked:
        if mouseX > 250 and mouseX < 300 and mouseY > 250 and mouseY < 300:
            stroke(random(255), random(255), random(255))
    if mouseClicked:
        if mouseX > 250 and mouseX < 300 and mouseY > 300 and mouseY < 350:
            stroke(255)
