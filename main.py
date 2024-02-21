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
           "les différentes fonctions natives"
          ]
         )

if onglet == "Home":
  st.header("Bienvenue sur le site officiel de la documentation du Dogy ! ")
  con1 = st.container()

  con1.markdown("""
**Dogy est un langage de programmation interprété codé en C, comme d'autres
langages tels que Python, JavaScript, PHP, etc...**
""")

  con1.write("Vous pouvez choisir les différentes documentations sur les côtés.")





elif onglet == "les variables":
  st.title("Les variables")

  con2 = st.container()
  con2.write(
    """
    En Dogy, les variables peuvent être déclarées ou modifiées comme ceci :
    """)

  con2.code("""
    a = 5
    ou
    b = Dogy
    """)

  con2.write("""
  On y accède en mettant leurs noms entre guillemets (")
  """)

  con2.code("""print("a")""")

  con2.write("Ce code affichera :")
  con2.code(5)

  con2.markdown("""
L'interpréteur reconnaît le type d'une variable automatiquement.\n
Et si je veux 5 comme une chaîne de caractères me direz-vous ?\n
Eh bien, le Dogy ne fait pas de différence\n
entre les deux, donc pas besoin de s'embêter avec ça !\n
""")




elif onglet == "les fonctions":
  st.title("Les fonctions")

  con3 = st.container()
  con3.write(
  """
  **En Dogy, il y a des fonctions natives (heureusement :) que je détaillerai plus bas.
  Quand une fonction retourne quelque chose, comme la fonction input() qui lit l'entrée de l'utilisateur,
  elle 'met' la valeur dans une variable nommée "output".
  Cette variable est normale et peut être utilisée dans d'autres fonctions ou dans le code principal.
  Exemple :**
  """)

  con3.code("""
  input(entrez votre nom svp :)

  print(bonjour, "output")
  """)

  con3.write("Si j'entre 'ficus', ce code affichera :")
  con3.code("""bonjour ficus """)

  con3.write("Et si vous desirez afficher une virgule, vous pouvez mettre votre message entre guillemets :")
  con3.code("""print("bonjour, et salut", ficus)""")
  con3.write("ce code affichera :")
  con3.code("""bonjour, et salut ficus""")
  #rien

elif onglet == "les différentes fonctions natives":
  st.title("Les différentes fonctions natives")

  con4 = st.container()
  select = con4.selectbox("**Choisissez une fonction native**", 
                          [
                            "input", "print"
                          ])

  if select == "input":
    con4.write("**input()**\n")
    con4.write("Cette fonction permet de lire l'entrée de l'utilisateur.")
    con4.write("**Exemple :**")
    con4.code("""
    input(entrez un nombre)
    print("output")
    """)
    con4.write("Si j'entre '42', ce code affichera :")
    con4.code("""42""")
  elif select == "print":
    con4.write("**print()**\n")
    con4.write("Cette fonction permet d'afficher un message.")
    con4.write("**Exemple :**")
    con4.code("""
    print(hello world)
    """)

    con4.write("Ce code affichera :")
    con4.code("""hello world""")
