def writer(name, *args) -> None:

    with open('{name}.js'.format(name= name), 'w') as writer:

        for arg in args:

            writer.write('{arg}\n'.format(arg= arg))