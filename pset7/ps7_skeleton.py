import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        '''
        name: Name of the adoption center
        species_type: a dictionary represents pets that each adoption center holds
        location: (x,y) floating point coordinate of the adoption center location
        '''
        self.name = name
        self.location = location
        self.species_types = species_types
    def get_number_of_species(self, animal):
        '''returns count of specific specie'''
        if animal not in self.species_types:
            return 0
        return self.species_types[animal]
    def get_location(self):
        '''returns floating point location of adoption center'''
        return "(%.1f, %.1f)" %(self.location[0], self.location[1]) 
    def get_species_count(self):
        temp = self.species_types.copy()
        return temp
    def get_name(self):
        '''returns name of adoption center'''
        return self.name
    def adopt_pet(self, species):
        '''
        Adopting a pet decrement the value of the specific specie, if count reach 0 
        specie will be remove from dictionary
        '''
        if self.species_types[species] != 0:
            self.species_types[species] -= 1
            if self.species_types[species] == 0:
                self.species_types.pop(species)


class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        '''get_score(Name of adoption center)'''
        #base score is 1 * num_desired
        num_desired = adoption_center.get_number_of_species(self.get_desired_species())
        score = 1.0 * num_desired
        return score 

class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
    def get_score(self, adoption_center):
        num_desired = adoption_center.get_number_of_species(self.get_desired_species())
        score = 1.0 * num_desired
        num_other = 0
        for i in self.considered_species:
            if i in adoption_center.get_species_count():
                num_other += adoption_center.get_species_count()[i]
        return score + (0.3*num_other)

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species
    def get_score(self, adoption_center):
        num_desired = adoption_center.get_number_of_species(self.get_desired_species())
        num_feared = 0
        if self.feared_species in adoption_center.get_species_count():
            num_feared = adoption_center.get_species_count()[self.feared_species]
        score = (1.0 * num_desired) - (0.3*num_feared)
        if score < 0:
            return 0.0
        return score 


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
    def get_score(self, adoption_center):
        num_desired = adoption_center.get_number_of_species(self.get_desired_species())
        score = 1.0 * num_desired
        for i in self.allergic_species:
            if i in adoption_center.get_species_count():
                return 0.0
        return score

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness
        
    def get_score(self, adoption_center):
        num_desired = adoption_center.get_number_of_species(self.get_desired_species())
        score = 1.0 * num_desired
        lowest_effectiveness = 1.0
        for i in self.medicine_effectiveness:
            if i in adoption_center.get_species_count():
                if self.medicine_effectiveness[i] < lowest_effectiveness:
                    lowest_effectiveness = self.medicine_effectiveness[i]
        return score * lowest_effectiveness

            


import random
class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location
    def get_linear_distantance(self, adoption_center):
        #range for coordinate are -5.0 to 5.0
        to_location = adoption_center.get_location()
        result = ((to_location[0] - self.location[0])**2 + (to_location[1] - self.location[1])**2)**(0.5)
        return result 
    def get_score(self, adoption_center):
        num_desired = adoption_center.get_number_of_species(self.get_desired_species())
        distance = self.get_linear_distantance(adoption_center)
        if distance < 1:
            return 1 * num_desired
        elif distance < 3:
            return random.uniform(.7, .9) * num_desired
        elif distance < 5:
            return random.uniform(.5, .7) * num_desired
        else:
            return random.uniform(.1, .5) * num_desired
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here 
    result = []
    score_dict = {}
    for i in list_of_adoption_centers:
        score_dict[i] = adopter.get_score(i)
    result = sorted(score_dict, key=score_dict.__getitem__, reverse=True)
    for j in range(1, len(result)):
        print score_dict[result[j]]
        if score_dict[result[j-1]] == score_dict[result[j]]:
            if result[j-1] < result[j]:
                result[j-1], result[j] = result[j], result[j-1]
            
    return result

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 
    score_dict = {}
    result = None
    for i in list_of_adopters:
        score_dict[i] = i.get_score(adoption_center)
    result = sorted(score_dict, key=score_dict.__getitem__, reverse=True)
    for j in range(1, len(result)+1):
        if score_dict[result[j-1]] == score_dict[result[j]]:
            if result[j-1] < result[j]:
                result[j-1], result[j] = result[j], result[j-1]
    return result
'''
My personal test case

inventory = {'Dog': 5, 'Cat': 3, 'Rabbit': 1}
considered = ['Cat']
feared = 'Horse'
Allgeric = ['Cat']
Allergic2 = ['Dog', 'Rabbit']
petco = AdoptionCenter('Petco', inventory, (1,1))
John = FlexibleAdopter('John','Dog', considered)
Tom = FearfulAdopter('Tom', 'Dog', feared)
David = AllergicAdopter('David', 'Dog', Allgeric)
meds = {'Dog':0.0,'Rabbit':0.5}
Jason = MedicatedAllergicAdopter('Jason', 'Cat', Allergic2, meds)

'''

adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

# how to test get_adopters_for_advertisement
#get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
# you can print the name and score of each item in the list returned

adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac9 = AdoptionCenter("Place9", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))
ac7 = AdoptionCenter("Place7", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))
ac8 = AdoptionCenter("Place8", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
print get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac9,ac7,ac8])                            
# you can print the name and score of each item in the list returned
                            