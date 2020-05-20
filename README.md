Reversi melyet egy 8x8-as táblán játszanak. Fekete és fehér korongokat szoktak alkalmazni, jelen esetben a játékos 1-sel, a számítógép 2-sel 
van jelölve.

Szabályok: 
          Kezdetben a tábla közepén 2-2 korong található átlósan egymásnak, érvényes lépésnek az számít ha a játékos a korongját egy adott
lépésben úgy helyezi le a táblára, hogy közrefogja az ellenfél korongját egy már táblán lévő koronggal. Ezt követően a közrefogott korongot
magáévá teszi. A játék akkor ér véget ha már nincs több szabad mező a táblán, ekkor a nyertes az akinek több korongja van.

Implementálás:
          A játékosnak a programot elíndítva lehetősége lesz megadni a billenytűről, hogy hány kört szeretne játszani, és hogy milyen nehezségi
szinten. Időkorlátozást sajnos nem sikerült megvalósítani, mivel legtöbb pythonban írt függvény Linux operációs rendszer alatt futtatható,
valamint a paraméterek parancssorról való átvétele is hiányzik.

A program Alfa-beta nyesést alkalmazva számítja ki a számítógép számára a nyerő/előnyösebb stratégiát, melyet döntési fákra alapozva határoz
meg, majd a rekurzív hivásokból visszalépve válassza ki a legoptimálisabbat.

A program által használt heurisztikus függvény azt nézi meg, hogy mely sarkok foglaltak és ki által, azoknak növelve nyerési esélyeit, és
hogy ha az aktuális pozicióba lépne mekkora előnyre ( hány korongot nyerne a lépésen ) tesz szert.



