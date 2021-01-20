db.persons.aggregate([
    {$match: {gender: "female"}},
    {$group: {_id: {"$location.state"}, totalPersons: {$sum: 1}}}
]).pretty()