from random import randint as r
from random import shuffle
import time


def slowPrint(text):
	for i in list(text):
		speed = r(10,90)/1000
		time.sleep(speed)
		print(i, end='', flush=True)
	print('\b', end='')
	
def quotes(quotesDict):
	speakers = list(quotesDict.keys())
	shuffle(speakers)
	speakerRoll = r(0,len(speakers)-1)
	speaker = speakers[speakerRoll]

	quoteRoll = r(0,len(quotesDict[speaker])-1)

	print()
	print("Inspirational quote of the day:")
	time.sleep(.3)
	slowPrint('"'+quotesDict[speaker][quoteRoll]+'"')
	time.sleep(.3)
	slowPrint('\n  -'+speaker)
	print()
	print()



quotesDict = {
    "Jesus":
    [
        "The first and greatest victory is to conquer yourself.",
        "Ignorance, the root and stem of all evil.",
        "Courage is knowing what not to fear.",
        "At the touch of love, everyone becomes a poet.",
        "One of the penalties for refusing to participate in politics is that you end up being governed by your inferiors.",
        "The measure of a man is what he does with power.",
        "Wise men speak because they have something to say; fools because they have to say something.",
        "Knowledge which is acquired under compulsion obtains no hold on the mind.",
        "He who commits injustice is ever made more wretched than he who suffers it.",
        "Justice means minding your own business and not meddling with other men's concerns.",
        "Love your neighbor as yourself.",
        "Blessed are the peacemakers, for they will be called children of God.",
        "Do to others as you would have them do to you.",
        "I am the way, the truth, and the life. No one comes to the Father except through me.",
        "Blessed are the poor in spirit, for theirs is the kingdom of heaven.",
        "You shall love the Lord your God with all your heart and with all your soul and with all your mind.",
        "Let him who is without sin among you be the first to throw a stone at her.",
        "For everyone who exalts himself will be humbled, and he who humbles himself will be exalted.",
        "Do not worry about tomorrow, for tomorrow will worry about itself. Each day has enough trouble of its own.",
        "It is not the healthy who need a doctor, but the sick. I have not come to call the righteous, but sinners."
    ],
    "Confucius":
    [
        "It does not matter how slowly you go as long as you do not stop.",
        "Our greatest glory is not in never falling, but in rising every time we fall.",
        "Real knowledge is to know the extent of one’s ignorance.",
        "The superior man is modest in his speech but exceeds in his actions.",
        "To see what is right and not do it is want of courage.",
        "He who learns but does not think, is lost! He who thinks but does not learn is in great danger.",
        "When we see men of a worthy character, we should think of equalling them; when we see men of a contrary character, we should turn inwards and examine ourselves.",
        "The superior man is distressed by the limitations of his ability; he is not distressed by the fact that men do not recognize the ability that he has.",
        "When we see men of a contrary character, we should turn inwards and examine ourselves.",
        "The man who says he can, and the man who says he can't are both correct."
    ],
    "Marcus Aurelius":
    [
        "The happiness of your life depends upon the quality of your thoughts.",
        "Waste no more time arguing what a good man should be. Be one.",
        "Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth.",
        "You have power over your mind, not outside events. Realize this, and you will find strength.",
        "Very little is needed to make a happy life; it is all within yourself, in your way of thinking.",
        "The best revenge is to be unlike him who performed the injury.",
        "When you arise in the morning, think of what a precious privilege it is to be alive—to breathe, to think, to enjoy, to love.",
        "Accept the things to which fate binds you, and love the people with whom fate brings you together, but do so with all your heart.",
        "If it is not right, do not do it; if it is not true, do not say it.",
        "The key is to keep company only with people who uplift you, whose presence calls forth your best."
    ],
    "Buddah":
    [
        "You yourself, as much as anybody in the entire universe, deserve your love and affection.",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
        "The mind is everything. What you think you become.",
        "Peace comes from within. Do not seek it without.",
        "The only real failure in life is not to be true to the best one knows.",
        "To keep the body in good health is a duty... otherwise, we shall not be able to keep the mind strong and clear.",
        "Three things cannot be long hidden: the sun, the moon, and the truth.",
        "In the end, only three things matter: how much you loved, how gently you lived, and how gracefully you let go of things not meant for you.",
        "Better than a thousand hollow words, is one word that brings peace.",
        "Just as a flower does not pick and choose the bees that come to it, it gives nectar to all."
    ],
    "Donald Trump":
    [
        "I like thinking big. If you're going to be thinking anything, you might as well think big.",
        "The harder I work, the luckier I get.",
        "I'm not a politician. I've always said I'm not a politician. I don't have the temperament for it.",
        "In the end, you're measured not by how much you undertake but by what you finally accomplish.",
        "I will fight for you with every breath in my body, and I will never, ever let you down.",
        "You have to think anyway, so why not think big?",
        "Sometimes by losing a battle you find a new way to win the war.",
        "Without passion, you don't have energy. Without energy, you have nothing.",
        "I have a great relationship with the Mexican people. I have many people working for me – look at the job in Washington – I have many legal immigrants working with me. And many of them come from Mexico. They love me, I love them.",
        "I'm not running for president to make things unstable for the country.",
        "I have never seen a thin person drinking  Diet Coke."
    ],
    "Thomas Aquinas":
    [
        "To one who has faith, no explanation is necessary. To one without faith, no explanation is possible.",
        "The things that we love tell us what we are.",
        "Beware the person of one book.",
        "There is nothing on this earth more to be prized than true friendship.",
        "The greatest kindness one can render to any man consists in leading him from error to truth.",
        "The things that are gained by the truth are better than the things that are gained by a lie.",
        "Man cannot live without joy; therefore when he is deprived of true spiritual joys, it is necessary that he become addicted to the joys of the body.",
        "Sorrow can be alleviated by good sleep, a bath, and a glass of wine.",
        "Faith has to do with things that are not seen and hope with things that are not at hand.",
        "The test of the artist does not lie in the will with which he goes to work, but in the excellence of the work he produces."
    ],
    "Gandhi":
    [
        "You must be the change you wish to see in the world.",
        "The best way to find yourself is to lose yourself in the service of others.",
        "Happiness is when what you think, what you say, and what you do are in harmony.",
        "An eye for an eye only ends up making the whole world blind.",
        "The future depends on what you do today.",
        "In a gentle way, you can shake the world.",
        "The weak can never forgive. Forgiveness is the attribute of the strong.",
        "The greatness of a nation and its moral progress can be judged by the way its animals are treated.",
        "You may never know what results come of your actions, but if you do nothing, there will be no results.",
        "There is no path to peace. Peace is the path."
    ],
    "Steve Jobs":
    [
        "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do.",
        "Innovation distinguishes between a leader and a follower.",
        "The people who are crazy enough to think they can change the world are the ones who do.",
        "Stay hungry, stay foolish.",
        "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose. You are already naked. There is no reason not to follow your heart.",
        "Your time is limited, don't waste it living someone else's life.",
        "The ones who are crazy enough to think they can change the world are the ones who do.",
        "The people who think they are crazy enough to change the world are the ones who do.",
        "Have the courage to follow your heart and intuition. They somehow already know what you truly want to become.",
        "Don't let the noise of others' opinions drown out your own inner voice."
    ],
    "Arnold Schwarzenegger":
    [
        "Strength does not come from winning. Your struggles develop your strengths. When you go through hardships and decide not to surrender, that is strength.",
        "The worst thing I can be is the same as everybody else. I hate that.",
        "The mind is the limit. As long as the mind can envision the fact that you can do something, you can do it, as long as you really believe 100 percent.",
        "I didn't mind basic training. It taught me that something that seems impossible at the start can be achieved.",
        "Failure is not an option. Everyone has to succeed.",
        "The resistance that you fight physically in the gym and the resistance that you fight in life can only build a strong character.",
        "The key thing that motivates me is seeing people in the gym and seeing that they're achieving results. If I can do it, they can do it, too.",
        "The last three or four reps is what makes the muscle grow. This area of pain divides a champion from someone who is not a champion.",
        "Milk is for babies. When you grow up you have to drink beer.",
        "It's simple if it jiggles, it's fat."
    ],
    "Rocky Balboa":
    [
        "It ain't about how hard you hit. It's about how hard you can get hit and keep moving forward.",
        "Every champion was once a contender that refused to give up.",
        "You, me, or nobody is gonna hit as hard as life, but it ain't how hard you hit; it's about how hard you can get hit, and keep moving forward. How much you can take, and keep moving forward. That's how winning is done.",
        "Going in one more round when you don't think you can - that's what makes all the difference in your life.",
        "I'm gonna show you how great I am.",
        "The world ain't all sunshine and rainbows. It's a very mean and nasty place, and I don't care how tough you are, it will beat you to your knees and keep you there permanently if you let it. You, me, or nobody is gonna hit as hard as life. But it ain't about how hard you hit. It's about how hard you can get hit and keep moving forward; how much you can take and keep moving forward. That's how winning is done!",
        "Life's not about how hard of a hit you can give... it's about how many you can take, and still keep moving forward.",
        "If you know what you're worth, then go out and get what you're worth, but you gotta be willing to take the hits.",
        "Until you start believing in yourself, you ain't gonna have a life.",
        "Don't let anyone tell you that you can't do something. Not even me. You got a dream, you gotta protect it. When people can't do something themselves, they're gonna tell you that you can't do it. You want something, go get it. Period."
    ],
    "Brundlefly (The Fly)":
    [
        "I'm saying I'm an insect who dreamt he was a man and loved it. But now the dream is over, and the insect is awake.",
        "The only problem is, I can't be sure who's having the dream.",
        "Have you ever heard of insect politics? Neither have I. Insects... don't have politics. They're very... brutal. No compassion, no compromise. We can't trust the insect."
    ],
    "John McClane (Die Hard)":
    [
        "Yippee-ki-yay, motherf****r!",
        "Come out to the coast, we'll get together, have a few laughs...",
        "Just a fly in the ointment, Hans. The monkey in the wrench. The pain in the a**.",
        "Nine million terrorists in the world, and I gotta kill one with feet smaller than my sister.",
        "You throw quite a party. I didn't realize they celebrated Christmas in Japan.",
        "I'm on vacation."
    ],
    "Sgt. Al Powell (Die Hard)":
    [
        "Welcome to the party, pal!"
    ],
    "Tony (Die Hard)":
    [
        "Now I have a machine gun. Ho Ho Ho."
    ],
    "Airport Cop (Die Hard 2)":
    [
        "You don't like me because I'm white trash?"
    ],
    "Dutch (Predator)":
    [
        "Get to the choppa!",
        "If it bleeds, we can kill it.",
        "Stick Around!"
    ],
    "Dillon (Predator)":
    [
        "You're hit, you're bleeding, man.",
        "Maybe I Can Get Even."
    ],
    "Mac (Predator)":
    [
        "I'm gonna have me some fun. I'm gonna have me some fun!"
    ],
    "Blain (Predator)":
    [
        "Ain't got time to bleed...",
        "Son of a bitch is dug in like an Alabama tick.",
        "Bunch of slack-jawed ****s around here. This stuff will make you a god damned sexual Tyrannosaurus, just like me.",
        "Old Painless Is Waiting."
    ],
    "Terminator (The Terminator)":
    [
        "I'll be back."
    ],
    "Sarah Connor (The Terminator)":
    [
        "There's a storm coming.",
        "You're terminated, f****r!"
    ],
    "Kyle Reese (The Terminator)":
    [
        "Come with me if you want to live."
    ],
    "John Connor (Terminator 2)":
    [
        "Hasta la vista, baby."
    ],
    "Terminator (Terminator 2)":
    [
        "I need a vacation."
    ],
    "Sarah Connor (Terminator 2)":
    [
        "There is no fate but what we make for ourselves."
    ],
    "Jules Winnfield (Pulp Fiction)":
    [
        "The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of evil men.",
        "Say 'what' again. Say 'what' again, I dare you, I double dare you, motherf****r, say 'what' one more goddamn time!",
        "I'm trying, Ringo. I'm trying real hard to be the shepherd."
    ],
    "Vincent Vega (Pulp Fiction)":
    [
        "You know what they call a Quarter Pounder with Cheese in Paris? They call it a 'Royale with Cheese.'",
        "Marsellus Wallace don't like to be f****d by anybody except Mrs. Wallace.",
        "You read the Bible, Brett?"
    ],
    "Mia Wallace (Pulp Fiction)":
    [
        "Don't you hate that? Uncomfortable silences. Why do we feel it's necessary to yak about bulls**t in order to be comfortable?",
        "An Elvis man should love it. You look like an Elvis man.",
        "I'll be down in two shakes of a lamb's tail."
    ],
    "Butch Coolidge (Pulp Fiction)":
    [
        "I'm an American, our names don't mean s**t.",
        "It's your future... I see a cab ride. Move out of the sticks, kids, don't be a dinosaur.",
        "Zed's dead, baby. Zed's dead."
    ],
    "Jerry Seinfeld":
    [
        "It's amazing that the amount of news that happens in the world every day always just exactly fits the newspaper.",
        "I am so busy doing nothing... that the idea of doing anything - which as you know, always leads to something - cuts into the nothing and then forces me to have to drop everything.",
        "Men don't care what's on TV. They only care what else is on TV."
    ],
    "George Costanza":
    [
        "I've driven women to lesbianism before, but never to a mental institution.",
        "I lie every second of the day. My whole life is a sham.",
        "I'm disturbed, I'm depressed, I'm inadequate. I got it all!"
    ],
    "Elaine Benes":
    [
        "I don't know how you guys walk around with those things.",
        "Maybe the dingo ate your baby.",
        "Sponge-worthy?"
    ],
    "Cosmo Kramer":
    [
        "Well, I've got gonorrhea.",
        "I'm out there, Jerry, and I'm lovin' every minute of it!",
        "I'm Cosmo Kramer, the Assman!"
    ],
    "Homer Simpson":
    [
        "D'oh!",
        "Mmm... donuts.",
        "You don't win friends with salad."
    ],
    "Marge Simpson":
    [
        "Homie, I can't help but think you're not taking this too seriously.",
        "I think that, as a good mother, it's my job to get you kids up to speed on the classics.",
        "Well, sometimes, when a parent and a child don't see eye to eye, the only way to get the kid to see your point of view is to put the kid in a sleeper hold."
    ],
    "Bart Simpson":
    [
        "Eat my shorts!",
        "I'm Bart Simpson, who the hell are you?",
        "I'm the king of the world!"
    ],
    "Lisa Simpson":
    [
        "I just don't want you to think you're not talented just because you didn't get the part you wanted.",
        "The time to worry about a gun is before you buy it.",
        "I am the Lizard Queen!"
    ],
    "Ned Flanders":
    [
        "Okily-dokily!",
        "Golly-doodily!",
        "Hi-diddly-ho, neighborino!"
    ],
    "Muhammad Ali":
    [
        "Float like a butterfly, sting like a bee.",
        "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion.'",
        "It's the repetition of affirmations that leads to belief. And once that belief becomes a deep conviction, things begin to happen."
    ],
    "Michael Jordan":
    [
        "I can accept failure, everyone fails at something. But I can't accept not trying.",
        "You have to expect things of yourself before you can do them.",
        "Talent wins games, but teamwork and intelligence win championships."
    ],
    "Serena Williams":
    [
        "The success of every woman should be the inspiration to another. We should raise each other up.",
        "I really think a champion is defined not by their wins, but by how they can recover when they fall.",
        "I've always considered myself the best and the top. I never considered anyone in my field as competition."
    ],
    "Usain Bolt":
    [
        "I know what I can do, so I never doubt myself.",
        "Worrying gets you nowhere. If you turn up worrying about how you're going to perform, you've already lost. Train hard, turn up, run your best, and the rest will take care of itself.",
        "I told my coach, 'If you think I'm going to work hard, give me a tough session.' And he said, 'Okay, we're going to work hard today.'"
    ]
}




if __name__ == "__main__":
	quotes(quotesDict)



