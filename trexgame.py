import sys

from random import randint
from random import choice

import pygame
from pygame.locals import *
 
pygame.init()

 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 900, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("T-Rex ahead!")

icon = pygame.image.load("icon.ico")
pygame.display.set_icon(icon)
# surfaces and rectangles

background = pygame.image.load("images/background.png")

crouching = False

         
ctrex = pygame.image.load("images/trex.png")
ctrex_rect = ctrex.get_rect(midbottom = (60,355))
print(ctrex_rect.x)
print(ctrex_rect.y)
trex = pygame.image.load("images/trexverycool.png")
trex_rect = trex.get_rect(midbottom = (60,355))


cactus = pygame.image.load("images/very_good_cactus.png")
cactus_rect = cactus.get_rect(midbottom = (-200,400))

petra = pygame.image.load("images/petrathing.png")
petra_rect = petra.get_rect(midbottom = (-200,250))

npt = pygame.image.load("images/petrathing.png")
npt_rect = npt.get_rect(midbottom = (-200,250))
npt_rect.y = 50


npd = pygame.image.load("images/petrathing.png")
npd_rect = npd.get_rect(midbottom = (-200,250))
npd_rect.y = 210


npb = pygame.image.load("images/petrathing.png")
npb_rect = npb.get_rect(midbottom = (-200,250))
npb_rect.y = 400


ground = pygame.image.load("images/ground.png")
ground_rect = ground.get_rect(midbottom = (450,600))

cieling = pygame.image.load("images/ground.png")
cieling_rect = cieling.get_rect(midbottom = (450,600))

puas = pygame.image.load("images/puas.png")
puas2 = pygame.image.load("images/puas2.png")

evilcactus = pygame.image.load("images/very_good_evil_cactus.png")
evilcactus_rect = evilcactus.get_rect(midbottom = (-200,250))

gms = pygame.image.load("images/gameoverscreen.png")
gmsf = pygame.image.load("images/gameoverscreenfade.png")

gravity = 0

cc = 0
pc = 0

score = 0
pause_score = 0

speed = 10

sp = 900

bs = 0

nofn = 0
nofd = 0

enemies = ["cactus","petra"]
nenemies = ["npt","npd","npb"]

jumping = True
paused = False
day = False
night = True
gm = False


# Game loop.
while True:
	if not gm:
		if paused:
			for event in pygame.event.get():
			  if event.type == QUIT:
			    pygame.quit()
			    sys.exit()
			  if event.type == pygame.KEYDOWN:
			    if event.key != pygame.K_p:
			      paused = False	

			screen.blit(puas,(0,0))
			screen.blit(puas2,(0,0))

		#key input
		elif not paused:


			score += 1
			if day:
				if bs == 0:
					ground_rect.y = 355
					bs += 1
					print("it changed :D")			


				DTN = (randint(0,2000))
				if DTN == 1:
					print(DTN)
				if DTN == 1:
					petra_rect.x = -200
					cactus_rect.x = -200
					npt_rect.x = -200
					npd_rect.x = -200
					npb_rect.x = -200

					day = False
					night = True


				gravity += 1
				for event in pygame.event.get():
				  if event.type == QUIT:
				    pygame.quit()
				    sys.exit()
				  if event.type == pygame.KEYDOWN:
				    if event.key == pygame.K_DOWN:
				      crouching = True

				  if event.type == pygame.KEYUP:
				    if event.key == pygame.K_DOWN:
				      crouching = False
				keys=pygame.key.get_pressed()
				if trex_rect.bottom >= ground_rect.top:
					jumping = True



				if keys[K_UP] and crouching:
					pass

				if keys[K_SPACE] and crouching:
					pass

				if keys[K_UP] and jumping and not crouching:
				  gravity = -22 
				  jumping = False

				if keys[K_SPACE] and jumping and not crouching:
				  gravity = -22
				  jumping = False

				if keys[K_p] and not crouching:
					paused = True

				  # Apply gravity
				trex_rect.y += gravity
				ctrex_rect.y += gravity
				cactus_rect.x -= speed
				petra_rect.x -= speed

				if ctrex_rect.bottom >= ground_rect.top:
				  ctrex_rect.bottom = ground_rect.top

				if trex_rect.bottom >= ground_rect.top:
				  trex_rect.bottom = ground_rect.top

				if score >= 50:
					speed += 0.15
					if speed >= 25:
						speed = 25
					score = 0




				if cactus_rect.right <= 0 and petra_rect.right <= 0:
				  if len(enemies) >= 30:
				  	enemies = ["cactus","petra"]
				  rng = (choice(enemies))
				  if rng == "cactus":
				  	enemies.append("petra")
				  	cactus_rect.left = sp
				  if rng == "petra":
				  	enemies.append("cactus")
				  	petra_rect.left = sp


				if cactus_rect.y >= 245:
				  cactus_rect.y = 245

				  # collisions
				if trex_rect.colliderect(cactus_rect) or ctrex_rect.colliderect(cactus_rect):
				  gm = True

				if trex_rect.colliderect(petra_rect) and crouching == False:
				  gm = True

				if ctrex_rect.colliderect(petra_rect) and not jumping:
				  gm = True


				  # Draw.
				screen.fill("white")
				screen.blit(cactus,cactus_rect)
				screen.blit(ground,ground_rect)
				if not crouching:
				  screen.blit(trex,trex_rect)
				elif crouching:
				  screen.blit(ctrex,ctrex_rect)
				screen.blit(petra,petra_rect)

			elif night:
				bs = 0

				NTD = (randint(0,2000))
				if NTD == 2000:
				    print(NTD)
				if NTD == 1:
					day = True
					night = False
					print("test")



				ground_rect.y = 480
				cieling_rect.y = -245
				crouching = False
				for event in pygame.event.get():
				  if event.type == QUIT:
				    pygame.quit()
				    sys.exit()

				keys=pygame.key.get_pressed()

				if keys[K_UP]:
					trex_rect.y += -10

				if keys[K_DOWN]:
					trex_rect.y += 10

				if score >= 50:
					speed += 0.15
					if speed >= 25:
						speed = 25
					score = 0

				npt_rect.x -= speed
				npd_rect.x -= speed
				npb_rect.x -= speed
				evilcactus_rect.x -= speed

				if trex_rect.colliderect(ground_rect):
					trex_rect.bottom = ground_rect.top

				if trex_rect.colliderect(cieling_rect):
					trex_rect.top = cieling_rect.bottom

				if npt_rect.right <= 0 and npd_rect.right <= 0 and npb_rect.right <= 0:
				  if len(nenemies) >= 30:
				  	nenemies = ["npt","npd","npb"]
				  rngrng = randint(0,100)
				  print(rngrng)
				  if rngrng == 0:
				  	evilcactus_rect.left = sp
				  rng = (choice(nenemies))
				  if rng == "npt":
				  	nenemies.append("npd")
				  	nenemies.append("npb")
				  	npt_rect.left = sp
				  if rng == "npd":
				  	nenemies.append("npt")
				  	nenemies.append("npb")
				  	npd_rect.left = sp

				  if rng == "npb":
				  	nenemies.append("npd")
				  	nenemies.append("npt")
				  	npb_rect.left = sp			  	

				if trex_rect.colliderect(npt_rect):
				  gm = True

				if trex_rect.colliderect(npd_rect):
				  gm = True

				if trex_rect.colliderect(npb_rect):
				  gm = True


				screen.fill("black")
				screen.blit(ground,ground_rect)
				screen.blit(cieling,cieling_rect)
				screen.blit(trex,trex_rect)
				screen.blit(evilcactus,evilcactus_rect)
				screen.blit(npt,npt_rect)
				screen.blit(npd,npd_rect)
				screen.blit(npb,npb_rect)

	if gm:
		for event in pygame.event.get():
			  if event.type == QUIT:
			    pygame.quit()
			    sys.exit()
			  if event.type == pygame.KEYDOWN:
			  	cactus_rect.x = -200
			  	petra_rect.x = -200
			  	npt_rect.x = -200
			  	npd_rect.x = -200
			  	npb_rect.x = -200
			  	ctrex_rect.x = 9
			  	ctrex_rect.y = 298
			  	trex_rect.x = 9
			  	trex_rect.y = 298
			  	night = False
			  	day = True
			  	gm = False


		print(f"nofn is {nofn}")
		print(f"nofd is {nofd}")
		if nofn == 0:
			if night:
				screen.blit(gmsf,(0,0))
				print("cool")
				nofn = 1
				nofd = 0
		if nofd == 0:
			if day:
				screen.blit(gmsf,(0,0))
				nofd = 0
				nofn = 0				


		screen.blit(gms,(0,0))


	pygame.display.flip()
	fpsClock.tick(fps)