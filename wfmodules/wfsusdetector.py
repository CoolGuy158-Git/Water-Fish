"""
Waterfish sus detector
----
Detects any sus sites.
Aka fishing sites and what not.
It does this by having a simple list of rules to follow of which sites might be sus.
rules include:
    any sites that contain domain names that looks like trusted sites.
    any sites that are basically a string of random numbers and letters.

it only warns the users however cuz the checker is not perfect meaning it could flag random safe sites,
or joke sites which are still not harmful like Guthib.
"""
import urllib.parse

def check(url, data):
    similarityList = []
    flags = []
    def checkCloseness(url):
        global similarityList
        """
        This func checks how close the domain name is to a known domain name.
        
        Uses something kinda like Hamming distance (I think) for now
        It compares every letter
        If any letter matches another make it 1 else 0
        Then calculate percentage
        and if percentage is over 50 flag
        """
        knownDomain = [
            "google", "youtube", "github", "facebook", "x", "twitter", "reddit", "pypi", "fiverr", "freelancer", "paypal", "wikipedia"
        ]
        similarityList = []
        url = url.lower()
        parsedurl = urllib.parse.urlparse(url)
        host = parsedurl.netloc
        host = host.replace("www.", "")
        domain = host.split(".")[0]
        domain = domain.replace(" ", "")
        for domains in knownDomain:
            letterdomains = list(domains)
            letterdomain = list(domain)
            for i in range(min(len(letterdomains), len(letterdomain))):
                if letterdomain[i] == letterdomains[i]:
                    similarityList.append(1)
                else:
                    similarityList.append(0)
            similarityList.append("|")
        chunks = []
        curent = []

        for item in similarityList:
            if item == "|":
                chunks.append(curent)
                curent = []
            else:
                curent.append(item)

        percentages = []
        for chunk in chunks:
            if len(chunk) == 0:
                continue
            percent = sum(chunk) / len(chunk) * 100
            percentages.append(percent)
            if data["devopts"] == "True":
                print("percent: " + str(percent) + "%")

        for percentagesThatViolateTheRulesOfTheGreatPondOfTheWaterFish in percentages: # Beutiful name indeed
            if percentagesThatViolateTheRulesOfTheGreatPondOfTheWaterFish > 50:
                flags.append("1")
                if data["devopts"] == "True":
                    print("Flagged first time due to: " + str(percentagesThatViolateTheRulesOfTheGreatPondOfTheWaterFish) + "%")
            else:
                flags.append("0")

    def checkReadable(url):
        """
        Now check if giberrish by counting consonants and number.

        if consonant is 50% of domain and if there's 2 num per 4 length of domain.
        """

        vowels = "aeiou"

        url = url.lower()
        parsedurl = urllib.parse.urlparse(url)
        host = parsedurl.netloc
        host = host.replace("www.", "")
        domain = host.split(".")[0]
        domain = domain.replace(" ", "")

        consonantStreak = 0
        numberCount = 0

        for letter in domain:
            if letter in vowels:
                pass
            else:
                consonantStreak += 1
            if letter.isdigit():
                numberCount += 1

        if consonantStreak >= len(domain) * 0.5 and numberCount > (len(domain) / 4) * 2:
            flags.append("1")
            if data["devopts"] == "True":
                print("Flagged second time due to: " + str(numberCount) + " number " + " and " + str(consonantStreak) + " consonants")
        else:
            flags.append("0")
    print()

    checkCloseness(url)
    checkReadable(url)

    amoutnOfOnes = 0

    for i in flags:
        if i == "1":
            amoutnOfOnes += 1
        else:
            pass
    if amoutnOfOnes == 1:
        return "Flagged"
    elif amoutnOfOnes == 2:
        return "Flagged TWICE"
    return "Unflagged"
