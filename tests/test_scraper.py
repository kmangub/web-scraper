import pytest
from scraper import get_citations_needed_count, get_citations_needed_report

url = 'https://en.wikipedia.org/wiki/Loch_Ness_Monster'

def test_get_citation_needed_count():
    actual = get_citations_needed_count(url)
    expected = 4
    assert actual == expected


# def test_get_citations_needed_report():
#     actual = get_citations_needed_report(url)
#     expected = '''
#     On 21 May 1977 Anthony "Doc" Shiels, camping next to Urquhart Castle, took "some of the clearest pictures of the monster until this day".[citation needed] Shiels, a magician and psychic, claimed to have summoned the animal out of the water. He later described it as an "elephant squid", claiming the long neck shown in the photograph is actually the squid's "trunk" and that a white spot at the base of the neck is its eye. Due to the lack of ripples, it has been declared a hoax by a number of people and received its name because of its staged look.[59][60]

#     On 24 August 2011 Loch Ness boat captain Marcus Atkinson photographed a sonar image of a 1.5-metre-wide (4.9 ft), unidentified object that seemed to follow his boat for two minutes at a depth of 23 m (75 ft), and ruled out the possibility of a small fish or seal. In April 2012, a scientist from the National Oceanography Centre said that the image is a bloom of algae and zooplankton.[citation needed]

#     In 1972, a group of researchers from the Academy of Applied Science led by Robert H. Rines conducted a search for the monster involving sonar examination of the loch depths for unusual activity. Rines took precautions to avoid murky water with floating wood and peat.[citation needed] A submersible camera with a floodlight was deployed to record images below the surface. If Rines detected anything on the sonar, he turned the light on and took pictures.

#     In 1972 a team of zoologists from Yorkshire's Flamingo Park Zoo, searching for the monster, discovered a large body floating in the water. The corpse, 4.9–5.4 m (16–18 ft) long and weighing as much as 1.5 tonnes, was described by the Press Association as having "a bear's head and a brown scaly body with clawlike fins." The creature was placed in a van to be carried away for testing, but police seized the cadaver under an act of parliament prohibiting the removal of "unidentified creatures" from Loch Ness. It was later revealed that Flamingo Park education officer John Shields shaved the whiskers and otherwise disfigured a bull elephant seal that had died the week before and dumped it in Loch Ness to dupe his colleagues.[citation needed] On 2 July 2003, Gerald McSorely discovered a fossil, supposedly from the creature, when he tripped and fell into the loch. After examination, it was clear that the fossil had been planted.[141]
#     '''
#     assert actual == expected

