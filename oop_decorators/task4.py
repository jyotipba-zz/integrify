from collections import namedtuple,OrderedDict



class PersonalJoiner:
    @staticmethod
    def joined(*args, **kwargs):
            h = OrderedDict()
            for arg in args:
                dd = arg._asdict()
                h.update(dd)
            person = namedtuple('person',h.keys())(*h.values())
            return person


PersonalDetails = namedtuple('PersonalDetails', 'date_of_birth')
person1_details = PersonalDetails('09-04-1991')

person_features = namedtuple('person_features','eye_color IQ_score')
person_1_features = person_features('green', 10)

print(PersonalJoiner.joined(person1_details,person_1_features,))
