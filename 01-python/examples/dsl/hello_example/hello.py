from textx import metamodel_from_file

if __name__ == '__main__':
    # kreiranje meta-modela
    hello_meta = metamodel_from_file('hello.tx')
    # vizualizacija meta-modela
    # $ textx visualize hello.tx
    # $ dot -Tpng -O hello.tx.dot

    # kreiranje modela iz datoteka
    example_hello_model = hello_meta.model_from_file('example.hello')
    # vizuelizacija modela
    # $ textx visualize hello.tx example.hello
    # $ dot -Tpng -O example.hello.dot
    print(example_hello_model)
