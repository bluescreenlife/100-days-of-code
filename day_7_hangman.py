import random

class Hangman_Game:
    
    # initialize game and its necessary variables
    def __init__(self):
            
        # word bank for game to choose from
        self.word_list = [
            "able", "about", "account", "acid", "across", "act", "addition", "adjustment", "advertisement", "after",
            "again", "against", "agreement", "air", "all", "almost", "among", "amount", "amusement", "and",
            "angle", "angry", "animal", "answer", "ant", "any", "apparatus", "apple", "approval", "arch", "argument",
            "arm", "army", "art", "as", "at", "attack", "attempt", "attention", "attraction", "authority", "automatic",
            "awake", "baby", "back", "bad", "bag", "balance", "ball", "band", "base", "basin", "basket", "bath", "be",
            "beautiful", "because", "bed", "bee", "before", "behaviour", "belief", "bell", "bent", "berry", "between",
            "bird", "birth", "bit", "bite", "bitter", "black", "blade", "blood", "blow", "blue", "board", "boat", "body",
            "boiling", "bone", "book", "boot", "bottle", "box", "boy", "brain", "brake", "branch", "brass", "bread",
            "breath", "brick", "bridge", "bright", "broken", "brother", "brown", "brush", "bucket", "building", "bulb",
            "burn", "burst", "business", "but", "butter", "button", "by", "cake", "camera", "canvas", "card", "care",
            "carriage", "cart", "cat", "cause", "certain", "chain", "chalk", "chance", "change", "cheap", "cheese",
            "chemical", "chest", "chief", "chin", "church", "circle", "clean", "clear", "clock", "cloth", "cloud", "coal",
            "coat", "cold", "collar", "colour", "comb", "come", "comfort", "committee", "common", "company",
            "comparison", "competition", "complete", "complex", "condition", "connection", "conscious", "control", "cook",
            "copper", "copy", "cord", "cork", "cotton", "cough", "country", "cover", "cow", "crack", "credit", "crime",
            "cruel", "crush", "cry", "cup", "cup", "current", "curtain", "curve", "cushion", "damage", "danger", "dark",
            "daughter", "day", "dead", "dear", "death", "debt", "decision", "deep", "degree", "delicate", "dependent",
            "design", "desire", "destruction", "detail", "development", "different", "digestion", "direction", "dirty",
            "discovery", "discussion", "disease", "disgust", "distance", "distribution", "division", "do", "dog", "door",
            "doubt", "down", "drain", "drawer", "dress", "drink", "driving", "drop", "dry", "dust", "ear", "early", "earth",
            "east", "edge", "education", "effect", "egg", "elastic", "electric", "end", "engine", "enough", "equal",
            "error", "even", "event", "ever", "every", "example", "exchange", "existence", "expansion", "experience",
            "expert", "eye", "face", "fact", "fall", "false", "family", "far", "farm", "fat", "father", "fear", "feather",
            "feeble", "feeling", "female", "fertile", "fiction", "field", "fight", "finger", "fire", "first", "fish",
            "fixed", "flag", "flame", "flat", "flight", "floor", "flower", "fly", "fold", "food", "foolish", "foot", "for",
            "force", "fork", "form", "forward", "fowl", "frame", "free", "frequent", "friend", "from", "front", "fruit",
            "full", "future", "garden", "general", "get", "girl", "give", "glass", "glove", "go", "goat", "gold", "good",
            "government", "grain", "grass", "great", "green", "grey", "grip", "group", "growth", "guide", "gun", "hair",
            "hammer", "hand", "hanging", "happy", "harbour", "hard", "harmony", "hat", "hate", "have", "he", "head",
            "healthy", "hear", "hearing", "heart", "heat", "help", "high", "history", "hole", "hollow", "hook", "hope",
            "horn", "horse", "hospital", "hour", "house", "how", "humour", "I", "ice", "idea", "if", "ill", "important",
            "impulse", "in", "increase", "industry", "ink", "insect", "instrument", "insurance", "interest", "invention",
            "iron", "island", "jelly", "jewel", "join", "journey", "judge", "jump", "keep", "kettle", "key", "kick", "kind",
            "kiss", "knee", "knife", "knot", "knowledge", "land", "language", "last", "late", "laugh", "law", "lead",
            "leaf", "learning", "leather", "left", "leg", "let", "letter", "level", "library", "lift", "light", "like",
            "limit", "line", "linen", "lip", "liquid", "list", "little", "living", "lock", "long", "look", "loose", "loss",
            "loud", "love", "low", "machine", "make", "male", "man", "manager", "map", "mark", "market", "married", "mass",
            "match", "material", "may", "meal", "measure", "meat", "medical", "meeting", "memory", "metal", "middle",
            "military", "milk", "mind", "mine", "minute", "mist", "mixed", "money", "monkey", "month", "moon", "morning",
            "mother", "motion", "mountain", "mouth", "move", "much", "muscle", "music", "nail", "name", "narrow", "nation",
            "natural", "near", "necessary", "neck", "need", "needle", "nerve", "net", "new", "news", "night", "no", "noise",
            "normal", "north", "nose", "not", "note", "now", "number", "nut", "observation", "of", "off", "offer", "office",
            "oil", "old", "on", "only", "open", "operation", "opinion", "opposite", "or", "orange", "order", "organization",
            "ornament", "other", "out", "oven", "over", "owner", "page", "pain", "paint", "paper", "parallel", "parcel",
            "part", "past", "paste", "payment", "peace", "pen", "pencil", "person", "physical", "picture", "pig", "pin",
            "pipe", "place", "plane", "plant", "plate", "play", "please", "pleasure", "plough", "pocket", "point", "poison",
            "polish", "political", "poor", "porter", "position", "possible", "pot", "potato", "powder", "power", "present",
            "price", "print", "prison", "private", "probable", "process", "produce", "profit", "property", "prose",
            "protest", "public", "pull", "pump", "punishment", "purpose", "push", "put", "quality", "question", "quick",
            "quiet", "quite", "rail", "rain", "range", "rat", "rate", "ray", "reaction", "reading", "ready", "reason",
            "receipt", "record", "red", "regret", "regular", "relation", "religion", "representative", "request", "respect",
            "responsible", "rest", "reward", "rhythm", "rice", "right", "ring", "river", "road", "rod", "roll", "roof",
            "room", "root", "rough", "round", "rub", "rule", "run", "sad", "safe", "sail", "salt", "same", "sand", "say",
            "scale", "school", "science", "scissors", "screw", "sea", "seat", "second", "secret", "secretary", "see",
            "seed", "seem", "selection", "self", "send", "sense", "separate", "serious", "servant", "sex", "shade", "shake",
            "shame", "sharp", "sheep", "shelf", "ship", "shirt", "shock", "shoe", "short", "shut", "side", "sign", "silk",
            "silver", "simple", "sister", "size", "skin", "skirt", "sky", "sleep", "slip", "slope", "slow", "small",
            "smash", "smell", "smile", "smoke", "smooth", "snake", "sneeze", "snow", "so", "soap", "society", "sock",
            "soft", "solid", "some", "son", "song", "sort", "sound", "soup", "south", "space", "spade", "special", "sponge",
            "spoon", "spring", "square", "stage", "stamp", "star", "start", "statement", "station", "steam", "steel",
            "stem", "step", "stick", "sticky", "stiff", "still", "stitch", "stocking", "stomach", "stone", "stop", "store",
            "story", "straight", "strange", "street", "stretch", "strong", "structure", "substance", "such", "sudden",
            "sugar", "suggestion", "summer", "sun", "support", "surprise", "sweet", "swim", "system", "table", "tail",
            "take", "talk", "tall", "taste", "tax", "teaching", "tendency", "test", "than", "that", "the", "then", "theory",
            "there", "thick", "thin", "thing", "this", "thought", "thread", "throat", "through", "through", "thumb",
            "thunder", "ticket", "tight", "till", "time", "tin", "tired", "to", "toe", "together", "tomorrow", "tongue",
            "tooth", "top", "touch", "town", "trade", "train", "transport", "tray", "tree", "trick", "trouble", "trousers",
            "true", "turn", "twist", "umbrella", "under", "unit", "up", "use", "value", "verse", "very", "vessel", "view",
            "violent", "voice", "waiting", "walk", "wall", "war", "warm", "wash", "waste", "watch", "water", "wave", "wax",
            "way", "weather", "week", "weight", "well", "west", "wet", "wheel", "when", "where", "while", "whip", "whistle",
            "white", "who", "why", "wide", "will", "wind", "window", "wine", "wing", "winter", "wire", "wise", "with",
            "woman", "wood", "wool", "word", "work", "worm", "wound", "writing", "wrong", "year", "yellow", "yes",
            "yesterday", "you", "young", "Bernhard", "Breytenbach", "Android"
        ]
        
        # hangman art to display as game progresses
        self.game_art = ['''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        ''', '''
        +---+
        |   |
            |
            |
            |
            |
        =========''']

        # logo for game to display upon starting
        self.logo = ''' 
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/    '''

        # assign a random word from the above list, create a list version of the characters
        self.random_word = random.choice(self.word_list).upper()
        self.random_word_list = [char for char in self.random_word]
    
        # create an empty placeholder for user as they try and guess the word;
        # with str for better readability
        self.scoreboard = ["_" for char in self.random_word]
        self.scoreboard_str = " ".join(self.scoreboard)

        # list of incorrect letters to be added to as user plays
        self.incorrect_guesses = []
        
        # number of chances in accordance with hangman pieces
        self.lives = 6

    def run_game(self):

        # print game logo when beginning
        print(self.logo)

        # loop to verify whether user's guess is correct or not
        while self.lives > 0:

            # print hangmann art as game progresses
            print(self.game_art[self.lives])
            
            # retrieve user guess, after displaying necessary information
            user_guess = input("\n------------------------------------------\n"
                    f"\nYour word is: {self.scoreboard_str}\n"
                    f"\n😓 Incorrect guesses: {', '.join(self.incorrect_guesses)}"
                    f"\n😳 Guesses remaining: {self.lives}\n"
                    "\nGuess a letter: ").upper()
            
            # check whether user's guess is correct
            if user_guess in self.random_word_list:
                print("\n------------------------------------------\n"
                    f"\nCorrect! {user_guess} is in the word.")

                # retrieve indices of the game word's letters for correct user guess
                indices = [index for index, character in enumerate(self.random_word_list) if character == user_guess]

                # for each index associated with the correct letter, assign the letter to the
                # scoreboard placeholder
                for index in indices:
                    self.scoreboard[index] = user_guess
                        
                # update the scoreboard
                self.scoreboard_str = " ".join(self.scoreboard)

                # if user has guessed each letter, display win message
                if self.scoreboard == self.random_word_list:
                    print("\n------------------------------------------\n"
                        f"\nYOU WIN! The word was: {self.random_word}.\n")
                    break
                
            else:
                # for a wrong guess, remove a life, and add wrong letter to list of incorrect guesses, notify user
                self.lives -= 1
                self.incorrect_guesses.append(user_guess)
                print("\n------------------------------------------\n"
                    f"\nSorry, the letter {user_guess} is not in the word.")

                # display losing message when user is out of lives
                if self.lives == 0:
                    print("\n------------------------------------------\n")
                    print(self.game_art[self.lives])
                    print(f"\nSorry, you lose! The word was: {self.random_word}.\n")
        
if __name__ == "__main__":
            game = Hangman_Game()
            game.run_game()