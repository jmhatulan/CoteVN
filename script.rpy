# The script of the game goes in this file.

# Characters Declaration
define Edgy = Character("Kiyotaka",color="#ffa44f")
define Dog = Character("Tsubasa",color="#f9ff4f")
define Tsun = Character("Suzune",color="#4f58ff")
define Loli = Character("Arisu",color="#c14fff")
define Bipo = Character("Kikyo",color="#ff4f52")

# GUI Custom Declaration
define gui.choice_button_text_idle_color = '#ffffff'
define gui.choice_button_text_hover_color = '#ffea4d'

# Time Freeze IMG Declaration

# CGS Declaration
image cg 1 = "cgs/1_Horikita_AWalkInThePark.png"
image cg 2 = "cgs/2_Arisu_SuperiorIntoInferior.png"


# Game Start
label start:

    play music "bgm/giniro_FrozenFingertips.mp3" fadein 0.5 volume 0.4
    
    "Zzz....."
    "......"
    "........."
    "...Zzzzz......."
    "....."
    "........"

    play sound "<from 0 to 3>sfx/system.mp3" volume 0.75

    "Beep!"

    scene bg prehouse_night 
    with fade 

    "Thanks to my senses, I could detect even the slightest hint of sound while asleep."

    play sound "sfx/blanket.mp3" volume 0.75

    "I immediately sat up from my bed and looked around to see where that beeping came from."
    "It couldn't have come from an alarm clock, I didn't set one before going to bed."
    "It couldn't have been the doorbell, that would be ridiculous."
    "A crazy idea popped up in my mind, which involved that man sending armed troops to the place where I was temporarily staying at in an attempt to bring me back."
    "Something like that can be expected from that man because it was just like him to go to drastic measures when it involved me."
    "Unfortunately, that wasn't the case either."

    
    stop music fadeout 2.0
    play music "bgm/sanobawitch_What.mp3" volume 3.0
    show screen system_1("Congratulations, you have become 'the Protagonist'!\nRaise flags, form relationships, and build your very\nown harem of beautiful heroines to love! Enjoy!",0.5,0.5)
    with dissolve

    "..."
    "I blinked in confusion, before staring at the floating pink screen with white text that was floating in front of me."
    "Today was supposedly my first day in high school and I had been preparing for it ever since a week ago."
    "I made sure that nothing would prevent me from going to Tokyo Metropolitan Advanced Nurturing High School and starting a new life, not even some lousy sickness."
    "I check my body temperature to see if I were sick." 
    "I seem to be in a good condition, so there was no reason for me to be having hallucinations this early in the morning."
    "However, even after blinking and rubbing my eyes several times, it didn't disappear."
    "I decide to think about this when I get out of bed properly."

    play sound "sfx/blanket.mp3" volume 0.75
    with hpunch
    
    "I moved to the edge but was surprised when the pink screen moved with me." 
    "Staying at a fixed distance in front of my face that I could still read the text no matter which direction I looked."
    "I thought of a way to make this strange image disappear because it would definitely be a distraction."
    "I try to reached out towards the screen and touched it."

    play sound "<from 0 to 3>sfx/system.mp3" volume 0.75
    hide screen system_1
    with pixellate

    "The screen then made a beeping sound that one would normally hear in video games before it finally disappeared."

    stop sound

    Edgy "...what was that?"

    play sound "<from 0 to 1>sfx/knock.mp3" volume 2.0
    
    "I mumbled to no one in particular, before the sound of the door opening got my attention."

    show nanase normal:
        align (.5, 0) zoom 2
    with dissolve

    voice "<from 4>voice/chp_0/1_nanase.wav"
    Dog "Kiyotaka-senpai? Breakfast is ready downstairs. You don't want to be late for your first day in high school!"
    "Nanase Tsubasa, a 15-year old blonde girl who was a close friend of the people whom I was staying with, entered my room with a bright smile on her face."
    "I almost forgot that this girl was here."
    "Sleepovers were a regular occurrence in this household."
    "With that, she had stayed over for the night under the excuse of it being the last time she would see me before I leave to attend high school."
    "While I didn't really care about her reasons, I found it interesting that she can sleep here without any repercussions."
    "Are sleepovers just that normal?"

    
    stop music fadeout 1.0
    play sound "<from 0 to 3>sfx/system.mp3" volume 0.75
    show time freeze:
        #matrixcolor SaturationMatrix(0)
    with squares
    pause 1.5
    play sound "<from 5 to 8>sfx/system.mp3" volume 0.75
    show time placeholder:
        matrixcolor SaturationMatrix(0)
    show screen system_1("Kiyotaka-senpai? Breakfast is ready downstairs.\nYou don't want to be late for your first day in high school!",0.5,0.05)
    with Pixellate(3.0,5)

    "!"

    queue music "bgm/sanobawitch_Arienai.mp3" volume 3.0

    "What the."
    Edgy "What's going on here..."
    "I stare at the three screens, especially the last one."
    "Thanks to my past, I couldn't show any kind of expression on my face even though I was capable of feeling emotions."
    "But this was the closest I had come to breaking that."
    "I had seen my fair share of shocking things, like people being killed and burned to oblivion."
    "But if I had to be honest, none of those could compare to this."
    "The sudden stop of time itself was already enough to break my usual apathetic expression."
    "It was the three 'choices' before me that got my jaw to slightly drop out of disbelief."
    "If that wasn't enough, I could also see Nanase's 'Breakfast is ready downstairs. You don't want to be late for your first day in high school!' on top of them in a separate screen."
    "Despite my true nature and what I was really like under that mask of indifference that I normally had, I am still a teenager and thus, shared a similar interest to things that other teens liked."
    "It didn't help that for the past month that he had been living here, Eiichiro Matsuo, the son of the butler who helped him escape from {i}that place{/i}."
    "Introduced me to the world of video games when we met."
    "After only a week, I was able to build his own computer and even program it to give me regular updates about {i}that man{/i} and the White Room."
    "Even though I preferred strategy and FPS games where I can truly be in my element, I still knew what this whole scenario was like."
    "Namely, Visual Novels."
    "They were a type of game wherein the player would have to assume the role of the protagonist and make his own choices that will affect the game in many ways."
    "In the novels that were also considered 'dating simulators', the player may choose between different 'routes', or girls whom he would end up with when the game is finished."
    "In my case, though, I had never played any cute/romantic ones, because there wasn't anything like that in this household."
    "Eiichiro liked the 'explicit' genre of visual novels more, which were the eroges."
    "He even had a collection of them which I decided to ignore the first time he saw it."
    "How would his father react to that when he sees it..."
    "Regardless, he had played a few eroges in the past month and it only left him curious and interested on how games like those were made, despite the {i}mature{/i} content that were included in them."
    
    show screen system_2("Congratulations, you have become 'the Protagonist'!\nRaise flags, form relationships, and build your very\nown harem of beautiful heroines to love! Enjoy!",0.5,0.667)
    with dissolve
    
    "The words from the first screen earlier then came back to my mind, making him shake his head."

    hide screen system_2
    with dissolve

    Edgy "This is ridiculous. I must be dreaming. Eiichiro's games have simply got into my head."
    "I refused to believe that I am experiencing the life of a dating sim protagonist."
    "It sounded like a lame plot for a cheap manga and this was no doubt just a weird dream."
    "Maybe seeing that eroge collection of Eiichiro got to his brain..."
    "It also sounded like some god up there took pity on me for essentially missing out on my entire childhood and made things this way to make it up to me."
    "Deciding that this was only a dream without a doubt, I threw my back to bed, ignoring the choices and closing my eyes."

    show time none
    hide screen system_1
    with irisin
    pause 3.0
    hide time none
    show time freeze
    show time placeholder:
        matrixcolor SaturationMatrix(0)
    show screen system_1("Kiyotaka-senpai? Breakfast is ready downstairs.\nYou don't want to be late for your first day in high school!",0.5,0.05)
    with irisin

    "An undetermined amount of time later, I looked at my clock frozen, things remained the same."
    "I tried tried a number of things in an attempt to wake himself up from this 'dream'."
    "From punching himself in the face and trying to step past the frozen and colorless form of Tsubasa (which magically teleported him back to his bed."
    "I come to the realization that this wasn't a dream..."
    "This is insane."
    "Thanks to Eiichiro's influence and my own curiosity, I had read a fair share of stories and manga where something similar to this happened..."
    "As in, the protagonists' life turning into a video game."
    "I never asked for this to happen!"
    "Did it really have to be a dating sim? Couldn't it have been an RPG or even being sent to another world where I can have a new life? That would have been better!"
    "Finally coming to the realization that I am basically 'trapped' here until I do something"
    Edgy "{i}sigh...{/i}"
    "I walked over towards Tsubasa, standing just before her before looking at the three choices I have."
    "Obviously, the option that caught my attention was the first one."
    "It was simple, direct, and can get rid of Tsubasa in a snap."
    "However, I quickly had second thoughts about it."
    "I have no idea how his answer would affect Tsubasa and from his experience in playing these games, choosing the wrong option would lead to something bad."
    "As much as I wanted Tsubasa to leave, I didn't want to be rude to the girl who was only trying to tell him that food was on the table."
    "The second choice was also plausible, but I could tell that it contained a passive-aggressive tone from the words alone."
    "Plus, it also had an inappropriate comment about going into a girl's room that wasn't needed at all."
    "Again, I didn't want to be rude to Nanase who has done nothing wrong as far as I am concerned."
    "And so, by process of elimination, my eyes fell on the last option."
    "The one that would have been discarded first out of logic if I were in a normal conversation."
    "Unfortunately, this was anything but normal. It was also remotely obvious that it was the 'right' option, considering his current predicament."
    "As much as he wanted to deny it, he was now curious about what would happen if he chooses this option."
    
    hide time placeholder
    hide screen system_1
    show time freeze:
        #matrixcolor SaturationMatrix(0)
    show freeze 1 nanase:
        matrixcolor SaturationMatrix(0)

label cMenu_0_1:
    show screen system_1("Kiyotaka-senpai? Breakfast is ready downstairs.\nYou don't want to be late for your first day in high school!",0.5,0.05)
    menu:
        "What should I pick?"
        "I heard you, and I'm going. Now get out. I have to change clothes.":
            jump chc_0_1_A
        "Nanase, you don't just barge into someone else's room without knocking. Would you mind it if I did the same?":
            jump chc_0_1_B
        "You know, I never realized how cute and adorable you are, Tsubasa-chan. Why don't you join me in bed for a few more minutes before we go down?":
            jump chc_0_1_C

label chc_0_1_A:
    hide screen system_1
    with dissolve
    "O-Okay, uhm... I'll... see you downstairs then, Kiyotaka-senpai... (She fears she did something wrong and feels guilty for it)"
    "Bad End A"
    jump cMenu_0_1
label chc_0_1_B:
    hide screen system_1
    "S-Sorry, senpai... I-I-I won't do it again, I promise! Please forgive me! (She feels ashamed of her mistake and because she disappointed Kiyo)"
    "Bad End B"
    jump cMenu_0_1
label chc_0_1_C:
    hide screen system_1
    "I made up my mind."
    jump chap_0_1

label chap_0_1:
    Edgy "{i}sigh...{/i}"
    "I reached my hand toward the screen and pushed 'Option C'."
    "Almost immediately, I had the weirdest feeling, it was as if the world became 'blurred' until he found himself back on his bed, in the exact same position he had been when the 'choices' first appeared."
    "I begin to feel dizzy with this sensation. I was unable to notice that the world around me was regaining its color and going back to the way it was."

    hide freeze 1 nanase
    hide time freeze
    with squares

    "I felt my mouth and body were moving by their own will, as if some kind of greater power had suddenly overriden his own mind."
    "If I had to be honest, I am getting nervous about this."
    "I was trained to fight against human threats, not divine ones."
    "Divine because what I'm going through at the moment can't be the work of a normal human at all."
    "You know, I never realized how cute you are, Tsubasa-chan," 
    "Kiyotaka spoke with a smile that took the blonde girl completely off guard, because she had never seen him make any kind of emotion before." 
    "Why don't you join me in bed for a few more minutes before going down?"
    "Silence was what followed even after the shocked Kiyotaka regained control over his body. He was already thinking of what to say as an apology, when he saw Tsubasa blushing furiously as she took a few steps back, unable to look at him in the eyes."
    "U-Uhm..... I-I-I-I'll leave you alone for now, Senpai....... D-Don't forget to come down for breakfast alright....?!"
    
    hide nanase normal
    with easeoutright

    "The poor Tsubasa squeaked in embarrassment before running away, leaving the dumbfounded Kiyotaka behind."
    "He didn't even have time to open his mouth and voice his shock at how this thing worked as well as the fact that he actually smiled, because several 'Notifications suddenly popped before him with some weird chiming that came from who-knows-were."
    
    show screen system_1("Congratulations!\nYou have unlocked the achievent:\n'Smooth Like Butter'!\nYou gained +1 in Charm!",0.25,0.1)
    show screen system_1("Tsubasa Route has been Unlocked!\nYou can now see 'Heroine Status'\nwith Nanase Tsubasa!",0.75,0.1)
    show screen system_1("Your current status with Tsubasa\nhas changed to 'Loyal Follower'!",0.25,0.5)
    show screen system_1("Congratulations!\nYou have unlocked the achievement:\n'The First of Many'!\nYou gain +1 in Aura!",0.75,0.5)

    "I can't believe it. This may actually be real,"
    "I slowly get over my shock."
    "I am getting curious about this strange 'power'."

    hide screen system_1

    "This was a completely different experience compared to playing video games, and he now wanted to know more about how this worked."

    # SCENE CHANGE

    "Breakfast had been quite a slightly awkward affair, mainly between him and Tsubasa. Eiichiro was as loud and boisterous as ever while Matsuo himself was offering Kiyotaka some advice before he leaves for school later on, but the young man wasn't listening at all."
    "It wasn't Kiyotaka's fault that he couldn't concentrate on what was happening. It's because of the 'screen' that appeared over Tsubasa's head that he couldn't ignore no matter how much he tried to think about something else."

    show screen system_1("""Nanase Tsubasa: 'Friendly Kouhai'

Relationship Status: Loyal Follower
Affection Points: 0/100
Heroine Summary: Tsubasa is a dear friend of Eiichiro
who met you a month ago when his father brought you here.
During all the times she has visited,
she always looks forward to being around you because of how much of a mystery you are.
She constantly wonders why you never show any kind of emotion,
but chooses not to ask anything because she thinks it is something you don't want to share.
She looks up to you as her 'senpai' and highly values your opinion.
She aims to go to Tokyo Metropolitan Advanced Nurturing High School like you in a year's time""",0.5,0.5)

    "Kiyotaka was trying hard not to stare at the screen that showed Tsubasa's information, but all it did was confirm to him that this was something he'd have to get used to. On the bright side, it did give him more insight on what the girl thought about him and he was slightly surprised at what he just found out."
    "More importantly, he was curious on how exactly this 'power' worked. Was it just about raising flags with 'heroines' and making a harem of his own? He remembered those as the exact words that were shown at the screen that he saw when he woke up."
    "Was that it then? Was he simply supposed to gain the affection of the girls he comes across with? Tsubasa was already one of them and from the looks of it, she wasn't going to be the only one."
    "To what end, though? How many girls would it take before this dating simulator becomes satisfied? Based on what he knew about games like this, the normal number of girls that a player can choose from would be five, but there's no telling if the same applies to this 'power' he now possessed."
    "Of course, like every other person out there, Kiyotaka desired to experience what was it like to love a person and if he was capable of doing so. Because of that, he wasn't going to be pissed at this turn of events and if anything, this might help him."
    "But can he really live with this predicament? He also wanted to enjoy the other aspects of his freedom like choosing where to go, what to do, and what to eat. With his life being akin to a protagonist of a dating simulator, he didn't feel as free anymore."
    "It's like someone from above was telling him to use this to his advantage and do with it as he wished, but could he really do this? He knew nothing about falling in love and relationships and he was completely sure that video games aren't the same as real life."
    Dog "Senpai, give me your plate and utensils, I'll wash them for you. You need to prepare to go to school, remember?"
    "spoke Tsubasa with a calm voice, bringing Kiyotaka out of his musings and making him realize that she had finally put the awkwardness from his earlier teasing/joke behind her."
    Edgy "Sorry, what were you saying?"
    Dog "Your plate, Senpai. I'm going to wash the dishes." #Tsubasa simply smiled.
    "Kiyotaka noticed that she was holding 3 sets of plates and utensils in her arms, which meant that Eiichiro and Matsuo were already done. Has he been deep in his thoughts for that long?"
    
    hide screen system_1

    "Before he could say anything however, the world around him screeched to a halt as three separate screens appeared before him."
    
    "I rolled my eyes as everything around him lost color, before doing a quick scan of the three new options."
    
    while True:
        menu:
            "I don't even need to think about this time. The third option seems to be the most logical one."
            "Sure. Here you go. You should head home soon too. Your parents might be getting worried.":
                Edgy "What are you doing? I said I'm picking the third option."
            "I'll handle it. Think of it as an apology for...... the joke I said earlier....":
                Edgy "What are you doing? I said I'm picking the third option."
            "No, let your senpai take care of this. Anything for my cute and adorable kouhai!":
                jump chap_0_2

label chap_0_2:
    "Even though he was ready this time, the feeling of some higher power taking over his mind and actions still felt weird and disturbing."
    "As the world returned to normal, Kiyotaka felt himself standing up while grabbing his own plate before taking the rest from Tsubasa in one smooth move."

    "No thank you, Tsubasa. Let your senpai take care of this,"
    "the 'overridden' young man declared with the same smile he used earlier, making the girl flinch in surprise."
    "Anything for my cute and adorable kouhai!"

    "The effect was instantaneous, and Kiyotaka found himself regaining control over his body in time to see Tsubasa's face turning red from the atomic blush that appeared on her cheeks."
    "I-I think you're being very weird today, Senpai.....!"
    "Tsubasa shook her head in an effort to rid herself of the embarrassment she was feeling, before running away from the scene to save herself."
    
    #Your sudden change in personality overwhelmed a Heroine! You gained +2 in Charm!"
    #You gained 15 Affection Points with Nanase Tsubasa!"

    "That went just about as I expected,"
    "Kiyotaka sighed while dismissing the new notifications that appeared."
    "It's going to take him some time to get used to this......."

    #scene new 

    "After going through the dishes, Kiyotaka went back to his room and prepared his new school uniform, before heading to the bathroom."
    "As he lowered himself inside the bathtub, Kiyotaka thought about this strange power that he now possessed and what it was capable of doing."
    "Somehow, this thing is strong enough to make someone like me show emotions, especially a smile. I wonder what else this thing can do....."

    "Even though he wasn't in control of himself when he chose from the three options earlier, he still felt himself smiling and acting like a normal person around Tsubasa, which was quite the experience, if he had to be honest."

    "Kiyotaka also wondered if he could be capable of smiling completely on his own, without the intervention of this strange power. The last time he smiled was before he was sent to that place, and it had been many years since that happened."

    "Time to put my knowledge about games to the test, I suppose," 
    "Kiyotaka leaned back, staring up at the ceiling as he thought deeply about figuring how this dating simulator worked. "
    "Hm, I know that in every game, there's some kind of tutorial that helps a player in how to play the whole thing. Should the player require another tip or hint, he could always open the menu-"

    "With another musical chime that his ears picked up, a new 'screen' materialized before him that was different from the 'choices' earlier. It was also further proof that this wasn't a dream by all means, but reality."

    "Voice activation, huh? That's pretty convenient," 
    "Kiyotaka washed his face before analyzing the pink-colored 'Menu' before him and what it had to offer."

    #[Dating Stats]
    #[Heroines' Status]
    #[Titles]
    #[Skills]
    #[Gallery] (Locked)
    #[Achievements]

    "So, it's pretty much the same as a normal visual novel, but with an emphasis on romance,"
    "he concluded."
    "Your life turning into a video game was likely a dream that many people shared, and even Kiyotaka thought about it once or twice after being introduced to them."

    "Having this happening to him was pure irony. He, who wished to know how to fall in love and have a girlfriend someday, was now bestowed with a strange gift that can help him accomplish that."

    "However, this was never what he wanted."

    "He could have been an RPG character who had limitless potential and can train to be the strongest there is but no, he was still a normal person who had this strange ability to stop time itself for the sole purpose of choosing from a list of options."

    "If it was up to me, I'd rather be reincarnated in another world where I'm in complete control of my life. This whole thing makes me feel like my freedom has just been taken away from me..... again."

    "Okay, perhaps he was being too pessimistic about this. Maybe there was something within this dating simulator mechanic that would be useful to him in the long run, so he turned back to the Menu and began to explore it for an ability or skill that can be beneficial for him."

    "Unfortunately, he was wrong."

    #[Dating Stats]

    #Charm: 13

    #Wisdom: 20

    #Aura: ?

    "These 'stats' were completely useless, at least for him. 'Charm' stood for his natural ability to make other people find him approachable/attractive/likable. He was actually surprised that it was more than a '1', as he was completely sure that his expressionless look was something that can chase other people away. 'Wisdom' didn't pertain to his actual intelligence or experience in life, but for his capacity to know what others liked/didn't like about him. The other stat was 'Aura', which apaprently stood for his natural ability to draw other people to himself. The question mark could either mean that it was something that couldn't be measured or he just can't access it yet."

    "'Heroines' Status' was likely going to show him the same screen that he saw above Tsubasa's head before, so he ignored it. The next one, though......"

    #[Titles]

    #[The Protagonist]: You're the MC! The most complicated and downright impossible things are going to come your way! (Grants mental immunity to any kind of illusion or trick that is designated to throw you off guard)

    "What a letdown. This title meant nothing in his eyes. Well, at least he was reassured that he can never be manipulated by someone else, even though he himself would never let that happen. Time to move to the next sub-menu, which looks more interesting than 'Titles'....."

    #[Skills]

    #[Eroge Protagonist]: Your life can be played like a Dating Sim.

    #[Eyes of the Main Character]: Grants you the ability to discern between 'Filler Characters' and 'Potential Heroines'.

    #[To Protect Her Smile]: ? (Skill Locked)

    "Nope. These skills were a disappointment as well, especially that last one which was apparently locked, so he couldn't see what it was about. Eh, it'll probably be a lame one thanks to that ridiculous name. The first one couldn't even be considered a 'skill' in his eyes, it's more of a status. The second one was pointless as well, because it was only a reminder that Tsubasa won't be the only girl who will be considered a 'heroine'."

    "Finally, Kiyotaka turned his attention to the last sub-menu, 'Achievements'. However, it wasn't any helpful either, because it worked the same as in many games. About 99\% of the achievements were hidden but showed the conditions on how to get them, while the two that were already unlocked didn't even show any rewards that he got from them. Who knows? There might not even be any rewards for these achievements, which would be disappointing."

    #[Achievements]

    #[First of Many]: Unlock a Heroine Route.

    #[Smooth Like Butter]: Choose the Best Option during your first interaction with a Heroine.

    ".....yep, there's nothing here that's helpful as well. The hidden achievements only served to disappoint him even further, actually. One of them even had the condition of 'unlocking more than 8 routes', which was a ridiculous thing to think about. "

    "All in all, it felt like someone above tried to put together a complicated system for a dating simulator in real life and just slapped it on him for no reason. If it was a god who did this, then Kiyotaka expected better. It may seem interesting at first glance but after taking a look at what this 'power' had to offer, it wasn't anything special."

    "And while he was a perfectly straight and healthy teenager, Kiyotaka didn't feel like taking advantage of this dating simulator to get a girlfriend (it was already doing it regardless). If anything, this system was taking advantage of him because he was forced to make the appropriate choice that one would make in a dating sim, even though it made him uncomfortable."

    "Assuming this thing will continue to work even while I'm in school, then I should just prepare for the worst,"
    "Kiyotaka sighed."

    "Since this dating sim mechanic was apparently powerful enough to force him to smile and show emotions to other people even if he didn't want to, there's bound to be some complicated situations which he would have to deal with in the aftermath. That's what the 'Protagonist' title was for, after all."

    "Hey, at least this will surely make that man lose his mind if he ever finds out about this, so..... consolation prize....?"

    #scene new

    "After taking a bath, Kiyotaka proceeded to dress himself in his school uniform before preparing his belongings. The thought of this dating sim power that he now possessed being a possible headache in the future still lingered in his mind, but he wasn't going to let that deter him from enjoying his new life in high school."

    "Once he was done with everything, the young man stood by the front door, where he was about to say farewell to the three people in the household."

    "I suppose this is goodbye," 
    "he said, shifting his gaze towards the man who helped make this possible. If there was anyone whom he felt grateful towards, it was Matsuo for helping him escape his life in the White Room and gave him the freedom to do what he wanted. "
    "Thank you for what you've done for me, Matsuo."

    "Matsuo offered him a smile, before shaking his head slowly. "
    "I don't believe this is goodbye, Kiyotaka-sama. After three years, we will meet each other again and by then, I hope you have lived your life to the fullest. Be what you want to be."

    "Kiyotaka nodded in acknowledgement as he turned to the next person, who gave him a big grin before throwing his hand for a handshake."

    "We'll meet again, Kiyotaka, I'm sure of it! Hell, I'm thinking of going to the same school as you when I'm done with my current school!"

    "The young man nodded in response as he accepted the gesture, shaking Eiichiro's hand." 
    "It would be nice to have a familiar face around, so why not?"

    "Kiyotaka then turned to the last person, who looked so nervous that she had no idea what to say. "

    "Senpai....." 
    "Tsubasa mumbled, as she struggled to come up with the proper words to tell him. She had not went home yet apparently, citing that she wanted to say goodbye to him before that."
    "Please wait for me! I'll be sure to follow you in that school when I'm done with middle school!"

    "Kiyotaka waited for a few moments, expecting the world to freeze once again and show him three choices to choose from, but nothing happened. It made him confused, because this was a clear opportunity to have him choose from different options on what would be his response. It also made him more curious about how this strange anomaly truly worked."

    "No choices this time? Strange. Does it expect me to say the right thing? Or is it letting me say what I want?" 
    "Kiyotaka thought, before quickly thinking of what to tell the girl as a response, since nothing was happening anyway. She was waiting for him to say something, after all. "
    "I'll wait when that happens then, Nanase."

    "The blonde girl stared up at him for a brief moment, and it was unclear what she was thinking right now."

    "Senpai!"

    "Tsubasa then rushed forward, wrapping her arms around Kiyotaka in a big hug. She buried her head into his chest, while Kiyotaka only stared at the girl hugging him in surprise as two new 'notifications' appeared in front of him, ignoring the amused smiles from Matsuo and his son."

    #[You gained 30 Affection Points with Nanase Tsubasa!]
    #[Congratulations! You have unlocked the achievement: 'We Will Meet Again'! You gain +1 in Charm!]

    "'30 Affection Points'.... seriously? I didn't even do or say anything that can gain her affection." 
    "Kiyotaka was dumbfounded above everything else, wondering how a boring and direct response actually caused that big of an increase in Affection Points with this girl. As far as he was concerned, nothing should have happened. But here he was, getting hugged by a girl and being aware of what she felt towards him."

    "Maybe it's because he still had a lot to learn about romance, as well as the mind of a girl."

    "He was too caught off guard to respond to Nanase's sudden hug that she already let go when he was about to take her arms off of him. She then stepped back, as she gave him a big smile that somehow caused the young man's heart to beat faster than before. Kiyotaka felt it and was left wondering if it was because of this strange power that's been bugging him since this morning."

    "Good luck, Senpai! Do your best!"

    "Instead of saying anything else, Kiyotaka simply nodded and walked out of the house before one of those three figure out that something was wrong with him."

    "Despite what just happened with Tsubasa, the brown-haired teen put the issue at the back of his mind for now, and instead chose to think about his new high school while he stood at the sidewalk. A bus soon stopped in front of him, and Kiyotaka was in deep thought while he stepped inside, then took a seat at the nearest empty spot he could find."

    "My new life begins now.... and with it comes this 'dating sim' power that I have. I have no idea what's in store for me in this school but with this 'power' I have, I'm sure it'll be filled with headaches. Still, it's bound to be interesting and I feel strangely excited for what the place is all about."

    "Somewhere out there, a few beings of higher power were having fits of laughter at the impending chaos that will happen soon enough."


    #Kiyotaka's Progress:


    #[Dating Stats]

    #Charm: 14

    #Wisdom: 20

    #Aura: ?

    #[Heroines' Status]
    #[Nanase Tsubasa: 'Friendly Kouhai']
    #[Relationship Status: Loyal Follower]
    #[Affection Points: 45/100]
    #[Heroine Summary: Tsubasa is a dear friend of Eiichiro who met you a month ago when his father brought you here. During all the times she has visited, she always looks forward to being around you because of how much of a mystery you are. She constantly wonders why you never show any kind of emotion, but chooses not to ask anything because she thinks it is something you don't want to share. She looks up to you as her 'senpai' and highly values your opinion. She aims to go to Tokyo Metropolitan Advanced Nurturing High School like you in a year's time]





label chap_2:
    play music "bgm/giniro_SnowingTown.mp3" volume 0.75
    scene cg 1
    with squares
    Tsun "Thank you for listening."
    
label chap_3_0:
    #play music "bgm/giniro_CertainBond.mp3" volume 0.75
    play music "bgm/Arisu_Piano_KoreKuraiDe_yumetoiro.mp3" volume 1.5
    scene cg 2
    with squares
    "The smug expression on Arisu's face fell apart quickly as she moved away from me, at least until her back met the door to her room seconds after."
    "I stopped about an inch away from her and leaned down so we could look at each other directly."
    "I slammed my arm against the door behind her, pulling off a kabe-don that startled the lilac-haired girl and even caused her cheeks to turn red."
    Edgy "Hoh? Is that a blush I see, Sakayanagi?"
    "My smirk growing wider at the sight of the girl like this."
    Loli "W-What are you trying to do?"
    "She stuttered, as she hasn't experienced something like this before."
    "Even though she had a disability that made her physically frail, no one had dared to cross her in any way due to her status as well as the fact that she can make anyone feel intimidated and fearful of her thanks to her intelligence."
    "Unfortunately for her, I wasn't one of those people."
    Edgy "I'm trying to see how much of a 'fan' you are,"
    "I chuckled in amusement."
    Edgy "And it seems that you really are one if I can get a reaction like this from you."
    "She was forced to turn her head away. She hated feeling helpless, but there's no way she could win against me like this."
    Loli "P-Please keep your distance from me, Ayanokouji-kun."
    Edgy "And if I don't? What exactly are you going to do?"
    "Kiyotaka smirked at her."
    Edgy "As you said, the cameras here aren't working, no one's going to see this. Will you push me away? I want to see you try."
    Loli "I-I'll scream for help,"
    "Sakayanagi knew that she was losing this battle and she hated it, especially now when she could feel her heart beating faster than before."
    Edgy "Can you even do that? Will you even do that?"
    "I challenged her, making her frown at me."
    "Despite her earlier threat, I wasn't even taking her seriously and it was annoying her."
    "She almost looked like a poor cat who had her favorite ball of yarn taken from her."
    Edgy "Something tells me that you're only lying to yourself, Sakayanagi."
    "She tried to flash a smirk of her own in an attempt to fight back, but was obviously failing due to the fact that her body began to tremble."
    Loli "How would you know? It's not like you can read minds, Ayanokouji-kun."
    Edgy "I can't, but..."
    "I lifted her chin with a finger, forcing her to look up at him as her eyes widened."
    Edgy "I can read your body language, Sakayanagi. I actually think that you're even liking this."
    "All Arisu could do was stare at me, completely helpless to do anything else."
    "Our faces were so close to each other that I could lean in and kiss her if I wanted to."
    "Even if she didn't want to, she couldn't actually do anything to stop me."
    "And so, surrendering to logic and Kiyotaka himself, Arisu simply closed her eyes and waited for something to happen, but nothing did."
    "When she opened her eyes though, she quickly noticed that I leaned close to her ear instead."
    Edgy "You have no chance of beating me, Sakayanagi. Especially not when you act like this around me,"
    "I whispered into her ear, which managed to send a chill down her spine."
    Edgy "Still, I might enjoy your company. While we have never met each other like this in the past, I feel that you and I have a certain connection that can't be imitated by anyone else."
    "And with that, I moved away from the her and got a good look at her blushing face as he heard the snapping of a camera followed by the familiar musical chime that the system had."
    show screen system_1("Superior into Inferior' was added to the gallery!",0.5,0.5)
    "I ignored both screens in favor of Arisu herself blushing in front of him like an embarrassed schoolgirl."
    "Her smug demeanor was nowhere to be found and while I was tempted to play around with her for a bit longer"
    "I wanted to rest his body so he should end this now."
    Edgy "Have a good night Arisu,"
    "I sent her one final smirk before I turned around and walked back to my unit."
    "I heard the sound of a door slamming shut behind him, several notifications then appeared in front of Kiyotaka."
    "~ end of test ~"
    return

screen system_1(textShow,xAlign,yAlign):
    #background "images/background/screen.png"
    frame:
        xpadding 30
        ypadding 30
        xalign xAlign
        yalign yAlign
        text textShow xalign 0.5 yalign 0.5

screen system_2(textShow,xAlign,yAlign):
    #background "images/background/screen.png"
    frame:
        xpadding 30
        ypadding 30
        xalign xAlign
        yalign yAlign
        text textShow xalign 0.5 yalign 0.5

