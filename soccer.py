import random as rdm

class Game():
    def __init__(self):
        return

    def pairing(self, a, b):
        self.a = a
        self.b = b
        t = [a, b]
        x = rdm.sample(t, 2)
        return t

    def score(self):
        s = rdm.randint(0, 4)
        t = rdm.randint(0, 4)
        return s,t

    def game(self, a, b, winProbA, winProbB, xx):
        teams = self.pairing(a, b)

        score = list(self.odds(winProbA, winProbB, xx))
        match = dict(zip(teams, score))
        for key, value in match.items():
            print(key, value)
        winner = max(match, key = lambda key: match [key])
        if not score [0] == score[1]:
            print("The winner is: ", winner, "\n")
        else:
            print("Draw: ", winner, "Wins after penalties\n")
        return winner

    def odds(self, aWin, bWin, draw):
        A = B = D = 0
        matches = 1000

        self.aWin = aWin
        self.bWin = bWin
        self.draw = draw
        all = list()

        for j in range(matches):
            a = b = 0
            for i in range(rdm.randint(0, 5)):
                g = rdm.randint(1, 100)
                if g <= bWin:
                    a += 1
                    b += 1
                elif (g > bWin) and (g <= draw):
                    a += 1
                    b += 1
                else:
                    a += 1

            c = (a, b)
            all.append(c)
            if a > b:
                A += 1
            elif a < b:
                B += 1
            else:
                D += 1
        result = rdm.choice(all)
        return result
class  Odds():
    def __init__ (self, teamA, teamB, oddsA, oddsB):
        self.teamA = teamA
        self.teamB = teamB
        self.oddsA = oddsA
        self.oddsB = oddsB
        return

    def transform(self):
        probA = round(self.oddsA * 100, 2)
        probB = round(self.oddsB * 100, 2)
        AwinProb = (probA/(probA + probB))
        BwinProb = 1 - AwinProb
        return round(AwinProb * 100, 1), round(BwinProb * 100, 1)

    def calcDraw(self):
        x = self.transform()
        if ((max(x))/(min(x))) <= 2:
            x = 0.25
        elif((max(x))/(min(x))) <= 5:
            x = 0.15
        elif((max(x))/(min(x))) >= 10:
            x = 0.01
        else:
            x = 0.05
        return round(x * 100)

r = Game()

allteams = ['Germany', 'Brasil', 'France', 'Spain', 'Argentina', 'Belgium', 'England', 'Portugal', 'Columbia',
            'Uruguay', 'Russia', 'Croatia', 'Poland', 'Mexico', 'Switzerland', 'Denmark',
            'Sweden', 'Serbia', 'Japan', 'Egypt', 'Netherlands', 'Nigeria', 'Iceland', 'Peru',
            'Costa Rica', 'Morocco', 'Iran', 'Australia', 'Tunisia', 'South Korea', 'Panama',
            'Saudi Arabia']
wcodds = [2/9, 1/5, 2/11, 1/7, 1/8, 1/12, 1/20, 1/20, 1/25, 1/25, 1/30, 1/30, 1/40,
          1/60, 1/80, 1/80, 1/80, 1/150, 1/150, 1/150, 1/50, 1/200, 1/200, 1/200,
          1/250, 1/250, 1/250, 1/250, 1/500, 1/500, 1/1000, 1/1000]

teamodds = dict(zip(allteams, wcodds))

advance = []
counter = 1

while len(allteams) > 1:
    print('====== ROUND ', counter, '========\n')
    for i in range(int(len(allteams)/2)):
        k, v = rdm.sample(allteams, 2)
        p = teamodds[k]
        q = teamodds[v]
        o = Odds (k, v, p, q)
        xx = o.calcDraw()
        yy = o.transform()
        c = r.game(k, v, yy[0], yy[1], xx)
        allteams.remove(k)
        allteams.remove(v)
        advance.append(c)
    allteams = advance
    if counter < 5:
        print('=== Round ', counter, ' complete ===\n')
        print(*advance, 'go to next round\n')
        counter += 1
        advance = []
    else:
        print('WORLD CHAMPION: ', *advance)
            

        
                
                     
