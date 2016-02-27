import random
class joueur: 

	def __init__(self,nom):
		self.nom=nom
		self.score=0
		self.victoire=0
		self.defait=0
		self.nul=0
		self.butsMarques=0
		self.butsAcceptes=0
	def miseajour1(self,res,BM,BA):
		if res==1:
			self.victoire=self.victoire+1
			self.score=self.score+3
		elif res==2:
			self.nul=self.nul+1
			self.score=self.score+1
		else:
			self.defait=self.defait+1
		self.butsMarques=self.butsMarques+BM
		self.butsAcceptes=self.butsAcceptes+BA
def classer(l):
	n=len(l)
	
	for i in range (n): #classement suivant le but
		k=i
		for j in range (i+1,n):
			if l[k].score < l[j].score:
				k=j
		l[k],l[i]=l[i],l[k]
	#classement suivant le goal average
	print("Le classement final est:")
	print("R","N","S","V","D","N","M","A","B")
	for m in range (n):
		print (m+1,l[m].nom,l[m].score,l[m].victoire,l[m].defait,l[m].nul,l[m].butsMarques,l[m].butsAcceptes,l[m].butsMarques-l[m].butsAcceptes)
nombre_de_joueurs=int(input("Veuillez saisir le nombre de joueurs ! \nNB: Chaque joueur doit avoir un nom unique \n ______________\n"))
Liste_matches=[]
Liste_matches2=[]
Liste_joueurs=[]
Liste_obj_joueurs=[]
for i in range(nombre_de_joueurs):
	b=0;
	while (b==0):
		nomJoueur=input("--> Donner le nom du joueur n=°%d "%(i+1))
		if nomJoueur not in Liste_joueurs:
			b=1
		player=joueur(nomJoueur)
		Liste_obj_joueurs.append(player)
		Liste_joueurs.append(player.nom)
for i in Liste_joueurs:
	for j in Liste_joueurs:
		if j!=i:
			match=[i,j]
			matchinv=[]
			matchinv.append(match[1])
			matchinv.append(match[0])
			
			if match not in Liste_matches and matchinv not in Liste_matches:
				Liste_matches.append(match)
matches_references={}
Liste_matches2=list(Liste_matches)
for i in range(len(Liste_matches)):
	match=random.choice(Liste_matches)
	print("Match n=°%d :%s VS %s"%(i+1,match[0],match[1]))
	Liste_matches.remove(match)
	matches_references[i+1]=match


j=0
while(j!=len(Liste_matches2)):
	numero_de_match=int(input("Donner le numéro de match que vous voulez saisir le résultat final \n"))
	match=matches_references[numero_de_match]
	
	score1=int(input("%s"%(match[0])))
	score2=int(input("%s"%(match[1])))
	for m in Liste_obj_joueurs:
		if (m.nom==match[0]):
			p1=m
	for m in Liste_obj_joueurs:
		if (m.nom==match[1]):
			p2=m
	if score1<score2:
		p1.miseajour1(3,score1,score2)
		p2.miseajour1(1,score2,score1)	
	elif score1>score2:
		p1.miseajour1(1,score1,score2)
		p2.miseajour1(3,score2,score1)	
	else:
		p1.miseajour1(2,score1,score2)
		p2.miseajour1(2,score2,score1)
	for m in Liste_obj_joueurs:
		if (m.nom==match[0]):
			m=p1
	for m in Liste_obj_joueurs:
		if (m.nom==match[1]):
			m=p2
	j=j+1
classer(Liste_obj_joueurs)

	
	
			
	

