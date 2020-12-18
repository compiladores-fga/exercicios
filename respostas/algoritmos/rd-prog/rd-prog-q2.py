import re

grammar = """
value : lst | var | pair
lst   : "[" [value ("," value)*] "]"
pair  : "(" value ":" value ")"
var   : /[a-z]+/
"""


class Token(str):
  kind : str
  def __new__(cls, value, kind):
    tk = str.__new__(cls, value)
    tk.kind = kind
    return tk

  def __repr__(self):
    value = super().__repr__()
    return value


REGEX_MAP = {
  "var" : r"[a-z]+",
  "op"  : r"[\[\],():]",
  "ws"  : r"\s+",
  "erro": r"."
}

REGEX = re.compile("|".join(f"(?P<{k}>{v})" for k, v in REGEX_MAP.items()))


def lex(str):
  tokens = []
  for m in REGEX.finditer(str):
    kind = m.lastgroup
    value = str[m.start():m.end()]
    tk = Token(value, kind)
    if kind == "ws":
      continue 
    elif kind == "erro":
      raise SyntaxError(r"Bad token: {tk}")
    else:
      tokens.append(tk)
  return tokens


def expect(tk, tokens):
  aux_tk = tokens[0]
  if aux_tk != tk:
    raise SyntaxError(f"Bad token: {aux_tk}")
  return tokens.pop(0)


def parse(str):
  tokens = lex(str)
  tokens.append("$")
  res = value(tokens)
  if tokens != ["$"]:
    raise SyntaxError("espera o fim do arquivo")
  return res


def value(tokens):
    if tokens[0] == "[":
        return lst(tokens)
    elif tokens[0] == "(":
        return pair(tokens)
    
    tk = tokens.pop(0)
    if tk.kind == "var":
        return tk


def lst(tokens):
    expect("[", tokens)
    if(tokens[0] == "]"):
        tokens.pop(0)
        return[]
    
    arr_tk = [value(tokens)]
    
    tk = tokens.pop(0)
    while tk == ",":
        arr_tk.append(value(tokens))
        tk = tokens.pop(0)
    if tk != "]":
        raise SyntaxError(f"Bad token: {tk}")
    return arr_tk


def pair(tokens):
    expect("(", tokens)
    left = value(tokens)
    expect(":", tokens)
    right = value(tokens)
    expect(")", tokens)
    return (left, right)
    

src = "[a,b,(c:d),[ab,cd,ef]]"
assert parse(src) == ["a", "b", ("c", "d"), ["ab", "cd", "ef"]]