import random
class Puzzle():
    def __init__(self, name, question, difficulty, tries, answers, tip, cong, dissapoint,failure_texts ,rewards):
        self.name=name #[kratky nazov pre hadanku alebo intro]
        self.question=question #[lubovolne dlhy text hadanky]
        self.difficulty=difficulty    #["easy","medium","hard"]
        self.tries=tries #[1-5]
        self.answers=answers #[list akceptovanych spravnych odpovedi]
        self.tip=tip #tip co dostanes ked si na poslednom pokuse
        self.cong=cong #Text gratulacie
        self.dissapoint=dissapoint #Text ked failnes hadanku
        self.failure_texts=failure_texts
        self.rewards=rewards #TOTO zatial neries, neskor si sam vyberies, 
        #ake su odmeny za hadanku a das ich sem, aby reward suvisel s flavourom hadanky :)

    def get_reward(self):
        if self.difficulty =="easy":
            print("You get some of the basic items that will be implemented ino game...")
        if self.difficulty =="medium":
            print("You get some of the rare items that will be implemented ino game...")
        if self.difficulty =="hard":
            print("You get the LEGENDARY item!")

    def resolve_puzzle(self):
        #print(self.name) 
        print(self.question)
        tries=self.tries
        while tries>0:
            your_answer=input("")
            your_answer=your_answer.lower()
            for answer in self.answers:
                if answer==your_answer:
                    print(self.cong)
                    #self.get_reward()
                    return
            if your_answer in self.failure_texts:
                print(self.failure_texts[your_answer])
            tries-=1
            if tries>=1:
                print("This was not the expected answer, you have {} more tries.".format(tries))
            if tries ==1:
                print("hint: "+self.tip)
        print(self.dissapoint)


puzzle_list=[]
def get_random_puzle(difficulty):
    random_list=[]
    for puzzle in puzzle_list:
        if puzzle.difficulty==difficulty:
            random_list.append(puzzle)
    if len(random_list)>0:
        random_list[random.randint(0,len(random_list)-1)].resolve_puzzle()
    else: 
        print("No puzzle of difficultye: {} exists".format(difficulty))

#takto ich vytvaras
q1=Puzzle(
    "Useless puzzle", #name
    "Kolko rozkov zjem na ranajky?", #question
    "easy", # difficulty
    3, #pokusy
    ["1","0","jeden","ziaden"], #answers
    "na dva rozky a viac, nikdy nemam chut.", #tip
    "Bravo, you have completed my test!", #success
    "You have failed my task!", #fail
    {"10" : "si normalny? videl si niekoho zjest 10 rozkov?","-1":"hej dava zmysel zjest zaporne rozky"},
    []
)
puzzle_list.append(q1)
#tuto konci vytvaranie 1 puzzle
q2=Puzzle(
    "Blue puzzle", 
    "Britain has me, just like France, but Japan's missing out when on this Danube I dance. What am I?", 
    "medium", 
    3,
    ["blue", "Blue"], 
    "Symbolism.",
    "Bravo, you have completed my test!", 
    "You have failed my task!", 
    []
)
puzzle_list.append(q2)

q3=Puzzle(
    "Egg puzzle", 
    "If you spin me, I shall wobble. But after a hot bath there is no trouble. What am I?", 
    "easy", 
    3,
    ["egg", "Egg"], 
    "the bath is boiling hot",
    "Bravo, you have completed my test!", 
    "You have failed my task!", 
    []
)
puzzle_list.append(q3)

q4=Puzzle(
    "Basket puzzle", 
    "My quarter is like a neutrons half-time, athletes fill me, in their prime. They throw me to score a goal, treys are worth 50% more. What am I?", 
    "hard", 
    3,
    ["basketball", "basket ball"], 
    "neutrons have a half-life of 12 minutes.",
    "Bravo, you have completed my test!", 
    "You have failed my task!", 
    []
)
puzzle_list.append(q4)

q5=Puzzle(
    "Do puzzle puzzle", 
    "You have one try, it's do or die.", 
    "medium", 
    1,
    ["do"], 
    "",
    "you survive", 
    "did you choose die? Or did you just not know?", 
    []
)
puzzle_list.append(q5)

q6=Puzzle(
    "DNA puzzle", 
    "I take three phosphates to store your energy, I'm the missing piece of the puzzle CAT-GT_. What am I?", 
    "medium", 
    3,
    ["adenine", "adenosine"],
    "CAT-GTA, I'd pay for that to be a thing.", 
    "You listened during biology class, nice job!", 
    "Go back to high school biology mate!", 
    []
)
puzzle_list.append(q6)

q7=Puzzle(
    "money puzzle", 
    "they say \"money is the root of all evil.\", however I am money in a square. What am I?", 
    "easy", 
    3,
    ["evil"], 
    "the answer is in the question.",
    "hahahaha, you got it, now tremble before me!", 
    "Gotcha!", 
    []
)
puzzle_list.append(q7)




#takto ich testujes
#q1.resolve_puzzle()

#toto odkomentuj ak chces random hadanku dostat
get_random_puzle("easy")