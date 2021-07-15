## List of words to an array

### Find
>([A-Za-z]+)$       	---- Alpha
>
>([0-9]+)$       	---- numbers

### Replace:
>'$1',

### Will turn a list like this
>should
>actually
>learn
>regex

### into this

>'should',
>'actually',
>'learn',
>'regex',



# Captures things in (brackets)
(\((?:\[??[^\[]*?\)))  


