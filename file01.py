# elágazás / szelekció / "if - if+else - elif..."

# if (ha) <logikai értéket visszaadó feltétel>:
    # egy indentációval (bekezdéssel/behúzással) jobbra 
    # az a szubrutin, ami akkor fut le,
    # ha a feltétel True (igaz) értéket ad vissza
# else (különben):
    # elhagyható, nem kell feltétlenül else ágat írni
    # egy indentációval (bekezdéssel/behúzással) jobbra 
    # az a szubrutin, ami akkor fut le,
    # ha az if utáni feltétel False (hamis) értéket ad vissza

# ciklus(ok) / iteráció / két fajta van pythonban: for és a while

# for ciklus - ún. 'bejáró' ciklus:

# for <valamilyen változónév> in <a kollekció referenciája, amit bejárunk>:
    # egy indentációval (bekezdéssel/behúzással) jobbra
    # egy szubrutin, amiben a változó felveszi a kollekció elemeit
    # addig ismétlődik a szubrutin,
    # amíg a kollekció minden egyes eleme sorra nem kerül

# while ciklus - ún. "feltételes" vagy elöltesztelős ciklus

# while (amíg) <logikai értéket visszaadó feltétel>:
    # egy indentációval (bekezdéssel/behúzással) jobbra
    # egy szubrutin, ami addig ismétlődik
    # amíg a feltétel igaz
    # megjegyzés 1: ha a feltétel igaz, és soha nem módosul, az egy ún.
    # "végtelen ciklust" eredményezhet
    # megjegyzés 2: ha a ciklus megkezdése előtt a feltétel hamis
    # a ciklus törzsében lévő szubrutin SOHA nem fog lefutni