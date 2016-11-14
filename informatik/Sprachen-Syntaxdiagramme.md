# Syntaxdiagramme

## Wie lässt sich die Syntax formaler Sprachen so präzise beschreiben, dass man nur mit Hilfe dieser Beschreibung entscheiden ann, ob ein Wort zur jeweiligen Sprache gehört oder nicht?

## Aus welchen Bestandteilen setzen sich Syntaxdiagramme zusammen?

- Terminalsymbole
- Nichtterminalsymbole
- Vebindungspfeile

## Zwischen welchen Konstruktionsmustern unterscheidet man bei Syntaxdiagrammen?

- Sequenz
- Alternative
- Iteration
- Rekursion

## Gibt für den gegebenen Rechenausdruck eine Wegbeschreibung durch die Sytaxdiagramme Ausdruck, Summand, Faktor, Variable, Zahl und Ziffer an.

### x-y-2

Ausdruck ->
Variable - Variable - Ziffer ->
(x - y) - 2


### x-(y-2)

Ausdruck ->
Variable - Summand ->
x - (Variable - Ziffer) ->
x - (y - 2)

### (x+y)\*(x-y)

Ausdruck ->
Faktor ->
Summand * Summand ->
(Variable + Variable) \* (Variable - Variable) ->
(x+y)\*(x-y)
