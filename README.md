# Zero 2 Model Checking
---
Raphaël AZOU
Goulven LE PENNEC
M2 ASSEL

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
```

Ce repository contient les travaux réalisés dans le cadre du projet *Zero to Model Checking* du cours de Validation.

### Artéfacts

- Tours de Hanoï version *Rooted Graph*
- Tours de Hanoï version *Rooted Relation*
- Alice & Bob (vérification de propriétés: deadlock, état final atteint par alice et bob en même temps)
- Embedded Domain Specific Language pour la spécification des automates
- Semantic Intersection: Intersection de deux automates (automate de la propriété et automate du système) pour vérifier si la propriété est vérifiée par le système. Si l'intersection est vide, la propriété est vérifiée.


### Propiétés vérifiées

- (P1) Tout état doit vérifier « not (Alice@CS and Bob@CS) » – pour garantir
l’exclusion mutuelle
- (P2) Tout état doit avoir une transition sortante – pour garantir l’absence d’un
deadlock.
- (P3) Un des deux (Alice@CS ou Bob@CS) arrivera finalement dans la section critique.
- (P4) Si un des deux hisse son drapeau il arrivera finalement dans la section critique.

### Fichiers clés pour l'exécution

#### Alice & Bob
Les fichiers `alice_bob_basic.py`, `alice_bob_deadlock.py` et `alice_bob_advanced.py` contiennent les définitions des automates d'Alice et Bob (RootedRelation), et contiennent chacun un `main` pour lancer la vérification de propriétés P1 et P2 à l'aide de `predicate_finder`. 

Le fichier `alice_bob_config.py` contient les configurations pour les automates d'Alice et Bob, à l'aide du embedded DSL. Chaque fonction de ce fichier correspond à un automate, et définit les pièces de celui-ci (nom)[guard] /-> action. Ces fonctions retournent un object de type `Soup`.


