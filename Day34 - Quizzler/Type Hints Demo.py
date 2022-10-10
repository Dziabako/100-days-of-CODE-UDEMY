# W ten sposob deklarujemy typ zmiennej jaki ma ona przyjac
# Podpowiada to nam pozniej jaki typ powinna miec okreslona zmienna / Wykrywanie potencjalnych bugow w dlugim kodzie
age: int
name: str
height: float
is_human: bool


# To samo co wyzej / Po strzalce okreslane sa typy danych jakie maja byc zwracane
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")







