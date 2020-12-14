import random
import math
yes = ["yes", "sure", "affirmative", "fine", "indeed", "of course", "positively", "unquestionably", "naturally", "surely", "undoubtedly", "very much so", "si", "definitely", "without a doubt", "aye", "yes, sir", "sir, yes, sir", "yes sir", "sir yes sir", "yes ma'am", "yes maam", "ay", "absolutely", "yeah", "yeah, yeah", "let's do this", "lets do this", "yea", "yep", "aye aye, captain", "aye, aye, captain", "aye aye captain", "ok", "aye aye", "aye, aye", "aye-aye", "okay", "alright", "alrighty", "ok then", "alright, then", "okay then", "alrighty then", "alright, then", "okie dokie", "oky doky", "okiey dokiey", "oki doki", "okie doki", "sure", "ya", "yah", "sí", "1"]
no = ""
ok = "okey"
while ok.lower() not in yes and ok.lower() not in ["", "no"]:
    if ok.lower() not in yes:
        print("Please don't leave any punctuation or extra characters in your responses. Press \"RETURN\" or \"ENTER\" to move on.")
    ok = input()
    if ok.lower() == "no":
        print("Alright, smarty-pants.")
    elif ok == "1":
        print("01110100011010000110000101101110011010110010000001111001011011110111010100101110")
    elif ok in yes or ok == "":
        print("Thank you.")
    else:
        print("Please provide a valid response, like \"yes\".")
while no.lower() not in yes and no.lower() not in ["no", "0"] and ok.lower() != "no":
    print("Are you ready for classical conditioning?")
    no = input()
    if no.lower() == "no":
        print("Fair enough.")
    elif no.lower() == "let's do this" or no.lower() == "lets do this":
        print("That's the spirit!")
    elif no.lower() == "fine" or no.lower() == "sure":
        print("What do you mean, \"" + no.lower() + "\"?")
    elif no.lower() in ["doki", "doki doki"]:
        print("Do you mean \"okie dokie\", Super Mario Bros. 2 USA in Japan, or the psychological horror visual novel?")
    elif no.lower() == "okey":
        print("Do you mean \"okay\", or are you imitating Ness? Either way, that isn't even a grammatically correct response.")
    elif no.lower() == "1":
        print("011101000110100001100101011100100110010100100000011101110110010100100000011001110110111100100001")
    elif no.lower() == "0":
        print("01100010011110010110010100101101011000100111100101100101")
    elif no.lower() in ["si", "sí"]:
        print("¡Aquí vamos!")
    elif no.lower() in yes:
        print("There we go!")
    else:
        print("I can't hear you!")
if no.lower() not in ["no", "0"] and ok.lower() != "no":
    if no.lower() == "fine":
        print("E", end="")
    else:
        print("Please e", end="")
    print("njoy all the references and easter eggs that you probably won't find.")
enjoy = input()
if enjoy.lower() == "no":
    print("You do you, (wo)man.\n")
restart = "yes"
while no not in ["no", "0"] and restart == "yes" and ok.lower() != "no":
    correctAnswers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    randomizer = ""
    wordList = ["analyze", "assess", "calculate", "comment", "compare", "consider", "contrast", "define", "demonstrate", "describe", "develop", "discuss", "evaluate", "examine", "explain", "give", "identify", "justify", "outline", "predict", "sketch", "state", "suggest", "summarize"]
    print("Your words are:")
    while sum(correctAnswers) < 24:
        randomNumber = random.randint(0, 23)
        if correctAnswers[randomNumber] == 0:
            print(wordList[randomNumber])
            correctAnswers[randomNumber] = 1
    while randomizer not in ["0", "1"]:
        print("\nIf you would like the questions to be in a preset order, please type \"0\" and press \"RETURN\"/\"ENTER\".\nIf you would like the questions to be randomized, please type \"1\" and press \"RETURN\"/\"ENTER\"\nThe word bank, however, will always be randomized.")
        randomizer = input()
        if randomizer not in ["0", "1"]:
            print("Please type in only one of the two options.")
    correctAnswers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Feel free to answer with any kind of capitalization. Every word is a present-tense verb, but alternate suffixes are allowed.\nRoot words are encouraged and yield a full point rather than part of one.\nPress \"RETURN\"/\"ENTER\" to continue.")
    input()
    randomNumber = 0
    retry = "yes"
    if randomizer == "1":
        randomNumber = random.randint(0, 23)
    while math.ceil(correctAnswers[0]) + math.ceil(correctAnswers[1]) + math.ceil(correctAnswers[2]) + math.ceil(correctAnswers[3]) + math.ceil(correctAnswers[4]) + math.ceil(correctAnswers[5]) + math.ceil(correctAnswers[6]) + math.ceil(correctAnswers[7]) + math.ceil(correctAnswers[8]) + math.ceil(correctAnswers[9]) + math.ceil(correctAnswers[10]) + math.ceil(correctAnswers[11]) + math.ceil(correctAnswers[12]) + math.ceil(correctAnswers[13]) + math.ceil(correctAnswers[14]) + math.ceil(correctAnswers[15]) + math.ceil(correctAnswers[16]) + math.ceil(correctAnswers[17]) + math.ceil(correctAnswers[18]) + math.ceil(correctAnswers[19]) + math.ceil(correctAnswers[20]) + math.ceil(correctAnswers[21]) + math.ceil(correctAnswers[22]) + math.ceil(correctAnswers[23]) < 23:
        if sum(correctAnswers) > 0:
            print("Score: " + str(sum(correctAnswers)) + "/24.")
        if retry == "no" and randomizer == "0":
            randomNumber = randomNumber + 1
            retry = "yes"
        if retry == "no" and randomizer == "1":
            randomNumber = random.randint(0, 23)
            retry = "yes"
        if randomNumber > 23:
            randomNumber = 0
        while randomizer == "0" and correctAnswers[randomNumber] > 0 and randomNumber <= 23:
            randomNumber += 1
            if randomNumber > 23:
                randomNumber = 0
        while randomizer == "1" and correctAnswers[randomNumber] > 0:
            randomNumber = random.randint(0, 23)
            if randomNumber > 23:
                randomNumber = 0
        retry = "yes"
        print("What's the word for ", end="")
        while retry in yes and randomNumber == 0:
            print("examining in detail to show meaning, and identifying elements and the relationship between them?")
            answer = input()
            if answer.lower() == "analyze":
                print("Correct! +1 point.")
                correctAnswers[0] = 1
                retry = 0
            elif answer.lower() in ["analyse", "analysing", "analysed"]:
                print("This spelling, although used in the photo attached to the assignment, isn't correct in America. The correct spelling is \"analyze.\"\nI'll give you 0.75 points anyway.")
                correctAnswers[0] = 0.75
                retry = 0
            elif answer.lower() in ["analysis", "analyzing", "analyzed", "analyses", "analyzes"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[0] = 0.5
                retry = 0
            else:
                if answer.lower() == "anal":
                    print("I think you mean a different word. Yeah, you definitely meant a different word.\nI", end="")
                else:
                    print("Not quite. I don't recognize that word, but i", end="")
                print("f you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 1:
            print("making an informed judgement?")
            answer = input()
            if answer.lower() == "assess":
                print("Correct! +1 point.")
                correctAnswers[1] = 1
                retry = 0
            elif answer.lower() in ["assessment", "assessing", "assessed", "assesses", "assessments"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[1] = 0.5
                retry = 0
            else:
                if answer.lower() in ["ass", "asses"]:
                    print("Woah, there! That isn't the right spelling, nor is it school-appropriate.\nI", end="")
                else:
                    print("Not quite. I don't recognize that word, but i", end="")
                print("f you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 2:
            print("working out from given facts?")
            answer = input()
            if answer.lower() == "calculate":
                print("Correct! +1 point.")
                correctAnswers[2] = 1
                retry = 0
            elif answer.lower() in ["calculating", "calculated", "calculates"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[2] = 0.5
                retry = 0
            elif answer.lower() in ["calculator", "calculators"]:
                print("Close enough... +0.25 points.")
                correctAnswers[2] = 0.25
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 3:
            print("giving an informed opinion?")
            answer = input()
            if answer.lower() == "comment":
                print("Correct! +1 point.")
                correctAnswers[3] = 1
                retry = 0
            elif answer.lower() in ["commenter", "commenting", "commented", "comments"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[3] = 0.5
                retry = 0
            elif answer.lower() in ["commentate", "commentator", "commentating", "commentated", "commentates"]:
                print("Close enough... +0.25 points.")
                correctAnswers[3] = 0.25
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 4:
            print("identifying/commenting on similarities and/or differences?")
            answer = input()
            if answer.lower() in ["comparing", "compared", "comparison", "compares", "comparisons"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[4] = 0.5
                retry = 0
            elif answer.lower() == "compare":
                print("Correct! +1 point.")
                correctAnswers[4] = 1
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 5:
            print("reviewing and responding to given information?")
            answer = input()
            if answer.lower() in ["considered", "considering", "consideration", "considerations", "considers"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[5] = 0.5
                retry = 0
            elif answer.lower() == "consider":
                print("Correct! +1 point.")
                correctAnswers[5] = 1
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 6:
            print("identifying and commenting on differences?")
            answer = input()
            if answer.lower() in ["contrasting", "contrasted", "contrasts"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[6] = 0.5
                retry = 0
            elif answer.lower() == "contrast":
                print("Correct! +1 point.")
                correctAnswers[6] = 1
                retry = 0
            else:
                if answer.lower() == "contra":
                    print("Contra? Unless you mean the video game franchise developed by Konami, I think you made a typo.\nI", end="")
                else:
                    print("Not quite. I don't recognize that word, but i", end="")
                print("f you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 7:
            print("giving a precise meaning?")
            answer = input()
            if answer.lower() in ["definition", "defined", "defining", "definitions", "defines"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[7] = 0.5
                retry = 0
            elif answer.lower() == "define":
                print("Correct! +1 point.")
                correctAnswers[7] = 1
                retry = 0
            elif answer.lower() in ["refine", "refines", "refined", "refining"]:
                print("Close enough... +0.25 points.")
                correctAnswers[7] = 0.25
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 8:
            print("showing how or giving an example?")
            answer = input()
            if answer.lower() in ["demonstrating", "demonstrated", "demonstration", "demonstrations", "demonstrates"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[8] = 0.5
                retry = 0
            elif answer.lower() == "demonstrate":
                print("Correct! +1 point.")
                correctAnswers[8] = 1
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 9:
            print("stating the points of a topic/giving characteristics and main features?")
            answer = input()
            if answer.lower() in ["description", "describing", "described", "descriptions", "describes"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[9] = 0.5
                retry = 0
            elif answer.lower() == "describe":
                print("Correct! +1 point.")
                correctAnswers[9] = 1
                retry = 0
            elif answer.lower() in ["prescribe", "prescription", "prescribes", "prescribed", "prescribing"]:
                print("Close enough... +0.25 points.")
                correctAnswers[9] = 0.25
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 10:
            print("taking forward to a more advanced stage or building upon given information?")
            answer = input()
            if answer.lower() in ["development", "developing", "developed", "develops", "developments"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[10] = 0.5
                retry = 0
            elif answer.lower() == "develop":
                print("Correct! +1 point.")
                correctAnswers[10] = 1
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 11:
            print("writing about issues or topics in depth in a structured way?")
            answer = input()
            if answer.lower() in ["discussion", "discussed", "discussing", "discusses", "discussions"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[11] = 0.5
                retry = 0
            elif answer.lower() == "discuss":
                print("Correct! +1 point.")
                correctAnswers[11] = 1
                retry = 0
            elif answer.lower() == "discus":
                print("Unless you're talking about the fish or the throwing disc, that's the wrong spelling. Still, +0.75 points for effort.")
                correctAnswers[11] = 0.75
                retry = 0
            elif answer.lower() == "discuses":
                print("Unless you're talking about fish or throwing discs, that's the wrong spelling. +0.5 points for anyway.")
                correctAnswers[11] = 0.5
                retry = 0
            elif answer.lower in ["disscus", "disscuss", "disscussing", "disscussion", "disscusses", "disscussed", "disscusing", "disscused", "disscuses", "disscusion"]:
                print("Close enough... +0.25 points.")
                correctAnswers[11] = 0.25
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 12:
            print("judging or calculating the quality, importance, amount, or value of something?")
            answer = input()
            if answer.lower() in ["evaluation", "evaluated", "evaluating", "evaluates", "evaluations"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[12] = 0.5
                retry = 0
            elif answer.lower() == "evaluate":
                print("Correct! +1 point.")
                correctAnswers[12] = 1
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 13:
            print("investigating closely, in detail?")
            answer = input()
            if answer.lower() in ["examination", "examined", "examining", "examinations", "examines"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[13] = 0.5
                retry = 0
            elif answer.lower() == "examine":
                print("Correct! +1 point.")
                correctAnswers[13] = 1
                retry = 0
            elif answer.lower() in ["exam", "exams"]:
                print("This isn't even a verb, but sure. +0.25 points.")
                correctAnswers[13] = 0.25
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 14:
            print("setting out purposes or reasons/making the relationships between things being clear/saying why and/or how and supporting with relevant evidence?")
            answer = input()
            if answer.lower() in ["explanation", "explaining", "explained", "explains", "explanations"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[14] = 0.5
                retry = 0
            elif answer.lower() == "explain":
                print("Correct! +1 point.")
                correctAnswers[14] = 1
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 15:
            print("producing an answer from a given source or recall/memory?")
            answer = input()
            if answer.lower() in ["given", "giving", "gave", "gives", "givings"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[15] = 0.5
                retry = 0
            elif answer.lower() == "give":
                print("Correct! +1 point.")
                correctAnswers[15] = 1
                retry = 0
            else:
                print("Not quite.", end="")
                if answer.lower() == "thanksgiving":
                    print("...That was a month ago as of this program's creation.\nI", end="")
                else:
                    print(" I don't recognize that word, but i", end="")
                print("f you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 16:
            print("a name/selection/recognition?")
            answer = input()
            if answer.lower() in ["identification", "identified", "identifying", "identifies"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[16] = 0.5
                retry = 0
            elif answer.lower() == "identify":
                print("Correct! +1 point.")
                correctAnswers[16] = 1
                retry = 0
            elif answer.lower() == "id":
                print("Close enough... +0.25 points.")
                correctAnswers[16] = 0.25
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 17:
            print("supporting a case with evidence/an argument?")
            answer = input()
            if answer.lower() in ["justification", "justifying", "justified", "justifies", "justification"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[17] = 0.5
                retry = 0
            elif answer.lower() == "justify":
                print("Correct! +1 point.")
                correctAnswers[17] = 1
                retry = 0
            elif answer.lower() in ["justice", "justices"]:
                print("Close enough... +0.25 points.")
                correctAnswers[17] = 0.25
                retry = 0
            else:
                if answer.lower() in ["juice", "juices"]:
                    print(answer.title() + "? Are you sure you're not just thirsty?\nI", end="")
                else:
                    print("Not quite. I don't recognize that word, but i", end="")
                print("f you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 18:
            print("setting out the main points?")
            answer = input()
            if answer.lower() in ["outlining", "outlined", "outlines"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[18] = 0.5
                retry = 0
            elif answer.lower() == "outline":
                print("Correct! +1 point.")
                correctAnswers[18] = 1
                retry = 0
            elif answer.lower() in ["out", "line", "outing", "outings", "lining", "lines", "outed", "outs", "lined"]:
                print("Close enough... +0.25 points.")
                correctAnswers[18] = 0.25
                retry = 0
            elif answer.lower() in ["silver lining", "line up", "lining up", "lined up"]:
                print("You know, you're lucky I'm even giving you .1 point right now.")
                correctAnswers[18] = 0.1
                retry = 0
            elif answer.lower() in ["line down", "lining down", "lined down"]:
                print("No.")
                retry = "no"
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 19:
            print("suggesting what may happen based on available information?")
            answer = input()
            if answer.lower() in ["prediction", "predicted", "predicting", "predicts", "predictions"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[19] = 0.5
                retry = 0
            elif answer.lower() == "predict":
                print("Correct! +1 point.")
                correctAnswers[19] = 1
                retry = 0
            elif answer.lower() in ["verdict", "verdicts", "jurisdiction", "jurisdictions"]:
                print("Close enough... +0.25 points.")
                correctAnswers[19] = 0.25
                retry = 0
            else:
                if answer.lower() in ["verdiction", "verdictions"]:
                    print("Uh... not quite...\nI", end="")
                else:
                    print("Not quite. I don't recognize that word, but i", end="")
                print("f you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 20:
            print("making a simple freehand drawing showing the key features, taking care over proportions?")
            answer = input()
            if answer.lower() in ["sketching", "sketched", "sketches"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[20] = 0.5
                retry = 0
            elif answer.lower() == "sketch":
                print("Correct! +1 point.")
                correctAnswers[20] = 1
                retry = 0
            elif answer.lower() in ["catch", "catching", "catcher", "pitch", "pitcher", "pitching", "pitched", "catchers", "catches", "pitches", "pitchers"]:
                print("Close enough... +0.25 points.")
                correctAnswers[20] = 0.25
                retry = 0
            elif answer.lower() in ["sketchers", "sketcher"]:
                print("What do shoes have to do with vocabulary...? +.2 for effort, I guess.")
                correctAnswers[20] = 0.2
                retry = 0
            elif answer.lower() in ["pitchster", "pitchsters"]:
                print("Get that word away from me.")
                correctAnswers[20] = 0.1
                retry = 0
            elif answer.lower() == "catchster":
                print("What.")
                correctAnswers[20] = 0.01
                retry = 0
            elif answer.lower() == "catchsters":
                print("Oh god, now there are two (or more) of them.")
                correctAnswers[20] = 0.02
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 21:
            print("expressing in clear terms?")
            answer = input()
            if answer.lower() in ["statement", "stating", "stated", "statements", "states"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[21] = 0.5
                retry = 0
            elif answer.lower() == "state":
                print("Correct! +1 point.")
                correctAnswers[21] = 1
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 22:
            print("applying knowledge and understanding to situations where there are a range of valid responses to make proposals/put forward considerations?")
            answer = input()
            if answer.lower() in ["suggestion", "suggested", "suggesting", "suggests", "suggestions"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[22] = 0.5
                retry = 0
            elif answer.lower() == "suggestive":
                print("Uh... not quite. +0.25 for effort.")
                correctAnswers[22] = 0.25
                retry = 0
            elif answer.lower() == "suggest":
                print("Correct! +1 point.")
                correctAnswers[22] = 1
                retry = 0
            else:
                print("Not quite. I don't recognize that word, but if you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
        while retry in yes and randomNumber == 23:
            print("choosing and presenting the main points, without detail?")
            answer = input()
            if answer.lower() in ["summary", "summarizing", "summarized", "summarizes", "summaries"]:
                print("Close! I'll give you 0.5 points.")
                correctAnswers[23] = 0.5
                retry = 0
            elif answer.lower() == "summarize":
                print("Correct! +1 point.")
                correctAnswers[23] = 1
                retry = 0
            else:
                if answer.lower() in ["summer", "summers"]:
                    print("That's a season, not a verb. This program wasn't even made during summer.\nI", end="")
                else:
                    print("Not quite. I don't recognize that word, but i", end="")
                print("f you want, you can retry this question. Would you like to?")
                retry = ""
                while retry not in yes and retry != "no":
                    retry = input()
                    if retry in yes:
                        print("What's the word for ", end="")
                    elif retry == "no":
                        print("Ok then.")
                    else:
                        print("I don't recognize this word, either.\nWould you like to retry the question?")
    print("You did it! Your final score is " + str(sum(correctAnswers)) + "/24")
    restart = ""
    while restart.lower() != "no" and restart.lower() not in yes:
        print("Would you like to try again?")
        restart = input()
        if restart.lower() == "no":
            print("Thanks for using this program!")
        elif restart.lower() in ["fine", "sure"]:
            print(restart.title() + "? That's not very nice...")
        elif restart.lower() not in yes:
            print("That wasn't a \"no\", but it wasn't a \"yes\", either... at least, it doesn't seem like one to me.")
if no == "0":
    print("01110000011100100110010101110011011100110010000000100010[31m011100100110010101110100011101010111001001101110001000100010111100100010[31m011001010110111001110100011001010111001000100010001000000111010001101111001000000111000101110101011010010111010000101110")
else:
    print("Press \"RETURN\"/\"ENTER\" to quit.")
bye = input()
if bye.lower() == "no":
    print("Yes.")
