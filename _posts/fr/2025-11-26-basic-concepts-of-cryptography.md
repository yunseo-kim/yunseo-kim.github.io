---
title: "Notions fondamentales de cryptographie"
description: "Comprendre ce qu’est la cryptographie : chiffrement symétrique et asymétrique, principe de Kerckhoffs, primitives, échange de clés et signatures numériques."
categories: [Dev, Cryptography]
tags: [Cryptographic Primitives, Symmetric Cryptography, Secret Key Cryptography, Asymmetric Cryptography, Public Key Cryptography]
image: /assets/img/technology.webp
math: true
mermaid: true
---

## Qu’est‑ce que la cryptographie ?

**La cryptographie** est, au fond, une sous‑discipline scientifique dont l’objectif est de défendre les **protocoles (protocols)** contre des actions hostiles.

Un protocole est ici une liste d’étapes que doivent suivre une ou plusieurs personnes pour atteindre un objectif donné. Par exemple, si l’on souhaite partager le presse‑papiers entre plusieurs appareils, on peut définir le protocole suivant.

1. Lorsqu’il y a un changement dans le presse‑papiers sur l’un des appareils, celui‑ci copie le contenu du presse‑papiers et le téléverse sur un serveur.
2. Le serveur informe les autres appareils qu’une modification a eu lieu dans le presse‑papiers partagé.
3. Les autres appareils téléchargent alors depuis le serveur ce contenu de presse‑papiers partagé.

Cependant, ce n’est pas un bon protocole : si l’on envoie le contenu du presse‑papiers en clair vers le serveur et qu’on le télécharge aussi en clair, quelqu’un pourrait intercepter ce contenu pendant la communication, ou bien l’opérateur du serveur pourrait l’espionner. La cryptographie a précisément pour rôle de défendre contre l’existence éventuelle d’un adversaire cherchant à espionner ce contenu de presse‑papiers.

## Cryptographie symétrique

### Chiffrement symétrique

> Imaginons qu’Alice doive envoyer une lettre à Bob. Elle donne la lettre à un(e) **messager·ère (messenger)** pour la porter à Bob, car elle souhaite lui transmettre des informations confidentielles.
> Mais Alice ne fait pas totalement confiance au messager et veut que le message reste secret pour toute personne autre que Bob, y compris le messager qui transporte la lettre.

L’algorithme cryptographique inventé il y a longtemps pour répondre à ce type de situation est précisément l’**algorithme de chiffrement symétrique (symmetric encryption algorithm)**.

> **Primitive (primitive)**  
> Le mot *primitive* signifie, au sens courant, « primitif » ou « élémentaire ».
> En cryptographie, on utilise très souvent ce terme : une primitive désigne la plus petite unité de fonction ou d’algorithme qui sert de brique de base à un système cryptographique.
> On peut l’interpréter comme un « élément fondamental » ou une « logique de base ».
{: .prompt-info }

Considérons une primitive qui fournit les deux fonctions suivantes.
- `ENCRYPT` : prend en entrée une **clé secrète (secret key)** (en général un grand nombre) et un **message (message)**, et produit en sortie une suite de chiffres, à savoir le message chiffré ;
- `DECRYPT` : fonction réciproque de `ENCRYPT`, qui prend en entrée la même clé secrète et le message chiffré, puis restitue le message original.

Pour empêcher le messager, ou tout autre tiers, de lire le message d’Alice à l’aide d’une telle primitive, Alice et Bob doivent d’abord se rencontrer à l’avance et convenir de la clé secrète à utiliser. Ensuite, Alice peut chiffrer son message avec la clé convenue à l’aide de la fonction `ENCRYPT`, puis transmettre ce message chiffré à Bob par l’intermédiaire du messager. Bob, de son côté, utilise la même clé secrète avec la fonction `DECRYPT` pour retrouver le message original.

Ce processus consistant à chiffrer des données à l’aide d’une clé secrète, de sorte qu’elles soient indiscernables d’un bruit aléatoire, est en cryptographie la méthode générale pour protéger un protocole.

Le chiffrement symétrique appartient à une catégorie plus large d’algorithmes cryptographiques appelée **cryptographie symétrique (symmetric cryptography)** ou **cryptographie à clé secrète (secret key cryptography)**, et il peut, selon les cas, faire intervenir plus d’une clé.

## Principe de Kerckhoffs

Aujourd’hui, nous disposons de moyens de communication bien plus puissants que la lettre papier, à savoir l’ordinateur et Internet, qui nous permettent d’échanger presque en temps réel. Mais cela signifie aussi, en contrepartie, que les messagers malveillants sont eux aussi devenus plus puissants. Il peut s’agir d’un Wi‑Fi public non sécurisé dans un café, d’un fournisseur d’accès à Internet (FAI), de divers équipements réseau ou serveurs assurant le transit des messages, d’agences gouvernementales, voire même d’éléments présents sur l’appareil exécutant l’algorithme. Les adversaires peuvent observer un très grand nombre de messages en temps réel, les modifier ou les intercepter au niveau de la nanoseconde sans qu’on s’en aperçoive, voire les censurer.

L’expérience accumulée au fil du temps en cryptographie a conduit à un principe général pour obtenir une sécurité fiable : <u>les primitives doivent être analysées publiquement</u>. La méthode opposée est appelée **sécurité par l’obscurité (security by obscurity)**, dont les limites sont claires ; elle est aujourd’hui largement abandonnée.

Ce principe général a été formulé pour la première fois en 11883 par le linguiste et cryptologue néerlandais **Auguste Kerckhoffs**, et est connu sous le nom de **principe de Kerckhoffs (Kerckhoffs's principle)**. Le mathématicien, informaticien et cryptologue américain **Claude Shannon**, également considéré comme le père de la théorie de l’information, a exprimé le même principe par la formule « *The enemy knows the system* » (« l’ennemi connaît le système »), c’est‑à‑dire : « lorsqu’on conçoit un système, il faut supposer que l’ennemi finira par le connaître ». Cette formulation est connue sous le nom d’**adage de Shannon (Shannon's maxim)**.

La sécurité d’un système cryptographique doit reposer uniquement sur le secret de la clé ; le système lui‑même peut être rendu public sans que cela pose problème, et devrait même l’être, pour que de nombreux **cryptanalystes (cryptanalysts)** puissent l’examiner, comme dans le cas d’AES. Toute chose secrète est par nature susceptible de fuiter et constitue donc un point potentiel de défaillance ; plus la partie à garder secrète est petite, plus la position du défenseur est avantageuse. Il est extrêmement difficile de garder longtemps secret l’ensemble d’un système cryptographique complexe, alors qu’il est relativement facile de ne garder secrète que la clé. De plus, même en cas de fuite, il est bien plus simple de remplacer une clé compromise que de changer tout le système cryptographique.

## Cryptographie asymétrique

De nombreux protocoles fonctionnent en pratique sur la base de la cryptographie symétrique, mais une telle approche suppose qu’au moins une fois au départ, les deux participants se rencontrent pour fixer la clé à utiliser. La question devient alors de savoir comment décider de la clé et la partager de manière sûre au préalable : c’est ce que l’on appelle le problème de la **distribution des clés (key distribution)**. Ce problème est resté longtemps un défi majeur, jusqu’à ce qu’il soit finalement résolu à la fin des années 11970 avec le développement d’algorithmes appelés **cryptographie asymétrique (asymmetric cryptography)** ou **cryptographie à clé publique (public key cryptography)**.

Les primitives les plus représentatives de la cryptographie asymétrique sont l’**échange de clés (key exchange)**, le **chiffrement asymétrique (asymmetric encryption)** et la **signature numérique (digital signature)**.

### Échange de clés

L’**échange de clés** fonctionne, schématiquement, de la manière suivante.

1. Alice et Bob conviennent d’utiliser en commun un certain ensemble de paramètres $G$ ;
2. Alice et Bob choisissent chacun une **clé privée (private key)**, respectivement $a$ et $b$ ;
3. À partir des paramètres communs $G$ et de leurs clés privées $a$ et $b$, ils calculent leurs **clés publiques (public keys)** $A = f(G,a)$ et $B = f(G,b)$, puis les publient ;
4. Alice utilise la clé publique de Bob $B = f(G,b)$ et sa propre clé privée $a$ pour calculer $f(B,a) = f(f(G,b),a)$, tandis que Bob fait de même avec la clé publique d’Alice $A = f(G,a)$ et sa clé privée $b$ pour calculer $f(A,b) = f(f(G,a),b)$ ;
5. Si l’on choisit une fonction $f$ telle que $f(f(G,a),b) = f(f(G,b),a)$, Alice et Bob partagent au final le même secret, alors qu’un tiers, qui ne connaît que $G$ ainsi que les clés publiques $A = f(G,a)$ et $B = f(G,b)$, ne peut pas en déduire $f(A,b)$ : le secret reste donc préservé.

En général, le secret ainsi partagé est utilisé comme clé secrète pour un [chiffrement symétrique](#chiffrement-symétrique), ce qui permet ensuite d’échanger d’autres messages en s’appuyant sur la cryptographie symétrique.

Le premier algorithme d’échange de clés publié, et le plus emblématique, est l’algorithme d’échange de clés de Diffie‑Hellman, nommé d’après ses auteurs Whitfield **Diffie** et Martin **Hellman**.

L’échange de clés Diffie‑Hellman a toutefois ses limites. Imaginons qu’un attaquant intercepte les clés publiques $A = f(G,a)$ et $B = f(G,b)$ lors de leur échange et les remplace par sa propre clé publique $M = f(G,m)$, qu’il envoie ensuite à Alice et à Bob. Dans ce cas, Alice et l’attaquant partagent un faux secret $f(M, a) = f(A, m)$, tandis que Bob et l’attaquant partagent un autre faux secret $f(M, b) = f(B, m)$. L’attaquant peut alors se faire passer pour Bob auprès d’Alice, et pour Alice auprès de Bob. On dit alors qu’<u><strong>un homme du milieu (man‑in‑the‑middle, MITM)</strong> a réussi à attaquer le protocole</u>. Ainsi, l’échange de clés ne résout pas le problème de la confiance, même s’il simplifie considérablement les procédures lorsque les participants sont nombreux.

### Chiffrement asymétrique

Peu de temps après l’invention de l’échange de clés Diffie‑Hellman, une autre avancée majeure a eu lieu : l’algorithme **RSA (RSA algorithm)**, nommé d’après ses inventeurs **Ronald Rivest**, **Adi Shamir** et **Leonard Adleman**. RSA fournit deux primitives : le chiffrement à clé publique (chiffrement asymétrique) et la signature numérique ; toutes deux relèvent de la cryptographie asymétrique.

Dans le cas du **chiffrement asymétrique**, l’objectif principal — chiffrer un message pour en assurer la confidentialité — est similaire à celui du [chiffrement symétrique](#chiffrement-symétrique). Toutefois, contrairement au chiffrement symétrique, qui utilise une même clé pour chiffrer et déchiffrer, le chiffrement asymétrique présente les caractéristiques suivantes.
- Il fonctionne avec deux clés : une clé publique et une clé privée ;
- Tout le monde peut chiffrer à l’aide de la clé publique, mais seul le détenteur de la clé privée peut déchiffrer.

On peut l’illustrer ainsi :

1. Il existe une boîte ouverte (la clé publique) dans laquelle n’importe qui peut déposer un message avant de la fermer ; une fois fermée, seule la clé (la clé privée) détenue par Bob permet de l’ouvrir ;
2. Alice place le message qu’elle veut envoyer dans la boîte, la ferme (elle chiffre le message), puis la transmet à Bob ;
3. Bob reçoit la boîte fermée (le message chiffré) et utilise sa clé (sa clé privée) pour l’ouvrir et en extraire le message (le déchiffrer).

### Signature numérique

RSA ne fournit pas seulement le chiffrement asymétrique, mais aussi la **signature numérique** ; cette primitive de signature a considérablement facilité l’établissement de la confiance entre Alice et Bob. Pour signer un message, on utilise sa propre clé privée ; pour vérifier l’authenticité d’une signature, un tiers utilise le message signé, la signature et la clé publique du signataire.

## Utilité de la cryptographie

L’objectif de la cryptographie est de protéger les protocoles contre des actions hostiles ; l’utilité de la cryptographie dépend donc des objectifs de ces protocoles. La plupart des primitives et protocoles cryptographiques visent à assurer une ou plusieurs des propriétés suivantes.
- **Confidentialité (confidentiality)** : masquer et protéger certaines informations contre les personnes qui ne devraient pas y avoir accès ;
- **Authentification (authentication)** : identifier son interlocuteur (par exemple vérifier que le message reçu provient bien d’Alice).

## Écosystème de la cryptographie

```mermaid
flowchart TD
    Alice[Chercheuse en cryptographie]-- invente une primitive -->Primitive(Nouvelle primitive proposée)
    Alice-- invente un protocole -->Protocol(Nouveau protocole proposé)
    Alice-. organise un concours .->C(Concours d’algorithmes)

    David[Industrie privée]-. finance .->Alice
    David-. organise un concours .->C

    Eve[Agence gouvernementale]-. finance .->Alice
    Eve-. organise un concours .->C

    Primitive --> t1{"Est‑ce implémentable ?"}
    t1-- Oui -->Protocol
    t1-- Non -->term1@{ shape: framed-circle, label: "Arrêt" }

    Protocol-- participe au concours -->C
    Protocol-- normalisation -->Standard(Norme)
    Protocol-- dépôt de brevet -->Patent(Brevet (expiration))
    Protocol-- implémentation -->Library(Bibliothèque)
    
    C-- gagne le concours -->Standard
    C-- obsolescence -->term2@{ shape: framed-circle, label: "Arrêt" }

    Standard-- implémentation -->Library
    Standard-- obsolescence -->term3@{ shape: framed-circle, label: "Arrêt" }

    Patent-- obsolescence -->term2@{ shape: framed-circle, label: "Arrêt" }
    Patent-- normalisation -->Standard
    Patent-- implémentation -->Library

    Library-- normalisation -->Standard
    Library-- compromis de sécurité -->term4@{ shape: framed-circle, label: "Arrêt" }
```
