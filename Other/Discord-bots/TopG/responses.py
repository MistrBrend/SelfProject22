import random

quotes = [  "The only way to do great work is to love what you do. - Steve Jobs",    
            "I can resist everything except temptation. - Oscar Wilde",    
            "The best way to predict your future is to create it. - Abraham Lincoln",    
            "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",    
            "I have no special talent. I am only passionately curious. - Albert Einstein",    
            "Do not take life too seriously. You will never get out of it alive. - Elbert Hubbard",    
            "If at first you don't succeed, then skydiving definitely isn't for you. - Steven Wright",    
            "I told my wife she was drawing her eyebrows too high. She looked surprised. - Unknown",    
            "I used to play piano by ear. Now I use my hands. - Unknown",    
            "I'm not arguing, I'm just explaining why I'm right. - Unknown",    
            "I don't suffer from insanity. I enjoy every minute of it. - Unknown",    
            "I'm not lazy, I'm just conserving energy. - Unknown",    
            "I'm not short, I'm concentrated awesome. - Unknown",    
            "I can't decide if I need a hug, a large coffee, or three days of sleep. - Unknown",    
            "If at first you don't succeed, redefine success. - Unknown",    
            "I can't adult today, I need a nap. - Unknown",    
            "I'm not arguing, I'm simply explaining why I'm right. - Unknown",    
            "I'm not great at the advice. Can I interest you in a sarcastic comment? - Unknown",    
            "I have a photographic memory but my camera is always out of focus. - Unknown",    
            "Why do they call it rush hour when nothing moves? - Unknown",    
            "I tried to organize a professional hide and seek tournament, but it was a complete failure. Good players are hard to find. - Unknown",    
            "I used to think I was indecisive, but now I'm not too sure. - Unknown",    
            "I'm not sure if I'm depressed or just really good at being lazy. - Unknown",    
            "I hate when I think I'm buying organic vegetables, and when I get home I discover they're just regular donuts. - Ellen DeGeneres",    
            "I told my wife she should embrace her mistakes. She gave me a hug. Now she's pregnant. - Unknown",    
            "I tried to make a belt out of watches, but it was a complete waist of time. - Unknown",    
            "I love it when I catch someone staring at me. I enjoy the attention and just smile at them. But then I remember, I look pretty weird when I eat. - Unknown",    
            "I'm not a morning person. I'm not an afternoon person. I'm not an evening person. I'm a night owl. - Unknown",    
            "I'm not sure if I'm the guy who always talks about himself or if I'm the guy who always listens. - Unknown",    
            "I used to think I was a people person, but then people ruined it for me. - Unknown",    
            "I wish I could turn back time, to when I had more money. - Unknown",    
            "I told my wife she should embrace her mistakes. She gave me a hug. Now she's pregnant. - Unknown",    
            "I'm not arguing, I'm just explaining why I'm right. - Unknown",    
            "I'm not lazy, I'm just conserving energy. - Levy Tate",
        ]

tags = [  
                        '<@264752552950759425>',
                        '<@303094746589691904>',
                        '<@289741164167561216>',
                        '<@387686468501635085>'
                    ]

jokes = [   "Waarom zit Jonathan altijd achter zijn computer? Omdat hij bang is voor virussen!",
            "Hoe noem je Jonathan's favoriete spel? Monopoly, omdat hij van geld houdt!",
            "Waarom heeft Jonathan een bril nodig als hij de krant leest? Omdat hij anders te veel geld zou uitgeven aan leesbrillen!",
            "Hoe noem je Jonathan als hij een fietstocht maakt? Jon Trappen!",
            "Hoe noem je Jonathan als hij aan het tuinieren is? Jon Deere!",
            "Hoe noem je Jonathan's favoriete drankje? Mountain Jon!",
            "Waarom ging Jonathan naar ClashGG? Hij wilde weten hoe je meer geld kunt verliezen!",
            "Waarom is Levy altijd zo cool? Omdat hij altijd de airconditioning aan heeft staan.",
            "Waarom kan Willem geen boeken lezen? Omdat ze hem altijd 'dicht slaan'.",
            "Wat zei Levy toen hij een dode mug op haar laptop zag? 'what the dog doing'.",
            "Waarom wilde Willem geen bladblazer kopen? Omdat hij allergisch is voor Levy",
            "Levy is botje",
            "Jona is botje",
            "Dana rhoades is kastoe a broer",
            "Ride or dordie",
            "Gewoon poep man",
            "Wat zei jona toen hij high was? 'kaas' .",
            "Waarom is die oma op die fiets gevaarlijk? Ze kan vallen op die kinderen. BAM!",
            "Hondje ook smoken? Kom maar hondje ik maak je pakje high n*gga.",
            "Welke kleur is jou fiets a sah?",
            "Sucky sucky long time",
            "Levy is een behoorlijke flikker",
            "Jonathan zuigt elke dag aan een knakworst"
        ]



def get_response(message: str) -> str:

    p_message = message.lower()
    quote = random.choice(quotes) 
    joke = random.choice(jokes)
    tag = random.choice(tags)

    if p_message == 'hello' or p_message == "ewa":
        return 'Ewa drerrie'

    elif p_message == 'quote' or p_message == '!quote':
        return quote

    elif p_message == 'joke' or p_message == '!joke':
        return joke

    elif p_message == 'kaas' or p_message == '!kaas':
        return f"{tag}  houd van kaas" or f'{tag} ik wil kaas, ik ben ook een klant'

    elif p_message == 'hoer' or p_message == 'hoeren':
        return "Jongeman die taal accepteren we hier niet";

    elif "ewa" in p_message:
        return "ewa my G"
    elif "kastoe" in p_message:
        return "Je bent geen kastoe, doe je pushups G."
    elif "vette" in p_message:
        return "vette maai jonge"

