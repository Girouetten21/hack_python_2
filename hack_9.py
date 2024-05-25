"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(dicc):
    dicc.pop("bar", None)
    valor_foo = dicc["foo"].replace("k", "")
    valor_foo = valor_foo[0].upper() + valor_foo[1:]
    clave_foo = "Foo"
    new_dicc = {clave_foo: valor_foo}
    return new_dicc