# Zero 2 Model Checking
---
Raphaël AZOU<br/>
Goulven LE PENNEC<br/>
M2 ASSEL<br/>
**ENSTA**<br/>
2024-2025<br/>

```
                  ,----,          ____           
                .'   .' \       ,'  , `.         
       ,----, ,----,'    |   ,-+-,.' _ |         
     .'   .`| |    :  .  ;,-+-. ;   , ||         
  .'   .'  .' ;    |.'  /,--.'|'   |  || ,---.   
,---, '   ./  `----'/  ;|   |  ,', |  |,/     \  
;   | .'  /     /  ;  / |   | /  | |--'/    / '  
`---' /  ;--,  ;  /  /-,|   : |  | ,  .    ' /   
  /  /  / .`| /  /  /.`||   : |  |/   '   ; :__  
./__;     .'./__;      :|   | |`-'    '   | '.'| 
;   |  .'   |   :    .' |   ;/        |   :    : 
`---'       ;   | .'    '---'          \   \  /  
            `---'                       `----'   

▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖▗▄▄▄▖▄▄▄▄▖
▐▌   ▐▛▚▖▐▌▐▌     █   ▗▖▜▌
▐▛▀▀▘▐▌ ▝▜▌ ▝▀▚▖  █ ▗▞▘ ▐▌
▐▙▄▄▖▐▌  ▐▌▗▄▄▞▘  █ ▝▘▄▄▄▖
                                                                           
```



Ce repository contient les travaux réalisés dans le cadre du projet *Zero to Model Checking* du cours de Validation.

_________________________________________________
- [Zero 2 Model Checking](#zero-2-model-checking)
    - [1 - Artéfacts](#1---artéfacts)
    - [2 - Propiétés vérifiées](#2---propiétés-vérifiées)
    - [3 - Fichiers clés pour l'exécution](#3---fichiers-clés-pour-lexécution)
      - [3.1 Alice \& Bob](#31-alice--bob)
      - [3.2 Les soupes](#32-les-soupes)
      - [3.3 Utilitaires](#33-utilitaires)
    - [4 - Exécution des automates:](#4---exécution-des-automates)
      - [4.1 Vérification de P1 et P2 (sans soupe):](#41-vérification-de-p1-et-p2-sans-soupe)
      - [4.2 Vérification de P1 et P2 (reachability):](#42-vérification-de-p1-et-p2-reachability)
      - [4.3 Vérification de P1, P2, P3, P4](#43-vérification-de-p1-p2-p3-p4)
      - [4.4 Vérification des propriétés en mode embedded DSL](#44-vérification-des-propriétés-en-mode-embedded-dsl)
_________________________________________________


### 1 - Artéfacts

- Tours de Hanoï version *Rooted Graph*
- Tours de Hanoï version *Rooted Relation*
- Alice & Bob (vérification de propriétés: deadlock, état final atteint par alice et bob en même temps)
- Embedded Domain Specific Language pour la spécification des automates
- Semantic Intersection: Intersection de deux automates (automate de la propriété et automate du système) pour vérifier si la propriété est vérifiée par le système. Si l'intersection est vide, la propriété est vérifiée.


### 2 - Propiétés vérifiées

- (P1) Tout état doit vérifier « not (Alice@CS and Bob@CS) » – pour garantir
l’exclusion mutuelle
- (P2) Tout état doit avoir une transition sortante – pour garantir l’absence d’un
deadlock.
- (P3) Une des deux entités (Alice@CS ou Bob@CS) arrivera forcément dans la section critique.
- (P4) Si Alice ou Bob hisse son drapeau, cette entité arrivera forcément dans la section critique.

### 3 - Fichiers clés pour l'exécution

#### 3.1 Alice & Bob
Les fichiers `alice_bob_basic.py`, `alice_bob_deadlock.py` et `alice_bob_advanced.py` contiennent les définitions des automates d'Alice et Bob (RootedRelation), et contiennent chacun un `main` pour lancer la vérification de propriétés **P1** et **P2** à l'aide de `predicate_finder`. 

Le fichier `alice_bob_config.py` contient les configurations pour les automates d'Alice et Bob, à l'aide du embedded DSL. Chaque fonction de ce fichier correspond à un automate, et définit les pièces de celui-ci (nom)[guard] /-> action. Ces fonctions retournent un object de type `Soup`.

Le fichier `alice_bob_config_extended.py` contient la configuration d'Alice et Bob pour la représentation d'automate du graphe de Petersen, avec une différence structurelle comparé à `alice_bob_config.py` via l'ajout d'un attribut de classe `turn` qui permet de désigner le tour d'une des entités du système (Alice ou Bob).

#### 3.2 Les soupes
`soup.py` permet de stocker un état initial ainsi que les pièces utilisées dans l'automate exécuté.

`soup_semantic.py` contient une méthode `main` pour exécuter les tests sur les différents automates d'Alice et Bob. Cette classe réalise un travail de conversion de la vision des objets de base pour les considérer comme des éléments de type `Soup`.

`soup_dependant_semantic.py` contient une méthode pour évaluer la vivacité de l'automate évalué.

`step_semantics_intersection.py` opèrer en tant qu'interpréteur de langage, en interprétant l'attribut `lhs` pour le traduire en `rhs`


#### 3.3 Utilitaires
`parent_tracer.py` permet de tracer un historique des étapes ayant abouti à un cas de figure spécifique

`predicate_finder.py` permet de chercher un cas de figure spécifique au sein de l'automate visé: solution, deadlock, livelock, ...

`rr2rg.py` sert de passerelle pour adapter les objets de type `RootedRelation` en objets de type `RootedGraph`.

### 4 - Exécution des automates:
Tout fichier doit être lancé avec `python3 <nom-de-fichier>`<br/>
Les propriétés à vérifier sont référencées au [chapitre 2](#2---propiétés-vérifiées) du README.

#### 4.1 Vérification de P1 et P2 (sans soupe):
- lancer:<br/>
`alice_bob_basic.py`<br/>
`alice_bob_deadlock.py`<br/>
`alice_bob_advanced.py` 

#### 4.2 Vérification de P1 et P2 (reachability):
- lancer:<br/>
`soup_semantic.py`

#### 4.3 Vérification de P1, P2, P3, P4
- lancer:<br/>
`soup_dependant_semantic.py`

#### 4.4 Vérification des propriétés en mode embedded DSL
- lancer:<br/>
`alice_bob_config.py`
