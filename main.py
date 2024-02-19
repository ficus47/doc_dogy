import streamlit as st

try:
  if st.session_state["a"] == 0:
    st.session_state["a"] = 1
    st.balloons()
except Exception:
  st.session_state["a"] = 1
  st.balloons()

onglet = st.sidebar.selectbox("**Onglet** (vous pouvez chercher dans la barre :)", 
          [
           "Home",
           "les variables",
           "les fonctions",
           "les differentes fonction natives"
          ]
         )

if onglet == "Home":
  st.header("Bienvenue sur le site officiel de la documentation du Dogy ! ")
  con1 = st.container()

  con1.markdown("""
**Dogy est un language de programmation interpreté codé en C comme d'autres
language comme pythone, javascript, php, etc...**
""")

  con1.write("vous pouvez choisir les differentes documentation sur les coté .")

elif onglet == "les variables":
  st.title("les variables")

  con2 = st.container()
  con2.write(
    """
    en dogy, les variable peuvent etre declarée ou modifier comme ceci :
    """)

  con2.code("""
    a = 5
    ou
    b = dogy
    """)
  
  con2.write("""
  on y acceder en mettant leurs nom entre gillemé (")
  """)
  
  con2.code("""print("a")""")

  con2.write("ce code affichera :")
  con2.code(5)

  con2.markdown("""
l'interpreteur reconnait le type d'une vaiable automatiquement .\n
Et si je veux 5 comme un string me diriez vous ?\n
Et bien le dogy ne fais pas de difference\n
entre les deux donc pas besoin de s'enbeter avec ca !\n
""")

elif onglet == "les fonctions":
  st.title("les fonctions")

  con3 = st.container()
  con3.write(
  """
  **en dogy, il y a des fonctions native (heuresement :) que je detaillerait plus bas.
  quand une fonction retourne quelque chose, comme la fonction input() qui lit l'entrée de l'utilisateur,
  elle 'met' la valeur dans une variable nommé "output" .
  cette variable est normale et peut etre utilisé dans d'autre fonctions ou dans le code principal.
  exemple :**
  """)
  
  con3.code("""
  input(entrez votre nom svp :)

  print(bonjour, "output")
  """)

  con3.write("si j'entre 'ficus', ce code affichera :")
  con3.code("""bonjour ficus """)

elif onglet == "les differentes fonction natives":
  st.title("les differentes fonction natives")

  con4 = st.container()
  select = con4.selectbox("**choisissez une fonction natives**", 
                          [
                            "input", "print"
                          ])

  if select == "input":
    con4.write("**input()**\n")
    con4.write("cette fonction permet de lire l'entrée de l'utilisateur")
    con4.write("**exemple :**")
    con4.code("""
    input(entrez un nombre)
    print("output")
    """)
    con4.write("si j'entre '42', ce code affichera :")
    con4.code("""42""")
  elif select == "print":
    con4.write("**print()**\n")
    con4.write("cette fonction permet d'afficher un message")
    con4.write("**exemple :**")
    con4.code("""
    print(hello world)
    """)

    con4.write("ce code afficheras :")
    con4.code("""hello world""")
