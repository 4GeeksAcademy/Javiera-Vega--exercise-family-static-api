"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
            
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## You have to implement this method
        ## Append the member to the list of _members
        first_name = member.get("first_name")
        age = member.get("age")
        lucky_numbers = member.get("lucky_numbers")

        if first_name is None or type(first_name) is not str:
            return None
        if age is None or type(age) is not int or age <= 0:
            return None
        if lucky_numbers is None or type(lucky_numbers) is not list:
            return None 
        
        new_member = {
            "id": self._generate_id(),
            "first_name": first_name,
            "last_name": self.last_name,
            "age": age,
            "lucky_numbers": lucky_numbers
        }
        self._members.append(new_member)
        return new_member

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        array_length = len(self._members)
        self._members = list(filter(lambda item : item["id"] != id, self._members))
        if len(self._members) < array_length:
            return True
        else:
            return False

    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        member = list(filter(lambda item : item["id"] == id, self._members))
        if member:
            return member[0]
        else:
            return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members