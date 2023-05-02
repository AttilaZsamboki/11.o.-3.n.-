# helytelen
IDEI_ÉV = 2023
felhasználó_kora = input('Hány éves vagy? ')
print(f'Te most {felhasználó_kora} éves vagy.')
# itt az error, alapértelmezetten az input funkcióra való válasz stringet ad vissza amit nem lehet kivonni az idei évből
születési_év = IDEI_ÉV - felhasználó_kora

# át kell alakítani a felhasználónak megadott értéket int-be
születési_év = IDEI_ÉV - int(felhasználó_kora)