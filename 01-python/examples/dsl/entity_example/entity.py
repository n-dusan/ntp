from textx import metamodel_from_file


class SimpleType(object):
    def __init__(self, parent, name):  # remember to include parent param.
        self.parent = parent
        self.name = name


myobjs = {'integer': SimpleType(None, 'integer'),
          'string': SimpleType(None, 'string')}

if __name__ == '__main__':
    entity_mm = metamodel_from_file('entity.tx',
                                    classes=[SimpleType],
                                    builtins=myobjs)
    m = entity_mm.model_from_file("example.entity")
    print(m)
    print(m.entities)
