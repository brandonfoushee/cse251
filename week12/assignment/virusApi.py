
import threading
import requests

hostName = "127.0.0.1"
serverPort = 8129

class Virus:

    def __init__(self, id, name, parents=None, family=None):
        self.id = id
        self.name = name
        self.parents = parents
        self.family = family

    @classmethod
    def createVirus(cls, data):
        return cls(data['id'], data['name'], data['parent_id'], data['family_id'])

    # the id is the family id of this virus's parents
    def add_parent(self, id):
        self.parents = id

    def add_family(self, id):
        self.family = id

    def get_dict(self):
        person_dict = {}

        person_dict["id"] = self.id
        person_dict["name"] = self.name
        person_dict["parent_id"] = self.parents
        person_dict["family_id"] = self.family

        return person_dict

    def __str__(self):
        output = f'id        : {self.id}\n'
        output += f'name      : {self.name}\n'
        output += f'parent id : {self.parents}\n'
        output += f'family id : {self.family}\n'
        return output

# ----------------------------------------------------------------------------


class Family:

    def __init__(self, id, virus1, virus2, offspring=[]):
        super().__init__()
        self.id = id
        self.virus1 = virus1
        self.virus2 = virus2
        self.offspring = offspring

    @classmethod
    def fromResponse(cls, data):
        return cls(data['id'], data['virus1_id'], data['virus2_id'], data['offspring'])

    def add_offspring(self, id):
        self.offspring.append(id)

    def get_dict(self):
        family_dict = {}

        family_dict["id"] = self.id
        family_dict["virus1_id"] = self.virus1
        family_dict["virus2_id"] = self.virus2
        ids = []
        for o in self.offspring:
            ids.append(o)
        family_dict["offspring"] = ids

        return family_dict

    def __str__(self):
        output = f'family id     : {self.id}\n'
        output += f'virus1       : {self.virus1}\n'
        output += f'virus2       : {self.virus2}\n'
        for o in self.offspring:
            output += f'offspring    : {o}\n'

        return output


class Pandemic:

    def __init__(self, start_family_id):
        super().__init__()
        self.viruses = {}
        self.families = {}
        self.start_family_id = start_family_id

    def add_virus(self, virus: Virus):
        if self.does_virus_exist(virus.id):
            print(
                f'ERROR: Virus with ID = {virus.id} Already exists in the tree')
        else:
            self.viruses[virus.id] = virus

    def add_family(self, family: Family):
        if self.does_family_exist(family.id):
            print(
                f'ERROR: Family with ID = {family.id} Already exists in the tree')
        else:
            self.families[family.id] = family

    def get_virus(self, id) -> Virus:
        if id in self.viruses:
            return self.viruses[id]
        raise Exception(
            f"The virus id '{id}' does not exist in list of possible viruses")

    def get_family(self, id) -> Family:
        if id in self.families:
            return self.families[id]
        raise Exception(
            f"The family id '{id}' does not exist in list of possible viruses")

    def get_virus_count(self):
        return len(self.viruses)

    def get_family_count(self):
        return len(self.families)

    def does_virus_exist(self, id):
        return id in self.viruses

    def does_family_exist(self, id):
        return id in self.families

    def display(self):
        print('\n\n')
        print(f'{" PANDEMIC DISPLAY ":*^40}')
        for family_id in self.families:
            fam = self.families[family_id]

            # Virus1
            virus1 = self.get_virus(fam.virus1)
            if virus1 == None:
                print(f'  Virus1: None')
            else:
                print(f'  Virus1: {virus1.name}')

            # Virus2
            virus2 = self.get_virus(fam.wife)
            if virus2 == None:
                print(f'  Virus2: None')
            else:
                print(f'  Virus2: {virus2.name}')

            # Parents of Virus1
            if virus1 == None:
                print(f'  Virus1 Parents: None')
            else:
                parent_fam_id = virus1.parents
                if parent_fam_id in self.families:
                    parent_fam = self.get_family(parent_fam_id)
                    parent1 = self.get_virus(parent_fam.virus1)
                    parent2 = self.get_virus(parent_fam.virus2)
                    print(
                        f'  Virus1 Parents: {parent1.name} and {parent2.name}')
                else:
                    print(f'  Virus1 Parents: None')

            # Parents of Wife
            if virus2 == None:
                print(f'  Virus2: None')
            else:
                parent_fam_id = virus2.parents
                if parent_fam_id in self.families:
                    parent_fam = self.get_family(parent_fam_id)
                    virus1 = self.get_virus(parent_fam.virus1)
                    virus2 = self.get_virus(parent_fam.virus2)
                    print(f'  Virus2 Parents: {virus1.name} and {virus2.name}')
                else:
                    print(f'  Virus2 Parents: None')

            # offspring
            output = []
            for index, offspring_id in enumerate(fam.offspring):
                virus = self.viruses[offspring_id]
                output.append(f'{virus.name}')
            out_str = str(output).replace("'", '', 100)
            print(f'  Offspring: {out_str[1:-1]}')

        print('')
        print(f'Number of viruses                       : {len(self.viruses)}')
        print(
            f'Number of families                      : {len(self.families)}')
        print(
            f'Max generations                         : {self._count_generations(self.start_family_id)}')
        print(
            f'Viruses connected to first virus family : {self._test_number_connected_to_start()}')

    def _test_number_connected_to_start(self):
        # start with first family, how many connected to that family
        inds_seen = set()

        def _recurive(family_id):
            nonlocal inds_seen
            if family_id in self.families:
                # count virus in this family
                fam = self.families[family_id]

                virus1 = self.get_virus(fam.virus1)
                if virus1 != None:
                    if virus1.id not in inds_seen:
                        inds_seen.add(virus1.id)
                    _recurive(virus1.parents)

                virus2 = self.get_virus(fam.virus2)
                if virus2 != None:
                    if virus2.id not in inds_seen:
                        inds_seen.add(virus2.id)
                    _recurive(virus2.parents)

                for offspring_id in fam.offspring:
                    if offspring_id not in inds_seen:
                        inds_seen.add(offspring_id)

        _recurive(self.start_family_id)
        return len(inds_seen)

    def _count_generations(self, family_id):
        print("!!!!!! count generations, {family_id=}")
        max_gen = -1

        def _recurive_gen(id, gen):
            nonlocal max_gen
            print(f'@@@@@@@@@@@@@@ number of families = {self.families}')
            if id in self.families:
                if max_gen < gen:
                    max_gen = gen

                fam = self.families[id]

                virus1 = self.get_virus(fam.virus1)
                if virus1 != None:
                    _recurive_gen(virus1.parents, gen + 1)

                virus2 = self.get_virus(fam.virus2)
                if virus2 != None:
                    _recurive_gen(virus2.parents, gen + 1)

        _recurive_gen(family_id, 0)
        return max_gen + 1